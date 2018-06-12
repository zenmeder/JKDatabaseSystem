#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import happybase
import datetime
import pandas as pd


class TimeSeriesData:
    NUMS_OF_PAST_DAYS = 20

    def __init__(self, modelName, date, sensorId):
        self.modelName = modelName
        self.date = date
        self.sensorId = sensorId

    # 根据所给modelName, date, sensorId获取该sensorId下的date之前NUMS_OF_PAST_DAYS天的所有测孔的数据
    def getData(self):
        connection = happybase.Connection('localhost')
        table = connection.table(self.modelName)
        endDate = datetime.datetime.strptime(self.date + ' 23:59:59', "%Y-%m-%d %H:%M:%S")
        startDate = endDate - datetime.timedelta(days=self.NUMS_OF_PAST_DAYS)
        endRow = self.date + ' 23:59:59|' + str(self.sensorId)
        startRow = datetime.datetime.strftime(startDate, "%Y-%m-%d %H:%M:%S") + '|' + str(self.sensorId)
        data = {}
        res = {}
        for key, value in table.scan(row_start=startRow, row_stop=endRow):
            key = bytes.decode(key)
            if key[key.index('|') + 1:] == str(self.sensorId):
                d = {}
                for (k, v) in value.items():
                    k = bytes.decode(k)
                    d[int(k[k.index(':') + 1:])] = float(bytes.decode(v))
                data[key[:key.index('|')]] = d
        df = pd.DataFrame(data=data).T
        for i in range(len(df.columns)):
            d1 = df[i]
            newd = pd.DataFrame(columns=['ds','y'])
            newd.ds = d1.index
            newd.y = d1.values
            res[i] = newd
        return res

