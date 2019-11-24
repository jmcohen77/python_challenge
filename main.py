#To Do Homework
#Import Modules/Dependencies
import os
import csv

#Variables:
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


#Set Path for FIle:
csvpath = os.path.join(".", "PyPoll", "Resources", "election_data.csv")

#Open & Read CSV File:
with open(csvpath, newline='') as csvfile:

    #CSV Reader Specifies Dlimiter & Variable to hold data:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read Header ROw First:
    csv_header = next(csvfile)

    #Read Each Row of Data After Header:
    for row in csvreader:

        #Calculate Total Number of Votes:
        total_votes += 1

        #Calculate TOtal Number of Votes for each Candidate:
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
    
    
    #Calculate Percentage of votes each candidate received:
    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

    #Calculate Who REceived Most Votes:
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

#Print Analysis:
print(f"Election Results")
print(f"------------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------------")
print(f"Khan: {khan_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {Li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"------------------------------")
print(f"Winner: {winner_name}")
print(f"------------------------------")

#Specify FIle to Write To:
output_file = os.path.join(".", "PyPoll", "Resources", "election_data_revised.text")


#Open File Using "Write" Mode:
with open(output_file, 'w',) as txtfile:

    #Write New Data:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"------------------------------\n")
    txtfile.write(f"Khan: {khan_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {Li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"------------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"------------------------------\n")
