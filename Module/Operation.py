import datetime
import time
import math
import random
import uuid
import string
import importlib

# DateTime And Time  Operation

def current_time_date():
    now = datetime.datetime.now()
    print(f"\n\nCurrent Date and Time: {now}")
    print("-----------------------------------")
    print("-----------------------------------")


def time_difference():
    dt1 = input("Enter the first date(YYYY-MM-DD):")
    dt2 = input("Enter the second date(YYYY-MM-DD):")
    dt1 = datetime.datetime.strptime(dt1, "%Y-%m-%d")
    dt2 = datetime.datetime.strptime(dt2, "%Y-%m-%d")
    gap = dt2 - dt1
    print("Diffrence:", gap)
    print("-----------------------------------")
    print("-----------------------------------")


def format_custom():
    my_dt = input("Enter any date (YYYY-MM-DD):")
    my_dt = datetime.datetime.strptime(my_dt, "%Y-%m-%d")
    converted_dt = my_dt.strftime("%d/%m/%Y")
    print("Formated Date:", converted_dt)
    print("-----------------------------------")
    print("-----------------------------------")


def stopwatch():
    input("\nPress Enter to start stopwatch...")
    start_time = time.time()
    input("Press Enter to stop stopwatch...")
    stop_time = time.time()
    total_time = stop_time - start_time
    print("\nTotal Time:", total_time, "seconds")
    print("-----------------------------------")
    print("-----------------------------------")


def countdown_timer():
    seconds = int(input("Enter countdown time in seconds: "))

    for i in range(seconds, 0, -1):
        print(f"\rCountdown: {i}   ", end="", flush=True)
        time.sleep(1)
    print()
    print("Time up!")
    print("-----------------------------------")
    print("-----------------------------------")


def datetime_timeop():
    print("Datetime and Time Operation:")
    while True:
        print("1.Display current date and time")
        print("2.Calculate difference between two dates /times")
        print("3.Formate date into custom format")
        print("4.Stopwatch")
        print("5.Countdown Timer")
        print("6.Back to Main Menu")

        choice = int(input("\nEnter your choice:"))

        if choice == 1:
            current_time_date()

        elif choice == 2:
            time_difference()

        elif choice == 3:
            format_custom()

        elif choice == 4:
            stopwatch()

        elif choice == 5:
            countdown_timer()

        elif choice == 6:
            break


# Mathematical Operation



def factorial():
    fact=int(input("\nEnter a Number: "))
    print("Factorial: ",math.factorial(fact))
    print("----------------------------------")
    print("----------------------------------")
def compound_interest():
    principal=float(input("Enter Principle amount: "))
    rate=float(input("Enter rate of interest(in %):"))
    time=float(input("Enter Time(in years):"))
    amount = principal * math.pow((1 + rate / 100), time)
    ci = amount - principal
    print("Compound Interest: ",ci)
    print("----------------------------------")
    print("----------------------------------")

def trigonometric():
    degree=int(input("Enter angle in degress: "))
    angle = math.radians(degree)
    sin=math.sin(angle)
    cos=math.cos(angle)
    tan=math.tan(angle)
    print("\nSin:",sin)
    print("Cos:",cos)
    print("Tan:",tan)
    print("----------------------------------")
    print("----------------------------------")
def geometric():
    print("1.Circle")
    print("2.Rectangle")
    print("3.Triangle")
    shape=int(input("\nChoose any shape:"))
    if shape == 1:
        radius=float(input("\nEnter Radius of circle:"))
        circle = math.pi * pow(radius, 2)
        print("Circle: ",circle)
    elif shape == 2:
        length=float(input("\nEnter length of Rectangle:"))
        width=float(input("Enter width of Rectangle:"))
        rectangle=length * width
        print("\nRectangle:",rectangle)
    elif shape == 3:
         base=float(input("\nEnter Base of Triangle:"))
         height=float(input("Enter Height of Triangle:"))
         Triangle=0.5*base*height   
         print("\nTriangle: ",Triangle)
         print("----------------------------------")
         print("----------------------------------")
def math_operation():
    print("Mathematical Operation")
    while True:
        
        print("1.Calculate Factorial")
        print("2.Solve Compound Interest")
        print("3.Trigonometric Calculation")
        print("4.Area of Geometric Shape")
        print("5.Back to Main Menu")
        choice = int(input("\nEnter your choice:"))

        if choice == 1:
            factorial()
        elif choice == 2:
            compound_interest()
        elif choice == 3:
            trigonometric()
        elif choice == 4:
            geometric()
        elif choice == 5:
            break
        
# Random Data Generation



def random_number():
    print(random.randint(1,100))
def random_list():
    no1=int(input("Enter Start Number:"))
    no2=int(input("Enter End Number:"))
    size=int(input("Enter Size:"))
    random_no=[]
    for i in range(size):
     random_no.append(random.randint(no1, no2))
    print("Random List:", random_no)

def random_password():
    length=int(input("Enter Password Length: "))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Random Password:", password)
def random_otp():
    length = 6
    otp = ""

    for i in range(length):
        otp = otp + str(random.randint(0, 9))

    print("Random OTP:", otp)




def random_data():
    print("Random Data Generation")

    while True:
        print("\n1.Generate Random Number:")
        print("2.Generate Random List:")
        print("3.Create Random Password:")
        print("4.Generate Random OTP:")
        print("5.Back to main menu")
        choice=int(input("\nEnter your choice:"))
        if choice == 1:
            random_number()
        elif choice == 2:
            random_list()
        elif choice == 3:
            random_password()
        elif choice == 4:
            random_otp()
        elif choice == 5:
            break




# Uique Identifier


def uuid_operation():
 print("Generate Unique Identifiers:")
 unique_id=str(uuid.uuid4())
 print("Generated UUID",unique_id)


 #  Dynamic Module Exploration

def module_attribute():

    print("Explore Module Attributes:")

    module_name = input("Enter module name to explore: ")

    module = __import__(module_name)

    print("Available Attributes in", module_name, "module:")
    print(dir(module))