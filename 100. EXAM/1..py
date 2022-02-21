from collections import deque

rose = "rose"
tulip = "tulip"
lotus = "lotus"
daffodil = "daffodil"
vowels = deque(input().split())
consonants = input().split()
found_word = ""

while True:
    if len(rose) == 0:
        found_word = "rose"
        break
    if len(tulip) == 0:
        found_word = "tulip"
        break
    if len(lotus) == 0:
        found_word = "lotus"
        break
    if len(daffodil) == 0:
        found_word = "daffodil"
        break
    if not vowels or not consonants:
        break
    # make it delete all occurences
    vowel = vowels.popleft()
    if vowel in rose:
        rose = rose.replace(vowel, "")
    if vowel in tulip:
        tulip = tulip.replace(vowel, "")
    if vowel in lotus:
        lotus = lotus.replace(vowel, "")
    if vowel in daffodil:
        daffodil = daffodil.replace(vowel, "")

    cons = consonants.pop()

    if cons in rose:
        rose = rose.replace(cons, "")
    if cons in tulip:
        tulip = tulip.replace(cons, "")
    if cons in lotus:
        lotus = lotus.replace(cons, "")
    if cons in daffodil:
        daffodil = daffodil.replace(cons, "")

if found_word != "":
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
