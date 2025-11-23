
Gwa = float(input("Enter General Weighted Average: "))
income = int(input("Enter Annual family income: "))

if Gwa <= 1.75:
    if income < 150000:
        print("Full Scholarship Granted")
    else:
        print("Partial Scholarship Granted")
elif Gwa > 1.75 and Gwa <= 2.0:
    print("Partial Scholarship Only")
else:
    print("Not Eligable")
