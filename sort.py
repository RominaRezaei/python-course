while True:
    def sort(array):
        n= len(array)
        for i in range(1 , n):
            if array[i] < array[i-1]:
                return False
        return True
    array = input("input array of numbers ex. : 1,2,3,...")
    array =[int(x) for x in array.split(",")]
    if sort(array):
        print("your array has been sorted respectively")
    else:
        print("your array is not sorted")