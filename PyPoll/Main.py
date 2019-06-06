import os
import csv

# variables
candidates = []
votes = 0
vote_count = []

# List 
election_data = ['1', '2']

# open file 
for files in election_data:
    csvpath = os.path.join("/Users/u370166/python-challenge/PyBank/Resources/election_data.csv')
    with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

        # loop
        for row in csv_reader:
            votes = votes + 1
            candidate = row[2]
            if candidate in candidates:
                candidate = candidates.index(candidate)
                vote_count[candidate] = vote_count[candidate] + 1
            else:
                candidates.append(candidate)
                vote_count.append(1)

    # variables
    percentages = []
    max_votes = vote_count[0]
    max_index = 0

    for count in range(len(candidates)):
        vote_percentage = vote_count[count]/votes*100
        percentages.append(vote_percentage)
        if vote_count[count] > max_votes:
            max_votes = vote_count[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]

    # Print 
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # txt
    output_file = election_data.csv[0:-4]
    write_election_data.csv = f"{output_file}pypoll_results.txt"
    filewriter = open(write_election_data.csv, mode = 'w')
    filewriter.write("Election Results\n")
    filewriter.write("-------------------------\n")
    filewriter.write(f"Total Votes: {votes}\n")
    for count in range(len(candidates)):
        filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})\n")
    filewriter.write("-------------------------\n")
    filewriter.write(f"Winner: {winner}\n")
    filewriter.write("-------------------------\n")