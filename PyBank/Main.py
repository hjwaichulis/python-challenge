import os
import csv
# Lists
date=[]
profit_losses=[]
profit_losses_change=[]

# Open csv
csvpath = os.path.join("/Users/u370166/python-challenge/PyBank/Resources/budget_data.csv")
with open(csvpath, newline="") as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
 
    # Total months
    for row in csv_reader:
        date.append(row[0])
        profit_losses.append(float(row[1]))
        total_months = len(date)

    # Total profit and losses    
    total_profit_losses = sum(profit_losses)
    
    # Average profit and losses change
    for i in range(1,len(profit_losses)):
            profit_losses_change.append(profit_losses[i] - profit_losses[i-1])
            average_profit_losses = sum(profit_losses_change)/len(profit_losses_change)
    # Max and min profit and losses
    max_profit_losses = max(profit_losses_change)
    max_profit_losses_date = str(date[profit_losses_change.index(max_profit_losses) +1])
    min_profit_losses = min(profit_losses_change)
    min_profit_losses_date = str(date[profit_losses_change.index(min_profit_losses) +1])

# Print 
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_profit_losses}")
    print(f"Greatest Increase in Profits: {max_profit_losses_date} {max_profit_losses}")
    print(f"Greatest Decrease in Profits: {min_profit_losses_date} {min_profit_losses}")

#Export.  Save the f string as a variable then use .write to output in a txt
analysis = os.path.join("/Users/u370166/python-challenge/PyBank/Resources/analysis.txt")
with open(analysis, 'w') as text:
    print("Financial Analysis", file=text)
    print("----------------------------", file=text)
    print(f"Total Months: {total_months}", file=text)
    print(f"Total: ${total_profit_losses}", file=text)
    print(f"Average Change: ${average_profit_losses}", file=text)
    print(f"Greatest Increase in Profits: {max_profit_losses_date} {max_profit_losses}",file=text)
    print(f"Greatest Decrease in Profits: {min_profit_losses_date} {min_profit_losses}", file=text)

