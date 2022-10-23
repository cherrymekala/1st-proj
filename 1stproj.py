import math

print("\t\t\t Multi-usage Calculator \t\t\t")
def arith(a,b):
	choice=int(input("Enter options from 1 to 6 :- "))
	if(choice==1):
		print("Addition is :- ",a+b)
	elif(choice==2):
		print("Subtaction is :- ",a-b)
	elif(choice==3):
		print("Multiplication is:- ",a*b)
	elif(choice==4):
		print("Floor division is :- ",a//b)
	elif(choice==5):
		print("Normal Division is:- ",a/b)
	elif(choice==6):
		if(b!=0):
			print("Modulo is :- ",a%b)
	else:
		print("Sorry we can't help....!")
def mathe(a,b):
	choice=int(input("Enter options from 1 to 3:- "))
	if(choice==1):
		print("Power is :- ",a**b)
	elif(choice==2):
		print("Square root of ",a," is:- ",a**0.5," and ",b," is:- ",b**0.5)
	elif(choice==3):
		print("We are going to find logarithms for our operands :- ")
		print("Enter base for logarithm function :- ")
		base=int(input())
		print("Logaarithm of ",a," to base ",base,"is ",math.log(a,base)," and for ",b," is:- ",math.log(b,base))
	else:
		print("Sorry we can't help:- ")
def trig(a,b):
	choice=int(input("Enter options from 1 to 4:- "))
	if(choice==1):
		print("Sine of ",a," is ",math.sin(a)," and for ",b," is:- ", math.sin(b))
	elif(choice==2):
		print("Cosine of ",a," is :- ",math.cos(a)," and for ",b," is:- ",math.cos(b))
	elif(choice==3):
		print("Tangent of ",a," is :- ",math.tan(a)," and for ",b," is:- ",math.tan(b))
	elif(choice==4):
		print("Hypotanuse of ",a," and ",b," is :- ",math.hypot(a,b))
	else:
		print("Sorry we can't help...")
		
while(1):
	n=int(input("Enter value :- "))
	if(n!=1 and n!=2 and n!=3):
		break;
	print("Enter two operands :- ")
	a=eval(input())
	b=eval(input())
	if(n==1):
		print("We are going to perform arithmetic operations....")
		arith(a,b)
	elif(n==2):
		print("We are going to perform basic mathematic operations...")
		mathe(a,b)
	elif(n==3):
		print("We are going to perform trignometric functions....")
		trig(a,b)

		
