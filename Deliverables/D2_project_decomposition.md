# Components

**Front-end UI**: For the user to input the ingredients, interact with the recipes given, and select a recipe. Usage of Kivy. 

**Webscraper**: This will be what takes all of the information for each recipe. 

**Dataframe**: This will be needed to store the recipes and their information with a sort of "tagging" system. 

**.pkl file**: This will store the data that was created by the dataframe that can be read from later. 

**Phone**: I intend for this to be an Android app, so it'll have to run with the software. 

**Back-end Script**: This will need to be run to compare user inputs against the dataframe and fetch recipes. 

# Understanding the Components

**The components will be running and interacting with each other in roughly this order.**
1. Webscraping - This is something I personally do before the user even downloads the app. The webscraper needs to run to populate the dataframe. The information that the webscraper pulls will then be placed into...
2. The dataframe - The dataframe will hold the recipes and the information about them. Yield size, ingredients, instructions... This will all be organized into a data frame that can be parsed with the user's input. 
3. .pkl file - This will be created after the webscraper collects data on the recipes. Once the dataframe is created, it needs to be "pickled", which ensures that my dataframe isn't just lost to the void. 

~~3. A phone - The user will download the app, and they will need to open it to interact with it. Upon opening it, they will find...~~
4. The Front-End UI - This is what the user will personally interact with to input their ingredients via a sort of text box search bar. After their ingredients are input, they hit go. This is when the background actions happen: 
5. The Back-end Script: This will compare the user's input against what's in the ~~dataframe~~ .pkl file, particularly the ingredients. A carefully constructed dataframe will be able to filter more user specifications later on. This will calculate a percentage match, which will then be displayed in...
6. Front-End UI Part 2: This is the page that will pop up after everything has been calculated, and will display the recipes for the user. It will display them in a scaling order based on the percentages matched, and display images of the recipe along with the name. The user will be able to click on the recipe and check it out, and back out to the results again if they so choose. 

**What will the components need?**

1. The webscraper I plan on using is located here: https://github.com/hhursev/recipe-scrapers
2. The dataframe I've been researching is the one included within the Pandas package. .pkl is also part of the Pandas package. 
3. I intend on using Android Studio to create an environment to test the app in in place of the phone. 
4. The front end UI I've been looking at ~~TKinter for-- While I don't love how most of the stuff in it comes out, I think it's viable for what I plan.~~ Tkinter doesn't work on Android! What an oversight. I want to use kivy, which will work on Android. 
5. The back end script will be interacting with the dataframe, so it'll be interacting with the Pandas library, but the base python library should be able to cover it otherwise. 

**What is the overall importance of each component?** 

I've tried to break this project down to the very BASE level components that would allow me to have a functioning application. The 'issue' with this app is that it can have what feels like an unlimited amount of features if you get overly zealous. 
I think the things that are the most important here are the dataframes and the script to compare it against. Without that, I essentially would just have UI that does nothing. That said, UI would be the 'least' important. 

That isn't to say that either of those things aren't important at all, and aren't needed for base-level app function. They definitely are. I just want to focus on gathering information, organizing it, and being able to retrieve it before I focus on the user experience, or any bells and whistles. 

# Bite-Sized Pieces

* **The Webscraper** 

For all intents and purposes, this webscraper is just a tool I'm using. It's, for the most part, already functional. It will be pulling the recipes I need for me, what I will be working with mainly, in the nitty gritty, is the dataframe, script, and UI. 

It will need to be fed URLs, because it cannot collect them on its own. 

* **The Dataframe & Saving the Dataframe** 

This is extremely important. I believe, after talking to Kaleb, I have the ability to 'link' two dataframes together, which is what I may end up doing to make sure the ingredients are easily indexable and searchable. If I can handle the data from the webscraper in an intuitive way, 
which I believe is the dataframe, I'll be able to store recipe attributes such as the ingredients, the images, the nutrition values, the instructions, which can be fetched later by the script. This is the meat of the application. 

It should be broken down into the different components that this webscraper can pull a recipe by. I view this data set like an excel sheet, so I hope to put each piece of data into its corresponding column. The webscraper can pull by: 

