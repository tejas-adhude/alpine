from alpine.constValues import constValues
from alpine.tradeValues import tradeValues

class statargy:

    constValues=None
    tradeValues=None 

    def __init__(self,constValuesObj,taradeValuesObj):
        if not isinstance(constValuesObj,constValues): raise Exception("invalid parameter value for costValuesObj")
        if not isinstance(taradeValuesObj,tradeValues): raise Exception("invalid parameter value for taradeValuesObj")

        self.constValues=constValuesObj
        self.tradeValues=taradeValuesObj

    def call_buy_condition(self,test):

        data=self.tradeValues.get_candles_data(test.scName,test.TIME_FRAME)

        if not data: 
            print("call_buy_condition,candle data not found") 
            return False
        
        data=data["data"]

        o1, h1, l1, c1 = float(data[0][1]), float(data[0][2]), float(data[0][3]), float(data[0][4])
        o2, h2, l2, c2 = float(data[1][1]), float(data[1][2]), float(data[1][3]), float(data[1][4])

        if ((o1 > c1) and ((c2-o2) > (2*(o1-c1))) and (c2 > h1)):
            buyp = c2
        
            trem=buyp%100
            if(trem>50):
                trem=trem-50

            strikeP=buyp-trem
            strikeP=int(strikeP)
            strikeP=19700

            opInfo=self.constValues.get_option_info(test.scName)

            if not opInfo:
                print("call_buy_condition,option info not found")

            inSymbol=opInfo["inSymbol"]
            exYear=opInfo["exYear"]
            exMonthNum=opInfo["exMonthNum"]
            # exMonthNum=opInfo["exMonthAlpha"]
            exDate=opInfo["exDate"]
            # exDate=""

            test.opName=f"{inSymbol}{exYear}{exMonthNum}{exDate}{strikeP}CE"

            self.tradeValues.set_tradeValue(test.scName,"buyP",buyp)
            self.tradeValues.set_tradeValue(test.scName,"highP",buyp)

            return True

        return False


    def call_sell_condition(self,test):

        data=self.tradeValues.get_candles_data(test.scName,test.TIME_FRAME)

        if not data: 
            print("call_sell_condition,candle data not found") 
            return False
        
        data=data["data"]

        scltp=self.tradeValues.get_tradeValue(test.scName,"ltp")
        if scltp is None:
            print("call_sell_condition,ltp not found") 
            return False
        else: scltp=scltp["ltp"]

        scltp=float(scltp)
        l1= float(data[0][3])

        if (scltp<l1):
            self.tradeValues.set_tradeValue(test.scName,"sellP",scltp)
            return True
        return False

    def put_buy_condition(self,test):

        data=self.tradeValues.get_candles_data(test.scName,test.TIME_FRAME)

        if not data: 
            print("put_buy_condition,candle data not found") 
            return False
        
        data=data["data"]

        o1, h1, l1, c1 = float(data[0][1]), float(data[0][2]), float(data[0][3]), float(data[0][4])
        o2, h2, l2, c2 = float(data[1][1]), float(data[1][2]), float(data[1][3]), float(data[1][4])

        if ((o1 < c1) and ((o2-c2) > (2*(c1-o1))) and (c2 < l1)):
            sellp = c2
        
            trem=sellp%100

            if(trem>50):
                trem=trem-50
            strikeP=sellp-trem+50

            strikeP=int(strikeP)
            strikeP=19400

            opInfo=self.constValues.get_option_info(test.scName)

            if not opInfo:
                print("put_buy_condition,option info not found")

            inSymbol=opInfo["inSymbol"]
            exYear=opInfo["exYear"]
            exMonthNum=opInfo["exMonthNum"]
            # exMonthNum=opInfo["exMonthAlpha"]
            exDate=opInfo["exDate"]
            # exDate=""

            test.opName=f"{inSymbol}{exYear}{exMonthNum}{exDate}{strikeP}PE"

            self.tradeValues.set_tradeValue(test.scName,"sellP",sellp)
            self.tradeValues.set_tradeValue(test.scName,"lowP",sellp)

            return True

        return False

    def put_sell_condition(self,test):

        data=self.tradeValues.get_candles_data(test.scName,test.TIME_FRAME)

        if not data: 
            print("put_sell_condition,candle data not found") 
            return False
        
        data=data["data"]

        scltp=self.tradeValues.get_tradeValue(test.scName,"ltp")
        if scltp is None:
            print("put_sell_condition,ltp not found") 
            return False
        else: scltp=scltp["ltp"]

        scltp=float(scltp)
        h1= float(data[0][2])

        if (scltp>h1):
            self.tradeValues.set_tradeValue(test.scName,"buyP",scltp)
            return True
        return False
    