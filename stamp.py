#!/usr/bin/env python
import time, os, sys, calendar

# compartmentalization
# spot1 = os.getenv("HOME")
spot1 = "."
targetdata = spot1 + "/" + 'logs' + "/" + 'past'

# this grabs the the most recently written timestamp
with open(targetdata,'rb') as aim:
    aim.seek(-2, os.SEEK_END)
    while aim.read(1) != b"\n":
        aim.seek(-2, os.SEEK_CUR)
    finder = aim.readline()

# this grabs the current timestamp
action = int(round(time.time()))
muscle = open(targetdata, 'a')
muscle.write(str(action) + "\n")
muscle.close()

move = int(action)
stop = int(finder)

grabMonth = time.strftime("%b", time.localtime(action))
grabYear = int(time.strftime("%Y", time.localtime(action)))

if grabYear % 4 == 0 or grabYear % 100 == 0:
    Months = { 'Feb' : 29 }

# it needs to be mentioned: with accuracy in mind, is any consideration being given to leap years...
Months = { 'Jan' : 31, 'Feb' : 28, 'Mar' : 31, 'Apr' : 30, 'May' : 31, 'Jun' : 30, 'Jul' : 31, 'Aug' : 31, 'Sep' : 30, 'Oct' : 31, 'Nov' : 30, 'Dec' : 31 }
calcYear = Months['Jan'] + Months['Feb'] + Months['Mar'] + Months['Apr'] + Months['May'] + Months['Jun'] + Months['Jul'] + Months['Aug'] + Months['Sep'] + Months['Oct'] + Months['Nov'] + Months['Dec'] 

# print(calcYear) # the audience knows there is a better way to do this
# spanMonthly = Months[grabMonth]
# print(spanMonthly)

##################################
try:
    if sys.argv[1]:
        element = sys.argv[1]
except IndexError as problemo:
    element = 'straight'
    # print(problemo.args)
##################################

yrs = "year"
mos = "month"
wks = "week"
dz = "day"
hrs = "hours"
mins = "minutes"
secs = "seconds"
timespan = move - stop

if element == "milestone":
    if sys.argv[2]:
        datestring = sys.argv[2]

    benefits = str(datestring)
    yeargood = benefits[:4]
    mossgood = benefits[4:6]
    daysgood = benefits[6:8]
    movement = calendar.timegm(time.strptime(yeargood + '-' + mossgood + '-' + daysgood + ' 09:00:01', '%Y-%m-%d %H:%M:%S'))
    #movement = calendar.timegm(time.strptime('2021-06-30 17:00:01', '%Y-%m-%d %H:%M:%S'))
    
    flexometer = int(movement)
    timespan = move - flexometer

if timespan < 0:
    print("You have requested information regarding a date in the future, be patient")

    near = time.strftime("%a, %d %b %Y", time.localtime(movement))
    print("That is " + str(timespan * -1) + " seconds away and will come to pass on " + near)
if (timespan > 1) and (timespan <= 60):
    secs = "seconds"
    seen = str(timespan) + " " + str(secs)

if timespan > 60:
    durationMinutes = timespan / 60
    durationSeconds = timespan % 60
    seen = str(durationMinutes) + " " + str(mins) + " " + str(durationSeconds) + " " + str(secs)

if timespan > 3599:
    durationHours = timespan / 3600
    intermediateSeconds = timespan % 3600
    durationMinutes = intermediateSeconds / 60
    durationSeconds = intermediateSeconds % 60
    hrs = "hours"
    mins = "minutes"
    secs = "seconds"
    seen = str(durationHours) + " " + str(hrs) + " " + str(durationMinutes) + " " + str(mins) + " " + str(durationSeconds) + " " + str(secs)

