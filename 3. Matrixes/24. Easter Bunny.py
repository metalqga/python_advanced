size=int(input())
matrix=[]
bunny_psn=()
eggs=0
result={}
result_direction= {}
coords=[]
hit_a_mine=False

for i in range(size):
    field=input().split()
    matrix.append(field)

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        element=matrix[row][col]
        if element=="B":
            bunny_psn=(row,col)
        elif element=="X":
            pass
        else:
            matrix[row][col]=int(element)

#right
for row in range(bunny_psn[0],bunny_psn[0]+1):
    for col in range(bunny_psn[1]+1,len(matrix[row])):
        element = matrix[row][col]
        if element=="X":
            hit_a_mine = True
            break
        else:
            eggs+=element
            coords.extend([[row,col]])
    if hit_a_mine:
        hit_a_mine=False
        break
if len(coords)>0:
    result_direction[eggs]="right"
    result[eggs]=coords
coords=[]
eggs=0

#left
for row in range(bunny_psn[0],bunny_psn[0]+1):
    for col in range(bunny_psn[1]-1,-1,-1):
        element = matrix[row][col]
        if element == "X":
            hit_a_mine = True
            break
        else:
            eggs += element
            coords.extend([[row, col]])
    if hit_a_mine:
        hit_a_mine=False
        break
if len(coords)>0:
    result_direction[eggs]="left"
    result[eggs]=coords
coords=[]
eggs=0

#down
for row in range(bunny_psn[0]+1,len(matrix)):
    for col in range(bunny_psn[1],bunny_psn[1]+1):
        element = matrix[row][col]
        if element == "X":
            hit_a_mine = True
            break
        else:
            eggs += element
            coords.extend([[row, col]])
    if hit_a_mine:
        hit_a_mine=False
        break
if len(coords)>0:
    result_direction[eggs]="down"
    result[eggs]=coords
coords=[]
eggs=0
#up
for row in range(bunny_psn[0]-1,-1,-1):
    for col in range(bunny_psn[1],bunny_psn[1]+1):
        element = matrix[row][col]
        if element == "X":
            hit_a_mine=True
            break
        else:
            eggs += element
            coords.extend([[row, col]])
    if hit_a_mine:
        hit_a_mine=False
        break
if len(coords)>0:
    result_direction[eggs]="up"
    result[eggs]=coords
coords=[]
eggs=0

if (max(result))==0 and len(result[0])<=1:
    result.pop(0)
    result_direction.pop(0)

print(result_direction[max(result_direction)])
for element in result[max(result)]:
    print(element)
print(max(result_direction))