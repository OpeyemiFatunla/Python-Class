
user_input=input("Please enter any random number:  ")
 
n= int(user_input)
if n %2==0:
    print(f"{n} is EVEN")
else:
            if n %2==1:
                print(f"{n} is ODD")
                
                
                
# Q2
user_input_l = input("Please enter any random letter :  ")
l = (user_input_l)
if l.lower() in ("a", "e", "i", "o", "u"):
    print(f"{l}, is VOWEL")
elif l.upper() in ("A", "E", "I", "O", "U"):
    print(f"{l}, is VOWEL")

else:
    print(f"{l}, is CONSONANT")
    
    
    
#Q3
def which_shape():
    user_input = int(input("Please enter any number starting from 3:\n  "))
    if user_input ==3:
        print(f"{user_input}, is a Triangle")
        return user_input
        
    elif user_input ==4:
        print(f"{user_input}, is a Rectangle")
        
    elif user_input ==5:
        print(f"{user_input}, is a Pentagon")
        
    elif user_input ==6:
        print(f"{user_input}, is a Hexagon")
        
    else:
        if user_input >=7:
            print(f"{user_input}, is a Polygon")
        
        
        
        
which_shape()

#Q4

def number_of_days_in_month():
    user_input = input("Please state month name : \n").title()
    if user_input =="January":
        print("There are 31 days in January")
    if user_input =="February":
       print("There are 28 or 29 days in February")
       
 
    if user_input =="March":
        print("There are 31 days in March")
    if user_input =="April":
        print("There are 30 days in April")
    if user_input =="May":
        print("There are 31 days in May")
    if user_input =="June":
        print("There are 30 days in June")
    if user_input =="July":
        print("There are 31 days in July")
    if user_input =="August":
        print("There are 31 days in August")
    if user_input =="September":
        print("There are 30 days in September")
    if user_input =="October":
        print("There are 31 days in October")
    if user_input =="November":
        print("There are 30 days in November")
    if user_input =="December":
        print("There are 31 days in December")
   
   
number_of_days_in_month()  

#Q5
def type_of_triangle(a,b,c):
    if a==b and b==c:
        print("Triangle is Equilateral")
    elif a==b or b==c or a==c:
        print("Triangle is Isosceles")
    else:
        print("Triangle is Scalane")
        
        
        
type_of_triangle(3,3,4)
    
    
      
        
#Q6  
def what_to_wear():
    month=input("Please insert name of month ( e.g. January, February etc.): ")
    day =int(input("Please insert day: "))
    if month in ('January', 'February', 'March'):
        season = 'winter'
    elif month in ('April', 'May', 'June'):
        season = 'spring'

    elif month in ('July', 'August', 'September'):
        season = 'summer'
    else:
        season = 'autumn'

    if (month == 'March') and (day >21):
        print(f" In March, {day} we wear coat")
    elif (month == 'June') and (day > 21):
        print(f" In June, {day} we wear shirt")
    elif (month == 'September') and (day > 23):
        print(f" In September, {day} we wear T-shirt")
    elif (month == 'December') and (day > 21):
        print(f" In December, {day} we wear sweater")
    
    
what_to_wear()

#Q7

def which_day():
    user_input1 = input("Please input any of the following:  M, T, W, Th, F, S, Su: ").title()
    user_input2 = input("Is it at the begining of the week?:  ").title()
   
    Week =["M", "T", "W", "Th", "F", "S", "Su"]
    if user_input1=="M" and user_input2 == "Yes":
        print(f" {user_input1} is Monday, the second day of the Week")
    
    elif user_input1 =="T" and user_input2 == "No":
        print(f" {user_input1} is Tuesday, the third day of the Week")
        
    elif user_input1 =="W" and user_input2 == "No":
        print(f" {user_input1} is Wednesday, the fourth day of the Week")
        
    elif user_input1 =="Th" and user_input2=="No":
        print(f" {user_input1} is Thursday, the fifth day of the Week")
    elif user_input1 =="F" and user_input2 == "No":
        print(f" {user_input1} is Friday, the third day of the Week")
    
    elif user_input1 =="S" and user_input2=="No":
        print(f"{user_input1} is Saturday, the begining of the weekend")
    else:
        print(f"{user_input1} is invalid")
        
        
which_day()


#Q8
def Odds_Evens():
    user_input=int(input("Please input a positive number, i.e.; 1, 2, 3,...8, 20 etc.:  "))
    if user_input ==int(user_input):
        print(type(user_input))
    if user_input >= 0:
         print(f"{user_input} is a positive number!")
    if user_input== 0:
        print(f"{user_input} is Zero! ") 
   
    if user_input %2==0:
        print(f"{user_input} is Even")
    if user_input % 2 ==1:
        print(f"{user_input} is Odd")
   
    if user_input %2== 0 and user_input <=10:
        print(f"{user_input} is Even of 10")
    
    if user_input >=11 and user_input %2== 0 and user_input<=21:
            print(f"{user_input} is Even of 20")
        
        
        
        
        
Odds_Evens()

    
 #Q9    
def sum_of_Odds_and_Evens():
    user_input1= int(input("Please input an integer, i.e. 1, 2, 3, etc:  "))
    user_input2= int(input("Please input another integer, i.e. 1, 2, 3, etc:  "))
    sum = float(user_input1) + float(user_input2)
    if sum %2==0:
        print(" Sum is Even")
    if sum %2==1:
        print("Sum is Odd")
        
        
sum_of_Odds_and_Evens()
    
# Q10
def countdown():
    user_input1= int(input("Please input an integer, i.e. 1, 2, 3, etc:  "))
    user_input2= int(input("Please input another integer, i.e. 1, 2, 3, etc:  "))
    if user_input1 > user_input2:
        print("First number is greater than Second number")
    if user_input1==user_input2:
        print("Both numbers are equal. ") 
    if user_input1 < user_input2:
        print("Second number is greater than the First")
    for i in range(user_input1, user_input2-1, -1):
        print(i)
        
    
        
        
countdown()