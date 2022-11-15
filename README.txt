The purpose of these bots are to support hiring efforts by providing convenient access to a large number of possible leads that Pamela, Cilinda, or Thu can follow up on.

--Clearance Jobs Bot--
This bot scrapes Clearance Jobs (similar to LinkedIn but for people with security clearance/ for government contracts) to gather profile information like name, email,
and phone number. Pamela will supply a search query that you can assign to the "query" variable. Next, there are two types of searches - Intellisearch and Boolean searches.
Double check to make sure that the Boolean for the different searches is assigned to the "search_type" variable. When the bot runs to the search page, some time is allotted
so that you can input additional filters. After, let the bot run and make sure to close the excel sheet that the script is writing into (will throw permission error if left 
open). When the bot is finished running, open the excel sheet, inspect it to make sure the bot ran correctly and grabbed all of the data, then email it to Pamela and cc 
Cilinda.

*Usually when there is an error/when data is missing, you can remedy it by looking at the CJ page and inputting the correct Xpath, class, or name of the element we want.


--Sharepoint Bot--
This bot scrapes Sharepoint to get information like name, email, and phone number from the resumes that are stored in the database. 


11/11/22 update for Joey and Sam:
We are attempting to put all the information into a new natural language processor like google to see if we can improve efficiency and you may have to go through the 
prior lines to understand how it works and lookup any code that you may not entirely know how it works. Lines 101-108 is where you need to expand and improve upon
the code that I have added. 

Implement adding into website for each resume information and extracting into excel as much as you can. 



-if we can get the google api to work, it may have better results than spacy