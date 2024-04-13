# input statements

# inputText recieve requested numbers
print("Please input your salary:")
salary =  float(input())
print("please input total number of dependents:")
numDependents = float(input())

# calculate taxes here

# calculateMonetary tax calculation statments
stateTax = (salary) * (0.065)
federalTax = (salary) * (0.280)
dependentDeduction = (salary) * (numDependents * (0.025))
totalWithholding = (stateTax) + (federalTax) + (dependentDeduction)
takeHomePay = (salary) - (totalWithholding)
# output statements

# displayText RETURNcalculateMonetary results 
print("~~~~~~~~~Here are your total taxes~~~~~~~~~")
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
