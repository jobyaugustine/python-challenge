import csv 
from collections import defaultdict

#function displayResult to display all the results.dictionary and total votes are the parameters.
def displayResult(sorted_result, count_votes):

    #the results are written to the file result1.txt

    with open('/Users/jobyaugustine/Desktop/Assignments/MyAssignmentRepos/python-challenge/PyPoll/Analysis/result1.txt','w') as f:
        f.write("Election Results\n----------------\n")
        f.write(f'Total Votes : {count_votes} \n------------------------\n')
    
        print("Election Results\n----------------")
        print(f'Total Votes : {count_votes} \n------------------------')
        
        for key, value in sorted_result.items():
            percent_candidate = (value/count_votes) *100
            print(f'{key} : {round(percent_candidate,2)} % ({value})')
            f.write(f'{key} : {round(percent_candidate,2)} % ({value})\n')
        print("---------------------------")
        f.write("---------------------------\n")
        print(f'Winner: {list(sorted_result.keys())[0]}')
        f.write(f'Winner: {list(sorted_result.keys())[0]}\n')
        print(" ---------------------------")
        f.write(" ---------------------------\n")
        return

with open("/Users/jobyaugustine/Desktop/Assignments/MyAssignmentRepos/python-challenge/PyPoll/Resources/election_data.csv","r") as pypoll_file:
    csv_reader=csv.reader(pypoll_file,delimiter=',')
    # moving to the first row , skipping the headers
    next(csv_reader)  

    # creating a dictionary
    my_dict = {}

    #populating the dictionary with VoterId as key and Candidate Name as value.
    my_dict = {rows[0]:rows[2] for rows in csv_reader}

    # finding the length of the dictionary which is the total number of votes casted.
    total_count = len(my_dict)

    # creating a default dictionary with elements of list
    v = defaultdict(list)

    #default dictionary is populated from the sorted my_dict dictionary with candidate as key and voterId as value.VoterIDs for the
    # candidate are added to the list

    for voterid, candname in sorted(my_dict.items()):
        v[candname].append(voterid)
    #print(len(v))

    # creating my_dict dictionary 
    my_dict={}

    # my_dict dictionary is populated with the data from the default dictionary.
    #my_dict dictionary is getting the key as the candidate name , value as the length of the list in the default dictionary
    #value of my_dict is the total number of votes for each candidate.
    for key,value1 in v.items():
        #print(key)
        #print(len(value1))
        my_dict.update({key:len(value1)})

    #displayResult function is called , passing the my_dict dictionary and total_count as the arguments.
    displayResult(my_dict,total_count)


    
        
    