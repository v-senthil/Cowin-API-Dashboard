
from flask import Flask,render_template, request, make_response, Response, redirect, url_for
import requests
from urllib.request import urlopen
import json
import urllib3
import certifi
import urllib.request
from datetime import datetime



app = Flask(__name__)

#State and Date
@app.route("/")
def index():
	return render_template('pincode.html')


@app.route("/getpin", methods=['GET', 'POST'])
def getpin():
	if request.method == 'POST':
		date = request.form['date']
		pin = request.form['pincode']

		URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pin+"&date="+date		
		response = requests.get(URL)
		data = response.json()
		lenno = len(data['centers'])
		
		if response.ok:
			if lenno == 0:
				error = "No centers available in this pincode"
				return render_template('pincode.html', error=error)

			if lenno != 0:
				return render_template('pincodetable.html', data=data, lenno = lenno)
		else:
			error = "Error"
			return render_template('pincode.html', error=error)	
	else:
		return render_template('pincode.html')



#State and Date
@app.route("/district")
def district():
    return render_template('district.html')


@app.route("/getdistrict", methods=['GET', 'POST'])
def getdistrict():
	
	state = request.form['countrya']
	district = request.form['district']

	return(district)


#Error Handling
@app.errorhandler(404)
def error(error):
    return render_template("error.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
