import re

def read_input():
    result = 0

    # read input
    with open('input.txt', 'r') as file:
        for index, line in enumerate(file, start=1):
            # if possible -> record index
            # if is_feasible(line):
            #     result = result + index
            result = power_calc(line) + result

    return result

# check each line (game) if it is feasible
# return type: boolean
def is_feasible(line):
    global red_possession, green_possession, blue_possession
    
    # detect the number of each color and store them as a list (number, color)

    data_list = re.findall(r'(\d+)\s(red|green|blue)', line)
    
    feasible = True

    for data in data_list:
        number, color = data
        if color == "red":
            if int(number) > red_possession:
                feasible = False
        
        elif color == "green":
            if int(number) > green_possession:
                feasible = False
        
        elif color == "blue":
            if int(number) > blue_possession:
                feasible = False


    return feasible
        
def power_calc(line):
    # get the smallest possible number of each color

    # get a list of numbers for each color
    red_list = re.findall(r'(\d+)\sred', line)
    green_list = re.findall(r'(\d+)\sgreen', line)
    blue_list = re.findall(r'(\d+)\sblue', line)

    # convert them into int
    red_list = [int(num) for num in red_list]
    green_list = [int(num) for num in green_list]
    blue_list = [int(num) for num in blue_list]

    red_max = max(red_list)
    green_max = max(green_list)
    blue_max = max(blue_list)


    return red_max*green_max*blue_max




if __name__ == "__main__":
    global red_possession, green_possession, blue_possession
    red_possession, green_possession, blue_possession = 12, 13, 14
    result = read_input()

    print(result)
