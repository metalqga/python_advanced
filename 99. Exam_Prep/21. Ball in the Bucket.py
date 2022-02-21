matrix = []
bucket = []


def setup():
    for row in range(6):
        line = input().split()
        matrix.append(line)

    for row in range(6):
        for col in range(6):
            if matrix[row][col].isalpha():
                bucket.append(str((row, col)))
            elif matrix[row][col].isdigit():
                matrix[row][col] = int(matrix[row][col])


def check_prizes(score):
    prize = ""
    if 100 <= score <= 199:
        prize = "Football"
    elif 200 <= score <= 299:
        prize = "Teddy Bear"
    elif score >= 300:
        prize = "Lego Construction Set"
    if prize != "":
        print(f"Good job! You scored {score} points, and you've won {prize}.")
    else:
        print(f"Sorry! You need {100 - score} points more to win a prize.")


def shot(matrix, bucket):
    score = 0
    for _ in range(3):
        shot = input()
        if shot in bucket:
            for row in range(6):
                if matrix[row][int(shot[4])] != "B":
                    score += matrix[row][int(shot[4])]
            bucket.remove(shot)
    return score


setup()
check_prizes(shot(matrix, bucket))
