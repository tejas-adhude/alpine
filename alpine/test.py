import datetime
import threading
import time
import multiprocessing

from alpine.constValues import constValues
from alpine.common import common
from alpine.tradeValues import tradeValues
from alpine.myKite  import myKite
from alpine.statargy import statargy
from alpine.myNeo import myNeo

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
    ORDER_PLACED=False
    HOLD01=False
    HOLD02=False
    HOLD03=True
    BUYT=None
    SELLT=None
    orderNo=None
    
    constValues=None
    tradeValues=None
    myKite=None
    common=None
    statargy=None
    myNeo=None

    def __init__(self):
        self.constValues=constValues()
        self.tradeValues=tradeValues(constValuesObj=self.constValues)

        self.myKite=myKite(constValuesObj=self.constValues)
        self.myKite.authenticate_user()

        self.myNeo=myNeo(constValuesObj=self.constValues)
        self.myNeo.temp_neo_auth()

        self.common=common(tradeValuesObj=self.tradeValues)
        self.common.open_record_file()

        self.statargy=statargy(constValuesObj=self.constValues,taradeValuesObj=self.tradeValues)
    
    def timeFrame_manager(self):
        print("time frame manager")
        self.nowTime=datetime.datetime.now()
        self.HOLD03=False
        while(True):
            self.nowTime=datetime.datetime.now()
            print(self.nowTime)

            while(True):
                CT=datetime.datetime.now()
                if (CT-self.nowTime).total_seconds()>=self.TIME_FRAME_INT*60:
                    self.HOLD02=False
                    self.HOLD03=False
                    break

    def candleData_loop(self):
        print("CANDLE DATA LOOP")
        while(True):
            if(not self.HOLD03):
                _,_,candleData=self.myKite.get_historical_data(nowTime=self.nowTime,timeFrame=self.TIME_FRAME,scName=self.scName,noCandle=self.noCandle,toDateTime=self.nowTime)

                self.tradeValues.set_candles_data(scname=self.scName,noCandle=self.noCandle,timeFrame=self.TIME_FRAME,data=candleData)

                self.CANDLE_DATA_SET_FLAG=True
                self.HOLD03=True

    def buy_loop(self):
        print("BUY LOOP")
        while(True):
            if not self.HOLD02 and not self.ORDER_PLACED and not self.BUY_FLAG and self.CANDLE_DATA_SET_FLAG and not self.HOLD01:

                status=self.statargy.call_buy_condition(self)

                if status:
                    print(".....placing call buy order....")
                    orderStatus,response=self.myNeo.place_order(tradingSymbol=self.opName,transectionType="B",quantity="50")
                    if orderStatus:
                        print("......call buy order placed.....")
                        self.orderNo=response["orderNo"]
                        self.ORDER_PLACED=True
                    self.OPTION_TYPE="CE"

                if not status:
                    status=self.statargy.put_buy_condition(self)

                    if status:
                        print(".....placing put buy order....")
                        orderStatus,response=self.myNeo.place_order(tradingSymbol=self.opName,transectionType="B",quantity="50")
                        if orderStatus:
                            print("......put buy order placed.....")
                            self.orderNo=response["orderNo"]
                            self.ORDER_PLACED=True
                        self.OPTION_TYPE="PE"

    def sell_loop(self):
        print("SELL LOOP")
        while(True):
            if not self.ORDER_PLACED and self.BUY_FLAG and self.LTP_SET_FLAG and not self.HOLD01:

                if self.OPTION_TYPE=="CE":
                    status=self.statargy.call_sell_condition(self)

                    if status:
                        print(".....placing call sell order....")
                        orderStatus,response=self.myNeo.place_order(tradingSymbol=self.opName,transectionType="S",quantity="50")
                        if orderStatus:
                            print("......call sell order placed.....")
                            self.orderNo=response["orderNo"]
                            self.ORDER_PLACED=True
                            self.LTP_SET_FLAG=False
                
                if self.OPTION_TYPE=="PE":
                    status=self.statargy.put_sell_condition(self)

                    if status:
                        print(".....placing put sell order....")
                        orderStatus,response=self.myNeo.place_order(tradingSymbol=self.opName,transectionType="S",quantity="50")
                        if orderStatus:
                            print("......put sell order placed.....")
                            self.orderNo=response["orderNo"]
                            self.ORDER_PLACED=True
                            self.LTP_SET_FLAG=False


    def ltp_thread_loop(self):
        print("LTP THREAD")
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
    
    def neo_order_feed_thread(self):
        print("NEO ORDER FIELD")
        self.myNeo.order_feed()
    
    def neo_order_status_track_thread(self):
        print("NEO ORDER STATUS TRACK")
        while(True):
            if self.ORDER_PLACED:
                for order in self.myNeo.orderIds:
                    if order["orderNo"]==self.orderNo:
                        status=order["status"]
                        if status=="rejected":
                            self.ORDER_PLACED=False
                            print("order rejected")
                        
                        if status=="complete":
                            self.HOLD01=True
                            self.ORDER_PLACED=False
                            print("......getting trade report.....")
                            response=self.myNeo.trade_report(orderId=self.orderNo)
                            if not response: 
                                print("problem while getting trade report")
                            else:
                                tranType=response["tranType"]
                                if tranType=="B":

                                    buyop=response["avgPrice"]
                                    self.tradeValues.set_tradeValue(self.opName,"buyP",buyop)
                                    self.tradeValues.set_tradeValue(self.opName,"highP",buyop)

                                    self.BUYT=response["completeTime"]
                                    self.BUY_FLAG=True
                                    self.HOLD01=False
                                    self.myNeo.orderIds.remove(order)
                                    print("..........setted trade buy value..........")

                                elif tranType=="S":

                                    sellop=response["avgPrice"]
                                    self.tradeValues.set_tradeValue(self.opName,"sellP",sellop)
                                    
                                    self.SELLT=response["completeTime"]

                                    self.common.sell(self)
                                    self.HOLD02=True
                                    self.BUY_FLAG=False
                                    self.HOLD01=False
                                    self.LTP_SET_FLAG=False
                                    self.myNeo.orderIds.remove(order)
                                    self.tradeValues.remove_tradeValue_script(scName=self.scName)
                                    self.tradeValues.remove_tradeValue_script(scName=self.opName)
                                    print("..........setted trade sell value..........")