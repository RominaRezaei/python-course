
'''
import random
pc_num = random.randint(0,20)
for i in range (10):
    user_num = int(input("enter your number"))

    if pc_num == user_num:
        print("dar hads {i+1} barande shodid")
        break
    if pc_num< user_num:
            print("paiintr")
    if pc_num>user_num:
                print("balatar")
else:
       print("kharej az baze")
             '''  
#arrays ex 2
#**********************************

import random
n = int(input("tedad?"))
array = []
while len(array) < n:
    num= random.randint(1, n +10)
    if number not in array:
        array.append(num)
        print(array)