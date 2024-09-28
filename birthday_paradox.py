import random 
import statistics
from statistics import mode
from datetime import datetime,timedelta,date
def generateRandomBirthday(num):
    birth_days=[]
    end_date= date.today()
    for i in range(num):
        start_date= date.today()
        birth_date= (start_date-timedelta(days=random.randint(0,36500))).strftime('%b %d')
        birth_days.append(birth_date)
    return birth_days


def birthday_paradox():
    TRIAL_REPETITION=100_000
    num= int(input("How many birthdays should I generate?\n"))
    counter=0
    repetition=0
    print(generateRandomBirthday(num))
    print(f'The date {mode(generateRandomBirthday(num))} is repeated!')
    print('Generating 23 random birthdays 100,000 times...')
    if input('Press Enter to begin...''')=='':
        while True:
            sample=generateRandomBirthday(num)
            if len(sample)!=len(set(sample)): repetition+=1
            counter+=1
            if(counter%10_000==0): print(f'{counter} simulations ran....')
            if counter>TRIAL_REPETITION: 
                print(repetition, TRIAL_REPETITION)
                break
birthday_paradox()