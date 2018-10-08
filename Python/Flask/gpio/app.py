from flask import Flask, render_template,request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "POST":
                msg1 = request.form.get("submitBtn1")
		msg2 = request.form.get("submitBtn2")
		GPIO.output(17,bool(msg1))
		GPIO.output(18,bool(msg2))
	else:
		GPIO.output(17,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
	msg1 = GPIO.input(17)
        msg2 = GPIO.input(18)
	msg= str(msg1) + str(msg2)
	print msg
	return render_template("index.html", msg=msg, led1=msg1, led2=msg2)
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
