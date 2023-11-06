from alpine.test import test
import datetime
import threading
import time

testobj=test()

thTimeManager=threading.Thread(target=testobj.timeFrame_manager)
thcandle=threading.Thread(target=testobj.candleData_loop)
thbuy=threading.Thread(target=testobj.buy_loop)
thsell=threading.Thread(target=testobj.sell_loop)
thltp=threading.Thread(target=testobj.ltp_thread_loop)
thNeoOrderFeed=threading.Thread(target=testobj.neo_order_feed_thread)
thNeoOrderTrack=threading.Thread(target=testobj.neo_order_status_track_thread)

thcandle.start()
thbuy.start()
thsell.start()
thltp.start()
thNeoOrderFeed.start()
thNeoOrderTrack.start()

hour = int(input("Enter start hour: "))
min = int(input("Enter start minute: "))

now = datetime.datetime.now()
target_time = datetime.datetime(now.year, now.month, now.day, hour, min)
print(f"Waiting for target time "+target_time.strftime("%Y-%m-%d %H:%M:%S")+".....")

while now < target_time:
    now = datetime.datetime.now()

thTimeManager.start()