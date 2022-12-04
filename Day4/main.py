input_values = open("input.txt").readlines()

x = 0
for line in input_values:
    x_value_x = int(line.split(',')[0].split('-')[0].strip())
    x_value_y = int(line.split(',')[0].split('-')[1].strip())

    y_value_x = int(line.split(',')[1].split('-')[0].strip())
    y_value_y = int(line.split(',')[1].split('-')[1].strip())

    x_diff = x_value_y - x_value_x
    y_diff = y_value_y - y_value_x

    x_list = list(range(x_value_x, x_value_y + 1))
    y_list = list(range(y_value_x, y_value_y + 1))

    # part 2
    if not set(x_list).isdisjoint(y_list):
        x += 1
    # end part 2
    
    # part 1
    #if (x_diff >= y_diff):
        #if y_value_x >= x_value_x and y_value_y <= x_value_y:
        #    x += 1
    #else:
        #if x_value_x >= y_value_x and x_value_y <= y_value_y:
        #    x += 1
    # end part 1

print(x)

