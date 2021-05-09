# Election Analysis

## Overview of Election Audit
### Purpose
The purpose of this analysis is to use Python to analyze a given data set to determine the outcomes of a recent local congressional election in Colarado.  Using the data set found in elections_results.csv we will determine the number of total votes cast, the candidates who recieved votes, the total amount of votes per candiate, the total amount of votes cast per county, the county with the highest voter turnout, and the overall winner.

## Election-Audit Results
### Summary
369,711 total votes were cast in the election. Below we will analyze the distribution of votes by county and by candidate.

### Votes per County

Votes for the election were cast in 3 counties in Colarado: Jefferson, Denver, and Arapahoe. These votes were disributed by county as follows:

- 38,855 votes were cast in Jefferson county
- 306,055 votes were cast in Denver county
- 24,801 votes were cast in Arapahoe county

From the above we can see that Denver had the highest voter turnout with 82.8% of the votes being cast there. Jefferson county is to follow, making up 10.5% of the voter turnout. And lastly Arapahoe county, with 6.7% of the total votes occouring there.

### Votes per Candidate

A total of 3 candidates - Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane, recieved votes in the election. The votes were distributed as follows: 

- 85,213 votes were cast for Charles Casper Stockham
- 272,892 votes were cast for Diana DeGette
- 11,606 votes were cast for Raymon Anthony Doane

From the above we can see that Diana DeGette had the most number of votes - winning 73.8% of the votes. Charles Casper Stockham follows with 23% of the votes, and lastly Raymon Anthony Doane with 3.1% of the votes.

We can conclude that with 73.38% of the votes, the winner of the election is Diana DeGette - with a total of 272,892 votes being cast for her.


## Election-Audit Summary

The script used to analyze the data set is not unique to the Colarado congressional election. This script can be used to analyze a data set for any election with just a few modifications.

***1.) Changing the path and file names***

In order to make sure the script is accessing the correct information for our analysis, minor adjustments need to be made where we are declaring which file to analyze:         
```
file_to_load = os.path.join("Resources", "election_results.csv")
```
and which file to save our results to:
```
file_to_save = os.path.join("analysis", "election_results.txt")
```

The names inside the brackets will need to be modified to the files being used for the analysis, as well as the path to the files. This will ensure that our code is able to access the correct data set and output the results in the correct location. 

***2.) Delcaring what data to read in the data set***

  In our data set the names of the counties and the names of the candidates were columns 2 and 3 respectivley:
  *insert pic*

  This was noted in our code as such:
  ```
  county_name = row[1]
  ```
  ```
  candidate_name = row[2]
  ```
  Note that columns are addressed as 1 and 2 as indexing starts at the number 0. Slight modification will need to be made in the code to suit the layout of the data set being    used in the analysis.
