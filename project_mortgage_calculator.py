"""

Mortgage Calculator - 
Calculate the monthly payments of a fixed term mortgage over given Nth terms \ 
at a given interest rate. Also figure out how long it will take the user to \
pay back the loan. For added complexity, add an option for users to select \
the compounding interval

"""

name = '*** Mortgage Calculator ***'
print
print name
print '-' * len(name)

# input variables

print "INPUTS"
print 'Cash details:'
purchase_price = float(raw_input('Enter purchase price: R '))
deposit = float(raw_input('Enter deposit amount: R '))
print
print 'Bond details:'
interest_rate = float(raw_input('Enter interest rate (annual): '))
bond_term = float(raw_input('Enter bond term (years): '))

# calculations

loan_amount = purchase_price - deposit
interest_rate /= 1200
bond_term *= 12 
monthly_payment = loan_amount*(interest_rate*(1+interest_rate)**bond_term) \
                  / (((1+interest_rate)**bond_term) - 1)
total_cost = monthly_payment * bond_term

# results

print
print '-' * len(name)
print 'RESULTS'
print 'Monthly repayment: R %.2f' % monthly_payment
print 'Total Cost: R %.2f' % total_cost
print
print '-' * len(name)