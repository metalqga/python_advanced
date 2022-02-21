from collections import deque

green_time = int(input())
free_window = int(input())
cars = deque()
counter = 0
time_left = 0

while True:

    command = input()
    if command == "END":
        break
    elif command == "green" and cars:
        time_left = green_time
        while time_left > 0 and cars:
            time = len(cars[0])
            if time <= time_left + free_window:
                cars.popleft()
                counter += 1
                time_left -= time

            else:
                print("A crash happened!")
                print(f"{cars[0]} was hit at {cars[0][time_left + free_window]}.")
                exit()

    else:
        cars.append(command)
print(f"Everyone is safe.")
print(f"{counter} total cars passed the crossroads.")
