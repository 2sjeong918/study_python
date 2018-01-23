import threading_test

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += 1
    print('subthread', total)

t = threading_test.Thread(target=sum, args=(1, 1000000))
t.start()

print('main thread')