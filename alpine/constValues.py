
class constValues:
    INSTRUMENT_INFO=[{"name":"NIFTY 50","symbol":"NIFTY","tokenId":"256265","exchange":"NSE","segment":"FO","type":"IN"}]

    OPTION_INFO=[{"name":"NIFTY 50","inSymbol":"NIFTY","exYear":"23","exMonthNum":"8","exMonthAlpha":"AUG","exDate":"10"}]

    API_CREDENTIAL=[{"apiName":"neo","userId":"xyz","password":"Piyush@2482","mobilenumber":"+917666942482","accessToken":"","consumerKey":"XwjXgUxpoDdJZ4azd0_Iz8J06uUa","consumerSecret":"R8Q4SUbKw74D_3IHMmM4sI6NgAoa"},{"apiName":"kite","userId":"ULH359","password":"Vaishu#2482@mk2","enctoken":"9BYElEBhw+7QtJg8Q7S2CG6hiuNA24+tgYOPn00Yw940MFduoXvJzr2ZoaUzAlZ1ZYGnS0Abj1+Ho4BWy156gtUYdCnMJukj4FlQ+sl7W+LXtGGpbc5b8w=="}]

    TIME_FRMAE={"minute":"1","5minute":"5","15minute":"15","30minute":"30"}

    def get_instrument_info(self,scName):
        for script in self.INSTRUMENT_INFO:
            if(script["name"]==scName):
                return script
            
        return None

    def get_option_info(self,scName):
        for script in self.OPTION_INFO:
            if(script["name"]==scName):
                return script
            
        return None
    
    def get_api_credential(self,apiName):
        for credential in self.API_CREDENTIAL:
            if(credential["apiName"]==apiName):
                return credential
            
        return None
    
    def get_time_frame(self):
        return self.TIME_FRMAE
    
# bought_flag=False #set to True when bought
# option_type_flag="" # True for call, False for put
# id=1

# th1=None
# th2=None

# kite_obj=None