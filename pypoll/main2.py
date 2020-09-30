import os        
import csv      

total_votes = 0
candidate_dict={}

filepath = os.path.join('.','Resources', 'election_data.csv')                  #os.path.join combines pathnames into one complete relative path

with open(filepath) as csvfileFileStream:
    data = csvfileFileStream.readlines()

    firstrow = True

    for row in data:
        if firstrow:
            firstrow = False                                                    # check to start the for loop after header row
            continue
        row_data = row.split(",")                                               #split to get values from all columns
        if row_data[2] in candidate_dict:
            candidate_dict[row_data[2]]=candidate_dict[row_data[2]]+1
        else:
            candidate_dict[row_data[2]]=1
        total_votes = total_votes + 1
       
    
    max_votes=0
    winner=""
    for key in candidate_dict:
        if max_votes < candidate_dict[key]:
            max_votes=candidate_dict[key]
            winner=key
   
        print (str(key).strip() + " got " + str(round(int(candidate_dict[key])/total_votes*100, 2)) + " % votes") # used strip to clear unwanted spaces
    
    print(f"Election Results:")
    print(f"----------------------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------------------------")
    print(f"The Candidates got votes as follows: {candidate_dict}")
    print(f"----------------------------------------------")
    print(f"Winner: {winner}")

    filename = "pypolloutput.txt"                                                 #define the o/p filename
    filepath = os.path.join('.','Analysis', 'pypolloutput.txt') 
    
    with open(filepath, 'w') as textfile:
        textfile.write(f"Election Results:")                                 
        textfile.write(f"\nTotal Votes: {total_votes}")                         
        textfile.write(f"\nThe Candidates got votes as follows: {candidate_dict}")                 #\n outputs on new line
        textfile.write(f"\nWinner: {winner}")
