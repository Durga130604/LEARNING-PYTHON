# 1st method ---  using COMMA SEPARATOR
a=10
b=20
a,b=b,a
print("1. after swapping a:",a,"and b:",b)

# 2nd method --- using ARITHEMATIC OPERATOR
a=10
b=20
a=a+b
b=a-b
a=a-b
print("2. after swapping a:",a,"and b:",b)

# 3rd method --- using XOR OPERATOR
a=10
b=20
a=a^b
b=a^b
a=a^b
print("3. after swapping a:",a,"and b:",b)

# 4th method --- using WALRUS OPERATOR(:=)
a=10
b=20
a=a+b-(b:=a)
print("4. after swapping a:",a,"and b:",b)

# 5th method --- using ARITHEMATIC OPERATOR
a=10
b=20
a=a*b
b=a/b
a=a/b
print("5. after swapping a:",a,"and b:",b)
