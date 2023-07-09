image=input("enter the type of image").lower().strip()
new_image=image
if '.gif' in new_image:
    print("image/gif")
elif '.jpg' in new_image:
    print("image/jpeg")
elif '.jpeg' in new_image:
    print("image/jpeg")
elif '.png' in new_image:
    print("image/png")
elif '.pdf' in new_image:
    print("application/pdf")
elif '.txt' in new_image:
    print("text/plain")
elif '.zip' in new_image:
    print("application/zip")
else:
    print("application/octet-stream")