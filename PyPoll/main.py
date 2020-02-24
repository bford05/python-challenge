#set up modules for csv

import os
import csv

#set initial values for Total number of votes
total_votes = 0


#set up list for candidates and vote count
candidate_list = []
candidate_vote_count = []

#set path for uploading file as well as file for outputing results
load_file = os.path.join("..", "PyPoll", "election_data.csv")
output_file = os.path.join("..","PyPoll","PyPollResults.txt")

#open CSV file containing election data
with open(load_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    first_row = next(csvreader)
    total_votes = total_votes + 1

    #set up loop to read values from election data csv calculate requested data
    for row in csvreader:
        total_votes = total_votes + 1
        election_candidate = first_row[2]

    #Identify all candidates from the csv file and count votes per candidate
        if election_candidate in candidate_list:
            candidate_index = candidate_list.index(election_candidate)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
            
        else:
            candidate_list.append(election_candidate)
            candidate_vote_count.append(1)

#store variables for determining percentage for each candidate along with determining winner        
candidate_percentages_list = []
max_votes = candidate_vote_count[0]
max_index = 0

for count in range(len(candidate_list)):
    candidate_vote_percent = candidate_vote_count[count]/total_votes*100

    candidate_percentages_list.append(candidate_vote_percent)

    if candidate_vote_count[count] > max_votes:
        max_votes = candidate_vote_count[count]
        print(max_votes)
        max_index = count
winner = candidate_list[max_index]

candidate_percentages_list = [round(i,2) for i in candidate_percentages_list]

#Print request values in terminal
print()
print("Election Results")
print("-----------------")
print("Total Votes: " + str(total_votes))
print("-----------------")
for count in range(len(candidate_list)):
    print(f"{candidate_list[count]}: {candidate_percentages_list[count]}% ({candidate_vote_count[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


#Write requested values to output file
#with open(output_file, "w") as txt_file:
    #txt_file.write("Total Votes: " + str(total_votes))
    #txt_file.write("Candidate Name: " + str(candidate_list))
