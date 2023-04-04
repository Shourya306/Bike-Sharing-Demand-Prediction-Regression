from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods = ["POST"])
def predict():
    Month__8 = float(request.form['Month__8'])
    Hour = float(request.form['Hour'])
    Is_Weekend = float(request.form['Is_Weekend'])
    Month__12 = float(request.form['Month__12'])
    Month__7 = float(request.form['Month__7'])
    Month__11 = float(request.form['Month__11'])
    Season__Winter = float(request.form['Season__Winter'])
    Month__10 = float(request.form['Month__10'])
    Visibility = float(request.form['Visibility'])
    Humidity = float(request.form['Humidity'])
    Season__Autumn = float(request.form['Season__Autumn'])
    Month__9 = float(request.form['Month__9'])
    Month__4 = float(request.form['Month__4'])
    Wind_speed = float(request.form['Wind speed'])
    year = float(request.form['year'])
    Month__5 = float(request.form['Month__5'])
    Season__Summer = float(request.form['Season__Summer'])
    Month__3 = float(request.form['Month__3'])
    Temperature = float(request.form['Temperature'])
    Is_snowing = float(request.form['Is_snowing'])
    Season__Spring = float(request.form['Season__Spring'])
    Month__6 = float(request.form['Month__6'])
    Month__2 = float(request.form['Month__2'])
    Solar_Radiation = float(request.form['Solar Radiation'])
    Holiday = float(request.form['Holiday'])
    Is_raining = float(request.form['Is_raining'])
    Month__1 = float(request.form['Month__1'])
    Functioning_Day = float(request.form['Functioning Day'])
    

    result = model.predict(np.array([Month__8,Hour,Is_Weekend,Month__12,Month__7,Month__11,Season__Winter,Month__10,Visibility,Humidity,Season__Autumn,
    Month__9,Month__4,Wind_speed,year,Month__5,Season__Summer,Month__3,Temperature,Is_snowing,Season__Spring,Month__6,Month__2,Solar_Radiation,
    Holiday,Is_raining,Month__1,Functioning_Day]).reshape(1, -1))
    return render_template('result.html',result = result)

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8080)