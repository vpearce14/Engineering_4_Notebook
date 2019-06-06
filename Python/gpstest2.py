from gps import *
import time
from time import gmtime, strftime

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
print 'latitude\tlongitude\ttime utc\t\t\talitude\tepv\tept\ttspeed\tclimb'

try:
	startTime = strftime("%Y-%m-%d-%H", gmtime())
	fb= open("/home/pi/Documents/SSAdata/Started" + str(startTime) + ".txt","a")
	while True:
		report = gpsd.next()
		if report['class'] == 'TPV':
			print getattr(report,'lat',0.0),"\t",
			dataAsInt = getattr(report,'lat',0.0)
			#fb= open("/home/pi/Documents/test","a")
			fb.write("latitude: ")
			fb.write(str(dataAsInt))
			fb.write('\t')
			#fb.close()
			print getattr(report,'lon',0.0),"\t",
			dataAsInt = getattr(report,'lon',0.0)
                        #fb= open("/home/pi/Documents/test","a")
			fb.write("longitude: ")
                        fb.write(str(dataAsInt))
                        fb.write('\n')
                        #fb.close()
			print getattr(report,'time',''),"\t",
			dataAsInt = getattr(report,'time','')
                        #fb= open("/home/pi/Documents/test","a")
			fb.write("Time: ")
                        fb.write(str(dataAsInt))
                        fb.write('\n')
                        #draw.text((2,2), 'time is: ' + str(dataAsInt), font=font, fill=255)
			print getattr(report,'alt','nan'),"\t",
			dataAsInt = getattr(report,'alt','nan')
                        #fb= open("/home/pi/Documents/test","a")
                        fb.write("Altitude: ")
			fb.write(str(dataAsInt))
                        fb.write('\n')
                        #fb.close()
			print getattr(report,'epv','nan'),"\t",
			print getattr(report,'ept','nan'),"\t",
			print getattr(report,'speed','nan'),"\t",
			print getattr(report,'climb','nan'),"\t"
		time.sleep(1)
except (KeyboardInterrupt, SystemExit):
	fb.close()
	print "Done.\nExiting."
