from datetime import datetime
from alpine.constValues import constValues

class tradeValues:
    # Prices=[{"name":"NIFTY 50","tokenId":"1234","buyP":"123.44",sellP="",strikeP":"","ltp":"1723.45","highP":"1230.34","lowP":""}]

    # candlesData=[{"name":"NIFTY2372019800","timeFrame":"minute","data":[[dateTimeObj,"12.23","34.54","56.56","67.56"],[dateTimeObj,"23","34","34.56","12"]]}]
    # "data":[ [dateTimeObj,"o","h","l","c"],[dateTimeObj,"o","h","l","c"] ]
    #  latest candle have data at last

    constValues=None
    prices=None
    candlesData=None

    def __init__(self,constValuesObj):
        if not isinstance(constValuesObj,constValues): raise Exception("invalid parameter value for costValuesObj")
        self.prices=[]
        self.candlesData=[]
        self.constValues=constValuesObj


    def valid_value(self,valueType,value):
        if not isinstance(value, float): value=float(value)

        # value=round(value,2)

        if valueType in ["tokenId", "strikeP"]:
            value=int(value)

        value=str(value)

        return valueType,value
    
    def validate_valueType(self,valueType):
        if valueType not in ["tokenId","buyP","sellP","strikeP","ltp","highP","lowP"]:
            raise Exception("invalid ValueType")
        
        return True

    def validate_timeFrame(self,timeFrame):
        if timeFrame not in self.constValues.get_time_frame():
            raise Exception("invalid timeFrame")
        
        return True
    
    def validate_candle_data(self,noCandle,data):
        if not isinstance(data, list):raise Exception("data should be in list")

        if int(noCandle)!=len(data): raise Exception("Number of candle doesn't match with candle in data")

        for candle in data:

            if not isinstance(candle, list):raise Exception("data should be in list")

            i=0
            for index in candle:
                if(not i):
                    if not isinstance(index, datetime):raise Exception("missing dateTimeObj")
                else:
                    if not isinstance(index, str):raise Exception("data of price should be string")
                i=i+1

            if(i!=5):raise Exception("incomplete data , give data [dateTimeObj,o,h,l,c]")

        return True
    
    def set_tradeValue(self,scname,valueType,value):
        self.validate_valueType(valueType)
        _,value=self.valid_value(valueType,value)

        for script in self.prices:
            if(script["name"]==scname):
                script[valueType]=value
                return
            
        self.prices.append({"name":scname,valueType:value})
            
    def get_tradeValue(self,scname,valueType):
        self.validate_valueType(valueType)

        for script in self.prices:
            if(script["name"]==scname):
                if valueType in script:
                    value=script[valueType]
                    return {"name":scname,valueType:value}
                
        return None
    
    def set_candles_data(self,scname,noCandle,timeFrame,data):
        self.validate_timeFrame(timeFrame)
        self.validate_candle_data(noCandle,data)
       
        for script in self.candlesData:
            if(script["name"]==scname and script["timeFrame"]==timeFrame):
                script["data"]=data
                return
            
        self.candlesData.append({"name":scname,"timeFrame":timeFrame,"data":data})
    
    def get_candles_data(self,scname,timeFrame):
        self.validate_timeFrame(timeFrame)

        for script in self.candlesData:
            if(script["name"]==scname and script["timeFrame"]==timeFrame):
                return script
            
        return None