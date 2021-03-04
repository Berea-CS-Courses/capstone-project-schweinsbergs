#Components

**Front-end UI**: For the user to input the ingredients, interact with the recipes given, and select a recipe. 

**Webscraper**: This will be what takes all of the information for each recipe. 

**Dataframe**: This will be needed to store the recipes and their information with a sort of "tagging" system. 

**Phone?**: I intend for this to be an app, so it'll have to run with phone software (Android) 

**Back-end Script**: This will need to be run to compare user inputs against the dataframe and fetch recipes. 

#Understanding the Components

**The components will be running and interacting with each other in roughly this order.**
1. Webscraping - This is something I personally do before the user even downloads the app. The webscraper needs to run to populate the dataframe. The information that the webscraper pulls will then be placed into...
2. The dataframe - The dataframe will hold the recipes and the information about them. Yield size, ingredients, instructions... This will all be organized into a data frame that can be parsed with the user's input. The user will need to input using...
3. A phone - The user will download the app, and they will need to open it to interact with it. Upon opening it, they will find... 
4. The Front-End UI - This is what the user will personally interact with to input their ingredients via a sort of text box search bar. After their ingredients are input, they hit go. This is when the background actions happen: 
5. The Back-end Script: This will compare the user's input against what's in the dataframe, particularly the ingredients. A carefully constructed dataframe will be able to filter more user specifications later on. This will calculate a percentage match, which will then be displayed in...
6. Front-End UI Part 2: This is the page that will pop up after everything has been calculated, and will display the recipes for the user. It will display them in a scaling order based on the percentages matched, and display images of the recipe along with the name. The user will be able to click on the recipe and check it out, and back out to the results again if they so choose. 

**What will the components need?**

1. The webscraper I plan on using is located here: https://github.com/hhursev/recipe-scrapers
2. The dataframe I've been researching is the one included within the Pandas package. 
3. I intend on using Android Studio to create an environment to test the app in in place of the phone. 
4. The front end UI I've been looking at TKinter for-- While I don't love how most of the stuff in it comes out, I think it's viable for what I plan. 
5. The back end script will be interacting with the dataframe, so it'll be interacting with the Pandas library, but the base python library should be able to cover it otherwise. 

**What is the overall importance of each component?** 

I've tried to break this project down to the very BASE level components that would allow me to have a functioning application. The 'issue' with this app is that it can have what feels like an unlimited amount of features if you get overly zealous. 
I think the things that are the most important here are the dataframes and the script to compare it against. Without that, I essentially would just have UI that does nothing. That said, UI would be the 'least' important. 

That isn't to say that either of those things aren't important at all, and aren't needed for base-level app function. They definitely are. I just want to focus on gathering information, organizing it, and being able to retrieve it before I focus on the user experience, or any bells and whistles. 

# Bite-Sized Pieces

* **The Webscraper** 

For all intents and purposes, this webscraper is just a tool I'm using. It's, for the most part, already functional. It will be pulling the recipes I need for me, what I will be working with mainly, in the nitty gritty, is the dataframe, script, and UI. 

* **The Dataframe** 

This is extremely important. I believe, after talking to Kaleb, I have the ability to 'link' two dataframes together, which is what I may end up doing to make sure the ingredients are easily indexable and searchable. If I can handle the data from the webscraper in an intuitive way, 
which I believe is the dataframe, I'll be able to store recipe attributes such as the ingredients, the images, the nutrition values, the instructions, which can be fetched later by the script. This is the meat of the application. 

It should be broken down into the different components that this webscraper can pull a recipe by. I view this data set like an excel sheet, so I hope to put each piece of data into its corresponding column. The webscraper can pull by: 

Title 

Total Time 

Yields

Ingredients 

Instructions 

Image

Host

Links

Nutrients 

By creating columns that correspond to each of these properties and successfully linking them together, I'll be able to write a manageable script to compare and pull from. 

* **The Script** 

This script starts very humbly as a user's input. The user will be able to input ingredients such as 'bread, jelly, peanut butter', and the script will hold onto all of those ingredients for when the user is ready to press go and search for the recipes in the database. 

When the go button is pressed, this script will compare against the database what recipes list those things as ingredients. Some advice I was given was that it's better to knock out non-matches rather than collect matches, so that may be a way I organize it. Dataframes are made to be fast, hence their application here with the script. 

While the script is collecting matches, it will be calculating a percentage match. So, for example, if it finds that the recipe "PB and J" from allrecipes.com has a 100% match with 'peanut butter, jelly, bread' for the ingredients, it will pull that recipe and note that it's 100% match. 

If the script pulls "Jelly Toast" from allrecipes.com with matches for "bread, jelly", it will mark that as a 66% match. 

Once it has been satisfied with its search against our dataframe, it will then arrange our recipes by percentage matched. So, for example, it will display the PB and J recipe because it got a 100% match FIRST, and the Jelly Toast match second, because it was only a 66% match. It will contain a way to reference back to the pertinent information of ingredients, instructions, and image. 

* **The Front-End UI** 

This is what the user will see when they want to send in their ingredients to get matched. 

There will be a textbox, along with an autocorrect/suggestion API that is built in, because this needs a catch against typos. If there are typos in an ingredient, there is a nonzero chance it won't get matched with anything at all. That defeats the purpose of the app. 

The user will then be able to press a go button to advance to the next screen. The script will run, so that the UI will be able to display the results of the script on the page. The user will be able to scroll through images that have been pulled by the script and assembled by the UI to create an interactive field. The user will be able to press on the images of the recipes to get more information on a recipe, ingredients and instructions. There will be a button to back out if needed, to look back at old results. 

For the time being, I just want to use Tkinter with this just to create something that is interactive and useable. 

* **Phone** 

To my understanding, you need to pay Apple to be able to use their developer tools and to actually create an app. I also just.. prefer Android, so I'd like to stick to Android and Android Studio to develop this app.

My knowledge of app design is limited to using the MIT app inventor, and I'm hoping to use the phone as something to host this application on. After all, when you see someone in a kitchen nowadays, you see them on their phone. 

I want to be able to put the app I create onto the phone, and I'm hoping I can develop the app and then sort of 'port' it for the Android phone. 

# Prioritization 
**Recipe App**
```
Phone (Android Studio)
|___Display 
|      |
|      |___Front-End UI 
|      |   |
|      |   |___ Tkinter
|      |
|      |___Back-End Script
|          |
|          |___Data Frame
|              |
|              |___ Web Scraper 
|              |
|              |___ Python Pandas
```

I'm not sure if this hierarchy makes sense in developmental terms, but it makes sense in operation terms when I visualize it... 

Developmental wise, the webscraper is already made for me. That's done. As are pandas, and tkinter. I'm not building any of this from the ground up. 

1. Data Frame - I want to focus on the data frame first, which will be populated by the web scraper. After all, there's nothing to do with a script or an interface if there's nothing to interact with! This is the most important first step. 

2. Back-End Script - This is what will actually do things *with* the data, pulling the needed calculations. It needs to be developed after the data frame so it has something to interact with, but it's important to have this script before the UI so that we can actually do something with the information we pull. 

3. UI - Once we have all of our data sorted and able to be pulled from as needed, we can create something so the user can interact with it from their end with ease! 

4. Phone Environment - Once all of this is handled, I want to focus on letting it be a useable Android app. 