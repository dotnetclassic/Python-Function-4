from datetime import date

def calculateBirthYear(dobYear):
    #calculate your age based on the current year and your birth year.
    today = date.today().year
    return today - int(dobYear)

def calculateAreaRectangle(length, width):
    #Write a program that calculates the area of a rectangle using length and width variables
    area = length * width #length * width
    return area

def calculateAreaCircle(radius):
    #Write a program that calculates the area of a circle.
    area = 3.14 * radius * radius #pi * r^2
    return area

def calculateAreaCube(side):
    #Write a program that calculates the area of the cube.
    area = 6 * side * side #6 * side^2
    return area
def calculateTemperature(fahrenheit):
    #Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
    celsius = (fahrenheit - 32) * 5/9 #(F - 32) * 5/9
    return celsius

def calculateMinutesAndSeconds(seconds):
    #Convert a given number of seconds into minutes and seconds using variables.
    minutes = seconds // 60
    remainingSeconds = seconds % 60 #1000 % 60 = 40
    return f"Minutes:{minutes} Seconds: {remainingSeconds}"

def calculatePercentage(totalMarks, obtainedMarks):
    percentage = (obtainedMarks / totalMarks) * 100
    return percentage

dobYear = input("Enter your birth year: ")
print(calculateBirthYear(dobYear))

length = 10
width = 20
print("Area of rectangle:", calculateAreaRectangle(10, 20))

radius = int(input("Enter radius: "))  #example radius of circle
print("Area of circle:", calculateAreaCircle(radius)) #314.0

side = int(input("Enter side: "))
print("Area of cube:", calculateAreaCube(side)) #600


fahrenheit = int(input("Enter temperature in Fahrenheit: ")) #100
print("Celsius:", calculateTemperature(fahrenheit)) #37.77777777777778

result = calculateMinutesAndSeconds(int(input("Enter seconds: ")))
print(result) #16 40

totalMarks = 100
obtainedMarks = 80
print("Percentage:", calculatePercentage(totalMarks, obtainedMarks)) #80.0%

