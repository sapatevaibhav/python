def get_amount():
    while True:
        amount = input("Enter amount: ")
        try:
            val = int(amount)
            if val >= 0:
                break
            #else:
                #pass
                #print("Amount can't be negative, try again")
        except ValueError:
            print("Amount must be a number, try again")
            return False;
    return val
print(get_amount())