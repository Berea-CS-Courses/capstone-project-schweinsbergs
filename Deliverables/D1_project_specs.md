# Deliverable 1 - Project Specifications

Name: Sam Schweinsberg

## Overview to summarize project 
Have you ever found yourself needing to make dinner, but find yourself at a loss as to what to make? 
This handy little dinner picker is the perfect solution for you. Input what ingredients you have into this android app, and it 
spits out potential recipes for you to use! No more wondering and scrolling Google as you desperately find ways to obtain nourishment! 
## Create a Concept section to detail your project idea.

At its base point, I want this project to be able to take user input and search for matches among lists of ingredients for recipes, 
and display those matches based on a scaling match percentage. 

I want to intially keep this project simple, because it is INCREDIBLY easy to get lost in all of the features that can be added to it. 

So the following is the base design, and if I end up going 'this is just TOO easy', I'll add more. 

* You'll be able to input ingredients that you have/want to work with into an android app. The intial input will not be saved, though that may be a feature 
added down the road. If implemented, you'll be able to cross off or remove ingredients you've inputted and stored as you use them. 


* This project will show recipe results as a list, with the highest matches towards the top, and the lowest towards the bottom. This will be by calculating percentage of ingredients matched versus input. An 
upgrade to this feature would be to filter results. 


* ~~I'd like for this project to contain substitutes as well. If you don't have milk but have almond milk, it might be tagged as a substitue 
ingredient.~~ I'm not currently interested in adding this feature as a core element. 


## Create a Requirements section with preliminary specifications.

* ~~Software must have some sort of input for the users to put their ingredients in.~~

* Software will be able to take in a text input from the user of their ingredients.

* Software must utilize recipe web-scrapers to find recipes. Webscraper is located: https://github.com/hhursev/recipe-scrapers

* Webscraper must be fed recipes through some sort of text file-- It will not feed itself recipes. 

* ~~Software must somehow sort and store recipe ingredients and the recipe itself.~~ 

* Webscraper will place data into a dataframe, and it will be "pickled" into a .pkl file for reading in the future. 

* Software must be able to compare the user-inputted ingredients against the stored ~~recipe list~~ .pkl file. 

* Software must be able to calculate percentage matches. 

* Software must be able to display matches to the user on a scale of the percentage match.  

* Software will be hosted on an Android app. 






