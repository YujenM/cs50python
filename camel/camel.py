# taking input
camel=input("camelcase: ")
# printing
print("snake_case:",end=" ")
#  using for loop to find upper case in the input
for U in camel:
    if U.isupper():
        print("_" +U.lower(),end="")
    else:
        print(U,end="")
print()