import random 
from datetime import datetime,timedelta,date
def generateRandomBirthday(num):
    birth_days=[]
    end_date= date.today()
    for i in range(num):
        start_date= date.today()
        birth_date= (start_date-timedelta(days=random.randint(0,36500))).strftime('%b %d, %Y')
        birth_days.append(birth_date)
    return birth_days


def birthday_paradox():
    TRIAL_REPETITION=100_000
    num= int(input("How many birthdays should I generate?\n"))
    counter=0
    repetition=0
    while True:
        sample=generateRandomBirthday(num)
        if len(sample)!=len(set(sample)): repetition+=1
        counter+=1
        if(counter%10_000==0): print(f'{counter} simulations ran....')
        if counter>TRIAL_REPETITION: 
            print(repetition, TRIAL_REPETITION)
            break
birthday_paradox()