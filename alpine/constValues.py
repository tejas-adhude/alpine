
class constValues:
    INSTRUMENT_INFO=[{"name":"NIFTY 50","symbol":"NIFTY","tokenId":"256265","exchange":"NSE","segment":"FO","type":"IN"}]

    OPTION_INFO=[{"name":"NIFTY 50","inSymbol":"NIFTY","exYear":"23","exMonthNum":"7","exMonthAlpha":"JUL","exDate":"27"}]

    API_CREDENTIAL=[{"apiName":"neo","userId":"xyz","password":"xyz"},{"apiName":"kite","userId":"ULH359","password":"Vaishu#2482@mk2","enctoken":"oZV/lsS2oM2Jt3hHIbxoXX6grAN/FEOriwZ1okMf5pu4yCWmRhpImne4tnHSW8+jd8ONo1XRfnpmUpqWE7bkMj8ahI59/tqTLbyUbYA9IB6kweWs25Gsog=="}]

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

