from flask import Flask,request,render_template
import json
import urllib.request

app = Flask(__name__)

@app.route("/getweather",methods=["GET","POST"])
def weather():
    if request.method == "POST":
      location = request.form["city"]
    else:
      location = "new delhi"
    
    api = "68b35b7b7c5f8ed58e12e06855050e94"
    try:
       source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+location+'&APPID='+api).read()
       responseData = json.loads(source)
       data = {
          "country_code": str(responseData["sys"]["country"]),
          "city":str(responseData["name"]),
          "rain": str(responseData["weather"][0]["description"]),
          "temp":str(responseData["main"]["temp"]),
          "humidity":str(responseData["main"]["humidity"]),
          "wind": str(responseData["wind"]["speed"]),

       }
       return render_template("index.html",data=data)
    except Exception as e:
         return render_template("index.html", error=e)

@app.route("/")
def home():
   return render_template("index.html")

app.run(debug=True)