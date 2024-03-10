def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price    

price = float(input("enter the original price :"))
discount_percent = float(input("enter the discount percentage :"))

final_price = calculate_discount(price,discount_percent)
print("the final price is :",final_price)