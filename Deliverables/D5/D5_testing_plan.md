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