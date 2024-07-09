import re

def read_input():
    result = 0

    # read input
    with open('input.txt', 'r') as file:
        for index, line in enumerate(file, start=1):
            # if possible -> record index
            if is_feasible(line):
                result = result + index
            print(result)

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

    print(feasible)

    return feasible
        



if __name__ == "__main__":
    global red_possession, green_possession, blue_possession
    red_possession, green_possession, blue_possession = 12, 13, 14
    result = read_input()

    print(result)
