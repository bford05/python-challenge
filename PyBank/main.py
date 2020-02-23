#set up modules for csv

import os
import csv

#set initial values for total month, total revenue, previous profit loss, and profit loss change
total_month_volume = 0
total_revenue_volume = 0

#set up list for net change and month list change from csv
profit_loss_change_list = []
month_change_list = []


#set path for uploading file as well as file for outputing results
load_file = os.path.join("..", "PyBank", "budget_data.csv")
output_file = os.path.join("..","PyBank","PyBankResults.txt")


#open CSV file containing budget data
with open(load_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    first_row = next(csvreader)
    total_month_volume = total_month_volume + 1
    total_revenue_volume = total_revenue_volume + int(first_row[1])
    previous_profit_loss = int(first_row[1]) 

#set up loop to read values from budget data csv and calculate requested information
    for row in csvreader:
        total_month_volume = total_month_volume + 1
        total_revenue_volume = total_revenue_volume + int(row[1])
        profit_loss_change = int(row[1]) - previous_profit_loss
        previous_profit_loss = int(row[1])
        profit_loss_change_list = profit_loss_change_list + [profit_loss_change]
        month_change_list = month_change_list + [row[0]]
        
Average_profit_loss_change = sum(profit_loss_change_list)/len(profit_loss_change_list)

#Calculate greatest decrease and greatest increase in profits
greatest_decrease = min(profit_loss_change_list)
greatest_increase = max(profit_loss_change_list)

#Assign appropriate month to greatest decrease in profits and greatest decrease in profits
greatest_decrease_index = (profit_loss_change_list).index(greatest_decrease)
greatest_decrease_month = (month_change_list)[greatest_decrease_index]

greatest_increase_index = (profit_loss_change_list).index(greatest_increase)
greatest_increase_month = (month_change_list)[greatest_increase_index]


#Print requested values in terminal
print()
print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(total_month_volume))
print("Total: " + "$" + str(total_revenue_volume))
print("Average Change: " + "$" + str(Average_profit_loss_change))
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " " + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " " + " " + "$" + str(greatest_decrease))

#Write requested values to output file
with open(output_file, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_month_volume))
    txt_file.write("Total: " + "$" + str(total_revenue_volume))
    txt_file.write("Average Change: " + "$" + str(Average_profit_loss_change))
    txt_file.write("Greatest Increase in Profits: " + str(greatest_increase_month) + " " + " " + "$" + str(greatest_increase))
    txt_file.write("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " " + " " + "$" + str(greatest_decrease))




