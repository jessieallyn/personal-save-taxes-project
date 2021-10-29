# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:16:08 2021

@author: The Woods
"""

import sys

# this is a program I created for my own personal use. I wanted to determine
# how much I'd be able to save, depending on our household income

#ASSUMPTIONS:
    #user is married, with tax status as married filing jointly
    #user & spouse are W-2 employees
    #user lives in Missouri, in a county without local income
    #user will contribute to medical premiums/contributions pre-tax
    #user will save 6% of income for retirement
    #user will donate 11% of income (under tithing)
    #user saves 10% (under "pay self first")
    #user will voluntarily withhold an extra $1300 for taxes voluntarily
    #user is paid bi-monthly
    #user is Jessie or Barry
    #user & family max discretionary spending is $1900

salary = int(input("What is your salary?"))
spouse = int(input("What is your spouse's salary?"))
gross = salary + spouse
retirement = gross * .06
tithing = (gross * .11) /12
premium = input("If you know your pretax medical premiums & FSA/HSA\
 contributions, enter yes. Else, enter no.")

if premium == "yes":
    premium = int(input("What's the amount?"))
elif premium == "no":
    premium = gross * .017
#if int(premium) <= 3500:
 #   premium = 3500
print("medical pre-tax amount has been set to", premium)
standard = input("When filing taxes, will you take the standard deduction?")
if standard == "yes":
    standard = True
elif standard == "no":
    standard = False

def taxable_income(gross, standard):
    # finding taxable income function
    # federal taxes
    # married filing jointly
    # input gross income, it will tell you taxable income
    
    taxable_income = 0
    standard_deduction = 24800
    itemized_deduction = 0
    if standard == True:
        taxable_income = gross - int(premium) - retirement - standard_deduction
    elif standard == False:
        itemized_deduction = int(input("What will be the amount of your itemized deductions?"))
        taxable_income = gross - premium - retirement - itemized_deduction
    return taxable_income

def mo_taxable_income(gross, standard):
    # finding taxable income function
    # missouri state taxes
    # married filing jointly
    # input gross income, it will tell you taxable income
    
    missouri_taxable_income = 0
    standard_deduction = 25100
    if standard == True:
        standard = gross - int(premium) - retirement - standard_deduction
    elif standard == False:
        standard = int(input("What will be the amount of your itemized deductions?"))
    missouri_taxable_income = gross - premium - retirement - standard_deduction
    return missouri_taxable_income

def effective_tax_rate(taxable_income):
    # effective income tax rate function
    # federal taxes
    # married filing jointly 2021
    # input taxable_income, it will tell you your effective income tax rate
    
    # 10% $0 - 19,750
    # 12% $19,751 - 80,250
    # 22% $80,251 - 171,050
    # 24% $171,051 - 326,600
    # 32% $326,601 - 414,700
    # 35% $414,701 - 622,050
    # 37% 622,051 + 
    
    bracket_1 = .10
    bracket_2 = .12
    bracket_3 = .22
    bracket_4 = .24
    bracket_5 = .32
    bracket_6 = .35
    bracket_7 = .37
    min1 = 0
    max1 = 19750
    min2 = 19751
    max2 = 80250
    min3 = 80251
    max3 = 171050
    min4 = 171051
    max4 = 326600
    min5 = 326601
    max5 = 414700
    min6 = 414701
    max6 = 622050
    min7 = 622051
    tax = 0
    if min7 <= taxable_income:
        taxable_income -= min7
        tax += (taxable_income * bracket_7)
        taxable_income = max6
    if min6 <= taxable_income <= max6:
        taxable_income -= min6
        tax += (taxable_income * bracket_6)
        taxable_income = max5
    if min5 <= taxable_income <= max5:
        taxable_income -= min5
        tax += (taxable_income * bracket_5)
        taxable_income = max4
    if min4 <= taxable_income <= max4:
        taxable_income -= min4
        tax += (taxable_income * bracket_4)
        taxable_income = max3
    if min3 <= taxable_income <= max3:
        taxable_income -= min3
        tax += (taxable_income * bracket_3)
        taxable_income = max2
    if min2 <= taxable_income <= max2:
        taxable_income -= min2
        tax += (taxable_income * bracket_2)
        taxable_income = max1
    if min1 <= taxable_income <= max1:
        tax += (taxable_income * bracket_1)
        print(tax, "is the total amount of federal income tax")
    big_kids = int(input("How many children between the ages of 6 & 17 do you have?"))
    little_kids = int(input("How many children between the ages of 0 & 5 do you have?"))
    tax_credit = (big_kids * 3000) + (little_kids * 3600)
    tax -= tax_credit
    print("Your child tax credit lowered your federal income tax by", tax_credit, "dollars, to", tax)
    effective_tax_rate = tax / gross
    print("Your effective federal income tax rate is", round((effective_tax_rate*100), 2), "percent.")
    if effective_tax_rate > 0:
        return effective_tax_rate
    elif effective_tax_rate <= 0:
        return 0

def missouri_effective_tax_rate(missouri_taxable_income, gross):
    # effective income tax rate function
    # missouri taxes
    # married filing jointly 2021
    # input missouri taxable_income, it will tell you your effective income tax rate
    
    # $0 - 108 - not taxed
    # $ 109 - 1088 - 1.5% of taxable income
    # $1088 - 2176 - $ 16 + 2.0% of excess over $1088
    # $2176 - 3264 - $ 38 + 2.5% of excess over $2176
    # $3264 - 4352 - $ 65 + 3.0% of excess over $3264
    # $4352 - 5440 - $ 98 + 3.5% of excess over $4352
    # $5440 - 6528 - $136 + 4.0% of excess over $5440    
    # $6528 - 7616 - $180 + 4.5% of excess over $6528
    # $7616 - 8704 - $229 + 5.0% of excess over $7616
    # $8704 & up   - $283 + 5.4% of excess over $8704 
    
    max1 = 108
    min2 = 109
    max2 = 1088
    min3 = 1089
    max3 = 2176
    min4 = 2177
    max4 = 3264
    min5 = 3265
    max5 = 4352
    min6 = 4353
    max6 = 5440
    min7 = 5441
    max7 = 6528
    min8 = 6529
    max8 = 7616
    min9 = 7617
    max9 = 8704
    min10 = 8705
    tax = 0
    if missouri_taxable_income <= max1:
        tax = 0
        print(round(tax, 2), "is the total amount of Missouri income tax")
        effective_tax_rate = tax / gross
        print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
        return tax
    if missouri_taxable_income >= min2:
        if missouri_taxable_income <= max2:
            tax = missouri_taxable_income * .015
            print(round(tax, 2), "is the total amount of Missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return tax
    if missouri_taxable_income >= min3:
        if missouri_taxable_income <= max3:
            tax = 16 + ((missouri_taxable_income - 1088) * .02) 
            print(round(tax, 2), "is the total amount of Missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return tax
    if missouri_taxable_income >= min4:
        if missouri_taxable_income <= max4:
            tax = 38 + ((missouri_taxable_income - 2176) * .025) 
            print(round(tax, 2), "is the total amount of Missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return tax
    if missouri_taxable_income >= min5:
        if missouri_taxable_income <= max5:
            tax = 65 + ((missouri_taxable_income - 3264) * .03) 
            print(round(tax, 2), "is the total amount of Missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return tax
    if missouri_taxable_income >= min6:
        if missouri_taxable_income <= max6:
            tax = 98 + ((missouri_taxable_income - 4352) * .035) 
            print(round(tax, 2), "is the total amount of Missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return tax
    if missouri_taxable_income >= min7:
        if missouri_taxable_income <= max7:
            tax = 136 + ((missouri_taxable_income - 5440) * .04) 
            print(round(tax, 2), "is the total amount of Missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return tax
    if missouri_taxable_income >= min8:
        if missouri_taxable_income <= max8:
            tax = 180 + ((missouri_taxable_income - 6528) * .045) 
            print(round(tax, 2), "is the total amount of Missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return tax
    if missouri_taxable_income >= min9:
        if missouri_taxable_income <= max9:
            tax = 229 + ((missouri_taxable_income - 7616) * .05) 
            print(round(tax, 2), "is the total amount of Missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return tax
    if missouri_taxable_income >= min10:
        tax = 283 + ((missouri_taxable_income - 8704) * .054) 
        print(round(tax, 2), "is the total amount of Missouri income tax")
        effective_tax_rate = tax / gross
        print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
        return tax
    # effective income tax rate function
    # missouri taxes
    # married filing jointly 2021
    # input missouri taxable_income, it will tell you your effective income tax rate
    
    # $0 - 108 - not taxed
    # $ 109 - 1088 - 1.5% of taxable income
    # $1088 - 2176 - $ 16 + 2.0% of excess over $1088
    # $2176 - 3264 - $ 38 + 2.5% of excess over $2176
    # $3264 - 4352 - $ 65 + 3.0% of excess over $3264
    # $4352 - 5440 - $ 98 + 3.5% of excess over $4352
    # $5440 - 6528 - $136 + 4.0% of excess over $5440    
    # $6528 - 7616 - $180 + 4.5% of excess over $6528
    # $7616 - 8704 - $229 + 5.0% of excess over $7616
    # $8704 & up   - $283 + 5.4% of excess over $8704 
    
    max1 = 108
    min2 = 109
    max2 = 1088
    min3 = 1089
    max3 = 2176
    min4 = 2177
    max4 = 3264
    min5 = 3265
    max5 = 4352
    min6 = 4353
    max6 = 5440
    min7 = 5441
    max7 = 6528
    min8 = 6529
    max8 = 7616
    min9 = 7617
    max9 = 8704
    min10 = 8705
    tax = 0
    if missouri_taxable_income <= max1:
        tax = 0
        print(tax, "is the total amount of missouri income tax")
        effective_tax_rate = tax / gross
        print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
        return effective_tax_rate
    if missouri_taxable_income >= min2:
        if missouri_taxable_income <= max2:
            tax = missouri_taxable_income * .015
            print(tax, "is the total amount of missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return effective_tax_rate
    if missouri_taxable_income >= min3:
        if missouri_taxable_income <= max3:
            tax = 16 + ((missouri_taxable_income - 1088) * .02) 
            print(tax, "is the total amount of missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return effective_tax_rate
    if missouri_taxable_income >= min4:
        if missouri_taxable_income <= max4:
            tax = 38 + ((missouri_taxable_income - 2176) * .025) 
            print(tax, "is the total amount of missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return effective_tax_rate
    if missouri_taxable_income >= min5:
        if missouri_taxable_income <= max5:
            tax = 65 + ((missouri_taxable_income - 3264) * .03) 
            print(tax, "is the total amount of missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return effective_tax_rate
    if missouri_taxable_income >= min6:
        if missouri_taxable_income <= max6:
            tax = 98 + ((missouri_taxable_income - 4352) * .035) 
            print(tax, "is the total amount of missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return effective_tax_rate
    if missouri_taxable_income >= min7:
        if missouri_taxable_income <= max7:
            tax = 136 + ((missouri_taxable_income - 5440) * .04) 
            print(tax, "is the total amount of missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return effective_tax_rate
    if missouri_taxable_income >= min8:
        if missouri_taxable_income <= max8:
            tax = 180 + ((missouri_taxable_income - 6528) * .045) 
            print(tax, "is the total amount of missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return effective_tax_rate
    if missouri_taxable_income >= min9:
        if missouri_taxable_income <= max9:
            tax = 229 + ((missouri_taxable_income - 7616) * .05) 
            print(tax, "is the total amount of missouri income tax")
            effective_tax_rate = tax / gross
            print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
            return effective_tax_rate
    if missouri_taxable_income >= min10:
        tax = 283 + ((missouri_taxable_income - 8704) * .054) 
        print(tax, "is the total amount of missouri income tax")
        effective_tax_rate = tax / gross
        print("Your effective Missouri income tax rate is", round((effective_tax_rate*100), 2), "percent.")
        return effective_tax_rate
    
    
state = mo_taxable_income(gross, standard)
state_tax = missouri_effective_tax_rate(state, gross)  
gov = taxable_income(gross, standard)
effective_tax = effective_tax_rate(gov)

withholdings = 1300
take_home = (gross - premium - retirement - withholdings - (gov * effective_tax) - (gross * .075) - state_tax) / 24
monthly_take_home = take_home * 2
pay_self_first = gross * .10
truck = input("Do you want to add a truck or car payment?")
if truck == "yes":
    truck = int(input("What will be the monthly amount of the payment + insurance increase?"))
elif truck == "no":
    truck = 0
childcare = input("Do you need childcare?")
if childcare == "yes":
    childcare = int(input("What will the amount of childcare be monthly?"))
elif childcare == "no":
    childcare = 0
monthly_bills = int(input("Monthly bills include bills that you receive an invoice\
 or a bill for. Ex: Utility bill, subscriptions, mortgage, etc. Do not\
 include childcare or added vehicle payment if you already entered them.\
 Do not include items we have already covered such as retirement, savings,\
 or medical. (Food and other discretionary bills will be covered later.)\
 What are your monthly bills?"))
monthly_bills += truck + childcare + tithing
if monthly_bills > (monthly_take_home):
    print("****WARNING - YOUR MONTHLY BILLS ARE LARGER THAN YOUR TAKE HOME PAY****")
    sys.exit()
discretionary = monthly_take_home - (pay_self_first / 12)  - monthly_bills 
print("Your monthly take home is", round(monthly_take_home, 2), "after an extra\
 voluntary tax withholding of $1300/year")
print("Bi-monthly pay yourself first is", round((pay_self_first / 12), 2))
print("Your total monthly bills are", round(monthly_bills, 2))
if discretionary <= 0:
    print("****WARNING - YOUR BILLS AND PAY SELF FIRST ARE LARGER THAN YOUR TAKE HOME PAY****")
    sys.exit()
elif discretionary > 0:
    print("For discretionary money, (food, household, clothing, fuel, ect.) you have $", (round(discretionary, 2)), "monthly")
barry = 300
jessie = 300
kids = 300
groceries = 1000
while 0 < discretionary and discretionary <= (barry + jessie + kids + groceries):
    barry = barry - .75
    jessie = jessie - .75
    kids = kids - .75
    groceries = groceries - 1
    if (discretionary - barry - jessie - kids - groceries) < 0:
        if (barry + jessie + kids + groceries) > 0:
            barry = discretionary / 4
            jessie = discretionary / 4
            kids = discretionary / 4
            groceries = discretionary / 4
print("Barry spending is", barry, "Jessie spending is", jessie, "kid spending\
 is", kids, "grocery spending is", groceries)
if discretionary == (barry + jessie + kids + groceries):
    print("This is a zero balance budget")
else:
    print("The remaining balance monthly of discretionary money is", round((discretionary - barry - jessie - kids - groceries),2))
annual_excess = 12 * (discretionary - barry - jessie - kids - groceries)
fed_taxes = (gov * effective_tax) + (gross * .075)
print("Annual federal income & FICA taxes are", round(fed_taxes, 2))
print("Your effective federal tax rate (including FICA & Income) is", round(((fed_taxes / gross)*100), 2), "percent")
print("Your annual Missouri State Taxes are", round(state_tax, 2))
print("Your combined federal income, FICA, and state income taxes are", (round(fed_taxes + state_tax, 2)))
print("Your effective tax rate for all taxes combined is", (round(((fed_taxes + state_tax)/gross)*100, 2)))
print("Your medical contributions are", premium)
print("Annual 401k amount saved is", retirement)
print("Annual pay-self-first savings is", pay_self_first)
print("Annual buget excess is", (round(annual_excess,2)))
print("If you save the 401k amount, pay-self-first savings, and budget excess\
 then your annual savings will be", round((retirement + pay_self_first + annual_excess), 2))
