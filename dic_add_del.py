def add_to_dict(dic={}, key="", val=""):
  if type(dic) != dict :
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif key == "" or val == "":
    print("You need to send a word and a definition.")
  else :
    if key in dic :
      print(f"{key} is already on the dictionary. Wont' add.")
    else :
      dic[key] = val
      print(f"{key} has been added.")    


def get_from_dict(dic={}, key=""):
  if type(dic) != dict :
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif key == "" :
    print("You need to send a word to search for.")
  else :
    if key in dic :
      for key, val in dic.items():
        print(key, ": ", val)
    else :
      print(f"{key} was not found in this dict.")


def update_word(dic={}, key="", val="sample"):
  if type(dic) != dict :
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif key == "" or val == "sample" :
    print("You need to send a word and a definition to update.")
  elif key !="" and val == "sample" :
    if key in dic :
      for key, val in dic.items() :
        print(key, ": ", val)
  else :
    if key in dic :
      dic[key] = val
      print(f"{key} has been updated to: {val}")
    else :
      print(f"{key} is not on the dict. Can't update non-existing word.")


def delete_from_dict(dic={}, key=""):
  if type(dic) != dict :
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif key == "" :
    print("You need to spacify a word to delete.")
  elif key != "" :
    if key in dic :
      del(dic[key])
      print(f"{key} has been deleted.")
    else :
      print(f"{key} is not in this dict. Won't delete.")
  else :  
      print(f"{key} was not found in this dict.")
    