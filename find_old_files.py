import os
import sys
import datetime
import datetime.datetime

age = input("Provide File Age: ")
dir_path = input("Provide Dir Path: ")
today = datetime.datetime.now
if not os.path.exists(dir_path):
    print("Please provide valid path: ")
    sys.exit(1)

if os.path.isfile(dir_path):
    print("Please provide valid Dir Path: ")
    sys.exit(2)

for files in os.listdir(dir_path):
    file_path = os.path.join(dir_path,files)
    if os.path.isfile(file_path):
        file_ctime = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        print(file_ctime)
        dif_days = (today-file_ctime).days
        print(dif_days)
        if dif_days > age:
           print(file_path,dif_days)