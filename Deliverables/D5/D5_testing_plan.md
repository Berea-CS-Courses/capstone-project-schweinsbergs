# Testing Plan and Documentation 

###**What tests do you plan to conduct, and how will they be useful?**

I am doing a cognitive walkthrough test and an end to end test. The cognitive walkthrough is important 
to my system because ultimately, this is a system for a user. This is something that, with refining, 
could be a product, or an app, so it's important to have human-centric design that can be tweaked and tested
upon. 

The end to end test is important for the same reason as the cognitive walkthrough. This has many parts and pieces, 
which made the walkthrough more sensible and time-effective to me vs. user testing, plus I've been
doing end to end testing throughout my entire programming. I wanted to stress test it in different situations 
that it would come across when a user interacts with it. 

###**Testing Objectives**

The goals of my tests are to make sure that this is a functional program that a user can navigate. So, 
in my testing, I try to see if the system will break under stress, under unexpected conditions, and I try
to make sure that the user is capable of using it with little stress. 

For my **cognitive walkthrough** tests I want a user to pretend they were going to cook. 

* Had the user input ingredients 
* Had the user navigate the top match in the dataframe 
* Had the user navigate literally any other match in the dataframe 

For my **end to end** testing, I want to test the following systems: 

* Create an xml sitemap spreadsheet with urls populating each row of the A column. 
* Have my webscraper read from each of those cells. 
* Convert that scraped information into a dataframe. 
* Save the dataframe. 
* Open the dataframe. 
* Accept user input for ingredients. 
* Compare user input versus the ingredients column of the dataframe. 
* Calculate a percentage matched against the user's input. 
* Sort and display the dataframe based on that percentage. 


-------------------------

#Cognitive Walkthrough

###**Goals**
1. User is able to successfully input data via a text window that pops up on screen. 
2. User is able to successfully bring up the dataframe window. 
3. User is able to correctly identify the top match displayed to them. 
4. User is able to navigate and identify any other match given to them. 

###**Happy Path** 
The dialogue box to enter ingredients pops up. The user inputs ingredients, separated by a space as the
dialogue box requests, hits OK, and the dataframe pops up. The user can notice that the first item 
is the best match, and that the descending order is each lesser match from there. 

###**Ideal Users** 

An ideal user for this program fulfill the following: 
* Can cook 
* Most likely 16-55 
* Are at least somewhat computer literate 
* Can read and write English 
* Any gender

###**The Walkthrough** 

I selected three potential users of this app of varying ages, gender, cooking level, and a moderately 
similar level of computer literacy. 

Worksheets are located within the D5 folder. 

###**Cognitive Walkthrough Notes** 

* User 1 does not like the column name 'percent' and should be changed to 'percentage matched', it should
be moved to all the way on the left.
  
  
* User 1 did not like not being able to see their input. 


* User 1 wants to be able to see what ingredients are matched. 


* User 1 did not struggle at all with the program and immediately understood it well enough to try and 
break it. User was a good stress test. Displayed no problems with navigating the system and did so with 
  ease.
  
  
* User 1 tried funny input to test the program.

  
* User 2 had a recipe already in mind when they searched, and were disappointed to not find it due
to vegan restrictions. 
  

* User 2 had no difficulty in navigating the system. 


* User 3 used system totally as intended. 


* User 3 did not stray off the path when testing, but they were intimidated by the sheer amount of 
stuff that was thrown at them on screen when the dataframe popped up. 
  

###**Cognitive Walkthrough Problems** 

I want this program to be more user friendly, so based on feedback, I've identified problems I would 
like to solve. 

* Add the matches onto the dataframe as a column. 
* Add options that aren't vegan onto the dataframe 
* Add the URL of the website onto the dataframe so that the user may navigate there as a catch-all.

The first issue of matches is not a trivial issue. It's actually a little complicated, because I have
the matches set up on a true-false system. I hope to toss the trues matches into a list of strings
and display like like everything else. 

To add options that aren't vegan into the dataframe, I just need to scrape a different recipe site. 

To add the URL of the website, I at first thought that I would need to just use the built-in link 
option on my webscraper. It turns out this pulls some sort of HTML garbage, so I ended up attaching the 
url that the datascraper reads from the excel sheet. 

###**Cognitive Walkthrough Reflection** 

