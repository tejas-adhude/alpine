# CONSTRUCTOR 
```python
__init__(self,constValues)
```
|PARAMETER  |PARAMETER DISCRIPTION     |PARAMETER TYPE     |PARMETER VALUE     |  
|--------------|--------------|--------------|--------------|
|constValues        |object of constValues class    |instance     |constValues instance     |

### updates
* set the constValues instance to attribute contValues

## Attributes

|NAME       |DISCRIPTION        |TYPE       |VALUE      |
|------------|------------|------------|------------|
|userId     |user id of kite        |str    |user id
|password       |password of kite       |str    |password   |
|twofa      |two factor authentication code for kite     |str    |two factor auth code  |
|enctoken       |enctoken for kite       |str    |enctoken  |
|constValues        |instance of ConstValues    |instance       |instance   |
|kiteApp        |instance of KiteApp        |instace        |instance   |

#   ATTRIBUTES AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|userId     |myKite       |-      | set_user_credentials<br>authenticate_user  |     
|password       |myKite       |-      |set_user_credentials<br>authenticate_user  |      
|twofa      |myKite       |-      |set_user_credentials<br>authenticate_user  |     
|enctoken       |myKite       |-      |set_user_credentials<br>authenticate_user  |      
|constValues        |myKite       |-      | get_historical_data   |    
|kiteApp        |myKite       |-      |authenticate_user<br>get_historical_data<br>get_ltp        |

## METHOADS
|METHOAD NAME       |METHOAD DISCRIPTION     |PARAMETR       |RETURN TYPE        |RETURN VALUE        |UPDATE        |
|----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|set_user_credentials       |set the user credential for kite       |-       |-   |-       |userId<br>password <br>twofa<br>enctoken<br><br>raise Exception("Credential not found!")        |
|authenticate_user      |authenticate the kiteApp   |-      |-      |-      |kiteApp
|get_historical_data        |get histrocial data    |nowTime,timeFrame,scName,<br>tokenId,noCandle,toDateTime,<br>fromDateTime        |tuple        |(scName,tokenId,candle data)     |-raise Exception("kite user not authenticated.")<br><br>-raise Exception("either pass the scName or tokenId")<br><br>-raise Exception("need parameter combination of : (noCandle,toDateTime) or (noCandle,fromDateTime) or(toDateTime,fromDateTime)")      |
|get_ltp        |get ltp    |inNames     |obj      |{"inName1":"ltp","inName2":"ltp"}       |-      |

### ```parameter discription```
|PARAMTER NAME       |PARAMETER DISCRIPTION     |PARAMETER TYPE     |VALID VALUES        |
|----------------------|-----------------------|-----------------------|-----------------------|
|nowTime        |reference current time     |datetime instance      |-  |
|timeFrame      |valid time frame for candle data       |str        |constValues.TIME_FRAME |
|scName     |script name |str       |valid script name  |
|tokenId        |token id for script        |str<br>int        |valid token id      |
|noCandle       |no of candle required      |str<br>int     |-      |
|toDateTime     |upto time for candle data      |datetime instance      |-      |
|fromDateTime       |from time for candle data      |datetiem instance     |-       |
|inNames     |instrument names        |list    |ex.<br>["NSE:NIFTY 50","NFO:NIFTY2361517800CE"]       |


#   METHOADS AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|set_user_credentials   |myKite       |-      |authenticate_user      |-      |-      |-      |
|authenticate_user  |
|get_historical_data    |-      |-      |-      |
|get_ltp    |-      |-      |-      |