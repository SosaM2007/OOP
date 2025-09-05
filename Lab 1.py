while 1:
    print("1. Addittion")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    option = input("Select an Option:")

    if option =="1":
        n1 = int(input("Insert n1:"))
        n2 = int(input("Insert n2:"))
        answer = n1+n2
        print("The answer is:", answer)
    elif option =="2":
        n1 = int(input("Insert n1:"))
        n2 = int(input("Insert n2:"))
        answer = n1-n2
        print("The answer is:" , answer)
    elif option =="3":
        n1 = int(input("Insert n1:"))
        n2 = int(input("Insert n2:"))
        answer = n1*n2
        print("The answer is:" , answer)
    elif option =="4":
        n1 = int(input("Insert n1:"))
        n2 = int(input("Insert n2:"))
        answer = n1/n2
        print("The answer is:" , answer)
    else:
        break



