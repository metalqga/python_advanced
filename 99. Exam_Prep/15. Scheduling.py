from collections import deque

jobs = [int(x) for x in input().split(", ")]
ind = int(input())
clock = 0
special_job = jobs[ind]

jobs = deque(jobs)

n = len(jobs)

for i in range(n):
    if min(jobs) == special_job and jobs.index(min(jobs)) == ind:
        clock += min(jobs)
        jobs.remove(min(jobs))
        break
    else:
        clock += min(jobs)
        if jobs.index(min(jobs)) < ind:
            ind -= 1
        jobs.remove(min(jobs))

print(clock)
