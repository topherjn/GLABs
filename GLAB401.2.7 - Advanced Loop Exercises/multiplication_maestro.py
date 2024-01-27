def print_table_row(multiplicand,multiplier):
    print(f'{multiplicand} X {multiplier} = {multiplicand*multiplier}')

# get input from user
multiplicand = int(input('Create a multiplication table for which number? ')) 

# generate table from 1 to 12 since 12 is 
# still hard for me to remember
for i in range(1, 13):
    print_table_row(multiplicand, i)