def Register(a,s):
    at = (a.find("@"))
    dot = (a.find("."))
    if at > 0 and dot > at + 1 and (a[0].isalpha()):
        l, u, p, d = 0, 0, 0, 0
        if len(s) >= 5 and len(s) <= 16:
            for i in s:
                if (i.islower()):
                    l += 1

                if (i.isupper()):
                    u += 1

                if (i.isdigit()):
                    d += 1

                if (i == "@" or i == "#" or i == "$" or i == "%" or i == "^" or i == "&" or i == "!" or i == "`" or i == "~"):
                    p += 1
        if (l >= 1 and u >= 1 and p >= 1 and d >= 1):
            file = open("Task2.txt", "a")
            file.write(a)
            file.write(" ")
            file.write(s)
            file.write("\n")
            file.close()
            print("Registrated sucessfully")


        else:
            print("invalid password please try again")

    else:
        print("invalid email please try again")


def Login(a,s):
    for i in open("Task2.txt", "r").readlines():
        userdata = i.split()
        if a == userdata[0] and s == userdata[1]:
            print("You are logged in")
            return True

    print("Incorrect credentials please try again")
    return False

def forgotpassword(a):
    for i in open("Task2.txt", "r").readlines():
        userdata = i.split()
        if a == userdata[0]:
            print(userdata[1])
            return True
    print("invalid id try again or please Register")
    return False

while True:
    print("Menu: ")
    print("1.Register")
    print("2.Login")
    print("3.Forgot password")
    print("please enter your choice: ")

    choice = int(input())

    if choice == 1:

        a = input("enter email: ")
        s = input("enter password: ")
        Register(a,s)

    elif choice == 2:

        a = input("enter email: ")
        s = input("enter password: ")
        Login(a,s)

    elif choice == 3:
        a = input("enter email: ")
        forgotpassword(a)


    else:
        print("invalid choice please try again")



































