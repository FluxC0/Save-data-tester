import json 
import os
def is_file_empty(file_path):
    return os.stat(file_path).st_size == 0
# Example usage  
def file_check():
  file_path = 'save.json'
  if is_file_empty(file_path):
      return True
  else:
      return False

# take values from user and stuff them into a json file ONLY if after that file is read the file is empty.
def read():
  with open('save.json', 'r') as file:
    data = json.load(file)
    if  file_check() == False:
      print(data)
    else:
      print("no data found in file. beginning write function now.")


def write():
  data = {
    "foo": "bar",
  }
  with open('save.json','w') as file:
    json.dump(data, file)
read()