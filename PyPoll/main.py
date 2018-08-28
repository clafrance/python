# -- The total number of votes cast
# -- A complete list of candidates who received votes
# -- The total number of votes each candidate won
# -- The percentage of votes each candidate won
# -- The winner of the election based on popular vote.
# -- print the analysis to the terminal and export a text file with the results.


import os
import csv

voters = []
counties = []
candidates = []
votes_per_candidate = []
votes_candidate = {}
candidate_votes = {}

# Read the input election data csv file
csvpath = os.path.join('../PyPoll', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	next(csvreader)

	for row in csvreader:
		voters.append(row[0])
		counties.append(row[1])
		candidates.append(row[2])

# Get the total number of votes
total_votes = len(set(voters))

if not total_votes == len(voters):
	print("Duplicate Voter IDs in the data")
	exit()

# Get the list of candidates who received votes
candidates_received_votes = set(candidates)

# GCalculate how many votes each candidate received, 
# Generate a list to track votes for each candidate
# Generate a Dictionary to track votes and candidate pair with votes as key, unsorted
for candidate in candidates_received_votes:
	votes = candidates.count(candidate)
	votes_per_candidate.append(votes)
	votes_candidate[votes] = candidate
	
# Sort the votes list generated above in decending order	
votes_per_candidate = sorted(votes_per_candidate, reverse=True)

# Generate a Dictionary to track votes and candidate pair with candidate as key, it is sorted by votes
for votes in votes_per_candidate:
	candidate = votes_candidate[votes]
	percentage = (votes / total_votes) * 100
	candidate_votes[candidate] = [votes, percentage]

# Through sorted candidate/votes dictionary, find the winner's name	
winner = list(candidate_votes.keys())[0]

def print_divider_line():
	print(f"{'-' * 30}")

# Print result on screen
print('')
print('Election Results')
print_divider_line()
print(f'Total Votes: { total_votes }')
print_divider_line()
for key in candidate_votes:
	candidate = key
	votes = candidate_votes[key][0]
	percentage = candidate_votes[key][1]
	print(f"{ candidate }: {percentage:7.3f}% ({ votes })")
print_divider_line()
print(f'Winner: { winner }')
print_divider_line()
print('')

# Output result to a text file

# Check to see if output directory exists
if not os.path.isdir('../PyPoll/output'):
	os.makedirs('../PyPoll/output')

outputfile = '../PyPoll/output/election_data_analysis.txt'

def write_divider_line():
	textfile.write(f"{'-' * 40}\n")

# Output to text file
with open(outputfile, 'w') as textfile:

	textfile.write("Election Results \n")
	write_divider_line()
	textfile.write(f'Total Votes: { total_votes }\n')
	write_divider_line()
	for key in candidate_votes:
		candidate = key
		votes = candidate_votes[key][0]
		percentage = candidate_votes[key][1]
		textfile.write(f"{ candidate }: {percentage:7.3f}% ({ votes })\n")	
	write_divider_line()
	textfile.write(f'Winner: { winner }\n')
	write_divider_line()




