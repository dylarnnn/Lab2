def display_main_menu():
    getuserInput = "0"
    while getuserInput != "Y":
        print("Welcome to the temperature calculator")
        print("Press Y (in caps) if you would like to continue")
        getuserInput =  input("Answer: ")
    get_user_input()

def get_user_input():
    print("Before you enter the values, enter some numbers seperated by commas")
    print("For example: 5, 67, 32")
    rawInput = input("Enter the temperature numbers: ")
    rawList = rawInput.split(",")
    temperatureData = []
    for i in rawList:
        temperatureData.append(float(i))
    return temperatureData

def calc_average(temperatureData):
    total = 0.0
    total = sum(temperatureData)
    averageTemperature = total / len(temperatureData)
    print("Average temperature: ", averageTemperature)
    return averageTemperature


def find_min_max(temperatureData):
    max = 0
    min = 0
    for i in temperatureData:
        if max < temperatureData[i]:
            max = temperatureData[i]
        elif min > temperatureData[i]:
            min = temperatureData[i]
    print("Highest Temp. = ", max)
    print("Lowest Temp. = ", min)
    return max and min

def sort_temperature(temperatureData):
    sorted_list = sorted(temperatureData) # or temp_list.sort() and reverse=True if u want desecending order
    return sorted_list

def calc_median_temperature(sorted_list):
    median = (len(sorted_list) + 1) / 2
    median = int(median)
    median = sorted_list[median]
    print("median temp. = ", median)
    return median

def main():
    temperatureData = []
    sorted_list = []
    averageTemperature = 0
    display_main_menu()
    sort_temperature()
    calc_average()
    find_min_max()
    calc_median_temperature()
    

if __name__ == '__main__':
    main()