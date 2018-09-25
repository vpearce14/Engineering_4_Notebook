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
		if msg == "You clicked!":
                	GPIO.output(17,GPIO.HIGH)
			msg1 = 'h'
		elif msg == "You unclicked!":
			GPIO.output(17,GPIO.LOW)
			msg1 = 'l'
		msg = request.form.get("submitBtn2")
		if msg == "You clicked2!":
			GPIO.output(18,GPIO.HIGH)
			msg2 = 'h'
		elif msg == "You unclicked2!":
			GPIO.output(18,GPIO.LOW)
			msg2 = 'l'
	else:
		GPIO.output(17,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
		msg1 = 'l'
		msg2 = 'l'
	msg= msg1 + msg2
	return render_template("index.html", msg=msg)
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
