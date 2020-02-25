#set up modules for csv

import os
import csv
import operator

#set initial values for total number of votes
total_votes = 0


#set up list for candidates and dictionary for vote count
candidate_list = []
candidate_vote_count = {}

#set path for uploading file as well as file for outputing results
load_file = os.path.join("..", "PyPoll", "election_data.csv")
output_file = os.path.join("..","PyPoll","PyPollResults.txt")

#open CSV file containing election data
with open(load_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)


    #set up loop to read values from csv, calculate total votes, and count votes per election candidate
    for row in csvreader:
        total_votes = total_votes + 1
        election_candidate = row[2]

        if election_candidate not in candidate_list:

            candidate_list.append(election_candidate)

            candidate_vote_count[election_candidate] = 0

        candidate_vote_count[election_candidate] = candidate_vote_count[election_candidate] + 1 



#Print Election Results with total votes and votes by each candidate

print()
print("Election Results")
print("-----------------")
print("Total Votes: ",total_votes)
print("-----------------")
print(candidate_vote_count)
print()

#Determine election winner

election_winner = max(candidate_vote_count.items(), key=operator.itemgetter(1))[0]

print("----------------------------------")
print("Election Winner: ",election_winner)

      

#Write requested values to output file
with open(output_file, "w") as txt_file:
    txt_file.write("Total Votes: " + str(total_votes))
    txt_file.write("Votes by Candidate: " + str(candidate_vote_count))
    txt_file.write("Election Winner: " + str(election_winner))
