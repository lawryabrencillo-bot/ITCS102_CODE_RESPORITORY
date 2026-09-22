age = int(input(" Enter your age: "))
is_employed = input("Are you employed? (True/False): ").strip().lower() == "true"
credit_score = float(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))
has_collateral = input("Do you have collateral? (True/False): ").strip().lower() == "true"

interest_rate = 0.0

if age >= 21 and is_employed == True:
    print("Accepted: You are eligible for a loan.")

    # Tier 1
    if credit_score >= 750:
        if annual_income >= 110000:
            interest_rate = 4.5
        elif annual_income >= 50000:
            interest_rate = 5.0

        print("Approved: ", interest_rate, "% interest rate")

    # Tier 2
    elif credit_score >= 600 and credit_score < 750:
        if has_collateral == True:
            interest_rate = 7.0
        elif annual_income <= 50000:
            interest_rate = 9.5
        else:
            interest_rate = 8.0

        print("Approved: ", interest_rate, "% interest rate")

    # Tier 3
    elif credit_score < 600:
        print("Rejected: Your credit score is too low for a loan.")

else:
    print("Rejected: You are not eligible for a loan.")