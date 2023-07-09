while True:
    fuel=input("Fraction: ")
    try:
        # entering numerator and denominator
        x,y= fuel.split("/")
        # converting to int
        new_x= int(x)
        new_y= int(y)
        z= new_x / new_y
        if z<=1:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
a=round(int(z*100.5))
if a<=1:
    print("E")
elif a>=99:
    print("F")
else:
    print(f"{a}%")