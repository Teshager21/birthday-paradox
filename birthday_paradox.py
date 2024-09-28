import random 
from datetime import datetime,timedelta,date
def generateRandomBirthday(num):
    birth_days=[]
    end_date= date.today()
    for i in range(num):
        start_date= date.today()
        birth_date= (start_date-timedelta(days=random.randint(0,36500))).strftime('%b %d, %Y')
        birth_days.append(birth_date)
    print(birth_days)

def birthday_paradox():
    SAMPLE_SIZE=1
    num= int(input("How many birthdays should I generate?\n"))
    counter=0
    while True:
        generateRandomBirthday(num)
        counter+=1
        if counter>SAMPLE_SIZE: break
birthday_paradox()