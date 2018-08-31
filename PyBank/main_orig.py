# -- The total number of months included in the dataset
# -- The total net amount of "Profit/Losses" over the entire period
# -- The average change in "Profit/Losses" between months over the entire period
# -- The greatest increase in profits (date and amount) over the entire period
# -- The greatest decrease in losses (date and amount) over the entire period
# -- print the analysis to the terminal and export a text file with the results.

import os
import csv

total_num_months = 0
total_profit = 0
profit_change = 0
total_profit_change = 0
average_monthly_profit_change = 0
greatest_increase_in_profit = 0
greatest_increase_month = ""
greatest_decrease_in_profit = 0
greatest_decrease_month = ""

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	next(csvreader)

	for row in csvreader:

		total_num_months = total_num_months + 1
		profit = float(row[1])
		total_profit = total_profit + profit

		if total_num_months > 1:
			profit_change = profit - previous_profit

		total_profit_change = total_profit_change + profit_change

		if profit_change > greatest_increase_in_profit:

			greatest_increase_in_profit = profit_change
			greatest_increase_month = row[0]

		elif profit_change < greatest_decrease_in_profit:

			greatest_decrease_in_profit = profit_change
			greatest_decrease_month = row[0]

		previous_profit = profit

	average_monthly_change = total_profit_change / (total_num_months - 1)

	print("")
	print("Financial Analysis")
	print("-" * 40)
	print("")
	print(f'Total Months: { total_num_months }')
	print(f'Total: ${ round(total_profit) }')
	print(f'Average  Change: ${ round(average_monthly_change, 2) }')
	print(f'Greatest Increase in Profits: { greatest_increase_month } (${ round(greatest_increase_in_profit) })')
	print(f'Greatest Decrease in Profits: { greatest_decrease_month } (${ round(greatest_decrease_in_profit) })')
	print("")

	if not os.path.isdir('../PyBank/output'):
		os.makedirs('../PyBank/output')

	outputfile = '../PyBank/output/bank_data_analysis.txt'

	with open(outputfile, 'w') as textfile:
	
		textfile.write('Financial Analysis \n')
		textfile.write("-" * 40)
		textfile.write("\n")
		textfile.write(f'Total Months: { total_num_months }\n')
		textfile.write(f'Total: ${ round(total_profit) }\n')
		textfile.write(f'Average  Change: ${ round(average_monthly_change, 2) }\n')
		textfile.write(f'Greatest Increase in Profits: { greatest_increase_month } (${ round(greatest_increase_in_profit) })\n')
		textfile.write(f'Greatest Decrease in Profits: { greatest_decrease_month } (${ round(greatest_decrease_in_profit) })\n')



