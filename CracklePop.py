for i in range(1, 101):
    if i % 15 == 0: 
        print("CracklePop")
    else:
        if i % 5 == 0:
            print("Pop")
        else:
            if i % 3 == 0:
                print("Crackle")
            else:
                print(i)


        