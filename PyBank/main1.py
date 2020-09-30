import os        
import csv      

total_months = 0
total_pl = 0
change_pl = 0
avg_change = 0
prev_total=0
running_avg_change = 0
greatest_increase = 0
greatest_decrease = 0
second_row = True

filepath=os.path.join('.','Resources', 'budget_data.csv')                  #os.path.join combines pathnames into one complete relative path

with open(filepath) as csvfileFileStream:
    data = csvfileFileStream.readlines()
    lastRow = data [-1]
   
    firstrow = True

    for row in data:
        if firstrow:
            firstrow = False
            continue
        total_months = total_months+(len(row[0]))
        amount = row.split(',')                                            #split rows to get values from both columns
        total_pl = total_pl + (int(amount[1]))
        if not second_row:
            avg_change= int(amount[1])-prev_total
            if (avg_change > 0) and (avg_change > greatest_increase):       #check for greatest increase
                greatest_increase = avg_change
                greatest_inc_date = amount[0]
            elif (avg_change < 0) and (avg_change < greatest_decrease):
                greatest_decrease = avg_change
                greatest_dec_date = amount[0]                              #check for greatest decrease
            running_avg_change = running_avg_change + avg_change
            avg_change = 0
            prev_total = int(amount[1])
        prev_total = int(amount[1])
        second_row = False
    avg_change = running_avg_change/(total_months-1)
    
    print(f"Financial Analysis:") 
    print(f"Total Months: {total_months}")                                  #prints the csv file
    print(f"Total Profit/Loss: ${total_pl}")
    print(f"Average Change: ${round(avg_change, 2)}")                       #rounds the output value to 2 decimal places
    print(f"Greatest Increase in Profits: {greatest_inc_date} ${greatest_increase}")
    print(f"Greatest Decrease in Losses: {greatest_dec_date} ${greatest_decrease}")  

    filename = "output.txt"                                                 #define the filename
    filepath = os.path.join('.','Analysis', 'output.txt') 
    
    with open(filepath, 'w') as textfile:
        textfile.write(f"Financial Analysis:")                                 
        textfile.write(f"\nTotal Months: {total_months}")                         
        textfile.write(f"\nTotal Profit/Loss: ${total_pl}")                 #\n outputs on new line
        textfile.write(f"\nAverage Change: ${round(avg_change, 2)}")              
        textfile.write(f"\nGreatest Increase in Profits: {greatest_inc_date} ${greatest_increase}")
        textfile.write(f"\nGreatest Decrease in Losses: {greatest_dec_date} ${greatest_decrease}")
