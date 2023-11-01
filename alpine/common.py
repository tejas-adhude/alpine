from alpine.tradeValues import tradeValues
import datetime
import json

class common:

    tradeValues=None

    def __init__(self,tradeValuesObj):
           if not isinstance(tradeValuesObj,tradeValues): raise Exception("invalid parameter value for tradeValuesObj")
           self.tradeValues=tradeValuesObj
    
    def open_record_file(self):
            now = datetime.datetime.now()
            try:
                fs = open("Record.json", "a")
                fs.write("\nRecord start:\n"+now.strftime("%Y-%m-%d %H:%M:%S")+"\n")
            except: raise Exception("can't able to open Record File")
            return fs

    def sell(self,test):
            scName=test.scName
            opName=test.opName

            buyT=test.BUYT
            sellT=test.SELLT
            
            scBuyP=self.tradeValues.get_tradeValue(scName,"buyP")["buyP"]
            scBuyP=float(scBuyP)

            scSellP=self.tradeValues.get_tradeValue(scName,"sellP")["sellP"]
            scSellP=float(scSellP)
            
            scHighP=self.tradeValues.get_tradeValue(scName,"highP")
            scLowP=self.tradeValues.get_tradeValue(scName,"lowP")

            scPal=scSellP-scBuyP

            if(scHighP):
                scHighP=scHighP["highP"]
                scHighP=float(scHighP)
                scPalH=scHighP-scBuyP
                scHighP=round(scHighP,2)

            if(scLowP):
                scLowP=scLowP["lowP"]
                scLowP=float(scLowP)
                scPalH=scSellP-scLowP
                scLowP=round(scLowP,2)


            opBuyP=self.tradeValues.get_tradeValue(opName,"buyP")["buyP"]
            opBuyP=float(opBuyP)

            opSellP=self.tradeValues.get_tradeValue(opName,"sellP")["sellP"]
            opSellP=float(opSellP)

            opHighP=self.tradeValues.get_tradeValue(opName,"highP")["highP"]
            opHighP=float(opHighP)

            opPal=opSellP-opBuyP
            opPalH=opHighP-opBuyP

            jsonobj={
                "scNAME":scName,
                "opNAME":opName,

                "BUYT":buyT,
                "SELLT":sellT,

                "scBUYP":round(scBuyP,2),
                "scSELLP":round(scSellP,2),
                "scHIGHP":scHighP,
                "scLOWP":scLowP,
                "scPAL":round(scPal,2),
                "scPALH":round(scPalH,2),

                "opBUYP":round(opBuyP,2),
                "opSELLP":round(opSellP,2),
                "opHIGHP":round(opHighP,2),
                "opPAL":round(opPal,2),
                "opPALH":round(opPalH,2)
            }
            temp = json.dumps(jsonobj)
            print(temp)

            fs = open("Record.json", "a")
            fs.write(temp+"\n")
            fs.close()