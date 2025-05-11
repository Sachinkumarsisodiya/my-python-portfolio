def calculate():
    print("Press 1 for sum")
    print("Press 2 for sub")
    print("Press 3 for mul")
    print("Press 4 for div")
    num1 = int(input("Press Button :"))
    if(num1 == 1):
        value1  =  int(input("enter the value: "))
        value2 =  int(input("enter the value: "))
        print(value1+value2)
    elif (num1 == 2):
            value1  =  int(input("enter the value: "))
            value2 =  int(input("enter the value:"))
            print(value1 - value2)
    elif(num1 == 3):
            value1  =  int(input("enter the value: "))
            value2 =  int(input("enter the value:"))
            print(value1 * value2)
    elif(num1 == 4):
            value1  =  int(input("enter the value: "))
            value2 =  int(input("enter the value:"))
            print(value1 / value2)
calculate()





