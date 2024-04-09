 # 02/4/24 Jordan Buckley - Class CC
def calculate_tax():
    print("--Welcome To The Tax Calculator--")
    salary = int(input("Enter your salary: "))
    children = int(input("Enter the amount of children you have: "))
    mortgage = int(input("Enter amount of monthly mortgage payments: "))

    # Step 1: Determine the tax-free allowance (TFA)
    if children == 0 or mortgage < 150:
        tfa = 0
    else:
        if children <= 3:
            if mortgage < 300:
                tfa = 237
            else:
                tfa = 275
        else:
            tfa = 305

    # Step 2: Calculate the taxable income
    taxable_income = salary - tfa

    # Step 3: Apply the tax rates
    if taxable_income <= 35800:
        tax_due = taxable_income * 0.20
    else:
        tax_due = (35800 * 0.20) + ((taxable_income - 35800) * 0.40)

    return round(tax_due), tfa
 # Example usage
tax_due, total_allowance = calculate_tax()
print("Tax due:\u20AC", tax_due, "Total allowance:\u20AC", total_allowance)
print("Total tax payed: \u20AC", tax_due - total_allowance)

def monthly_pay():
     print("--Welcome To The Monthly Pay Calculator--")
     years_worked = int(input("Enter the amount of years worked: "))
     sales_region = input("Which region are you in 1.SW, 2.MW, 3.NW, 4.SE, 5.ME, 6.NE: ")
     monthly_sales = int(input("Enter total sales within this month: "))
     mileage = int(input("Enter amount of mileage: "))

     # Define commission rates based on years of service and sales region
     if years_worked >= 5 and sales_region in ['SW', 'MW', 'NW']:
         commission_rate = 0.04
         if mileage > 2000:
             commission_rate += 0.003
     else:
         commission_rate = 0.035
         if mileage > 3000:
             commission_rate += 0.005

     # Assuming no basic salary defined here
     total_monthly_pay = commission_earned = monthly_sales * commission_rate

     return round(total_monthly_pay, 2), round(commission_earned, 2)

total_monthly_pay, total_commission = monthly_pay()
print("Total monthly pay:", total_monthly_pay)
print("Total commission:", total_commission)
