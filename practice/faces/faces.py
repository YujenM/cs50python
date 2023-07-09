def emoji(user):
        user_1=user.replace(":)","🙂")
        user_2=user_1.replace(":(","🙁")
        return user_2

user=input()
new_user=emoji(user)
print(new_user)

