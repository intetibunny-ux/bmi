# Split Bill - Normal Print

'''total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

share = total_bill / people

print("Each person should pay:", share)'''



# Split Bill - f-String

'''total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

share = total_bill / people

print(f"Each person should pay: {share:.2f}")'''




# Split Bill - format()

total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

share = total_bill / people

print("Each person should pay: {:.2f}".format(share))
