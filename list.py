days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def is_on_list(days_list, val_day):
  return val_day in days_list

def get_x(days_list, num_day):
  return days_list[num_day]

def add_x(days_list, add_day):
  return days_list.append(add_day)

def remove_x(days_list, remove_day):
  return days_list.remove(remove_day)