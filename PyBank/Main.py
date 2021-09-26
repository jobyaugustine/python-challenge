import csv
from os import lseek

with open("/Users/jobyaugustine/Desktop/Assignments/Python_Assignment_Oct2/WorkFolder/budget_data.csv","r") as pybank_file:
    csv_reader=csv.reader(pybank_file,delimiter=',')
    next(csv_reader)  # moving to the first row , skipping the headers
   
    count_months = 0
    tot = 0
   
    change = 0
    change_total = 0
    array_profit = []
    array_dates = []
    for line in (csv_reader):
       tot =tot + int(line[1])
       prevprofit = int(line[1])
       count_months = count_months + 1
       array_profit.append(line[1])
       array_dates.append(line[0])

k=0
l =1
change_n1 = 0
change_n1_tot =0
max_inc = 0
min_dec =0
max_index = 0
min_index = 0
while k<=len(array_profit)-2:
    change_n1 = int(array_profit[l]) - int(array_profit[k])
    change_n1_tot += change_n1
    if max_inc < change_n1:
        max_inc = change_n1
        max_index=l
    if change_n1 < min_dec:
        min_dec = change_n1
        min_index = l
    k=k+1
    l=l+1

#print(change_n1_tot)
print(f'Greatest Increase in Profits: + {max_inc} + {array_dates[max_index]}' )
print(f'Greatest Decrease in Profits: + {min_dec} + {array_dates[min_index]}')
print(change_n1_tot/(len(array_profit)-1))
print(f'Total Months: {count_months} ')
print(f'Total: ${tot} ')
print(f'Average Change: + {change_n1_tot/(len(array_profit)-1)}')
# print(f)

final_result = (f'Total Months: {count_months} ')+"\n" +(f'Total: ${tot} ') + "\n"+(f'Average Change: + {change_n1_tot/(len(array_profit)-1)}') + (f'{max_inc} + {array_dates[max_index]}') 

print(final_result)

with open('result.txt','w') as f:
    f.write(final_result)



