from alpine.test import test
import datetime
import threading
import time

testobj=test()

thcandle=threading.Thread(target=testobj.candleData_loop)
thbuy=threading.Thread(target=testobj.buy_loop)
thsell=threading.Thread(target=testobj.sell_loop)
thltp=threading.Thread(target=testobj.ltp_thread_loop)

hour = int(input("Enter start hour: "))
min = int(input("Enter start minute: "))

now = datetime.datetime.now()
target_time = datetime.datetime(now.year, now.month, now.day, hour, min)
print(f"Waiting for target time "+target_time.strftime("%Y-%m-%d %H:%M:%S")+".....")

while now < target_time:
    now = datetime.datetime.now()

thcandle.start()
thbuy.start()
thsell.start()
thltp.start()
