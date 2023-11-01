from alpine.myKite import myKite
from alpine.constValues import constValues
from alpine.kiteTrade import KiteApp
from alpine.tradeValues import tradeValues
from alpine.common import common
from pytz import timezone
import datetime

const=constValues()
trade=tradeValues(const)
co=common(tradeValuesObj=trade)
fs=co.open_record_file()
fs.write("sdsdsdsdsddsd")


