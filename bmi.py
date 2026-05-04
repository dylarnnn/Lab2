def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight)) # + can only support string variable
    BMI = weight / (height ** 2) #use float() to convert str to float
    print("BMI = ", BMI)

    if BMI < 18.5:
        print("You are underweight")
        return -1
    elif BMI >= 18.5 and BMI <= 25.0:
        print("You are at normal weight")
        return 0
    elif BMI > 25.0:
        print("You are overweight")
        return 1
def main():
    calculate_bmi(weight = 57, height = 1.73)
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

if __name__ == '__main__':
    main()