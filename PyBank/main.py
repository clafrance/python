# -- The total number of months included in the dataset
# -- The total net amount of "Profit/Losses" over the entire period
# -- The average change in "Profit/Losses" between months over the entire period
# -- The greatest increase in profits (date and amount) over the entire period
# -- The greatest decrease in losses (date and amount) over the entire period
# -- print the analysis to the terminal and export a text file with the results.

import os
import csv

profits = []
months_profits = []


# Read csv data file
csvpath = os.path.join('Resources', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	next(csvreader)

	for row in csvreader:
		months_profits.append([row[0], float(row[1])])


# Get total number of months
num_of_months = len(months_profits)


# Set initial values
total_profits = months_profits[0][1] + months_profits[1][1]
total_profit_change = months_profits[1][1] - months_profits[0][1]
greatest_increase_in_profit = total_profit_change
greatest_decrease_in_profit = total_profit_change
greatest_increase_month = months_profits[1][0]
greatest_decrease_month = months_profits[1][0]


# Calculatie total profit change
# Get the greatest increase in profit
# Get the greatest decrease in profit
i = 2

while i <= (num_of_months - 1):
	profit_change = months_profits[i][1] - months_profits[i-1][1]
	total_profit_change = total_profit_change + profit_change

	if profit_change > greatest_increase_in_profit:
		greatest_increase_in_profit = profit_change
		greatest_increase_month = months_profits[i][0]

	if profit_change < greatest_decrease_in_profit:
		greatest_decrease_in_profit = profit_change
		greatest_decrease_month = months_profits[i][0]

	i = i + 1


# Calculate average profit change
average_monthly_profit_change = total_profit_change / (num_of_months - 1)


# Print result on screen
print("")
print("Financial Analysis")
print(f"{'-' * 40}")
print(f'Total Months: { num_of_months }')
print(f'Total: ${ round(total_profits) }')
print(f'Average  Change: ${ round(average_monthly_profit_change, 2) }')
print(f'Greatest Increase in Profits: { greatest_increase_month } (${ round(greatest_increase_in_profit) })')
print(f'Greatest Decrease in Profits: { greatest_decrease_month } (${ round(greatest_decrease_in_profit) })')
print("")


# print result to a text file
if not os.path.isdir('../PyBank/output'):
	os.makedirs('../PyBank/output')

outputfile = '../PyBank/output/bank_data_analysis.txt'

with open(outputfile, 'w') as textfile:

	textfile.write('Financial Analysis \n')
	textfile.write(f"{'-' * 40}\n")
	textfile.write(f'Total Months: { num_of_months }\n')
	textfile.write(f'Total: ${ round(total_profits) }\n')
	textfile.write(f'Average  Change: ${ round(average_monthly_profit_change, 2) }\n')
	textfile.write(f'Greatest Increase in Profits: { greatest_increase_month } (${ round(greatest_increase_in_profit) })\n')
	textfile.write(f'Greatest Decrease in Profits: { greatest_decrease_month } (${ round(greatest_decrease_in_profit) })\n')



