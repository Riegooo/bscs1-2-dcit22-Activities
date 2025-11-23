
def lines(line=0, lineType=""):
    line_num = 0
    for line_num in range(line):
        print(f"{lineType}", end="")
    print("")

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
    lines(30, "=")
    print(f"Delivery Fee: {DeliveryDiscount_Fee}")
    print(f"Order Amount: {order_amount}")
    lines(30, "-")
    print("Delivery is FREE because your order amount is ₱1000 or above.")
    lines(30, "=")
    print(f"Total Amount to Pay: {total}")
    lines(30, "=")

else:
    if is_member == True:
        discount_fee = DeliveryDiscount_Fee - (DeliveryDiscount_Fee * 0.20)
        total = order_amount + discount_fee

        print("")
        lines(30, "=")
        print("Order Amount:", order_amount)
        print("Original Delivery Fee:", DeliveryDiscount_Fee)
        print("Discounted Delivery Fee:", discount_fee)
        lines(30, "-")
        print("Delivery fee has been discounted because the customer is a registered member.")
        lines(30, "=")
        print("Total Amount to Pay:", total)
        lines(30, "=")

    else:
        total = order_amount + DeliveryDiscount_Fee
        
        print()
        lines(30, "=")
        print(f"Delivery Fee: {DeliveryDiscount_Fee}")
        print(f"Order Amount: {order_amount}")
        lines(30, "=")
        print(f"Total Amount to Pay: {total}")
        lines(30, "=")
        