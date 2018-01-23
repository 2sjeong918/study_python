from datetime import datetime
import time

start = datetime.now()
ret = 0
for i in range(1000000):
    ret += i
print(ret)
end = datetime.now()
elapsed = end - start
print(elapsed)

start = datetime.now()

while True:
    tstamp = datetime.now()
    elapased = tstamp - start
    if elapased.total_seconds() > 0.5:
        break

print(type(elapased))
print('0.5초가 지났습니다.')

t1 = time.time()
print(t1)

mytime = time.localtime(t1)
print(mytime)

datetime()
