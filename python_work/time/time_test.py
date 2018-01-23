from time import localtime, strftime

t = localtime()
print(t)
print(t.tm_year, t.tm_mon)

logfile = 'test.log'
def writelog(logfile, log):
    time_stamp = strftime('%Y-%m-%d %X\t', localtime())
    log = time_stamp + log + '\n'

    with open(logfile, 'a') as f:
        f.writelines(log)

writelog(logfile, 'logfile')

weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

t = localtime()
week =weekdays[t.tm_wday]

print(week)