print("---------------------------")
print(" Monthly Expense Tracker ")
print("-------------------------")
name = input("Enter your name:  ")
month = input("Enter your month : (e.g., August): ")
budget = float(input("Monthly inhand Budget: Rs "))
rent = float(input("Enter your rent expense: Rs "))
investment = float(input("Enter investment expense: Rs "))
food = float(input("Enter food expense: Rs "))
shopping = float(input("Enter shopping expense: Rs "))
entertainment = float(input("Enter your entertainment expense: Rs "))
miscellaneous = float(input("Enter your miscellaneous expense: Rs "))
total_expense = rent + investment + food + shopping + entertainment+ miscellaneous
remaining_budget = budget - total_expense
print()
if remaining_budget < 0:
    print ("WARNING ! you have exceeded your budget !")
elif remaining_budget == 0:
    print ("you have exhausted your budget !")
else:
    print ("You are in your budget limit. ")

print ("\nWelcome", name + "!" )
print ("Month ", month)
print("Your monthly budget is  ",budget)

print("\n-----------expense summary -----------")
print ("Rent :              ",rent)
print ("Investment :        ",investment)
print ("Food :             ",food)
print ("Shopping :          ",shopping)
print ("Entertainment :         ",entertainment)
print ("Miscellaneous:          ",miscellaneous)

print("--------------------------")
print()

print("Total expense is:  RS   ", total_expense)
print ("Remaining balance is Rs " ,  remaining_budget)
