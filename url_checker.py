import requests
import os

def isit_down_url():
  print("Welcome to IsItDown.py!")
  get_url = input("Please write a URL or URLs you want to check. (separated by comma)\n")
  lower_url = get_url.lower()
  split_url = lower_url.split(',')
  url_list = []
  for input_url in split_url:
    if '.com' in input_url:
      if 'http://' in input_url:
        url_list.append(input_url.strip())
      else :
        url_list.append('http://' + input_url.strip())
    else :
      url_list.append(input_url.strip() + " is not a valid URL.")
  check_url(url_list)

def check_url(url_list):
  for check in url_list:
    if '.com' in check:
      r = requests.get(check)
      if requests.codes.ok == r.status_code:
        print(f"{check} is up!")
      else :
        print(f"{check} is down!")
    else : 
      print(check)
  over_answer()

def over_answer():
  answer = input("Do you want to start over? y/n")
  if answer == 'y':
    os.system('clear')
    isit_down_url()
  elif answer == 'n' :
    print("k. bye")
  else :
    print("that's not a valid answer") 
    over_answer()
      
isit_down_url()
