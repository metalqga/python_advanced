N=int(input())
matrix=[]
temp_list=[]
collisions= {}
counter=0
for i in range(N):
    figures=input()
    for i in range(len(figures)):
        temp_list.append(figures[i])
    matrix.append(temp_list)
    temp_list=[]

while True:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]=="K":
                intersections=0
                if (row+2)<=(N-1) and (col+1)<=(N-1):
                    if matrix[row + 2][col + 1] == "K":
                        intersections +=1


                if 0<=(row-2)<=(N-1) and 0<=(col-1)<=(N-1):
                    if matrix[row - 2][col - 1] == "K":
                        intersections += 1

                if 0<=(row-1)<=(N-1) and 0<=(col-2)<=(N-1):
                    if matrix[row - 1][col - 2] == "K":
                        intersections += 1


                if (row+1)<=(N-1) and (col+2)<=(N-1):
                    if matrix[row + 1][col + 2] == "K":
                        intersections += 1


                if (row+1)<=(N-1) and 0<=(col-2)<=(N-1):
                    if matrix[row + 1][col - 2] == "K":
                        intersections += 1

                if 0<=(row-1)<=(N-1) and (col+2)<=(N-1):
                    if matrix[row - 1][col + 2] == "K":
                        intersections += 1

                if 0<=(row-2)<=(N-1) and (col+1)<=(N-1):
                    if matrix[row - 2][col + 1] == "K":
                        intersections += 1

                if (row+2)<=(N-1) and 0<=(col-1)<=(N-1):
                    if matrix[row + 2][col - 1] == "K":
                        intersections += 1
                if intersections>0:
                    collisions[row, col] = intersections
    if len(collisions)==0:
        break
    best_counter=0
    best_coords=None
    for coords, count in collisions.items():
        if count>best_counter:
            best_counter=count
            best_coords=coords
    if best_counter>0:
        matrix[best_coords[0]][best_coords[1]]=0
        counter+=1
        collisions={}
print(counter)