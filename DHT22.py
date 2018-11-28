#引入Adafruit_DHT
import Adafruit_DHT
import time
#定义sensor型号
sensor = Adafruit_DHT.DHT22
#定义引脚为27（BOARD编码为13）
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