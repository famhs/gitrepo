nb1= float(input("Enter The First Number: "))
op= input("Enter The Operator: ")

def Addition():
   nb2= float(input("Enter The Second Number: "))
   print(nb1 + nb2)
 
def Subtraction():
   nb2= float(input("Enter The Second Number: "))
   print(nb1 - nb2)

def Multiplication():
   nb2= float(input("Enter The Second Number: "))
   print(nb1 * nb2)

def Division():
    nb2= float(input("Enter The Second Number: "))
    if nb2 == 0:
     print("Error")  
    else:
     print(nb1 / nb2)

def Factorial():
  if nb1 == 0:
    print(1)
  elif nb1 < 0: 
    print("Please Enter a Positive Number")
  else:
    i= 1
    fact = 1 
    while i <= nb1:
        fact = fact * i
        i += 1 
    print(fact) 
 
if op == "+":
   Addition()
 
elif op == "-":
   Subtraction()

elif op == "*":
   Multiplication()

elif op == "/":
   Division()

elif op == "!":
   Factorial()

else:
   print("Invalid Operator")



   