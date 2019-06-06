from gps import *
import time
#import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from BetterMPL import MPL3115A2
mpl3115a2 = MPL3115A2()
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

from time import gmtime, strftime
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
print ('latitude\tlongitude\ttime utc\t\t\talitude\tepv\tept\ttspeed\tclimb')

try:
        startTime = strftime("%Y-%m-%d-%H", gmtime())
        fb= open("/home/pi/Documents/SSAdata/Started" + str(startTime) + ".txt","a")
        while True:
                draw.rectangle((0,0,width,height), outline = 0, fill = 0)
                report = gpsd.next()
                if report['class'] == 'TPV':
                        mpl3115a2.control_alt_config()
                        mpl3115a2.data_config()
                        alt = mpl3115a2.read_alt_temp()
                        print ("Altitude : %.2f m"%(alt['a']))
                        print ("Temperature in Celsius : %.2f C"%(alt['c']))
                        print ("Temperature in Fahrenheit : %.2f F"%(alt['f']))
                        mpl3115a2.control_pres_config()
                        pres = mpl3115a2.read_pres()
                        print ("Pressure : %.2f kPa"%(pres['p']))
                        print (getattr(report,'lat',0.0),"\t", end = '')
                        dataAsInt = getattr(report,'lat',0.0)
                        #fb= open("/home/pi/Documents/test","a")
                        fb.write("latitude: ")
                        fb.write(str(dataAsInt))
                        fb.write('\t')
                        #fb.close()
                        print (getattr(report,'lon',0.0),"\t", end = '')
                        dataAsInt = getattr(report,'lon',0.0)
                        #fb= open("/home/pi/Documents/test","a")
                        fb.write("longitude: ")
                        fb.write(str(dataAsInt))
                        fb.write('\n')
                        #fb.close()
                        print (getattr(report,'time',''),"\t", end = '')
                        dataAsInt = getattr(report,'time','')
                        #fb= open("/home/pi/Documents/test","a")
                        fb.write("Time: ")
                        fb.write(str(dataAsInt))
                        fb.write('\n')
                        draw.text((10,10), "time is: " + str(dataAsInt), font=font, fill=255)
                        print (getattr(report,'alt','nan'),"\t", end = '')
                        dataAsInt = getattr(report,'alt','nan')
                        #fb= open("/home/pi/Documents/test","a")
                        fb.write("Altitude: ")
                        fb.write(str(dataAsInt))
                        fb.write('\n')
                        #fb.close()
                        print (getattr(report,'epv','nan'),"\t", end = '')
                        print (getattr(report,'ept','nan'),"\t", end = '')
                        print (getattr(report,'speed','nan'),"\t", end = '')
                        print (getattr(report,'climb','nan'),"\t", )
                disp.image(image)
                disp.display()
                time.sleep(1)
except (KeyboardInterrupt, SystemExit):
        fb.close()
        print ("Done.\nExiting.")
