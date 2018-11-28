#����Adafruit_DHT
import Adafruit_DHT
import time
#����sensor�ͺ�
sensor = Adafruit_DHT.DHT22
#��������Ϊ27��BOARD����Ϊ13��
pin = 27

while True:
	try:
		hu, temp = Adafruit_DHT.read_retry(sensor,pin)
		print('temp:{0:0.1f} hu:{1}'.format(temp,hu))
		time.sleep(3)
	except RuntimeError as e:
		print("error\n{0}".format(e))
	except:
		print("error\nFailed to read sensor data!")