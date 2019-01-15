print("Grade points")

num = int(input("Type your number: "))

if num >=80:
    print("you got A+")
elif num<=79 and num >= 69:
    print("you got A")
elif num<=69 and num >=59:
    print("you got A-")
elif num<59 and num >=49:
    print("you got B")
elif num <49 and num>=39:
    print("you got C")
elif num>=33 and num<=38:
    print("you got D")
else :
    print("You fail")


