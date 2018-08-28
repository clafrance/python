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
candidate_votes = {}

def percentage(votes, total_votes):
	return (votes / total_votes) * 100

# votes_candidate = {}

# candidate_votes = {}
# highest_percentage = 0
# winner = ""


csvpath = os.path.join('../PyPoll', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	next(csvreader)

	for row in csvreader:
		voters.append(row[0])
		counties.append(row[1])
		candidates.append(row[2])

total_votes = len(set(voters))

candidates_received_votes = set(candidates)

votes_per_candidate_temp = []
votes_candidate = {}

for candidate in candidates_received_votes:
	votes = candidates.count(candidate)
	votes_per_candidate_temp.append(votes)
	votes_candidate[votes] = candidate
	
votes_per_candidate = sorted(votes_per_candidate_temp, reverse=True)

for votes in votes_per_candidate:
	candidate = votes_candidate[votes]
	candidate_votes[candidate] = votes

winner = list(candidate_votes.keys())[0]

print('')
print('Election Result')
print('-' * 40)
print(f'Total Votes: { total_votes }')
print('-' * 40)
print(f'{ candidate_votes }')
for key in candidate_votes:
	print(f'{ key }: { percentage(candidate_votes[key], total_votes) }% ({ candidate_votes[key] }) ')
print('-' * 40)
print(f'Winner: { winner }')
print('-' * 40)
print('')
# print(f'{ votes_per_candidate }')
# print(candidate_votes)
# print(f'{ candidate_votes }')
# print(f'{ winner }')


# if len(total_votes) == len(votes):
# 	print("yes")
# else:
# 	print("Duplicate Voter ID in the data, please cleanup the data first")

# print(total_votes)
# print(len(counties))
# print(len(candidates))
# print(len(candidates_who_received_votes_set))
# print(candidates_who_received_votes_set)
# print(candidate_votes)
