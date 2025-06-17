from math import ceil
#Setting product 

productA = {"name" : "productA","price" : 20,"quantity" : 0,"gift" : "n"} 
productB = {"name" : "productB","price" : 40,"quantity" : 0,"gift" : "n"}
productC = {"name" : "productC","price" : 50,"quantity" : 0,"gift" : "n"}

#getting information from user

product_list = [productA, productB, productC]



#product
for i in product_list:
    i["quantity"] = int(input(f'enter the quantity of {i["name"]} : '))
    i["gift"] = input("if the product need to be wrapped (y/n) : ")
    i["total"] = i["quantity"] * i["price"]


#Cart & quantity total
cart_total = productA["total"] + productB["total"] + productC["total"] 
quantity_total = productA["quantity"] + productB["quantity"] + productC["quantity"]    

#gift and shipping charges
gift = 0
shipping = ceil(quantity_total/10)*5 #shipping charge is 5 per 10 items 

#Discount functions

def flat_10_discount():  #cart discound
    return 10

def bulk_5_discount(product_total): #single product discount  
    discount_rate = (product_total/100)*5
    return discount_rate

def bulk_10_discount(cart_total): #cart discound
    discount_rate = (cart_total/100)*10
    return discount_rate

def tiered_50_discount(product_quantity,product_price): #single product discount 
    dicountable_quantity = product_quantity - 15
    discount_rate = (product_price/100)*50
    return dicountable_quantity * discount_rate





#Applyinmg discount

#------------------ tiered_50_discount & bulk_5_discount ---------------
bulk_5_discount_rate = 0
tiered_50_discount_rate = 0  
for i in product_list:
    if i["quantity"]>10:
        i["temp_bulk_5_discount_rate"] = bulk_5_discount(i["total"]) 
        bulk_5_discount_rate+= i["temp_bulk_5_discount_rate"]
    
    if quantity_total > 30 and i["quantity"] > 15:
        i["temp_tiered_50_discount_rate"] = tiered_50_discount(i["quantity"],i["price"]) 
        tiered_50_discount_rate += i["temp_tiered_50_discount_rate"]


#------------- flat_10_discount ------------
flat_10_discount_rate = 0
if cart_total>200:
    flat_10_discount_rate = flat_10_discount() 


#------------- bulk_10_discount ------------
bulk_10_discount_rate = 0 
if quantity_total>20:
    bulk_10_discount_rate = bulk_10_discount(cart_total) 


# sort discount
discounts = {
    "flat_10_discount": flat_10_discount_rate, 
    "bulk_5_discount":bulk_5_discount_rate, 
    "bulk_10_discount": bulk_10_discount_rate, 
    "tiered_50_discount": tiered_50_discount_rate 
}    


discount_name = max(discounts,key=discounts.get) 
dicount_value = discounts[discount_name] 



#Printing the Bill

print("\n\n\tProducts \t Price \t \t Quantity \t gift \t\t Total")
print("\t------------------------------------------------------------------------")
for i in product_list:
    if i["gift"] == "y":
        gift= gift + 1 * i["quantity"] # gift wrapping charge is 1 per item 
    print(f'\t{i["name"]} \t {i["price"]}$  \t x\t {i["quantity"]}\t\t {"Yes" if i["gift"] == "y" else "No"} \t\t {i["total"]}$')
print("\t------------------------------------------------------------------------")
print(f"\tSub total: \t\t\t\t\t\t\t {cart_total}") 
print("\t------------------------------------------------------------------------")
print(f"\tApplied coupon: {discount_name} \t\t\t\t -{dicount_value}$") 
print(f"\tGift charge: \t\t\t\t\t\t\t +{gift}$") 
print(f"\tShipping charge: \t\t\t\t\t\t +{shipping}$") 
print("\t------------------------------------------------------------------------")
print(f"\tGrand Total: \t\t\t\t\t\t\t -{cart_total + shipping + gift - dicount_value}$")
print("\t------------------------------------------------------------------------")
