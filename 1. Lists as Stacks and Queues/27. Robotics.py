from collections import deque

robots = input().split(";")
robots_dic = {}
items = deque()
timer = 0
free_robots = []
busy_robots = {}
End = False
free_robot = False

for robot in robots:
    name, time = robot.split("-")
    robots_dic[name] = int(time)
    free_robots.append(name)
free_robots = deque(free_robots)

start_time = input().split(":")
hours = int(start_time[0])
mins = int(start_time[1])
seconds = int(start_time[2])
time_seconds = hours * 60 * 60 + mins * 60 + seconds

while True:

    timer += 1
    if not End:
        command = input()
    time_now = time_seconds + timer
    item = command

    for name, time in busy_robots.items():
        if time == time_now:
            free_robot = True
            free_robots.append(name)

    if item != "End":
        items.insert(0,item)

    if not free_robots and len(items)>1:
        items.append(items.popleft())

    if free_robot:
        del busy_robots[free_robots[-1]]
        free_robot = False

    if free_robots and items:
        name = free_robots[0]
        import time
        print(f'{name} - {items[0]} [{(time.strftime("%H:%M:%S", time.gmtime(time_now)))}]')
        free_robots.popleft()
        busy_robots[name] = (robots_dic[name] + time_now)
        items.popleft()

    if command == "End":
        End = True

    if End and len(items) == 0:
        break

# datetime.timedelta(seconds=time_now)
