#Write a Python program to drop microseconds from datetime
from datetime import datetime
now=datetime.now()
#print(now)
print(now.strftime('%d/%m/%Y %H:%M:%S')) #21/02/2023 20:15:37