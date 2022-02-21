punctuation = {"-", ",", ".", "!", "?"}
with open("text.txt") as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            reversed_line = " ".join(reversed(line.strip().split()))
            for ch in punctuation:
                reversed_line = reversed_line.replace(ch, "@")
            print(reversed_line)
