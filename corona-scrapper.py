from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask("SuperScrapper")

url = "https://www.seoul.go.kr/coronaV/coronaStatus.do"

@app.route("/")
def home():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  status_seoul = soup.find("div", {"class": "status-seoul"}).find("h4").find("span").text
  new_wrap_num = soup.find("div", {"class": "cell1"}).find("div").find("p", {"class": "counter"}).text
  num1 = soup.find("div", {"class": "num1"}).find("p", {"class": "counter"}).text
  num8 = soup.find("div",{"class": "cell5"}).find("div", {"class": "num8"}).find("p", {"class": "counter"}).text
  num9 = soup.find("div", {"class": "num9"}).find("p", {"class": "counter"}).text
  return render_template("home.html",
  status_seoul = status_seoul,
  new_wrap_num = new_wrap_num,
  num1 = num1,
  num8 = num8,
  num9 = num9)


app.run(host="0.0.0.0")
