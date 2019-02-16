# -- The total number of months included in the dataset
# -- The total net amount of "Profit/Losses" over the entire period
# -- The average change in "Profit/Losses" between months over the entire period
# -- The greatest increase in profits (date and amount) over the entire period
# -- The greatest decrease in losses (date and amount) over the entire period
# -- print the analysis to the terminal and export a text file with the results.

import os
import csv


def read_csv(file_path, file_name):
    csvpath = os.path.join(file_path, file_name)
    profit_data = []
    total_profit = 0
    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvfile)

        for row in csvreader:
            profit = float(row[1])
            profit_data.append([row[0], profit])
            total_profit += profit

    return [profit_data, round(total_profit, 2)]


def calculate_total_number_of_months(profit_data):
    return len(profit_data[0])

def calculate_profit_changes(profit_data):
    months = []
    profit_changes = []
    profit_data = profit_data[0]
    
    i = 1
    while i < (len(profit_data)):
        profit_change = profit_data[i][1] - profit_data[i-1][1]
        profit_changes.append(profit_change)
        months.append(profit_data[i][0])
        i = i + 1
   
    total_profit_change = sum(profit_changes)
    avg_profit_change = round(total_profit_change / len(profit_changes), 2)
    max_profit_change = int(max(profit_changes))
    max_profit_month = months[profit_changes.index(max_profit_change)]
    min_profit_change = int(min(profit_changes))
    min_profit_month = months[profit_changes.index(min_profit_change)]

    return {"avg_profit_change": avg_profit_change, 
            "min_profit_change": min_profit_change,
            "min_change_month": min_profit_month, 
            "max_profit_change": max_profit_change, 
            "max_change_month": max_profit_month 
            }


def main():
    file_path = 'Resources'
    file_name = 'budget_data.csv'
    profit_data = read_csv('Resources', 'budget_data.csv')

    total_profit = profit_data[1]
    num_of_months = calculate_total_number_of_months(profit_data)
    profit_changes = calculate_profit_changes(profit_data)

    max_change_month = profit_changes["max_change_month"]
    max_profit_change = profit_changes["max_profit_change"]
    
    min_change_month = profit_changes["min_change_month"]
    min_profit_change = profit_changes["min_profit_change"]

    print("Financial Analysis")
    print(f"{'-' * 40}")
    print(f'Total Months: {num_of_months }')
    print(f'Total: ${total_profit}')
    print(f'Average  Change: ${ round(profit_changes["avg_profit_change"], 2) }')
    print(f'Greatest Increase in Profits: { max_change_month } (${ max_profit_change })')
    print(f'Greatest Decrease in Profits: { min_change_month } (${ min_profit_change })\n')


# profits = []
# months_profits = []


# csvpath = os.path.join('Resources', 'budget_data.csv')


# with open(csvpath, newline='') as csvfile:

# 	csvreader = csv.reader(csvfile, delimiter=',')

# 	next(csvreader)

# 	for row in csvreader:
# 		months_profits.append([row[0], float(row[1])])


# # Get total number of months
# num_of_months = len(months_profits)


# # Set initial values
# total_profits = months_profits[0][1] + months_profits[1][1]
# total_profit_change = months_profits[1][1] - months_profits[0][1]
# greatest_increase_in_profit = total_profit_change
# greatest_decrease_in_profit = total_profit_change
# greatest_increase_month = months_profits[1][0]
# greatest_decrease_month = months_profits[1][0]


# # Calculatie total profit change
# # Get the greatest increase in profit
# # Get the greatest decrease in profit
# i = 2

# while i <= (num_of_months - 1):
# 	profit_change = months_profits[i][1] - months_profits[i-1][1]
# 	total_profit_change = total_profit_change + profit_change

# 	if profit_change > greatest_increase_in_profit:
# 		greatest_increase_in_profit = profit_change
# 		greatest_increase_month = months_profits[i][0]

# 	if profit_change < greatest_decrease_in_profit:
# 		greatest_decrease_in_profit = profit_change
# 		greatest_decrease_month = months_profits[i][0]

# 	i = i + 1


# # Calculate average profit change
# average_monthly_profit_change = total_profit_change / (num_of_months - 1)


# # Print result on screen
# print("")
# print("Financial Analysis")
# print(f"{'-' * 40}")
# print(f'Total Months: { num_of_months }')
# print(f'Total: ${ round(total_profits) }')
# print(f'Average  Change: ${ round(average_monthly_profit_change, 2) }')
# print(f'Greatest Increase in Profits: { greatest_increase_month } (${ round(greatest_increase_in_profit) })')
# print(f'Greatest Decrease in Profits: { greatest_decrease_month } (${ round(greatest_decrease_in_profit) })')
# print("")


# # print result to a text file
# if not os.path.isdir('output'):
# 	os.makedirs('output')

# outputfile = 'output/bank_data_analysis.txt'

# with open(outputfile, 'w') as textfile:

# 	textfile.write('Financial Analysis \n')
# 	textfile.write(f"{'-' * 40}\n")
# 	textfile.write(f'Total Months: { num_of_months }\n')
# 	textfile.write(f'Total: ${ round(total_profits) }\n')
# 	textfile.write(f'Average  Change: ${ round(average_monthly_profit_change, 2) }\n')
# 	textfile.write(f'Greatest Increase in Profits: { greatest_increase_month } (${ round(greatest_increase_in_profit) })\n')
# 	textfile.write(f'Greatest Decrease in Profits: { greatest_decrease_month } (${ round(greatest_decrease_in_profit) })\n')



