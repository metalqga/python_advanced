from collections import deque
robots_dic = {}
items = deque()
timer = 0
free_robots = deque()
busy_robots = {}
free_robot = False

robots = input().split(";")
for robot in robots:
    name, time = robot.split("-")
    robots_dic[name] = int(time)
    free_robots.append(name)

start_time = input().split(":")
hours = int(start_time[0])
mins = int(start_time[1])
seconds = int(start_time[2])
time_seconds = hours * 60 * 60 + mins * 60 + seconds

while True:

    command = input()
    if command!="End":
        items.append(command)
    else:
        break

while items:
    timer += 1
    time_now = time_seconds + timer

    if busy_robots:
        for name, time in busy_robots.items():
            if time <= time_now:
                free_robot = True
                free_robots.append(name)

    if free_robot:
        del busy_robots[free_robots[-1]]
        free_robot = False

    if not free_robots and len(items)>1:
        items.append(items.popleft())

    if free_robots:
        name = free_robots[0]
        import time
        print(f'{name} - {items[0]} [{(time.strftime("%H:%M:%S", time.gmtime(time_now)))}]')
        free_robots.popleft()
        busy_robots[name] = (robots_dic[name] + time_now)
        items.popleft()