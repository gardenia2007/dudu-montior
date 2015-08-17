import time
import os
import setting

# take a snapshot
snapshot_param = "raspistill -w 1024 -h 768 -q 90 -o now.jpg"
os.system(snapshot_param)

# genreate time key
key = time.strftime("%F_%T")

# qrstcl can be download from "http://developer.qiniu.com/docs/v6/tools/qrsctl.html"
# need copy qrsctl to /usr/bin first
# login to qiniu.com
login_param = "qrsctl login %s %s"%(setting.username, setting.password)
os.system(login_param)

# upload photo to qiniu.com
upload_param = "qrsctl put %s %s.jpg now.jpg"%(setting.bucket, key)
print upload_param
os.system(upload_param)