Title - String 

Total Time - Int

Yields - String

Ingredients - List 

Instructions - String 

Image - String 

Host - String

Links - List

Nutrients  - Dict

By creating columns that correspond to each of these properties and successfully linking them together, I'll be able to write a manageable script to compare and pull from. 

Once the dataframe is taken care of, I'll be able to take the dataframe and put it into a storage file. This is the .pkl, and I'll be able to access and read from it later so that data is static and can be saved as a file onto the app. 

* **The Script** 

This script starts very humbly as a user's input. The user will be able to input ingredients such as 'bread, jelly, peanut butter', and the script will hold onto all of those ingredients for when the user is ready to press go and search for the recipes in the database. Currently, this is as a list, because the Webscraper stores items in the dataframe as a list natively. 

When the go button is pressed, this script will compare against the ~~database~~ .pkl file, in the ingredient column (a list), what recipes list those things as ingredients. Some advice I was given was that it's better to knock out non-matches rather than collect matches, so that may be a way I organize it. Dataframes are made to be fast, hence their application here with the script. 

While the script is collecting matches, it will be calculating a percentage match. So, for example, if it finds that the recipe "PB and J" from allrecipes.com has a 100% match with 'peanut butter, jelly, bread' for the ingredients, it will pull that recipe and note that it's 100% match. 

If the script pulls "Jelly Toast" from allrecipes.com with matches for "bread, jelly", it will mark that as a 66% match. 

Once it has been satisfied with its search against our dataframe, it will then arrange our recipes by percentage matched. So, for example, it will display the PB and J recipe because it got a 100% match FIRST, and the Jelly Toast match second, because it was only a 66% match. It will contain a way to reference back to the pertinent information of ingredients, instructions, and image. 

* **The Front-End UI** 

This is what the user will see when they want to send in their ingredients to get matched. 

There will be a textbox, along with an autocorrect/suggestion API that is built in, because this needs a catch against typos. If there are typos in an ingredient, there is a nonzero chance it won't get matched with anything at all. That defeats the purpose of the app. 

The user will then be able to press a go button to advance to the next screen. The script will run, so that the UI will be able to display the results of the script on the page. The user will be able to scroll through images that have been pulled by the script and assembled by the UI to create an interactive field. The user will be able to press on the images of the recipes to get more information on a recipe, ingredients and instructions. There will be a button to back out if needed, to look back at old results. 

For the time being, I just want to use Tkinter with this just to create something that is interactive and useable. 

~~* **Phone**~~ 

~~To my understanding, you need to pay Apple to be able to use their developer tools and to actually create an app. I also just.. prefer Android, so I'd like to stick to Android and Android Studio to develop this app.~~

~~My knowledge of app design is limited to using the MIT app inventor, and I'm hoping to use the phone as something to host this application on. After all, when you see someone in a kitchen nowadays, you see them on their phone.~~ 

~~I want to be able to put the app I create onto the phone, and I'm hoping I can develop the app and then sort of 'port' it for the Android phone.~~ 

# Prioritization 
**Recipe App**

*Part 1:* text file of URLS -> web scraper reads urls -> webscraper puts recipe information into a dataframe -> data frame is stored into .pkl file

*Part 2:* user inputs their ingredients -> .pkl file is read -> user ingredients list is compared against the recipe column in the data frame -> percentage match is calculated -> matches are displayed on screen for user -> user can navigate between matches via UI. 

Basically, the meat of this is in part 1 and up to the percentages matched in part 2. The UI will be important for creating a "marketable" and usable app, but I can adapt that as needed as long as I have a working product. 

The first thing that I want to focus on is for the webscraper to put information into the dataframe, save it, and read from it. I won't be able to play with that data with the script and run 
comparisons on user lists until I have that done. 

Once that's done, I want to write the script that will compare the user data to the recipe data. 

Then, I can write the part of it that calculates the percentage match. 

Once I'm sure that's working, I'll populate the dataframe with URLs for the webscraper to scrape. 

Then, the dataframe and pkl that contains it will be done. I can then start focusing on the UI that will display all of this information. 
