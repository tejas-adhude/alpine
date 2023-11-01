from alpine.kiteTrade import KiteApp
from alpine.kiteTrade import get_enctoken
from alpine.constValues import constValues
import datetime

class myKite:
    userId=None
    password =None
    twofa=None
    enctoken=None
    constValues=None
    kiteApp=None

    def __init__(self,constValuesObj):
        if not isinstance(constValuesObj,constValues): raise Exception("invalid parameter value for costValuesObj")
        self.constValues=constValuesObj
        
    def set_user_credentials(self):
        credential=self.constValues.get_api_credential("kite")

        if credential:
            # self.userId=credential["userId"]
            # self.password=credential["password"]
            self.enctoken=credential["enctoken"]
            # self.twofa = input("Enter Kite TOTP: ")
        else: raise Exception("Credential not found!")
        
    def authenticate_user(self):
        self.set_user_credentials()
        # self.enctoken = get_enctoken(self.userId, self.password, self.twofa)
        self.kiteApp = KiteApp(enctoken=self.enctoken)
    
    def get_historical_data(self,nowTime,timeFrame,scName=None,tokenId=None,noCandle=None,toDateTime=None,fromDateTime=None):
        """ 
            parameters:
                NowTime:-(datetime instance) current time instance (reference time object, as current time)
                timeFrame:-(str) time frame for candle data
                scName:- (str) script name (optional is tokenId is passed)
                tokenId:- (int) instrument token Id of script (optional if scName is passed)
                noCandle:-(str) no of candle (optionla if toDateTime and fromDateTime is passed)
                toDateTime:- (datetime instance) upto time for candle data (optional if noCandle and fromDateTime passed )
                fromDateTime:- (datetime instance) from time for candle data (optional if)

            return:
                tuple
        """

        if not self.kiteApp: raise Exception("kite user not authenticated.")

        if (not scName and not tokenId): raise Exception("either pass the scName or tokenId")

        # ensuring two parameter should pass out of (noCandle,toDateTime,fromDateTime)
        if not ((noCandle and toDateTime and not fromDateTime) or (noCandle and not toDateTime and fromDateTime) or (not noCandle and toDateTime and fromDateTime)): raise Exception("need parameter combination of : (noCandle,toDateTime) or (noCandle,fromDateTime) or(toDateTime,fromDateTime)")

        #getting tokenId for given script name (scName)
        if scName:
            scName=scName.upper()
            tokenId=self.constValues.get_instrument_info(scName)["tokenId"]

        #getting minute conversion for timeframe
        validTime=self.constValues.get_time_frame()
        cmul=int(validTime[timeFrame])

        noCandle=int(noCandle)

        #calculating the fromDateTime when toDateTime and noCandle given
        if (noCandle and toDateTime and not fromDateTime): 
            fromDateTime=toDateTime - datetime.timedelta(minutes=noCandle*cmul+1)
            toDateTime=toDateTime-datetime.timedelta(minutes=cmul)

        #calculating the toDateTime when fromDateTime and noCandle given
        if (noCandle and not toDateTime and fromDateTime):
            toDateTime=fromDateTime + datetime.timedelta(minutes=noCandle*cmul-1)
            fromDateTime=fromDateTime + datetime.timedelta(minutes=cmul-1)

        #if the fromDateTime is less than 9:15 (market open time), then set it to 9:15
        if fromDateTime<datetime.datetime(nowTime.year,nowTime.month,nowTime.day,9,15): fromDateTime=datetime.datetime(nowTime.year,nowTime.month,nowTime.day,9,15)

        #if the toDateTime is grather than 15:30 (market close time), then set it 15:29
        #why 15:29 not 15:30, because it will give result also for candle which start at 15:30 
        if toDateTime>datetime.datetime(nowTime.year,nowTime.month,nowTime.day,15,30): toDateTime=datetime.datetime(nowTime.year,nowTime.month,nowTime.day,15,29)

        #sending request for data to kite
        data = self.kiteApp.historical_data(instrument_token=str(tokenId), from_date=fromDateTime, to_date=toDateTime, interval=timeFrame, continuous=False, oi=False)

        # print(data)

        candleData=[]
        for candle in data:
            [dateTimeObj,o, h, l, c] = candle["date"],str(candle['open']), str(candle['high']), str(candle['low']), str(candle['close'])
            
            candleData.append([dateTimeObj,o, h, l, c])

        return scName,tokenId,candleData
    
    def get_ltp(self,inNames):
        """
            parameter:
                inName: name of script in the format (list)
                        ex. inName=["NFO:NIFTY2361517800CE","NSE:NIFTY 50"] 
            return:
                object
                {"inName":"ltp","inName":"ltp"}
        """
        """
            INSTRUMENT_INFO=self.constValues.get_instrument_info()
            INSTRUMENT_INFO=[{"name":"NIFTY 50","symbol":"NIFTY","tokenId":"256265","exchange":"NSE","segment":"FO","type":"IN"}]
            combination of exchange+name

            inName="NSE:NIFTY 50"  

            OPTION_INFO=self.constValuesget_option_info()
            OPTION_INFO=[{"name":"NIFTY 50","inSymbol":"NIFTY","exYear":"23","exMonthNum":"7","exMonthAlpha":"JUL","exDate":"20"}]
            cpmbination of exchange and segment+expiray year month date+strike price+ce/pe

            inName="NFO:NIFTY2361517800CE"
        """
           
        if not self.kiteApp: raise Exception("kite user not authenticated.")

        ltp = self.kiteApp.ltp(inNames)
        
        ltpdic={}
        for inName in inNames:
            ltpdic[inName]=str(ltp[inName]["last_price"])

        return ltpdic
