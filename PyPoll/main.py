# -- The total number of votes cast
# -- A complete list of candidates who received votes
# -- The total number of votes each candidate won
# -- The percentage of votes each candidate won
# -- The winner of the election based on popular vote.
# -- print the analysis to the terminal and export a text file with the results.


import os
import csv
import sys


def read_csv(file_path, file_name):
    csvpath = os.path.join(file_path, file_name)

    voters = []
    counties = []
    candidates = []

    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)

        for row in csvreader:
            voters.append(row[0])
            counties.append(row[1])
            candidates.append(row[2])

    return {"voters": voters, "counties": counties, "candidates": candidates}


def invalid_votes(voters):
    return len(voters) != len(set(voters))


def analyze_candidates_votes(candidates):
    """     """
    candidates_list = set(candidates)
    total_votes = len(candidates)

    candidate_votes_dict = {}

    for candidate in candidates_list:
        candidate_votes_dict[candidate] = 0

    for candidate in candidates:
        candidate_votes_dict[candidate] += 1 

    candidates_list = list(candidate_votes_dict.keys())
    candidate_votes = list(candidate_votes_dict.values())
    candidate_vote_percentage = [round((vote / total_votes) * 100, 1) for vote in candidate_votes]
    winner = candidates_list[candidate_votes.index(max(candidate_votes))]
    return {"total_votes": total_votes, 
            "candidates": candidates_list, 
            "votes": candidate_votes, 
            "votes_percentages": candidate_vote_percentage, 
            "winner": winner}


def main():
    file_path = "Resources"
    file_name = 'election_data.csv'
    
    try:
        voting_data = read_csv(file_path, file_name)
    except Exception as e:
        print("Reading csv file failed")
        sys.exit(1)
        
    voters = voting_data["voters"]
    
    if invalid_votes(voters):  
        print("Exit. There are duplicate data in voterID column")
        sys.exit()
  
    candidates = voting_data["candidates"]
    voting_data_analysis = analyze_candidates_votes(candidates)

    total_votes = voting_data_analysis["total_votes"]
    candidates = voting_data_analysis["candidates"]
    votes = voting_data_analysis["votes"]
    votes_percentages = voting_data_analysis["votes_percentages"]
    winner = voting_data_analysis["winner"]

    max_len = len(max(candidates, key=len))
    print('\nElection Results\n')
    print(f"{'-' * 30}")
    print(f'Total Votes: { total_votes }')
    print(f"{'-' * 30}")
    for i in range(len(candidates)):
        white_space = max_len - len(candidates[i])
        print(f"{ candidates[i] }:{' '* white_space} {votes_percentages[i]: 7.3f}% ({ votes[i] })")
    print(f"{'-' * 30}")
    print(f'Winner: { winner }')
    print(f"{'-' * 30}\n")
    
    if not os.path.isdir('output'):
        os.makedirs('output')

    outputfile = 'output/election_data_analysis.txt'
    with open(outputfile, 'w') as textfile:
        textfile.write("\nElection Results \n\n")
        textfile.write(f"{'-' * 30}\n")
        textfile.write(f'Total Votes: { total_votes }\n')
        textfile.write(f"{'-' * 30}\n")
        for i in range(len(candidates)):
            white_space = max_len - len(candidates[i])
            textfile.write(f"{ candidates[i] }:{' '* white_space} {votes_percentages[i]: 7.3f}% ({ votes[i] })\n")
        textfile.write(f"{'-' * 30}\n")
        textfile.write(f'Winner: { winner }\n')
        textfile.write(f"{'-' * 30}\n")

main()






