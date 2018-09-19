from flask import Flask, render_template,request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "P2ST":
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(18,GPIO.LOW)
                msg = request.form.get("submitBtn1")
	elif request.method == "POST":
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(17,GPIO.LOW)
		msg = request.form.get("submitBtn2")
	else:
		GPIO.output(17,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
		msg = "No click yet."
	return render_template("index.html", msg=msg)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
