#!/usr/bin/python
import time
import os

#seeking improvement

# relics of strangeness:  coldLofty = '/home/userlessuser/logs/past'
spot1 = os.getenv("HOME")
spot2 = 'logs'
spot3 = 'past'
spot6 = spot1 + "/" + spot2 + "/" + spot3 # no comment

with open(spot6,'rb') as aim:
    #need catch error 'file not found'
    #also, throw an 'IF' file not found / write the file!
    aim.seek(-2, os.SEEK_END)
    while aim.read(1) != b"\n":
        aim.seek(-2, os.SEEK_CUR)
    grip = aim.readline()

action = int(round(time.time()))
muscle = open(spot6, 'a')
muscle.write(str(action) + "\n")
muscle.close()

move = int(action)
stop = int(grip)

wks = "week"
dz = "day"
hrs = "hours"
mins = "minutes"
secs = "seconds"
timespan = move - stop

if timespan <= 60:
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
    #i'm very angry, you won't like me when i'm angry

    seen = str(durationWeeks) + " " + str(wks) + " " + str(durationDays) + " " + str(dz) + " " + str(durationHours) + " " + str(hrs) + " " + str(durationMinutes) + " " + str(mins) + " " + str(durationSeconds) + " " + str(secs)

race = str(seen)
print "you have been busy for " + race
