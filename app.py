from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def mainpage():
    return render_template("trial.html", result="",equal_sign="")


@app.route("/Converter",  methods=['POST', 'GET'])
def conv():
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()
    fromRate = request.form.get("fromVulue")
    toRate = request.form.get("toVulue")
    amount = request.form.get("amount")
    date = data['date']
    from_Value = data["rates"][str(fromRate)]
    to_Value = data["rates"][str(toRate)]
    result = round((to_Value / from_Value) * float(amount), 2)
    
    return render_template("trial.html", from_rate=fromRate, to_rate=toRate, amount=amount, result=result, date=date,equal_sign="=")


if __name__ == "__main__":
    app.run(debug=True)

