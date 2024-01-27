# filing statuses
statuses = ('Single',
            'Married Filing Jointly',
            'Married Filing Separately',
            'Head of Household')

# rates for each status didn't strain to hard to make sure ranges right
# painful data entry job
# this allows for simplying if statement
single_rates = (0,8350,8351,33950,33951,82250,82251,171550,171551,372950,372951)
joint_rates = (0,16700,16701,67900,67901,137050,137051,208850,208851,372950,372951)
separate_rates = (0,8350,8351,33950,33951,68525,68526,104425,104256,186475,186476)
head_rates = (0,11950,11951,45500,45501,117450,117451,190200,190201,372950,372951)

# get status from user
print("Filing statuses: ")
for status in statuses:
    print(status)

status = input("Enter your filing status: ")

while status not in statuses:
    print("Try again.")
    status = input("Enter your filing status: ")

income = int(input("Enter your income: "))

while income < 0:
    print("Your expenses don't count")
    income = int(input("Enter your income: "))

# set the ranges of income based on the status
if status == statuses[0]:
    tax_bracket = single_rates
elif status == statuses[1]:
    tax_bracket = joint_rates
elif status == statuses[2]:
    tax_bracket = separate_rates
elif status == statuses[3]:
    tax_bracket = head_rates

# find out the rate
marginal_rate = 0
if income >= tax_bracket[0] and income <= tax_bracket[1]:
    marginal_rate = 10
if income >= tax_bracket[2] and income <= tax_bracket[3]:
    marginal_rate = 15
if income >= tax_bracket[4] and income <= tax_bracket[5]:
    marginal_rate = 25
if income >= tax_bracket[6] and income <= tax_bracket[7]:
    marginal_rate = 28
if income >= tax_bracket[8] and income <= tax_bracket[9]:
    marginal_rate = 33
if income >= tax_bracket[10]:
    marginal_rate = 35

# test
print(f'For an income of {income} filing {status}, your marginal tax rate is {marginal_rate}%')