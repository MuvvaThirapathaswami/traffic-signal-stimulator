import time
while True:
    print("1.Manual Mode ")
    print("2.Auto Mode ")
    print("3.EXIT")
    choice=eval(input("Enter choice (1/2/3): "))
    if(choice==1):
        while True:
            signal=input("enter the signal (red/yellow/green) or back: ").lower()
            if(signal=="red"):
                print("red-STOP")
            elif(signal=="yellow"):
                print("yellow-READY TO MOVE")
            elif(signal=="green"):
                print("Green-MOVE")
            elif(signal=="back"):
                print("exit back")
                break
            else:
                print("Enter valid signal: ")
    elif(choice==2):
        print("red-STOP")
        for i in range(10,0,-1):
            print(i)
            time.sleep(1)
        print("yellow-READY TO MOVE")
        for i in range(10,0,-1):
            print(i)
            time.sleep(1)
        print("Green-MOVE")
        for i in range(10,0,-1):
            print(i)
            time.sleep(1)
        print("one cycle completed")
        again=input("enter yes or no : ").lower()
        if(again!="yes"):
            print("execution stop,Thank you")
            break
    elif(choice==3):
        print("exit")
        break