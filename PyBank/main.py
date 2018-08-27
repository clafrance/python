
def main():

	def read_csv():
		return 0

	def as_currency(amount):
	    if amount >= 0:
	        return '${:,.2f}'.format(amount)
	    else:
	        return '-${:,.2f}'.format(-amount)

	def total_number_of_months():
		return 0

	def total_profit_or_loss():
		return 0

	def average_monthly_profit_or_loss():
		return 0

	def greatest_increase():
		return 0

	def greatest_decrease():	
		return 0
	def write_csv():
		return 0
	read_csv()

	total_months = total_number_of_months()
	total_amount_change = as_currency(total_profit_or_loss())
	average_monthly_change = as_currency(average_monthly_profit_or_loss())
	greatest_increase = as_currency(greatest_increase())
	greatest_decresse = as_currency(greatest_decrease())

	print("")
	print("Financial Analysis")
	print("-" * 30)
	print("")
	print(f"Total Months: {total_months}")
	print(f"Total: {total_amount_change}")
	print(f"Average  Change: {average_monthly_change}")
	print(f"Greatest Increase in Profits: {greatest_increase}")
	print(f"Greatest Decrease in Profits: {greatest_decresse}")
	print("")

	write_csv()


main()
