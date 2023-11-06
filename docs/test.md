# CONSTRUCTOR 
```python
__init__(self)
```

### updates
* set values of attributes: constValues, tradeValues, myKite, common, statargy, myNeo

## Attributes

|NAME       |DISCRIPTION        |TYPE       |VALUE      |
|------------|------------|------------|------------|
|scName     |script name to trade       |str        |script name        |
|opName     |option name to trade       |str        |option symbol      |
|TIME_FRAME     |time frame on which have to trade      |str        |check constValues.TIME_FRAME       |
|TIME_FRAME_INT     |time frame in minute int       |int        |time frame int     |
|noCandle       |number of candle for historical data       |str (int)      |number of candle       |
|fs     |file instance      |instance       |instance       |
|nowTime        |Reference now time for historical candle data      |instance (datetime)        |instance       |
|BUY_FLAG       |set while script is bought and in Trade        |boolean        |True or False      |
|CANDLE_DATA_SET_FLAG       |set when the candle data setted        |boolean        |True or False      |
|LTP_SET_FLAG       |set when the ltp is setted     |boolean        |True or False      |
|OPTION_TYPE        |Type of the option     |str        |"CE" or "PE"       |
|ORDER_PLACED       |set when the order is placed and unset when the order completed        |boolean        |True or False      |
|HOLD01     |hold the buy and sell loop from the order complete till trade values set       |boolean        |True or False      |
|HOLD02     |hold the buy loop after the trade close till next candle data set (consider you taken a trade for parituclar historical data and the stops loss hitted before the new candle data set, in this situation buy loop will check the same historical data and will execute the trade)      |boolean        |True or False      |
|HOLD03     |maintain the cnadle data loop with time frame      |boolean    |True or False      |
|BUYT       |buy time of script     |instance (datetime)        |datetime instance      |
|SELLT      |sell time of script        |instance (datetime)      |datetime instance        |
|orderNo        |order number of currently placed order     |str (int)      |valid order id     |
|constValues        |instance of constValues class      |instance   |constValues instance       |
|tradeValues        |instance of tradevalues class      |instance   |tradeValues instance       |
|myKite     |instance of Mykite class       |instance       |myKite instance        |
|common     |instance of common class       |instance       |common instance        |
|statargy       |instance of statargy class     |instance       |statargy instance      |
|myNeo      |instance of myneo class        |instance       |myNeo instance     |


#   ATTRIBUTES AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|scName     |test       |-      |candleData_loop<br>ltp_thread_loop<br>neo_order_status_track_thread        |
|opName     |test       |-      |buy_loop<br>sell_loop<br>ltp_thread_loop<br>neo_order_status_track_thread      |  
|TIME_FRAME     |test       |-      |candleData_loop        |
|TIME_FRAME_INT     |test       |-      |timeFrame_manager      |
|noCandle       |test       |-      |candleData_loop        |
|fs     |test       |-      |-      |
|nowTime        |test       |-      |timeFrame_manager<br>candleData_loop       |
|BUY_FLAG       |test       |-      |buy_loop<br>sell_loop<br>ltp_thread_loop<br>neo_order_status_track_thread      |
|CANDLE_DATA_SET_FLAG       |test       |-      |candleData_loop<br>buy_loop        |
|LTP_SET_FLAG       |test       |-      |sell_loop<br>ltp_thread_loop<br>neo_order_status_track_thread       |
|OPTION_TYPE        |test       |-      |buy_loop<br>sell_loop<br>ltp_thread_loop       |
|ORDER_PLACED       |test       |-      |buy_loop<br>sell_loop<br>neo_order_status_track_thread     |
|HOLD01     |test       |-      |buy_loop<br>sell_loop<br>neo_order_status_track_thread         |
|HOLD02     |test       |-      |timeFrame_manager<br>buy_loop<br>neo_order_status_track_thread     |
|HOLD03     |test       |-      |timeFrame_manager<br>candleData_loop       |
|BUYT       |test       |-      |neo_order_status_track_thread      |
|SELLT      |test       |-      |neo_order_status_track_thread      |
|orderNo        |test       |-      |buy_loop<br>sell_loop<br>neo_order_status_track_thread         |
|constValues        |test       |-      |init       |
|tradeValues        |test       |-      |init<br>candleData_loop<br>ltp_thread_loop<br>neo_order_status_track_thread        |
|myKite     |test       |-      |init<br>candleData_loop<br>ltp_thread_loop     |
|common     |test       |-      |init<br>neo_order_status_track_thread      |
|statargy       |test       |-      |init<br>buy_loop<br>sell_loop      |
|myNeo      |test       |-      |init<br>buy_loop<br>sell_loop<br>ltp_thread_loop<br>neo_order_feed_thread<br>neo_order_status_track_thread     |


## METHOADS
|METHOAD NAME       |METHOAD DISCRIPTION     |PARAMETR       |RETURN TYPE        |RETURN VALUE        |UPDATE        |
|----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|timeFrame_manager      |mange the loop to maintain the timegrame       |-      |-          |-          |nowTime<br>HOLD02<br>HOLD03        |
|candleData_loop        |works with the historical required data        |-      |-          |-          |HOLD03<br>CANDLE_DATA_SET_FLAG<br>HOLD03       |
|buy_loop       |checks buy condition and place buy order       |-      |-          |-          |scName<br>opName<br>orderNo<br>ORDER_PLACED<br>OPTION_TYPE      |
|sell_loop      |check sell condition and place sell order      |-      |-          |-          |ORDER_PLACED<br>LTP_SET_FLAG       |
|ltp_thread_loop        |works with the ltp data and manage the highp and lowp      |-      |-          |-          |LTP_SET_FLAG       |
|neo_order_feed_thread      |connect to the order feed      |-      |-          |-          |-      |
|neo_order_status_track_thread      |check the order status         |-      |-          |-          |ORDER_PLACED<br>HOLD01<br>BUY_FLAG<br>HOLD02<br>LTP_SET_FLAG       |

### ```parameter discription```
|PARAMTER NAME       |PARAMETER DISCRIPTION     |PARAMETER TYPE     |VALID VALUES        |
|----------------------|-----------------------|-----------------------|-----------------------|
|-  |-  |-  |-  |

#   METHOADS AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|timeFrame_manager      |-      |-      |-      |
|candleData_loop        |-      |-      |-      |
|buy_loop       |-      |-      |-      |
|sell_loop      |-      |-      |-      |
|ltp_thread_loop        |-      |-      |-      |
|neo_order_feed_thread      |-      |-      |-      |
|neo_order_status_track_thread      |-      |-      |-      |