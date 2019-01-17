"""
balance ​=​ ​2250
interestRate ​=​ ​.​045
term ​=​ ​120

We’re going to create an simple interest calculator with a loop.

Write a loop so that each month interest is calculated on this investment.
Each month the following should occur:

A) Monthly interest earned should be calculated by multiplying the balance
by the interest rate divided by 12. (Interest is given yearly, but is being
calculated monthly.

B) The new balance should be determined.

C) The month number, interest earned and new balance should be output to the console.

To make your output neat you can use the character entity \t for a tab.

"""
balance = 2250
interestRate = .045
term = 120

x = 1
while x < term + 1:
    interest = balance * interestRate/12
    balance = balance + interest
    print('Month', x, '\t Inerest: $', interest, '\t Balance: $', balance)
    x += 1
