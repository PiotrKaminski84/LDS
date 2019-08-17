# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 08:40:32 2019

@author: Kaminskipi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:30:23 2019

@author: Kaminskipi
"""

from flask import Flask
from flask import request
from flask import send_file
from flask import render_template
from motor_controller_arduino import MotorController
from p_meter_ctrl import PowerMeterCtrl

app = Flask(__name__)
mc=MotorController()
#p_meter = PowerMeterCtrl(1,2,mc)

@app.route("/")
def hello():
    return render_template('main.html')

@app.route("/open")
def open_one():
    number=request.args.get('name')    
    mc.open_motor(int(number))
#    reading=p_meter.get_reading()
    return render_template("open.html",name=number,power=reading)

@app.route("/open_menu")
def open_menu():
    mc.close_all()
    return render_template("open.html")

@app.route("/get_references")
def get_ref1():
    mc.close_all()
    return render_template("ref1.html")

@app.route("/ref")
def get_ref():
    mc.close_all()
    r=mc.get_pwr()    
    return render_template("ref.html",ref=r.decode("utf-8"))

#@app.route("/losses")
#def get_losses():
#    r=p_meter.get_meas()
#    return render_template("change.html",res=r)

if __name__=='__main__':
    app.run(host = "0.0.0.0")