from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
LEDpin = 4
LEDStatus = False

@app.route('/')
def index():
    if LEDStatus:
        return render_template('off.html')
    else:
        return render_template('off.html')

@app.route('/on')
def on():
    print "on"
    # digitalWrite(LED, 1)
    LEDStatus = True
    return render_template('on.html')

@app.route('/off')
def off():
    print "off"
    LEDStatus = False
    # digitalWrite(LED, 1)
    return render_template('off.html')