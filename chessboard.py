black = "#"
white = "$"
def chess (row, column):
        while True:
        
            for n in range (column):
                for m in range (row):
                    if m%2==0:
                        print (black , end="")
                    else :
                        print (white , end="")
                    break
column = int(input("enter the number of columns:"))
row = int (input ("enter the number of rows:"))
print()

chess (row ,column)

