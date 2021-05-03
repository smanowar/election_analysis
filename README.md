# Election Analysis

## Overview of Project

### Purpose

The primary purpose of this analysis is to observe the annual volume traded and the annual return of 12 different stocks, comparing their outcomes between 2017 and 2018.
This was accomplished using 2 macros on VBA – the original macro and a macro which was refactored. Below we will compare and contrast the ability of the 2 different macros to analyze our data.

## Analysis and Results

From the photos below we can see that our stocks took a hit in 2018. 10 of our 12 stocks being observed had a negative annual return (shown in red) in comparison to 2017, where only 1 of our 12 stocks had a negative return.
(insert pic)
We observed this result in 2 ways – through our original macro and through our refactored macro. Below we will see the differences between the 2 macros and their effect on the length of time needed to perform the task.
The data sheet in question consisted of 3013 rows of data for both 2017 and 2018. For our analysis we wanted to satisfy 3 things: firstly, to display the total daily volume for the respective ticker for the year in question, secondly to display the annual return for the ticker in question, and lastly to display the ticker in question.
Therefore, the we formatted the original macro in the following steps:
1.	work through the rows to determine the total daily volume for the respective ticker
Then
2.	work through all of the rows to obtain the starting price for the respective ticker 
Then
3.	work through all of the rows to obtain the closing price for the respective ticker
This method yielded the following times:

(instert pic) (insert pic)

As we can see we have a result of ___ and ___ respectively for the years 2017 and 2018 using our original macro.
The intuition behind our refactored code is to work through the same pathway as our original code, however instead of looping through our rows multiple times to get values for our variables, we looped through the rows once to obtain values for each of the tickerVolume, tickerStartingPrice and tickerEndingPrice, indexing them as a function of a new variable – tickerIndex. Our tickerIndex variable has a range of only 0 to 11 (one value for each stock in our analysis) versus the range in our original macro being all the rows.
(insert pic)

This allowed us to reduce our calculation time by a relatively large amount as seen below:
(insert pic)

Using our refactored macro saved us ___ seconds in our 2017 analysis and __ seconds in our 2018 analysis.

## Summary

***What are the advantages or disadvantages of refactoring code?***

A huge advantage of refactoring code is that it allows the task to be accomplished at a much faster speed - improving efficiency for large amounts of data. Another advantage is that it condenses the original code – makes everything more concise. This allows less chance for error as things may get lost in a long repetitive code.
A disadvantage is that for a longer code it can be time consuming to work through the refactor the code.

***How do these pros and cons apply to refactoring the original VBA script?***

Our refactored code allowed us to cut down on the time needed for the macro to output the results, it cut the time down by 0.7 seconds. This may seem like a small time difference, however we are running this macro for only 12 different stocks - if the macro had to run for a few hundred different stocks, that saved time could add up. With that being said, we wouldn’t know how long it would actually take for the macro to run through a larger data set. If there wasn’t a significant time difference for larger amounts of data the time being used to refactor the already efficient code could be used elsewhere.
