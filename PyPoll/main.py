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
	print("Duplicate Voter ID in the data, please cleanup the data first")
	exit()

# Get the list of candidates who received votes
candidates_received_votes = set(candidates)

# GCalculate how many votes each candidate received, 
# Generate a list to track votes for each candidate
# Generate a Dictionary to track votes and candidate pair with votes as key
for candidate in candidates_received_votes:
	votes = candidates.count(candidate)
	votes_per_candidate.append(votes)
	votes_candidate[votes] = candidate
	
# Sort the votes list generated above in decending order	
votes_per_candidate = sorted(votes_per_candidate, reverse=True)

# Generate a Dictionary to track votes and candidate pair with candidate as key, it is sorted by votes
for votes in votes_per_candidate:
	candidate = votes_candidate[votes]
	candidate_votes[candidate] = votes

# Through sorted candidate/votes dictionary, find the winner's name	
winner = list(candidate_votes.keys())[0]

# function for priting format
def percentage(votes, total_votes):
	return (votes / total_votes) * 100

# Print result on screen
print('')
print('Election Result')
print('-' * 40)
print(f'Total Votes: { total_votes }')
print('-' * 40)
for key in candidate_votes:
	print(f'{ key }: { percentage(candidate_votes[key], total_votes) }% ({ candidate_votes[key] }) ')
print('-' * 40)
print(f'Winner: { winner }')
print('-' * 40)
print('')

# Output result to a text file

# Check to see if output directory exists
if not os.path.isdir('../PyPoll/output'):
	os.makedirs('../PyPoll/output')

outputfile = '../PyPoll/output/election_data_analysis.txt'

with open(outputfile, 'w') as textfile:

	textfile.write('Election Results \n')
	textfile.write("-" * 40)
	textfile.write('\n')
	textfile.write(f'Total Votes: { total_votes }\n')
	textfile.write("-" * 40)
	textfile.write('\n')
	for key in candidate_votes:
		textfile.write(f'{ key }: { percentage(candidate_votes[key], total_votes) }% ({ candidate_votes[key] }) ')
		textfile.write('\n')
	textfile.write("-" * 40)
	textfile.write('\n')
	textfile.write(f'Winner: { winner }\n')
	textfile.write("-" * 40)
	textfile.write('\n')




