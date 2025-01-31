from practice8 import format_msg
from datetime import datetime

employees=["Jonah","Amy","Garett","Cheyenne"]
store="Cloud 9"

for i in employees:
    msg=format_msg(my_name=i,my_store=store)
    print(datetime.now())
    print(msg)

    
  