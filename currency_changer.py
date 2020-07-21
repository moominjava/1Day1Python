import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"


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


print("Hello! Please choose select a country by number:")
count = 0
for count, country_name in enumerate(country_list, start=0):
  print(f"# {count}" , country_name)
  
def choose_num():
  get_num = input("#: ")
  try:
    get_num = int(get_num)
    if count >= get_num >= 0:
      print(f"You chose {country_list[int(get_num)]}")
      print(f"The currency code is {currency_list[int(get_num)]}")
    elif get_num > count :
      print("Choose a number from the list.")
      choose_num()  
  except:
    print("That wasn't a number.")
    choose_num()
      

    
choose_num()
  
