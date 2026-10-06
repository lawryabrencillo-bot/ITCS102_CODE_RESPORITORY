#inputs
age = int(input("Age? =--->"))
rev = float(input("Revenue --->"))
cs = int(input("Credit Score --->"))
years = float(input("Years of Business?--->"))
has_defaults = bool(input("File for Bankruptcy ---?"))
collaterals = input("Collaterals Name ---?")
c_value = float(input("Collaterals Value --->"))

#baseline age >= 21 , years >= 2.0, False in Defaults
max_loan = 0
base_fee = 0

if age >= 21 and years >= 2.0 and has_defaults == False:
    print("Your loan is succesful")
    if cs >= 720: #tier1
        max_loan = rev * 3
        print("Maximum loanable amount is set to", max_loan)
        print("high credit score")
        if rev >= 50000:
            print("revenue higher than 50k")
            base_fee = max_loan * 0.015
            print("Base fee rate is set to", base_fee)
else:
    print("revenue lower than 50k")
    base_fee = max_loan * 0.025
    print("base fee rate is set to", base_fee)

    #collateral
    if c_value >= max_loan:
        print("collateral ", collaterals, " with a value of ", c_value, "is accepted")
    else: 
        print("rejected: insufficient collateral value for ",collateral)

#surcharge
surge_fee_rate = max_loan * base_fee
print("additional charge of " ,surge_fee_rate)
if max_loan % 5000 != 0:
    print("additional charge added")
    surge_fee_rate += 250
    print("updated base fee is " ,surge_fee_rate)

elif cs >= 620 and cs < 720: #tier2
    print("Credit score within range of 620 to 720")
    max_loan = rev = 1.5
    print("maximum loan for this credit score is", max_loan)
    if years >= 5:
        print("Business year more than 5 years")
        base_fee = max_loan = 0.02
        print("base fee rate is set to", base_fee)
    else:
        print("Business year less than 5 years")
        base_fee = max_loan * 0.035
        print("base fee rate is set to", base_fee)

elif cs < 620 and cs >= 1: #tier3
    print("credit score too low")
else:
    print("invalid")