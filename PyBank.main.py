#To DO Homework
# Import
import os
import csv

# Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Set Path for File
csvpath = "budget.data.csv"

#Open and Read CSV File


    #CSV Reader Specifies Delimiter & Variable that Holds Contents
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read Header Row First
    csv_header = next(csvreader)
    row = next(csvreader)

    #Calculate Total Number of Months, Net Amount of P&L, and Set Variables for Rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

#Read Each Row of Data After the Header
    for row in csvreader:
    #Calculate Total Number of Months Included in Dataset
        total_months += 1
    #Calculate Net Amount of P&L over Entire Period
        net_amount += int(row[1])

    #Calculate Change from Current Month to Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

    #Calculate the Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
    #Calculate the Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    #Calculate the Average & The Date
        average_change = sum(monthly_change)/ len(monthly_change)

        highest = max(monthly_change)
        lowest = min(monthly_change)

    #Print Analysis
    print(f"Financial Analysis")
    print(f"----------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_amount}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
    print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

    #Create File to Write To:
    output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')

    #Open FIle in Write mode and write Print Analysis:
    with open(output_file, "w",) as txtfile:
        txtfile.write(f"Financial Analysis\n")
        txtfile.write(f"-----------------------\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${net_amount}\n")
        txtfile.write(f"Average Change: ${average_change}\n")
        txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
        txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
        