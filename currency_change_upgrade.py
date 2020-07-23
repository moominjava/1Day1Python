import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

url = "https://www.iban.com/currency-codes"
currency_url ="https://transferwise.com/gb/currency-converter"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

get_table = soup.find("tbody")

country_list = []
currency_list = []

for tr in get_table.find_all('tr'):
  td_list = list(tr.find_all('td'))
  country_name = td_list[0].text
  currency_code = td_list[2].text
  if currency_code != "":
    country_list.append(country_name)
    currency_list.append(currency_code)


print("Welcome to CurrencyConvert 2000\n")
count = 0
for count, country_name in enumerate(country_list, start=0):
  print(f"#{count}" , country_name)
  
def choose_country():
  print("\n Where are you from? Choose a country by number.\n")
  get_num = input("#: ")
  try:
    get_num = int(get_num)
    if count >= get_num >= 0:
      print(f"{country_list[int(get_num)]}\n")
      first_currency = currency_list[int(get_num)]
      print("Now choose another country.\n")
      select_country(first_currency)
    elif get_num > count :
      print("Choose a number from the list.")
      choose_country()  
  except:
    print("That wasn't a number.")
    choose_country()


def select_country(first_currency):
  get_num_2 = input("#: ")
  try:
    get_num_2 = int(get_num_2)
    if count >= get_num_2 >= 0:
      print(f"{country_list[int(get_num_2)]}\n")
      secound_currency = currency_list[int(get_num_2)]
      print(f"How many {first_currency} do you want to convert to {secound_currency}?")
      currency_converter(first_currency, secound_currency)
    elif get_num_2 > count :
      print("Choose a number from the list.")
      select_country(first_currency)
  except:
    print("That wasn't a number.")
    select_country(first_currency)
    

def currency_converter(first_currency, secound_currency):
  amount = input()
  try:
    amount = int(amount)
    if type(amount) == int:
      result = requests.get(f"{currency_url}/{first_currency}-to-{secound_currency}-rate?amount={amount}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find("span", {"class": "text-success"}).text
      results = round(amount * float(results))
      print(f"{first_currency}{amount} is", format_currency(f"{results}", f"{secound_currency}", locale="ko_KR"))

  except:
    print("That wasn't a number.\n")
    print(f"How many {first_currency} do you want to convert to {secound_currency}?")
    currency_converter(first_currency, secound_currency)
      
choose_country()