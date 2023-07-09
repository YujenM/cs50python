def main():
    user=input("Greeting: ")
    new_user=greeting(user)
    print(new_user)

def greeting(user):
    user=user.lower().strip()
    if user=="hello":
        return("$0")
    elif user=="hello, newman":
        return("$0")
    elif user=="h":
        return("$20")
    elif user=="how you doing?":
        return("$20")
    else:
        return("$100")
if __name__=="__main__":
    main()
