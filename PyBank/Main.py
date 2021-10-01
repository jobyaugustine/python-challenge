import csv

with open("/Users/jobyaugustine/Desktop/Assignments/MyAssignmentRepos/python-challenge/PyBank/Resources/budget_data.csv","r") as pybank_file:
    csv_reader=csv.reader(pybank_file,delimiter=',')
    next(csv_reader)  # moving to the first row , skipping the headers

# initializing variables for total number of months and total profit/loss   
    count_months = 0  
    tot = 0
   
    change_total = 0
    array_profit = []  #creating array for profits
    array_dates = [] #creating array for months
    for line in (csv_reader):
       tot =tot + int(line[1])
       count_months = count_months + 1
       array_profit.append(line[1])
       array_dates.append(line[0])

k=0
l =1
change_n1 = 0  # for each month's change 
change_n1_tot =0  # total change 
max_inc = 0  #for greatest increase in profit
min_dec =0   # for greatest decrease in profit
max_index = 0
min_index = 0
while k<=len(array_profit)-2:
    change_n1 = int(array_profit[l]) - int(array_profit[k])
    change_n1_tot += change_n1
    if max_inc < change_n1:
        max_inc = change_n1
        max_index = l
    if change_n1 < min_dec:
        min_dec = change_n1
        min_index = l
    k=k+1
    l=l+1



print(f'Total Months: {count_months} ')
print(f'Total: ${tot} ')
print(f'Average Change:  {round(change_n1_tot/(len(array_profit)-1),2)}')
print(f'Greatest Increase in Profits:  {array_dates[max_index]} (${max_inc})  ' )
print(f'Greatest Decrease in Profits:  {array_dates[min_index]} (${min_dec} ) ')


final_result = (f'Total Months: {count_months} ')+"\n" +(f'Total: ${tot} ') + "\n"+(f'Average Change: + {round(change_n1_tot/(len(array_profit)-1),2)}') + "\n" +  (f'Greatest Increase in Profits: {array_dates[max_index]} (${max_inc}) ')+"\n" + (f'Greatest Decrease in Profits:  {array_dates[min_index]} (${min_dec})') 

#print(final_result)

# writing the result to a text file
with open('/Users/jobyaugustine/Desktop/Assignments/MyAssignmentRepos/python-challenge/PyBank/Analysis/result.txt','w') as f:
    f.write(final_result)



