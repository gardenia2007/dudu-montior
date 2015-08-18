import time
import os
import setting
import picamera

# take a snapshot
# snapshot_param = "raspistill -w 1024 -h 768 -q 90 -o now.jpg"
# os.system(snapshot_param)
def take_snapshot():
	with picamera.PiCamera() as camera:
		camera.resolution = (1280, 720)
		camera.start_preview()
		time.sleep(2)
		camera.capture('now.jpg')
		camera.stop_preview()


# need copy `qrsctl` to /usr/bin first
# qrstcl can be download from "http://developer.qiniu.com/docs/v6/tools/qrsctl.html"
def upload_picture(local_name, key_name):
	# login to qiniu.com
	login_param = "qrsctl login %s %s"%(setting.username, setting.password)
	os.system(login_param)

	# upload photo to qiniu.com
	upload_param = "qrsctl put %s %s %s"%(setting.bucket, key_name, local_name)
	print upload_param
	os.system(upload_param)

if __name__ == "__main__":
	take_snapshot()
	# genreate time key
	key = time.strftime("%F_%T")
	upload_picture('now.jpg', key+'.jpg')


