#set up modules for csv

import os
import csv

#set initial values for Total number of votes
total_votes = 0


#set up list for Candidates
#candidate_list = []


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
        #candidate_list = candidate_list + [row[2]]




print()
print("Election Results")
print("-----------------")
print("Total Votes: " + str(total_votes))
print("-----------------")
#print("Candidate Name: " + str(candidate_list))

#Write requested values to output file
with open(output_file, "w") as txt_file:
    txt_file.write("Total Votes: " + str(total_votes))
    #txt_file.write("Candidate Name: " + str(candidate_list))
