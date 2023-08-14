while True:
    def  multiplication_table( ):
        row=int(input("Enter a number(0-9) :"))
        column=int(input("Enter a number(0-9): "))
        for i in range(0,row+1):
            for j in range(0,column+1):
                if i==0 and j==0:
                    print("x",end=" |")
                elif i==0:
                    print(j-1,end=" |")
                elif j==0:
                    print(i-1,end=" |")
                else:
                    print((i-1)*(j-1),end=" |")
            print()
    multiplication_table( )