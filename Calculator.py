


# adding 

def add(x1,x2):
  y = x1+x2
  return y 

# substract
def subtract(x1,x2):
  y=x1-x2
  return y 

# multiply
def multiply(x1,x2):
  y=x1*x2
  return y



# divide
def divide(x1,x2):
  y=x1/x2
  return y


# square
def square(x1,x2):
  y = x1**x2
  return y

def main():
  correct = True
  while correct:
    try:
      userinput = int(input("Please choose the following options by entering the corrrsponding number ( 1: adding, 2:subtracting 3:multiply 4:divide 5:square"))
    except:
      print("Please choose one of the valid options")
      userinput = int(input("Please choose the following options by entering the corrrsponding number ( 1: adding, 2:subtracting 3:multiply 4:divide 5:square"))

    if userinput <1 or userinput > 5:
      correct = True
      print("choose one of the valid options")
    else:
      correct = False
      try:
        x1 = int(input(" Enter first number"))
        x2 = int(input(" Enter second number"))
      except:
        print("Please enter a integer number")
        x1 = int(input(" Enter first number"))
        x2 = int(input(" Enter second number"))
        
      if userinput == 1:
        res = add(x1,x2)
      if userinput ==2:
        res = subtract(x1,x2)
      if userinput == 3:
        res = multiply(x1,x2)
      if userinput  ==4:
        res = divide(x1,x2)
      if userinput==5:
        res = square(x1,x2)
      
      print(res)





main()

