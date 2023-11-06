# CONSTRUCTOR 
```python
__init__(self,constValuesObj)
```
|PARAMETER  |PARAMETER DISCRIPTION     |PARAMETER TYPE     |PARMETER VALUE     |  
|--------------|--------------|--------------|--------------|
|constValuesObj        |object of constValues class    |instance     |constValues instance     |

### UPDATE
* initilize attribute prices with empty list
* initilize attribute candleData with empty list
* set the constValues instance to attribute contValues



# VALUES DISCRIPTION

## Attributes

### 1] constValues
Info:The instance of constValue class

### 2] prices
```python
Prices=[{"name":"NIFTY 50","tokenId":"1234","buyP":"123.44","sellP"="","strikeP":"","ltp":"1723.45","highP":"1230.34","lowP":""}]
```
#### info 
conatain the info of the script , editable.

| ELEMENT KEY NAME      | DISCRIPTION       | VALUES      |TYPE     |
|-----------------      |-------------      |-------      |----     |
|name           |name of the script     |name of script (as u need)<br> -for index or stocks ex.Nifty 50<br> -for option (intitial+expiry+strike price) ex.NIFTY2372019800  |str   |
|tokenId        |token id of script (aas per api or exchange)           | token id      | str (contain int value)|
|buyP       |bought price of script         | buy price         |str (contain float value)|
sellP       |sell price of script       | sell price         |str (contain float value)|
|strikeP        |strike price for option        |strike price           |str (contain int value)|
|ltp       |last traded price of script         | ltp         |str (contain float value)|
|highP       |high created after script bought         | high price after buy         |str (contain float value)|
|lowP       |low created after script bought         | low price  after buy      |str (contain float value)|

### 3] candleData
```python
candlesData=[{"name":"NIFTY2372019800","timeFrame":"minute","data":[[dateTimeObj,"12.23","34.54","56.56","67.56"],[dateTimeObj,"23","34","34.56","12"]]}]
```
| ELEMENT KEY NAME      | DISCRIPTION       | VALUES      |TYPE     |
|-----------------      |-------------      |-------      |----     |
|name           |name of the script     |name of script (as u need)<br> -for index or stocks ex.Nifty 50<br> -for option (intitial+expiry+strike price) ex.NIFTY2372019800  |str   |
|timeFrame      |time frame of candle data      |refer:-constValues.TIME_FRAME     |str        |
|data       |data of candle     |[ [dateTimeObj,"o","h","l","c"],[dateTimeObj,"o","h","l","c"] ]        |list       |

### 4] valueTypeAllowed
*   list containing the allowed valueTypes (keys) in prices<br><br>
    EXAMPLE.
    ```python
    valueTypeAllowed=["tokenId","buyP","sellP","strikeP","ltp","highP","lowP"]
    ```

#   ATTRIBUTES AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|constValues    |tradeValues        |-      |init<br>validate_timeFrame      |
|prices     |tradeValues        |-      |init<br>set_tradeValue<br>get_tradeValue <br>remove_tradeValue_script      |
|candleData     |tradeValues        |-      |init<br>set_candles_data<br>get_candles_data        |
|valueTypeAllowed       |tradeValues        |-      |validate_valueType     |

## METHOADS
|METHOAD NAME       |METHOAD DISCRIPTION     |PARAMETR       |RETURN TYPE        |RETURN VALUE        |UPDATE        |
|----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|valid_value        |return valid value <br> -for "tokenId", "strikeP" :-str (containing int)<br> -for "buyP","ltp","highP","lowP":- str (containing float)       |valueType,value       |tuple       |(valueType,str(values ))        |none       |
|validate_valueType     |check wheather the given valueType is valid is not         |valueType      |boolean       |-       |raise Exception("invalid ValueType")     |
|validate_timeFrame     |check whwather the given timefrmae is valid or not     |timeFrame      |boolean       |-       |raise Exception("invalid timeFrame")        |
|validate_candle_data       |check wetaher the data is in proper format:-<br>[ [dateTimeObj,"o","h","l","c"],[dateTimeObj,"o","h","l","c"] ]       |noCandle,data      |boolean       |-       |-raise Exception("Number of candle doesn't match with candle in data")<br><br>-raise Exception("data should be in list")<br><br>raise Exception("missing dateTimeObj")<br><br>-raise Exception("data of price should be string")<br><br>-raise Exception("incomplete data , give data o,h,l,c")       |
|set_tradeValue         |set the value for script       |scname,valueType,value     |-       |-       |map "value" to "valueType" and set for given script name, in attribute prices      |
|get_tradeValue     |get the required value for script      |scname,valueType       |object        |{"name":scName,valueType:value}<br>None    |-        |
|remove_tradeValue_script       |remove the script of given scName from the Prices      |scName     |-      |-      |remove of script from prices       |
|set_candles_data       |set candle data to attribute candleData        |scname,timeFrame,noCandle,data      |-       |-       |set the candle data in candleData      |
|get_candles_data       |get the candle data        |scname,timeFrame       |object       |-data object<br>-none<br>ex.candlesData={"name":"NIFTY2372019800","timeFrame":"1min","data":[[dateTimeObj,"12.23","34.54","56.56","67.56"],[dateTimeObj,"23","34","34.56","12"]]}     |-       |

### ```parameter discription```
|PARAMTER NAME       |PARAMETER DISCRIPTION     |PARAMETER TYPE     |VALID VALUES        |
|----------------------|-----------------------|-----------------------|-----------------------|
|valueType        | value type for script       |str        |refer: tradeValues.valueTypeAllowed     |
|value      |value for given valueType      |str<br>int<br>float        |value      |
|scname     |script name        |str        |-stock or index name ex."NIFTY 50"<br>-option name ex.NIFTY2372019800
|timeFrame      |time frame for candle      |str        |refer:-constValues.TIME_FRAME     |
|noCandle   |parameter to ensure the required number of candle data is getting set      |int<br>str     |number of candle       |
|data       |candle data        |list       |[ [dateTimeObj,"o","h","l","c"],[dateTimeObj,"o","h","l","c"] ]<br><br>-latest data will at last       |

#   METHOADS AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|valid_value        |tradeValues        |-      |set_tradeValue     |
|validate_valueType     |tradeValues        |-      |set_tradeValue<br>get_tradeValue       |
|validate_timeFrame         |tradeValues        |-      |set_candles_data<br>get_candles_data       |
|validate_candle_data       |tradeValues        |-      |set_candles_data       |
|set_tradeValue     |test        |-      |ltp_thread_loop      |
|       |test       |-      |neo_order_status_track_thread      |
|get_tradeValue     |-        |-      |-      |
|remove_tradeValue_script| -        |-      |-      |
|set_candles_data       |test        |-      |candleData_loop      |
|get_candles_data       |-        |-      |-      |
