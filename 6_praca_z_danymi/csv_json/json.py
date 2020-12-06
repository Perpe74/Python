import json
import os

file_name = 'zamowienia.json'
file_new = False

if not os.path.isfile(file_name):
    file = open(file_name, 'w+')
    file.close()
    file_new = True

file = open(file_name, 'r+')

if file_new:
    data = {}
    data["orders"] = []
else:
    data = json.load(file)

run = True
while run:
    print("List of operations:\n"
          "1 - add order\n"
          "2 - delete order\n"
          "3 - print orders\n"
          "4 - save and exit\n")

    operation = int(input())

    if operation == 1:
        number = input("Give a order numer\n")
        price = input("Give a price\n")
        order = {"order number": number, "price": price}
        data["orders"].append(order)

    elif operation == 2:
        title_to_delete = input("Give a order number\n")
        index = -1
        for i in range (len(data["orders"])):
            order = data["orders"][i]
            if order["number"] == order_to_delete:
                index = i
                break
        if index != -1:
            del data["orders"][index]
        else:
            print("Order not found")

    elif operation == 3:
        print(json.dumps(data, sort_keys=True, indent=4))

    elif operation == 4:
        file.seek(0)
        json.dump(data, file)
        file.truncate()
        file.close()
        run = False

