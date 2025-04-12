name = input("Enter your name : ")

#items in the supermarket

list = '''
FOOD ITEAMS
Rice          ---------------> 50/kg
Paneer        ---------------> 45/kg
Sugar         ---------------> 30/kg
Wheat Flour   ---------------> 40/kg
Teapowder     ---------------> 200/kg
Boost         ---------------> 250/kg.bottle
Oil           ---------------> 180/liter
Salt          ---------------> 40/kg

'''
#declartion
price = 0
totalprice = 0
finalprice = 0
item_list=[]
quantity_list=[]
price_list=[]
plist=[]

#Price for each item

items = {"rice":50,"paneer":45,"sugar":30,"wheatflour":40,"teapowder":200,"boost":250,"oil":180,"salt":40}
print("----->option 1 for Shopping")
print("----->option 2 for Exit")
while True:
    option = int(input("Choose the option : "))
    if option == 2:
        print("Thank you for visiting")
        break
    elif option == 1:
        print(list)
        
        while True:
            select_option =int(input("To Buy press 1 (or) press 2 for exit : "))
            if select_option == 2:
                print("Thank you for shopping")
                break
            elif select_option == 1:
                item = input("Choose item :").lower()
                    
                while True:
                    qunatity_input = input("Enter you quantity : ")
                    if qunatity_input.isdigit():
                        quantity = int(qunatity_input)
                        break
                    else:
                        print("please enter the valid quantity")
                        
            if item in items:
                price = quantity * items[item]
                price_list.append((item,quantity,items[item],price))
                totalprice += price
                item_list.append(item)
                quantity_list.append(quantity)
                plist.append(price)
                    
            else:
                    print("Selected item is not avaliable in these supermarket")
    if totalprice > 0:
        tax = (totalprice*3)/100
        finalprice=tax+totalprice
        print(30 * "=","SWEETY SUPER MARKET",30 * "=")
        print(33 *" ","HYDERABAD")
        print("Name:",name,30 *" ")
        print(80 * "-")
        print("Sno",15 * " ","items",8 * " ", "qunatites",13* " ","price",13 *" ")
        for i in range(len(price_list)):
            print(i,17 * " ",item_list[i],13 *" ",quantity_list[i],18* " ",plist[i])
        print(80 *"-")
        print(55 * " ",'Totalamount:','Rs',totalprice)
        print('Taxamount', 55 * " ",'Rs',tax)
        print(80 * "-")
        print(55 * " ", 'Finalamount:','Rs',finalprice )
        print(80 * "-")
        print(25 * " ","Thank you for Shopping")
        print(80 * "-")



                
    



