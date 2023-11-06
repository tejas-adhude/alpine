# VALUES DISCRIPTION

## 1] INSTRUMENT_INFO

```python
INSTRUMENT_INFO=[{"name":"NIFTY 50","symbol":"NIFTY","tokenID":"256265","exchange":"NSE","segment":"FO","type":"IN"}]
```
### Elements
### all values are in upper case

| ELEMENT KEY NAME      | DISCRIPTION       | VALUES      |TYPE     |
|-----------------      |-------------      |-------      |----     |
|name           |name of the script     |name of script (as u need) or<br>-NONE     |str   |
|symbol     |symbol of script as per exchange or broker     |symbol of script or<br>-NONE  |str     |
|tokenId        |token id of script (in numerical form) as per exchange or broker       |token Id or<br>-NONE   | str (contain numerical value)      |
|exchange       |name of the exchnage   |NSE<br>BSE      |str       |
|segment        | segment of script         |FO:-future and option<br>F:-future<br>O:-option<br>        |str        |
|type       |type of script     |IN:-index<br>EQ:-Equity     |str     |

## 2] OPTION_INFO

```python
OPTION_INFO=[{"name":"NIFTY 50","inSymbol":"NIFTY","exYear":"23","exMonthNum":"7","exMonthAlpha":"JUL","exDate":"20"}]
```
### Elements
### all values are in upper case

| ELEMENT KEY NAME      | DISCRIPTION       | VALUES      |TYPE     |
|-----------------      |-------------      |-------      |----     |
|name           |name of the script     |name of script (as u need) or<br>-NONE     |str   |
|inSymbol       |initial symbol for option name     |intial symbol   |str     |
|exYear     | expiry year of option (in str numerical form)     |expiry year   |str (contain numerical value)       |
|exMonthNum     |expiary month of option (in str numerical form)    | expiry month (str numerical)     |str (contain numerical value)    |
|exMonthAlpha       |expiary month of option (in Alpha form)    | expiry month (str Aplha)   |str  |
|exDate     |expiry date for option     |expiry date of option (in str numerical form)     |str (contain numerical value)   |

## 3] API_CREDENTIAL

```python
API_CREDENTIAL=[{"apiName":"neo","userId":"xyz","password":"xyz"}]
```
### Elements

| ELEMENT KEY NAME      | DISCRIPTION       | VALUES      |TYPE     |
|-----------------      |-------------      |-------      |----     |
|apiName        |api name for identification        |api name       |str    |
|can contain more keys like userId, password etc. add values as per used and required for given api.|

## 4] TIME_FRMAE

```python
TIME_FRMAE={"minute":"1","5minute":"5","15minute":"15","30minute":"30"}
```
### discription
consist the key value pair of valid timeframe and there str int conversion in minute
<br><br>

#   ATTRIBUTES AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|INSTRUMENT_INFO    |constValues        |-       |get_instrument_info        |
|OPTION_INFO        |constValues        |-       |get_option_info    |
|API_CREDENTIAL     |constValues        |-       |get_api_credential     |
|TIME_FRMAE     |constValues        |-       |get_time_frame     |



#  METHOADS

|METHOAD NAME       |METHOAD DISCRIPTION     |PARAMETR       |RETURN TYPE        |RETURN VALUE        |UPDATE        |
|----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|get_instrument_info       |get instrment info from attribute INSTRUMENT_INFO   |scName   |-object<br>-None       |object for given script name from attribute INSTRUMENT_INFO       |-   |
|get_option_info        |get basic option info for given name , info like expiray etc.      |scName       |-object<br>-None     |object for given script name from attribute OPTION_INFO    |-   |
|get_api_credential     |get api credential     |apiName        |-object<br>-None   |object for given api name from attribute API_CREDENTIAL    |- |
|get_time_frame     |return attribute TIME_FRAME        |none       |object     |return attribute TIME_FRAME        |-       |


## ```parameter discription```
|PARAMTER NAME       |PARAMETER DISCRIPTION     |PARAMETER TYPE     |VALID VALUES        |
|----------------------|-----------------------|-----------------------|-----------------------|
|scName     |script name  |str      |script name       |
|apiName    |api name   |str    |api name       |

#   METHOADS AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|get_instrument_info        |myKite        |-      |get_historical_data    |
|get_option_info        |-        |-        |-      |
|get_api_credential     |myKite       |-      |set_user_credentials   |
|       |myNeo      |-      |set_neo_credential     |
|get_time_frame         |tradeValues        |-      |validate_timeFrame     |
|           |myKite       |-      |get_historical_data        |