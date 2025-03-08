def add(nu1,nu2):
      answer=nu1+nu2
      print(str(nu1) + "+" + str(nu2) + "="+ str(answer))

def sub(nu1,nu2):
      answer=nu1-nu2
      print(str(nu1)+ "-"+str(nu2)+"="+str(answer))

def mul(nu1,nu2):
      answer=nu1*nu2
      print(str(nu1)+ "*"+str(nu2)+"="+str(answer))
      
def div(nu1,nu2):
      answer=nu1/nu2
      print(str(nu1)+ "/"+str(nu2)+"="+str(answer))
def remainder(nu1, nu2):
    answer = nu1 % nu2
    print(str(nu1) + "%" + str(nu2) + "=" + str(answer))
 
     
print("a.add")
print("b.sub")
print("c.mul")
print("d.div")
print("e.Remainder")
print("f.exit")
choice=input("input your choice:")

if choice == "A" or choice == "a":
    print("add")
    nu1 = int(input("enter your first number: "))
    nu2 = int(input("enter your second number: "))
    add(nu1, nu2)
elif choice == "B" or choice == "b":
    print("sub")
    nu1 = int(input("enter your first number: "))
    nu2 = int(input("enter your second number: "))
    sub(nu1, nu2)
elif choice == "C" or choice == "c":
    print("mul")
    nu1 = int(input("enter your first number: "))
    nu2 = int(input("enter your second number: "))
    mul(nu1, nu2)
elif choice == "D" or choice == "d":
    print("div")
    nu1 = int(input("enter your first number: "))
    nu2 = int(input("enter your second number: "))
    div(nu1, nu2)
elif choice == "E" or choice == "e":
    print("Remainder")
    nu1=int(input("enter your first number: "))
    nu2=int(input("enter your second number: "))
    remainder(nu1,nu2)

elif choice == "F" or choice == "f":
    print("bye")
