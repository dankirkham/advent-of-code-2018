from collections import defaultdict
import re

with open('input4.in', 'r') as f:
    log = sorted(map(lambda l: l.rstrip('\n'), f))

# [1518-07-23 23:58] Guard #223 begins shift
# [1518-08-21 00:59] wakes up
# [1518-05-09 00:43] wakes up
# [1518-06-26 00:16] falls asleep

schedules = defaultdict(lambda : [0] * 60)
current_guard = None

for entry in log:
    guard_change = re.search("Guard #(\d+) begins shift", entry)

    if guard_change:
        current_guard = int(guard_change.group(1))
        continue

    wake = re.search("(\d{2})\] wakes", entry)

    if wake:
        minute = int(wake.group(1))
        for i in range(minute, 60):
            schedules[current_guard][i] -= 1
        continue

    sleep = re.search("(\d{2})\] falls", entry)

    if sleep:
        minute = int(sleep.group(1))
        for i in range(minute, 60):
            schedules[current_guard][i] += 1
        continue

# Strategy 1
max_hours = 0
for guard, schedule in schedules.items():
    hours_slept = sum(schedule)
    if hours_slept > max_hours:
        max_hours = hours_slept
        max_guard = guard

hours = schedules[max_guard].index(max(schedules[max_guard]))

print(max_guard * hours)

# Strategy 2
max_frequency = 0
for guard, schedule in schedules.items():
    for minute, frequency in enumerate(schedule):
        if frequency > max_frequency:
            max_frequency = frequency
            max_guard = guard
            max_minute = minute

print(max_guard * max_minute)
