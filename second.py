#Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
cost_price=float(input("enter the value of cost price: "))
selling_price=float(input("enter the value of selling price: "))
if selling_price>cost_price:
    print("profit")
else:
    print("loss")



