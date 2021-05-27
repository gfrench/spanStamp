#!/usr/bin/python
import time, os, sys, calendar

# put the different parts of this in referenced capsules
#spot1 = os.getenv("HOME")
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

##################################
try:
    if sys.argv[1]:
        element = sys.argv[1]
except IndexError as problemo:
    element = 'straight'
    # print(problemo.args)
##################################

wks = "week"
dz = "day"
hrs = "hours"
mins = "minutes"
secs = "seconds"
timespan = move - stop

if element == "milestone":
    if sys.argv[2]:
        datestring = sys.argv[2]
    #flexometer = int(datestring converted to seconds)
    #timespan = move - flexometer
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
    #structure = (stop * 1) + (timespan * 1)
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
    #believe it, mr late man
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

try:
    race = str(seen)
    print("you have been busy for " + race)
except NameError as problemo2:
    print("You are speculating about the future; You have not seen that timespan yet")
