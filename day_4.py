# Project: advent_of_code
# File: day_4
# Author: Joinemm
# Date created: 04/12/18
# Python Version: 3.6.6

import re
from datetime import datetime

logs = []
with open("input_4.txt", "r") as input:
    for line in input:
        log = line.rstrip()
        logs.append(log)

events = []
for log in logs:
    event = log.split("] ")[1]
    timestamp = re.findall("\[([^]]+)\]", log)[0]
    time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    events.append((time, event))

guards = {}
for item in sorted(events):
    if item[1].startswith("Guard"):
        guard_id = re.findall("#(.*?) ", item[1])[0]
        if guard_id not in guards:
            guards[guard_id] = [0]*60
    elif item[1].startswith("falls"):
        sleeptime = item[0].minute
    elif item[1].startswith("wakes"):
        time_slept = item[0].minute - sleeptime
        for i in range(time_slept):
            guards[guard_id][sleeptime+i] += 1

most_sleep = 0
sleepiest_minute = 0
for guard in guards:
    print(guards[guard])
    total_sleep_time = sum(guards[guard])
    guard_max_val = max(guards[guard])
    if guard_max_val > sleepiest_minute:
        sleepiest_minute = guard_max_val
        frequent_sleeper = guard
    if total_sleep_time > most_sleep:
        most_sleep = total_sleep_time
        sleepiest_guard = guard

minute_most_slept = guards[sleepiest_guard].index(max(guards[sleepiest_guard]))
freq_minute_most_slept = guards[frequent_sleeper].index(sleepiest_minute)

print(int(sleepiest_guard)*int(minute_most_slept))
print(int(frequent_sleeper) * int(freq_minute_most_slept))
