
import os
import csv

total_num_months = 0
total_profit_loss = 0
profit_loss_change = 0
total_profit_loss_change = 0
average_monthly_profit_loss_change = 0
greatest_increase_in_profit_loss = 0
greatest_increase_month = ""
greatest_decrease_in_profit_loss = 0
greatest_decrease_month = ""

csvpath = os.path.join('../PyBank', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	next(csvreader)

	for row in csvreader:

		total_num_months = total_num_months + 1
		profit_loss = float(row[1])
		total_profit_loss = total_profit_loss + profit_loss

		if total_num_months > 1:
			profit_loss_change = profit_loss - previous_profit_loss

		total_profit_loss_change = total_profit_loss_change + profit_loss_change

		if profit_loss_change > greatest_increase_in_profit_loss:
			greatest_increase_in_profit_loss = profit_loss_change
			greatest_increase_month = row[0]
		elif profit_loss_change < greatest_decrease_in_profit_loss:
			greatest_decrease_in_profit_loss = profit_loss_change
			greatest_decrease_month = row[0]

		previous_profit_loss = profit_loss

	average_monthly_change = total_profit_loss_change / (total_num_months - 1)

	print("")
	print("Financial Analysis")
	print("-" * 40)
	print("")
	print(f'Total Months: {total_num_months}')
	print(f'Total: ${round(total_profit_loss)}')
	print(f'Average  Change: ${round(average_monthly_change, 2)}')
	print(f'Greatest Increase in Profits: {greatest_increase_month} (${round(greatest_increase_in_profit_loss)})')
	print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${round(greatest_decrease_in_profit_loss)})')
	print("")

	if not os.path.isdir('../PyBank/output'):
		os.makedirs('../PyBank/output')

	output_path = os.path.join("../PyBank", "output", "bank_data_analysis.csv")

	with open(output_path, 'w', newline='') as csvfile:

		csvwriter = csv.writer(csvfile, delimiter=',')
		csvwriter.writerow(['Financial Analysis'])
		csvwriter.writerow(["-" * 40])
		csvwriter.writerow("")
		csvwriter.writerow([f'Total Months: {total_num_months}'])
		csvwriter.writerow([f'Total: ${round(total_profit_loss)}'])
		csvwriter.writerow([f'Average  Change: ${round(average_monthly_change, 2)}'])
		csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase_month} (${round(greatest_increase_in_profit_loss)})'])
		csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease_month} (${round(greatest_decrease_in_profit_loss)})'])

		# def as_currency(amount):
		# 	if amount >= 0:
		# 		return '${:,.2f}'.format(amount)
		# 	else:
		# 		return '-${:,.2f}'.format(-amount)


