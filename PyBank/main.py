# -- The total number of months included in the dataset
# -- The total net amount of "Profit/Losses" over the entire period
# -- The average change in "Profit/Losses" between months over the entire period
# -- The greatest increase in profits (date and amount) over the entire period
# -- The greatest decrease in losses (date and amount) over the entire period
# -- print the analysis to the terminal and export a text file with the results.

import os
import csv
import sys

def read_csv(file_path, file_name):
    """ Read csv file, returns data and calculated total profit 
    
    Parameters
    ----------
    file_path: string
        File directory for the csv file
        
    file_name: string
        Name of the csv file
        
    Returns
    -------
    profit_data: list
        List of profit data
        
    total_profit: float
        Calculated profit
        
    """
    
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

    total_profit = round(total_profit, 2)  
    
    return profit_data, total_profit


def calculate_total_number_of_months(profit_data):
    """Calculate total number of months
    
    parameters
    ----------
    profit_data: list
        List of profit data
    
    Return
    ------
    length: int
        Length of input list
        
    """
    return len(profit_data[0])


def calculate_profit_changes(profit_data):
    """ Perform calculations
    
    parameters
    ----------
    profit_data: list
        List of profit data
    
    return 
    ------
    profit_calculations: dictiontory 
        A dictionary with the following:
            avg_profit_change, 
            min_profit_change,
            min_change_month, 
            max_profit_change, 
            max_change_month 
    """
    
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
    
    profit_calculations = {
        "avg_profit_change": avg_profit_change, 
        "min_profit_change": min_profit_change,
        "min_change_month": min_profit_month, 
        "max_profit_change": max_profit_change, 
        "max_change_month": max_profit_month 
    }

    return profit_calculations


def main():
    """Main function that is called when pybank is run on the command line"""
    
    file_path = 'Resources'
    file_name = 'budget_data.csv'
    
    try:
        profit_data = read_csv('Resources', 'budget_data.csv')
    except Exception as e:
        print("Reading csv file failed")
        sys.exit(1)

    total_profit = profit_data[1]
    num_of_months = calculate_total_number_of_months(profit_data)
    profit_changes = calculate_profit_changes(profit_data)

    max_change_month = profit_changes["max_change_month"]
    max_profit_change = profit_changes["max_profit_change"]
    
    min_change_month = profit_changes["min_change_month"]
    min_profit_change = profit_changes["min_profit_change"]

    print("Financial Analysis")
    print(f"{'-' * 40}")
    print(f'Total Months: { num_of_months }')
    print(f'Total: ${ total_profit }')
    print(f'Average  Change: ${ round(profit_changes["avg_profit_change"], 2) }')
    print(f'Greatest Increase in Profits: { max_change_month } (${ max_profit_change })')
    print(f'Greatest Decrease in Profits: { min_change_month } (${ min_profit_change })\n')
    
    if not os.path.isdir('output'):
        os.makedirs('output')

    outputfile = 'output/bank_data_analysis.txt'

    with open(outputfile, 'w') as textfile:
        textfile.write('Financial Analysis \n')
        textfile.write(f"{ '-' * 40 }\n")
        textfile.write(f'Total Months: { num_of_months }\n')
        textfile.write(f'Total: ${ total_profit }\n')
        textfile.write(f'Average  Change: ${ round(profit_changes["avg_profit_change"], 2) }\n')
        textfile.write(f'Greatest Increase in Profits: { max_change_month } (${ max_profit_change })\n')
        textfile.write(f'Greatest Decrease in Profits: { min_change_month } (${ max_profit_change })\n')


if __name__ == '__main__':
    main()

