from flask import Flask, render_template, redirect, url_for
import sys
sys.path.append('../GrovePi/Software/Python/')
from grovepi import *

app = Flask(__name__)
LED = 4
LEDStatus = False

#setup

pinMode(LED, "OUTPUT")

@app.route('/')
def index():
    if LEDStatus:
        return render_template('off.html')
    else:
        return render_template('off.html')

@app.route('/on')
def on():
    digitalWrite(LED, 1)
    LEDStatus = True
    return render_template('on.html')

@app.route('/off')
def off():
    LEDStatus = False
    digitalWrite(LED, 0)
    return render_template('off.html')