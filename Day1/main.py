input_values = open("input.txt").read()

calory_lists = input_values.split('\n\n')
elf_stacks = []

for elf_list in calory_lists:
    food_values = elf_list.split('\n')

    total_food = 0
    for food in food_values:
        total_food += int(food)

    elf_stacks.append(total_food)

sorted_stacks = sorted(elf_stacks, reverse=True)

x = sorted_stacks[0] + sorted_stacks[1] + sorted_stacks[2]
print(x)
