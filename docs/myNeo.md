# CONSTRUCTOR 
```python
__init__(self,constValuesObj)
```
|PARAMETER  |PARAMETER DISCRIPTION     |PARAMETER TYPE     |PARMETER VALUE     |  
|--------------|--------------|--------------|--------------|
|constValuesObj        |instance of constValues class    |instance     |constValues instance     |

### updates
* set the constValues instance to attribute contValues
* initilize the orderId to empty list


## Attributes
### 1] orderIds
```python
[{"tradingSymbol"="NIFTY23JUL184400CE","orderNo":"1234567","status":"completed","executeTime"=" "}]
```

| ELEMENT KEY NAME      | DISCRIPTION       | VALUES      |TYPE     |
|-----------------      |-------------      |-------      |----     |
|tradingSymbol      |trading symbol of order script     |trading symbol as per broker or exchange       |str        |
|orderNo        |order number of order      |order number       |str        |
|status         |order status of placed order       |order status ex.completed      |str        |
|executeTime        |order excuted time if excuted at exchange      |time in string     |str        |


## Attributes

|NAME       |DISCRIPTION        |TYPE       |VALUE      |
|------------|------------|------------|------------|
|constValues        |instance of class constValues      |instance       |instance       |
|password       |password of neo account        |str    |password (alphanumerical)      |
|mobilenumber       |mobile number of neo account       |str        |mobile number with country code   |
|accessToken        |access token of neo api        |str        |access token       |
|consumerKey        |consumer key of neo api        |str        |consumerKey        |
|consumerSecret     |consumer secret key of neo api     |str        |consumer secrt     |
|neo        |instance of neo api        |instance       |instance       |
|orderIds       |order id with its trading symbol and the order status and executed time       |list       |trading symbol and order id        |


#   ATTRIBUTES AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|constValues        |myNeo      |-      |set_neo_credential     |
|password       |myNeo      |-      |set_neo_credential<br>authenticate_neo    |
|mobilenumber       |myNeo      |-      |set_neo_credential<br>authenticate_neo     |
|accessToken        |myNeo      |-      |set_neo_credential<br>authenticate_neo     |
|consumerKey        |myNeo      |-      |set_neo_credential<br>authenticate_neo     |
|consumerSecret     |myNeo      |-      |set_neo_credential<br>authenticate_neo     |
|neo        |myNeo      |-      |authenticate_neo<br>temp_neo_auth<br>place_order<br>order_feed<br>trade_report     |
|orderIds       |myNeo      |-      |place_order<br>order_feed      |
|       |test       |-      |neo_order_status_track_thread      |

## METHOADS
|METHOAD NAME       |METHOAD DISCRIPTION     |PARAMETR       |RETURN TYPE        |RETURN VALUE        |UPDATE        |
|----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|on_message<br>on_error<br>on_open<br>on_close      |parameters for the neo api constructor     |massage for particular event        |-     |-      |-      |
|set_neo_credential     |set the neo credential values      |-      |-      |-      |set value to attributes:password,mobilenumber,accessToken,consumerKey,consumerSecret<br><br>raise Exception("Credential not found!")       |
|authenticate_neo       |authenticate to the neo api        |-      |-      |-      |set value to attribute: neo        |
|place_order        |place order to neo     |tradingSymbol<br>transectionType<br>quantity<br>price<br>orderType<br>exchangeSegment<br>product<br>validity<br>amo<br>disclosedQuantity<br>marketProtection<br>pf<br>triggerPrice<br>tag      |tuple      |(boolean,dict)<br>(False,None)<br><br>(True,{"tradingSymbol":tradingSymbol,"price":price,"transectionType":transectionType,"orderNo":orderNo})     |orderIds       |
|order_feed_message     |paramter for order feed websocket (on_massage)     |message        |-      |-      |orderIds       |
|order_feed_reconnect       |reconnect to the order field after connection closed       |-      |-      |-      |-      |
|order_feed     |connect to order feed  |-      |-      |-      |-      |
|trade_report       |get trade report of neo trade          |orderId        |dict or None     |{"orderId":data["nOrdNo"],"tradingSymbol":data["sym"],"avgPrice":data["avgPrc"],"tranType":data["trnsTp"],"completeTime":data["hsUpTm"]}     |-      |

### ```parameter discription```
|PARAMTER NAME       |PARAMETER DISCRIPTION     |PARAMETER TYPE     |VALID VALUES        |
|----------------------|-----------------------|-----------------------|-----------------------|
|message        |message for particular event       |unknown        |-      |
|tradingSymbol<br>transectionType<br>quantity<br>price<br>orderType<br>exchangeSegment<br>product<br>validity<br>amo<br>disclosedQuantity<br>marketProtection<br>pf<br>triggerPrice<br>tag      |check the neo api docs     |check neo api docs         |-      |
|orderId        |order id of neo order      |str (numeric )     |valid order id     |

#   METHOADS AND ITS USE
|NAME       |USE CLASS    |USE CLASS ATTRIBUTES       |USE CLASS METHOAD       |
|------------------|------------------|------------------|------------------|
|on_message<br>on_error<br>on_open<br>on_close  |myNeo      |-      |authenticate_neo       |
|set_neo_credential     |myNeo      |-      |authenticate_neo       |
|authenticate_neo       |-      |-      |-      |
|place_order        |test      |-      |buy_loop      |
|       |test       |-      |sell_loop      |
|order_feed_message     |myNeo      |-      |order_feed     |
|order_feed_reconnect       |myNeo      |-      |order_feed     |
|order_feed     |test      |-      |neo_order_feed_thread      |
|trade_report       |test      |-      |neo_order_status_track_thread      |