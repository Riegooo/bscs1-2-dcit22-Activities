
distance = float(input("Enter distance in km : "))
is_member = input("Is the customer a member? (Yes | No) : ").capitalize()
order_amount = float(input("Enter your order amount : "))

if is_member == "Yes":
    is_member = True
else:
    is_member = False

if 0 <= distance <= 3:
    DeliveryDiscount_Fee = 40
elif 4 <= distance <= 7:
    DeliveryDiscount_Fee = 60
elif distance >= 8:
    DeliveryDiscount_Fee = 80
else:
    print("Invalid distance")
    exit()

if order_amount >= 1000:
    DeliveryDiscount_Fee = 0
    total = order_amount + DeliveryDiscount_Fee
    
    print()
    print("==============================")
    print(f"Delivery Fee: {DeliveryDiscount_Fee}")
    print(f"Order Amount: {order_amount}")
    print("------------------------------")
    print("Delivery is FREE because your order amount is ₱1000 or above.")
    print("==============================")
    print(f"Total Amount to Pay: {total}")
    print("==============================")

else:
    if is_member == True:
        discount_fee = DeliveryDiscount_Fee - (DeliveryDiscount_Fee * 0.20)
        total = order_amount + discount_fee

        print("\n==============================")
        print("Order Amount:", order_amount)
        print("Original Delivery Fee:", DeliveryDiscount_Fee)
        print("Discounted Delivery Fee:", discount_fee)
        print("------------------------------")
        print("Delivery fee has been discounted because the customer is a registered member.")
        print("==============================")
        print("Total Amount to Pay:", total)
        print("==============================")

    else:
        total = order_amount + DeliveryDiscount_Fee
        
        print()
        print("==============================")
        print(f"Delivery Fee: {DeliveryDiscount_Fee}")
        print(f"Order Amount: {order_amount}")
        print("==============================")
        print(f"Total Amount to Pay: {total}")
        print("==============================")
        