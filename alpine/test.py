import datetime
import threading
import time
import multiprocessing

from alpine.constValues import constValues
from alpine.common import common
from alpine.tradeValues import tradeValues
from alpine.myKite  import myKite
from alpine.statargy import statargy


class test:
    scName="NIFTY 50"
    opName=None
    TIME_FRAME="minute"
    TIME_FRAME_INT=1
    noCandle="2"
    fs=None

    nowTime=None
    BUY_FLAG=False
    CANDLE_DATA_SET_FLAG=False
    LTP_SET_FLAG=False
    OPTION_TYPE=None
    BUYT=None
    SELLT=None
    
    constValues=None
    tradeValues=None
    myKite=None
    common=None
    statargy=None

    def __init__(self):
        self.constValues=constValues()
        self.tradeValues=tradeValues(constValuesObj=self.constValues)

        self.myKite=myKite(constValuesObj=self.constValues)
        self.myKite.authenticate_user()

        self.common=common(tradeValuesObj=self.tradeValues)
        # self.fs=self.common.open_record_file()

        fs = open("Record.json", "a")
        fs.write("\nRecord start:\n"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n")
        fs.close()

        self.statargy=statargy(constValuesObj=self.constValues,taradeValuesObj=self.tradeValues,myKiteObj=self.myKite)

    def candleData_loop(self):
        print("candle data loop")
        while(True):
            self.nowTime=datetime.datetime.now()
            print(self.nowTime)

            _,_,candleData=self.myKite.get_historical_data(nowTime=self.nowTime,timeFrame=self.TIME_FRAME,scName=self.scName,noCandle=self.noCandle,toDateTime=self.nowTime)

            self.tradeValues.set_candles_data(scname=self.scName,noCandle=self.noCandle,timeFrame=self.TIME_FRAME,data=candleData)

            self.CANDLE_DATA_SET_FLAG=True

            while(True):
                CT=datetime.datetime.now()
                if (CT-self.nowTime).total_seconds()>=self.TIME_FRAME_INT*60:
                    break

    def buy_loop(self):
        print("buy loop ")
        while(True):
            if not self.BUY_FLAG and self.CANDLE_DATA_SET_FLAG:

                status=self.statargy.call_buy_condition(self)

                if status:
                    self.BUY_FLAG=True
                    self.OPTION_TYPE="CE"
                    print("bought CE")

                if not status:
                    status=self.statargy.put_buy_condition(self)

                    if status:
                        self.BUY_FLAG=True
                        self.OPTION_TYPE="PE"
                        print("bought PE")
            

    def sell_loop(self):
        print("sell loop")
        while(True):
            if self.BUY_FLAG and self.LTP_SET_FLAG:

                if self.OPTION_TYPE=="CE":
                    status=self.statargy.call_sell_condition(self)

                    if status:
                        self.BUY_FLAG=False
                        self.LTP_SET_FLAG=False
                        self.common.sell(self)
                
                if self.OPTION_TYPE=="PE":
                    status=self.statargy.put_sell_condition(self)

                    if status:
                        self.BUY_FLAG=False
                        self.LTP_SET_FLAG=False
                        self.common.sell(self)


    def ltp_thread_loop(self):
        print("ltp thread")
        while(True):
            if self.BUY_FLAG:
                ltps=self.myKite.get_ltp([f"NSE:{self.scName}",f"NFO:{self.opName}"])
                scltp=ltps[f"NSE:{self.scName}"]
                opltp=ltps[f"NFO:{self.opName}"]

                self.tradeValues.set_tradeValue(scname=self.scName,valueType="ltp",value=str(scltp))
                self.tradeValues.set_tradeValue(scname=self.opName,valueType="ltp",value=str(opltp))

                self.LTP_SET_FLAG=True

                ophighP=self.tradeValues.get_tradeValue(scname=self.opName,valueType="highP")["highP"]
                
                if(float(opltp)>float(ophighP)):
                    self.tradeValues.set_tradeValue(scname=self.opName,valueType="highP",value=str(opltp))

                if(self.OPTION_TYPE=="CE"):
                    schighP=self.tradeValues.get_tradeValue(scname=self.scName,valueType="highP")["highP"]
                    if(float(scltp)>float(schighP)):
                        self.tradeValues.set_tradeValue(scname=self.scName,valueType="highP",value=str(scltp))
                
                if(self.OPTION_TYPE=="PE"):
                    sclowP=self.tradeValues.get_tradeValue(scname=self.scName,valueType="lowP")["lowP"]
                    if(float(scltp)<float(sclowP)):
                        self.tradeValues.set_tradeValue(scname=self.scName,valueType="lowP",value=str(scltp))

                time.sleep(1)