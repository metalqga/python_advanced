text=input()
counter=dict()

for i in range(len(text)):
    if text[i] not in counter:
        counter[text[i]]=1
    else:
        counter[text[i]]+=1

for element,count in sorted(counter.items()):
    print(f"{element}: {count} time/s")