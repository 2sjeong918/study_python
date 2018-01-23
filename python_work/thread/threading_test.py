import threading, requests, time

def getHtml(url):
    resp = requests.get(url)
    # time.sleep(1)
    print(url, len(resp.text), resp.text)

t1 = threading.Thread(target=getHtml, args=('https://google.com',))
t1.start()

print('### end ###')