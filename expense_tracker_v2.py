name = input ("Enter your name : ")
month = input ("Enter Month : ")
budget = float(input("Budget for the month: "))
print()
print ("----------------------------")
print("Monthly expense Tracker ")
print ("----------------------------")
print ("Welcome !", name)
print ("Month : ", month)
print ("budget : Rs", budget)
expense_name = ""
total_expense = 0 
while expense_name != "done" :
    expense_name = input("Enter your expense : ")
    if expense_name == "done":
            break
    amount = float(input("Enter the amount "))
    total_expense = total_expense + amount
remaining_budget = budget - total_expense
print ("Total expense RS : ", total_expense)
print ("Remaining_budget: Rs " , remaining_budget)
if remaining_budget < 0: 
      print("Your budget has exceeded")
elif remaining_budget == 0:
      print("you have exhausted your budget")
else:
      print ("you are in your budget limit")

