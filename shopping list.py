list= []
def read_data():
    f= open("/Users/Surface/Desktop/pythoncourse/ses7/text.txt", 'r')
    for i in f:
        list= i.split(",")
        dic = {"barcode":list[0],"name":list[1], 
             "price":list[2],"count":list[3]}
        list.append(dic)
def show_menu():
    print("1- add")
    print("2- delete")
    print("3- search")
    print("4- buy")
    print("5- edit")
    print("6- exit")
    print("7- display products available")
def add():
    barcode=input("enter barcode: ")
    name=input("enter name: ")
    price=input("enter price: ")
    count=input("enter count")

    dic= {"barcode":barcode, "name":name ,"price":price ,"count":count}
    list.append(dic)
    print(list)
def delete():
    while True:
        barcode = input("narcode kala ra vared konid:")
        
        with open("/Users/Surface/Desktop/pythoncourse/ses7/text.txt", 'r') as f:
            lines = f.readlines()
        with open("/Users/Surface/Desktop/pythoncourse/ses7/text.txt", 'r') as f:
            for line in lines:
                if line.split(",")[0] != barcode:
                    f.write(line)
        print("deleted")

def search():
    mode=input("enter your mode: ")
    for list in list:
        if mode == list["barcode"] or mode == list["name"]:
          print(list)
          break
    else:
        print("not found")


def buy():
    cart=[]
    while True:
        barcode = input("enter required barcode or exit")
        if barcode == "exit":
            break

        found = False
        for list in list:
            if int(barcode) == list["barcode"]:
                found = True
                quantity = int(input("enter quantity: "))

                if quantity > list["count"]:
                    print("not enough products")
                    break
                else:
                   list["count"] = list["count"] - quantity
            item = {
                        "barcode": list["barcode"],
                        "name":list["name"],
                        "price": list["price"],
                        "count": quantity
                    }
        cart.append(item)
        break

        if not found:
            print(f"barcode{barcode} not found.")

        print("your list")
        for item in cart:
            print(f"\t price per product{item['name']}: {item['price']} Toman / {item['count']} of {item['name']} (ID: {item['barcode']}) \t your total is: {item['count'] * item['price']}")
total_cost = 0
for item in cart:
        total_cost = total_cost + (int(item["count"]) * int(item["price"]))
print(f"your total is {total_cost}")



def edit():
    barcode = input(' barcode kala morede nazar ra vared konid: ')
    for list in list:
        print(f"enter barcode aand price: {barcode}:")
        print(f"Name: {list['name']}")
        print(f"Price: {list['price']}")
        print(f"Count: {list['count']}")            
        print("1- Name")
        print("2- price")
        print("3- quantity")
        item_to_edit = int(input("enter the number"))

        if item_to_edit == 1:
                new_name = input("new name: ")
                list["name"] = new_name
        elif item_to_edit == 2:
                new_price = int(input("new price: "))
                list["price"] = new_price
        elif item_to_edit == 3:
                new_count = int(input("new quantity: "))
                list["count"] = new_count
        break
    else:
        print(f"not identified.")
        return
def exit():
    pass
def showproducts():
    print('barcode\t name\t price\t count')
    for list in list:
        print(list['barcode'],'\t',list['name'], 
              '\t' , list['price'], '\t', list["count"])
        print(f"{list['barcode']}\t {list['name']}")

read_data()
show_menu()

user_choice= int(input("enetr your choice: "))
if user_choice==1:
    add()
elif user_choice==2:
    delete()
elif user_choice==3:
    search()
elif user_choice==4:
    buy()
elif user_choice==5:
    edit()
elif user_choice==6:
    exit()
elif user_choice==7:
    showproducts()    

else:
    print("wrong number! ")