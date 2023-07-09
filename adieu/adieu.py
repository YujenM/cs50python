import inflect
p = inflect.engine()
greeting=["Adieu","adieu"]
while True:
    try:
        user=input("Name: ")
    except:
        print()
        break
    greeting.append(user)
greeting[2]="to "+ greeting[2]
if len(greeting)== 3:
    new_greeting =p.join(greeting, conj='')
elif len(greeting)==4:
    new_greeting = p.join(greeting, final_sep='')
else:
    new_greeting=p.join(greeting)
print(new_greeting)