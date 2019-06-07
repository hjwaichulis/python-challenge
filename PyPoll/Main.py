import os
import csv
import collections
import sys

#Import csv
csvpath = os.path.join("/Users/u370166/python-challenge/PyPoll/Resources/election_data.csv")
with open(csvpath, newline="") as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    #my lists
    vote_count=[]
    candidate = []
    votes = {}

    # Total votes
    for row in csv_reader:
        vote_count.append(row[0])
        candidate.append(row[2])
    vote_total = len(vote_count)
    
    # Candidate dictionary 
    for i in candidate:
        if i not in votes:
            votes[i] = 1
        else:
            votes[i] += 1
    voters=dict(sorted(votes.items(), key=lambda x: x[1], reverse=True))
     
    # voting list
    voting_list=list(voters.values())
    first_place_votes = voting_list[0]
    second_place_votes =voting_list[1]
    third_place_votes = voting_list[2]
    fourth_place_votes = voting_list[3]
    
    # voting perecentages
    first_place_percentage = format(first_place_votes/vote_total*100,'.3f')
    second_place_percentage = format(second_place_votes/vote_total*100,'.3f')
    third_place_percentage = format(third_place_votes/vote_total*100,'.3f')
    fourth_place_percentage = format(fourth_place_votes/vote_total*100,'.3f')
 
    # candidate list 
    candidate_list=list(voters)
    winner = candidate_list[0]
    second_place = candidate_list[1]
    third_place = candidate_list[2]
    fourth_place = candidate_list[3]


#Print out results to terminal
print("Election Results")
print("------------------------------")
print(f'Total Votes: {vote_total}')
print("------------------------------")
print(f'{winner}: {first_place_percentage}% ({first_place_votes})')
print(f'{second_place}: {second_place_percentage}% ({second_place_votes})')
print(f'{third_place}: {third_place_percentage}% ({third_place_votes})')
print(f'{fourth_place}: {fourth_place_percentage}% ({fourth_place_votes})')
print("------------------------------")
print(f'Winner: {winner}')
print("------------------------------")

#Print out results to file
txtpath = os.path.join("/Users/u370166/python-challenge/PyPoll/Resources/results.txt")
with open(txtpath, 'w') as f:
    print("Election Results",file=f)
    print("------------------------------",file=f)
    print(f'Total Votes: {vote_total}',file=f)
    print("------------------------------",file=f)
    print(f'{winner}: {first_place_percentage}% ({first_place_votes})',file=f)
    print(f'{second_place}: {second_place_percentage}% ({second_place_votes})',file=f)
    print(f'{third_place}: {third_place_percentage}% ({third_place_votes})',file=f)
    print(f'{fourth_place}: {fourth_place_percentage}% ({fourth_place_votes})',file=f)
    print("------------------------------",file=f)
    print(f'Winner: {winner}',file=f)
    print("------------------------------",file=f)