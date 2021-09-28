import csv ,operator

def displayResult(sorted_result, count_votes):
    with open('/Users/jobyaugustine/Desktop/Assignments/MyAssignmentRepos/python-challenge/PyPoll/Analysis/result.txt','w') as f:
        f.write("Election Results\n----------------\n")
        f.write(f'Total Votes : {count_votes} \n------------------------\n')
    
        print(sorted_result,count_votes)
        print("Election Results\n----------------")
        print(f'Total Votes : {count_votes} \n------------------------')
        
        for key, value in sorted_result:
         percent_candidate = (value/count_votes) *100
         print(f'{key} : {round(percent_candidate,2)} % ({value})')
         f.write(f'{key} : {round(percent_candidate,2)} % ({value})\n')
        print("---------------------------")
        f.write("---------------------------\n")
        print(f'Winner: {sorted_result[0][0]}')
        f.write(f'Winner: {sorted_result[0][0]}\n')
        print(" ---------------------------")
        f.write(" ---------------------------\n")
        return

       
with open("/Users/jobyaugustine/Desktop/Assignments/MyAssignmentRepos/python-challenge/PyPoll/Resources/election_data.csv","r") as pypoll_file:
    csv_reader=csv.reader(pypoll_file,delimiter=',')
    # moving to the first row , skipping the headers
    next(csv_reader)  
    # sort data on the basis of candidate
    csv_reader= sorted(csv_reader, key=operator.itemgetter(2))    
    count_votes=0
    sorted_candidate_list=[]
    for line in csv_reader:
        sorted_candidate_list.append(line[2])
        count_votes= count_votes + 1
    
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
                dict_result.update({sorted_candidate_list[current]:totCandidateCnt})   
                totCandidateCnt = 1
                
   
        next +=1
        current +=1  
        counter += 1  

    dict_result.update({sorted_candidate_list[current-2]:totCandidateCnt})  
    sorted_result = sorted(dict_result.items(), key=operator.itemgetter(1),reverse=True) 

    # to display results and write to result file       
    displayResult(sorted_result,count_votes)




