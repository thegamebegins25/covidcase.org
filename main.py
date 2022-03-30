import datetime
import time
print("Days since start of COVID-19: " + str((datetime.datetime(2022, 3, 29) - datetime.datetime(2020, 1, 22)).days))
#all numbers are in days since 1/22/20
deaths = []
cases = []

def format(list):
    for i in list:
        list[list.index(i)] = int(i)
    return list

def get():
    global cases
    global deaths
    
    casesf = open(r"cases.csv", "r")
    casesl = casesf.read()
    cases = casesl.split(",")
    cases = format(cases)
    casesf.close()
    deathsf = open(r"deaths.csv", "r")
    deathsl = deathsf.read()
    deaths = deathsl.split(",")
    deathsf.close()
    deaths = format(deaths)

def set():
    global cases
    global deaths

    casesf = open(r"cases.csv", "w")
    write = ""
    for i in cases:
        write = write + str(i) + ","
    casesf.write(write)
    casesf.close()
    deathsf = open(r"deaths.csv", "w")
    write = ""
    for i in deaths:
        write = write  + str(i) + ","
    deathsf.write(write)
    deathsf.close()

def add():
    global cases
    global deaths

    print("Cases?")
    totalcases = int(input())
    print("Deaths?")
    totaldeaths = int(input())
    days = (datetime.datetime.now() - datetime.datetime(2020, 1, 22)).days
    get()
    for i in range(0, days - len(cases)):
        cases.append(totalcases)
        deaths.append(totaldeaths)
    print(cases)
    print(deaths)
    print("Are you satisfied? (y/n)")
    yn = input()
    if yn == "y":
        set()
    else:
        print("Rerun the program to try again.")

def compute(daysfromcovid):
    now = (datetime.datetime.now() - datetime.datetime(2020, 1, 22)).days
    casestotal = cases[daysfromcovid]
    try:
        casesbefore = cases[daysfromcovid-1]
    except Exception as e:
        casesbefore = 0
        print(e)
    casesonday = casestotal-casesbefore
    print(casesonday)
    deathsafter = deaths[now-1] - deaths[daysfromcovid]
    print(deathsafter)
    caused = deathsafter / casesonday
    return caused

get()
c = compute() #put day of case
print(c)