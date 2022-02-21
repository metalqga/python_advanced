from collections import deque

special_words = "rosetuliplotusdaffodil"
rose = "rose"
tulip = "tulip"
lotus = "lotus"
daffodil = "daffodil"
vowels = deque(input().split())
consonant = input().split()
found_word = ""

while True:
    if found_word == "rose" or found_word == "tulip" or found_word == "lotus" or found_word == "daffodil":
        break

    vowel = vowels.popleft()
    if vowel in special_words:
        found_word += vowel

    cons = consonant.pop()
    if cons in special_words:
        found_word += cons

print(found_word)
