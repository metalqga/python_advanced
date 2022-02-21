territory = []
my_psn = []
my_temp_psn = []
target_psn = []
shot_target_psn = []
shot_target = 0

for i in range(5):
    line = input().split()
    territory.append(line)

for row in range(len(territory)):
    for col in range(len(territory[row])):
        if territory[row][col] == "A":
            my_psn.append(row)
            my_psn.append(col)
        elif territory[row][col] == "x":
            target_psn.append([row, col])


def is_valid_psn(a, b, c):
    if a < 0 or a > c:
        return False
    if b < 0 or b > c:
        return False
    else:
        return True


commands = int(input())
for _ in range(commands):
    command = input().split()
    if len(my_temp_psn)==0:
        my_temp_psn.append(my_psn[0])
        my_temp_psn.append(my_psn[1])

    if "move" in command:
        steps = int(command[2])
        if "up" in command:
            my_psn[0] -= steps
        elif "down" in command:
            my_psn[0] += steps
        elif "right" in command:
            my_psn[1] += steps
        elif "left" in command:
            my_psn[1] -= steps

        if is_valid_psn(my_psn[0], my_psn[1], 4):
            if territory[my_psn[0]][my_psn[1]] == ".":
                territory[my_psn[0]][my_psn[1]] = "A"
                territory[my_temp_psn[0]][my_temp_psn[1]]="."
                my_temp_psn=[]
                my_temp_psn.append(my_psn[0])
                my_temp_psn.append(my_psn[1])
            else:
                my_psn =[]
                my_psn.append(my_temp_psn[0])
                my_psn.append(my_temp_psn[1])
        else:
            my_psn = []
            my_psn.append(my_temp_psn[0])
            my_psn.append(my_temp_psn[1])

    else:
        if "up" in command:
            for i in range(my_psn[0], -1, -1):
                if territory[i][my_psn[1]] == "x":
                    territory[i][my_psn[1]] = "."
                    shot_target_psn.append([i, my_psn[1]])
                    shot_target += 1
                    break
        elif "down" in command:
            for i in range(my_psn[0], 5):
                if territory[i][my_psn[1]] == "x":
                    territory[i][my_psn[1]] = "."
                    shot_target_psn.append([i, my_psn[1]])
                    shot_target += 1
                    break
        elif "right" in command:
            for i in range(my_psn[1], 5):
                if territory[my_psn[0]][i] == "x":
                    territory[my_psn[0]][i] = "."
                    shot_target_psn.append([my_psn[0], i])
                    shot_target += 1
                    break
        elif "left" in command:
            for i in range(my_psn[1], -1, -1):
                if territory[my_psn[0]][i] == "x":
                    territory[my_psn[0]][i] = "."
                    shot_target_psn.append([my_psn[0], i])
                    shot_target += 1
                    break

    if shot_target == len(target_psn):
        print(f"Training completed! All {shot_target} targets hit.")
        break
if shot_target < len(target_psn):
    print(f"Training not completed! {len(target_psn) - shot_target} targets left.")

for element in shot_target_psn:
    print(element)

print(territory)