from flask import Flask, render_template,request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "POST":
                msg = request.form.get("submitBtn1")
		print msg
		if msg != None:
			if msg[0]=='1':
				if msg[1] == 'l':
					GPIO.output(17,GPIO.LOW)
				if msg[1] == 'h':
					GPIO.output(17,GPIO.HIGH)
			if msg[0]=='2':
				if msg[1] == 'l':
					GPIO.output(18,GPIO.LOW)
				if msg[1] == 'h':
					GPIO.output(18,GPIO.HIGH)
	else:
		GPIO.output(17,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
	msg1 = GPIO.input(17)
        msg2 = GPIO.input(18)
	msg= str(msg1) + str(msg2)
	return render_template("index.html", msg=msg)
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
