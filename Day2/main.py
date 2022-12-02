input_values = open("input.txt").readlines()

def calculate_victor(x, y):
    x = x.strip()
    y = y.strip()

    print("X: " + x + ", Y: " + y)
    if x == "A" and y == "X":
        print("you drew")
        return 3
    elif x == "B" and y == "Y":
        print("you drew")
        return 3
    elif x == "C" and y == "Z":
        print("you drew")
        return 3


    if x == "A" and y == "Y":
        print("you won")
        return 6
    elif x == "B" and y == "Z":
        print("you won")
        return 6
    elif x == "C" and y == "X":
        print("you won")
        return 6
    else:
        print("you lost")
        return 0

def point_value(y):
    values = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    return values[y.strip()]

def get_round_outcome(x, y):
    round_score = 0
    if y == "X":
        round_score += get_key_lose(x)
    elif y == "Y":
        round_score += get_draw_value(x)
        round_score += 3
    elif y == "Z":
        round_score += get_key_win(x)
        round_score += 6

    return round_score

    

def get_key_win(x):
    values = {
        "A": 2,
        "B": 3,
        "C": 1
    }
    return values[x]

def get_key_lose(x):
    values = {
        "A": 3,
        "B": 1,
        "C": 2
    }
    return values[x]

def get_draw_value(x):
    values = {
        "A": 1,
        "B": 2,
        "C": 3
    }
    return values[x]

score = 0
for line in input_values:
    x, y = line.split(" ")

    x = x.strip()
    y = y.strip()

    temp_score = 0
    #temp_score += calculate_victor(x, y)
    #temp_score += point_value(y)

    score += get_round_outcome(x, y)
    print(temp_score)
    #score += temp_score

print(score)