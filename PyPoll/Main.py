import csv ,operator
from itertools import groupby
with open("/Users/jobyaugustine/Desktop/Assignments/MyAssignmentRepos/python-challenge/PyPoll/Resources/election_data.csv","r") as pypoll_file:
    csv_reader=csv.reader(pypoll_file,delimiter=',')
    next(csv_reader)  # moving to the first row , skipping the headers
    # sort data on the basis of candidate
    csv_reader= sorted(csv_reader, key=operator.itemgetter(2))    
    count_votes=0
    sorted_candidate_list=[]
    for line in csv_reader:
        sorted_candidate_list.append(line[2])
        count_votes= count_votes + 1
    print(len(sorted_candidate_list))
    
    dict_result = {}

    next=1
    current = 0
    totCandidateCnt = 1
    counter = 0
    while counter <= len(sorted_candidate_list) :
        if next < len(sorted_candidate_list):
            if (sorted_candidate_list[current] == sorted_candidate_list[next]):
                totCandidateCnt += 1
                
            else:
                print(sorted_candidate_list[current],totCandidateCnt) 
                dict_result.update({sorted_candidate_list[current]:totCandidateCnt})   
                totCandidateCnt = 1
                
   
        next +=1
        current +=1  
        counter += 1  
    #print(sorted_candidate_list[current-2],totCandidateCnt)  
    dict_result.update({sorted_candidate_list[current-2]:totCandidateCnt})  
    print(dict_result)
    sorted_result = sorted(dict_result.items(), key=operator.itemgetter(1),reverse=True)    
    print(sorted_result)
    print("Election Results\n ----------------")
    print(f'Total Votes : {count_votes} \n ------------------------')
    for key, value in sorted_result:
         #print(key,value)
         percent_candidate = (value/count_votes) *100
         print(f'{key} : {round(percent_candidate,2)} % ({value})')
    print(" ---------------------------")
    print(f'Winner: {sorted_result[0][0]}')
    print(" ---------------------------")

#writing the result to a text file
# with open('/Users/jobyaugustine/Desktop/Assignments/MyAssignmentRepos/python-challenge/PyPoll/Analysis/result.txt','w') as f:
#     f.write(final_result)


# 