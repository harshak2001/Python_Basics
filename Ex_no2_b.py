n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
#By Basic operators
a=int(n1/n2)
b=n1-n2*a
#By the divmod function
r=divmod(n1,n2)
#By % operator
remainder= n1%n2

print(f"Remainder using basic operater is {b} \n "
      f"Remainder using divmod function is {r[1]}\n"
      f"Remainder using % operater is {remainder}")