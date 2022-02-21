punctuation = {"-", ",", ".", "!", "?", "\'"}
with open("text.txt") as file:
    for row, line in enumerate(file):
        count_chars = 0
        count_punctuation = 0
        for ch in line:
            if ch.isalpha():
                count_chars += 1
            if ch in punctuation:
                count_punctuation += 1
        print(f"Line {row + 1}: {line.strip()} ({count_chars})({count_punctuation})")
