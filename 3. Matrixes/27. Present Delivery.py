m = int(input())
n = int(input())
territory = []
santa_psn = []
naughty_psn = []
nice_psn=[]
cookie_psn=[]
counter=0

for i in range(n):
    line = input().split()
    territory.append(line)

for row in range(len(territory)):
    for col in range(len(territory[row])):
        if territory[row][col] == "S":
            santa_psn.append(row)
            santa_psn.append(col)

        elif territory[row][col] == "X":
            naughty_psn.append([row,col])

        elif territory[row][col] == "V":
            nice_psn.append([row,col])

        elif territory[row][col] == "C":
            cookie_psn.append([row,col])

def is_valid_psn(a,b,c):
    if a<0 or a>c:
        return False
    if b<0 or b>c:
        return False
    else:
        return True

while m>0:

    command=input()
    territory[santa_psn[0]][santa_psn[1]] = "-"
    if command == "up":
        santa_psn[0] -= 1
    elif command == "down":
        santa_psn[0] += 1
    elif command == "right":
        santa_psn[1] += 1
    elif command == "left":
        santa_psn[1] -= 1

    if command=="Christmas morning":
        territory[santa_psn[0]][santa_psn[1]] = "S"
        break

    if is_valid_psn(santa_psn[0],santa_psn[1],n):
        territory[santa_psn[0]][santa_psn[1]] = "S"

        if santa_psn in cookie_psn:
            territory[santa_psn[0]][santa_psn[1]] = "-"
            if territory[santa_psn[0]+1][santa_psn[1]] in "XV" and m>0:
                m-=1
                if territory[santa_psn[0]+1][santa_psn[1]] == "V":
                    counter+=1
                territory[santa_psn[0]+1][santa_psn[1]] = "-"
                if ([santa_psn[0]+1, santa_psn[1]]) in nice_psn:
                    nice_psn.remove([santa_psn[0]+1, santa_psn[1]])
            if territory[santa_psn[0]-1][santa_psn[1]] in "XV"and m>0:
                m-=1
                if territory[santa_psn[0]-1][santa_psn[1]] == "V":
                    counter+=1
                territory[santa_psn[0]-1][santa_psn[1]] = "-"
                if ([santa_psn[0]-1, santa_psn[1]]) in nice_psn:
                    nice_psn.remove([santa_psn[0]-1, santa_psn[1]])
            if territory[santa_psn[0]][santa_psn[1]+1] in "XV"and m>0:
                m-=1
                if territory[santa_psn[0]][santa_psn[1]+1] == "V":
                    counter+=1
                territory[santa_psn[0]][santa_psn[1]+1] = "-"
                if ([santa_psn[0], santa_psn[1]+1]) in nice_psn:
                    nice_psn.remove([santa_psn[0], santa_psn[1]+1])
            if territory[santa_psn[0]][santa_psn[1]-1] in "XV"and m>0:
                m-=1
                if territory[santa_psn[0]][santa_psn[1]-1] == "V":
                    counter+=1
                territory[santa_psn[0]][santa_psn[1]-1] = "-"
                if ([santa_psn[0], santa_psn[1]-1]) in nice_psn:
                    nice_psn.remove([santa_psn[0], santa_psn[1]-1])
        elif santa_psn in nice_psn:
            m-=1
            counter += 1
            nice_psn.remove([santa_psn[0],santa_psn[1]])

    else:
        continue

territory[santa_psn[0]][santa_psn[1]] = "S"

if m==0 and len(nice_psn)>0:
    print("Santa ran out of presents!")

for row in range(len(territory)):
    for col in range(len(territory[row])):
        print(territory[row][col], end=" ")
    print()
if len(nice_psn)==0:
    print(f"Good job, Santa! {counter} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_psn)} nice kid/s.")