if timespan > 86399:
    durationDays = timespan / 86400
    intermediateSeconds = timespan % 86400
    durationHours = intermediateSeconds / 3600
    intermediateSecondsMin = intermediateSeconds % 3600
    durationMinutes = intermediateSecondsMin / 60
    durationSeconds = intermediateSecondsMin % 60
    if durationDays >= 2:
        dz = "days"
    seen = str(durationDays) + " " + str(dz) + " " + str(durationHours) + " " + str(hrs) + " " + str(durationMinutes) + " " + str(mins) + " " + str(durationSeconds) + " " + str(secs)

if timespan > 604799:
    durationWeeks = timespan / 604800
    lastStandMain = timespan % 604800
    durationDays = lastStandMain / 86400
    intermediateSecondsHrs = lastStandMain % 86400
    durationHours = intermediateSecondsHrs / 3600
    intermediateSecondsMinutes = intermediateSecondsHrs % 3600
    durationMinutes = intermediateSecondsMinutes / 60
    durationSeconds = intermediateSecondsMinutes % 60
    if durationWeeks >= 2:
        wks = "weeks"
    if durationDays >= 2:
        dz = "days"
    
    seen = str(durationWeeks) + " " + str(wks) + " " + str(durationDays) + " " + str(dz) + " " + str(durationHours) + " " + str(hrs) + " " + str(durationMinutes) + " " + str(mins) + " " + str(durationSeconds) + " " + str(secs)

if timespan > 2592000:  #it is an estimate but hey ..

    durationMonths = timespan / 2592000
    intermediateWks = timespan % 2592000
    durationWeeks = intermediateWks / 604800
    intermediateDays = intermediateWks % 604800
    durationDays = intermediateDays / 86400
    intermediateSecondsHrs = intermediateDays % 86400
    durationHours = intermediateSecondsHrs / 3600
    intermediateSecondsMinutes = intermediateSecondsHrs % 3600
    durationMinutes = intermediateSecondsMinutes / 60
    durationSeconds = intermediateSecondsMinutes % 60
    if durationMonths >= 2:
        mos = "months"
    if durationWeeks >= 2:
        wks = "weeks"
    if durationDays >= 2:
        dz = "days"

    seen = str(durationMonths) + " " + str(mos) + " " + str(durationWeeks) + " " + str(wks) + " " + str(durationDays) + " " + str(dz) + " " + str(durationHours) + " " + str(hrs) + " " + str(durationMinutes) + " " + str(mins) + " " + str(durationSeconds) + " " + str(secs)

if timespan > 31536000:

    intYear = Months['Jan'] + Months['Feb'] + Months['Mar'] + Months['Apr'] + Months['May'] + Months['Jun'] + Months['Jul'] + Months['Aug'] + Months['Sep'] + Months['Oct'] + Months['Nov'] + Months['Dec'] # you do know that: year = 365 would have sufficed
    calYear = intYear * 86400
    durationYears = timespan / calYear
    intermediateMonths = timespan % calYear
    durationMonths = intermediateMonths / 2592000
    intermediateWks = intermediateMonths % 2592000
    durationWeeks = intermediateWks / 604800
    intermediateDays = intermediateWks % 604800
    durationDays = intermediateDays / 86400
    intermediateSecondsHrs = intermediateDays % 86400
    durationHours = intermediateSecondsHrs / 3600
    intermediateSecondsMinutes = intermediateSecondsHrs % 3600
    durationMinutes = intermediateSecondsMinutes / 60
    durationSeconds = intermediateSecondsMinutes % 60
    if durationYears >= 2:
        yrs = "years"
    if durationMonths >= 2:
        mos = "months"
    if durationWeeks > 1:
        wks = "weeks"
    if durationDays >= 2:
        dz = "days"

    seen = str(durationYears) + " " + str(yrs) + " " + str(durationMonths) + " " + str(mos) + " " + str(durationWeeks) + " " + str(wks) + " " + str(durationDays) + " " + str(dz) + " " + str(durationHours) + " " + str(hrs) + " " + str(durationMinutes) + " " + str(mins) + " " + str(durationSeconds) + " " + str(secs)

try:
    race = str(seen)
    print("you have been busy for " + race)
except NameError as problemo2:
    print("You are speculating about the future; You have not seen that timespan yet")
