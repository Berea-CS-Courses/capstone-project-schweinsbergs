# Proof of Concept 

# Concept Documentation 

**What external software or tools are needed to run proof of concept?**

Currently my project is utilizing the pandas library, and a recipe webscraper library. 

Otherwise, it's just a script to read a pickle fiel. 

**What steps need to be taken to run proof of concept?**

It just needs to be run once to save the dataframe, and then to actually open it. 

**What is the current functionality of the proof of concept?**

Pulls a recipe from a recipe website, stores some information from it into a dataframe. That dataframe
is then saved into a pickle, and then opened from and read. 

**Are there any components of the code or systems you have submitted that you did not create?**

The webscraper:
https://github.com/hhursev/recipe-scrapers


# Updates

### D1

__Feedback__ : "Define the non-technical requirements like where you will host your application."


* Added a few minor details that specified that this would be an Android app. 

* Removed the section about adding substitute ingredients. I'm not really interested in that at this point in development.

* Added specifications to the requirements of the app, making them much more narrow. Ex: "must somehow store data" turns into "must be placed in data frame and turned into .pkl file." 
The goal here was to address the feedback given above. 


### D2 

__Feedback__ : "Once you have your prototype mocked up, that can help you clarify if you want this to be native Android, cross-platform, or a responsive web-app." 

"Will there be spell check or autocorrect if users are typing in ingredients?" - already addressed in document 

"Make flow of data a little more obvious."

"Break down components into a step-by-step procedure of how you plan to implement each one. What type of data will you be receiving?"

"What are the plans for UI? What will the components need?"

In class: "Try and think of the webscraping and what's done with the information as two separate entities."

* Specified this to be an Android app, though not a native one. 

* Specified the use of Kivy instead of tkinter. 

* Added in the fact that I'll need to "pickle" the dataframe so I can read from it later in multiple sections. 

* Removed the phone section. Unnecessary. 

* Added some information on how the webscraper will interact with the dataframe in the script, and how that will look on the backend. 

* Totally removed the image that I had to try to show the prioritization. That was clunky and confusing. 

* Added a dataflow that addresses the in-class recommendation that I got from Dr. Jones to view the app and webscraper as two different entities. 

* Removed and reworked the prioritization section. It's much more detailed and has a better understanding of what I'm doing. 


### D3 

__Feedback__ : 

"Your recipe entity could include a 'black-listed' boolean as a property along with its list of ingredients, etc."

"The data flow diagram could use some distinction to what types of data are being transferred from process to process."

"I would put a little more work into the flowchart to create more of an understanding the full concept of your app."

* Updated the data flow chart to try to make it a little more comprehensive and understandable.

* Made a note about the boolean for disliked ingredients. 

# Proof of Concept

<img src="https://i.imgur.com/7Y6tpJk.jpg"/>

This is none too exciting, but it was pretty exciting to me. This is the result of a webscraping that was 
put into a dataframe. The dataframe was then pickled for storage, and this little screenshot is the 
result of reading that stored information. :D 

# Reflection 

**How confident do you feel about your project now that you have created a working proof of concept?**

I actually feel pretty confident about my project now. Though I haven't worked with MOST of the systems in 
place for it, I'm finding it's not actually as hard as I anticipated. 

**Have you faced any significant challenges in the creation of your project so far?** 

Mostly just trying to research, finding what can and can't work for what I'm envisioning. 

**What do you need from instructors/TA to better help you?** 

I don't think I necessarily am in need of anything right now as it stands. Everything, so far, has been straightforward, 
but that could change when I implement other things like the UI... 

