
#add dependencies
import csv
import os

#assign variable to load a file from a path
file_to_load = os.path.join("election_results.csv")

#assign variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#-------------------------------(variables)-----------------------------------
total_votes = 0
candidate_options = [] #(as list)
candidate_votes = {} #(as dictionary)

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#-----------------------------(open file:no indent)---------------------------------------------------
#open "election results" and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)

#----------(obtain data from file to fill list and dictioinary:indent 1)-------------
    #print each row in the CSV file
    for row in file_reader:
        #1. add to the total vote count.
        total_votes += 1
        #2. get the candidate name from each row.
        candidate_name = row[2]

        #if the candidate does not match any existing candidate add it the
        # the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #and begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        #then add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
#----done with file

#---------------------------(generate and print results)------------------------------
#summary of results
for candidate_name in candidate_votes:
    #redefine vote count and percentage
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    
    #print each candidate, voter count, and percentage to terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#determine the winner
    #determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

# Print the winning candidates' results to the terminal.

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)
