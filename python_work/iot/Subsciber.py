import paho.mqtt.client as mqtt
import Monitor

def on_connect(client, userdata, flags, rc):
    print('connected with result code' + str(rc))
    if rc == 0:
        client.subscribe('C:\python-work\pycharm\iot/#')
    else:
        print('연결실패', str(rc))


def on_message(client, userdata, msg):
    value = msg.payload.decode('utf-8')
    print('light', value)


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect('localhost', 1883)
    client.loop_forever()
except Exception as err:
    print('에러 : %s ' % err)