From these tests, I learned that my program was a little more robust than I thought it was. Between 
User 1 trying to intentionally break my program by any means possible, and none of the users seeming to 
deviate from the path, I was surprised that it seemed... pretty solid for a baseline. I thought that someone 
would navigate off the happy path and mess with the PandasGUI, but it seemed like no one wanted to mess with
things that they didn't know about. 

Hopefully these tests help my design be more user-friendly for people to navigate. I'm particularly 
pleased with getting rid of the vegan options for now, because they were a little strange. 

------------------------------------
#End to End Testing

###**Testing Requirements** 

The back end: 

The xml scraper has to pull urls and put them into an excel sheet. 

The excel sheet has to be successfully read by my recipe scraper and save that data into a dataframe.

The dataframe must be able to be saved. 

The dataframe must be able to be opened. 

The user end: 

The program must be able to accept user input. 

The program must be able to compare that user input against the open dataframe. 

The program must be able to calculate a percentage matched. 

The program must be able to display these matches. 

All of these things have to happen as a step by step process, and if one thing malfunctions, the entire
program can't really function. It won't scrape the internet every time it runs, but it must be able to 
get to the point where the dataframe is able to be saved. 

###**Testing Scraping** 

Scenarios: I wanted to scrape websites that aren't vegan, because the user is going to want options that 
are not vegan. 

Results: 
Upon scraping different websites, I encountered 2 errors. One of which was a NoneType, which would cause
the program to stop scraping and then render the rest of the process like saving, and then everything that
occurs after saving, unable to work. High priority, and I'll keep scraping websites to find a correlation.
Sometimes if the scraper is missing some information from a website, it'll just stop, so I imagine that's what's
happening. 

The other error I encountered was a little trickier than the previous. My program will only scrape around
350 recipes successfully, and then it'll just quit. Not error out, it'll give me an exit code and pretty 
much say 'I'm done'. I've done some research on this exit: -1073741571 (0xC00000FD), which apparently just...
can be anything from memory issues, to my version of python and pycharm... I've listed this one as low
priority, because it's bizarre and time consuming. I have enough recipes to successfully test and share 
with, so I'm going to focus on those. 

###**Testing User Input** 

Scenario: I wanted to pretend that I was a user in multiple different mindsets. One was to use the 
product as it was intended. I would enter reasonable ingredients, such as 'sugar', 'water', 'milk', and I would 
get reasonable outputs. 

The problems arose when I stress tested the system and wanted to cause as much chaos as possible, because 
the user can input anything they want. Ezra helped me with this in the user testing, because Ezra 
really likes to break things. 

Division by 0 error: If there are no matches or input, the system is forced to divide by 0 and it just
won't run. This is high priority, the program needs to run. (Entering nothing) I'll create a case for if it catches a 0. 

Over 100% matches: If the user puts in something that would match multiple times in one instance of 
the recipe list, it'll certainly do that. You're able to get matches over 100% in the dataframe. Unfortunately, 
this isn't all that useful to the user. This is mid-priority-- While it needs fixed, it's still functional. (Entering
something like 'cup cup 1 cup 1111 7 the number seven') Depending on whether this ends up being trivial or not, I'll 
check the user's data against stopwords. Otherwise, I'll add a quick fix where I can just display '100%'

Too many matches results in an error: This started happening after implementing the matches column. If there
are too many matches, the program will not run. Unfortunately, I don't believe I have enough time to 
actually fix this one, though it would be high-priority if I did. For now, the soft-fix is going to be 
to not display the matches column just to make sure it works. (Caused by inputting something like 'cup tablespoon
1 2 3 4 cup tablespoon teaspoon table spoon') I might try to do a shallow copy, but this would need to be fixed by 
refactoring code, which may be impossible right now. 

Previous bugs, found during informal end-to-end testing, that have since been fixed: 

Adding the web crawler/excel sheet xml: When I was working with my scraper, I realized that the 
scraper couldn't actually do webcrawling. This was fixed by utilizing sitemaps. 

Reading user data and comparing: I found if I didn't have exact, perfect word for word matches with the 
dataframe and user ingredients, there would be no match. This made the system just unusable unless 
you knew the recipe you were looking for, word for word. This was fixed by splitting words apart 
in the list of strings for both the user ingredients and the recipe's ingredients. 


