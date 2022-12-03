input_values = open("input.txt").readlines()
rucksacks = input_values

def convert_char(x):
    i = ord(x)
    if i >= 97:
        print(x + "Lowercase: " + str(i - 96))
        return i - 96
    elif i >= 65 and i < 97:
        print(x + "Uppercase: " + str(i - 37))
        return i - 38
    
    return -1

def day3_part1():
    priority_sum = 0
    for rucksack in rucksacks:
        rucksack_length = len(rucksack)
        first_half, second_half = rucksack[:rucksack_length//2].strip(),rucksack[rucksack_length//2:].strip()

        objects_in_bag = []
        for letter in first_half:
            objects_in_bag.append(letter)

        mutual_objects = []
        for letter in second_half:
            if letter in objects_in_bag:
                mutual_objects.append(letter)

        priority_sum += convert_char(mutual_objects[0])

    print(priority_sum)

def create_groups():
    x = 0
    groups = []
    group = []
    for rucksack in rucksacks:
        x += 1

        group.append(rucksack)

        if x == 3:
            x = 0
            groups.append(group)
            group = []
    
    return groups

def day3_part2():
    groups = create_groups()
    priority_sum = 0
    for group in groups:

            letters = []
            for letter in group[0]:
                letters.append(letter)

            mutual_letters = []
            for letter in group[1]:
                if letter in letters:
                    mutual_letters.append(letter)
            
            final_letters = []
            for letter in group[2]:
                if letter in mutual_letters:
                    final_letters.append(letter)

            priority_sum += convert_char(final_letters[0])

    print(priority_sum)

            



if __name__ == '__main__':
    #day3_part1()
    day3_part2()

# capital letters 65 - 90
# lowercase letters 97 - 122
