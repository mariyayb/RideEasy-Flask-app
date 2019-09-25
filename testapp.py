#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:00:19 2019

@author: m
"""

from flask import Flask
from flask import request
from flask import render_template
#sys.path.insert(/)
from return_prob import return_prob

app = Flask(__name__)

# here's the homepage
@app.route('/')
def homepage():
    return render_template("form.html")


@app.route('/result', methods=['POST','GET'])
def results():
    # if request.method == 'POST':
    title=request.form['title']
    #title=request.form.get('title')
    category = request.form['category']
    price = request.form['currentprice']
    year = request.form['year']
    #conditiondescription = request.form('conditiondescription')
    numPics = request.form['numPics']
    zipcode = request.form['zipcode']
    forSaleBy = request.form['forSaleBy']
    warranty = request.form['warranty']
    vehicleTitle = request.form['vehicleTitle']
    type_bike = request.form['type']
    fuelType = request.form['fuelType']
    mileage = request.form['mileage']
    engine = request.form['engine']
    color = request.form['color']
    make = request.form['make']
    bike_model = request.form['model']
    title = request.form['title']
    subtitle = request.form['subtitle']
    trim = request.form['trim']
    
    price = float(price)
    
    returned = return_prob(title,category,price,year,numPics,zipcode,forSaleBy,warranty,vehicleTitle,type_bike,fuelType,mileage,engine,color,make,bike_model,subtitle,trim)
    prob = returned[0]
    reasons = returned[1] #a list of reasons
    reason1 = reasons[0]
    reason2 = reasons[1]
    reason3 = reasons[2]
    prob = round(prob,3)
    perc = round(100*prob,2)
    if prob <= 0.35:
        probcat = 'L'
        probcatlong = 'Your listing is unlikely to end with a sale at the price $' + "%.2f" % price# +'.'
    elif prob <= 0.7:
        probcat = 'M'
        probcatlong = 'Your listing has a borderline chance of ending with a sale at the price $' + "%.2f" % price# + '.'
    else:
        probcat = 'H'
        probcatlong = 'Your listing is very likely to end with a sale at the price $' + "%.2f" % price# + '.'

    if price < 500:
        probcat = 'H'
        probcatlong = 'Your listing is very likely to end with a sale at the price $' + "%.2f" % price# + '.'

    elif price > 15000:
        probcat = 'L'
        probcatlong = 'Your listing is unlikely to end with a sale at the price $' + "%.2f" % price# +'.'
    else:
        probcat = probcat

    return render_template("results.html", probcatlong = probcatlong, probcat = probcat, probability = prob, currentprice = price, percent=perc, reason1 = reason1, reason2 = reason2, reason3 = reason3)
#return title


    
if __name__ == "__main__":
    app.run(debug=True)
  
