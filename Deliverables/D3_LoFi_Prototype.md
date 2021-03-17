# "Paper" Prototype

My paper prototype was made digitally. I found that it was easier to make it digitally, so I just went ahead and did it that way.

<img src="https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-schweinsbergs/D3/Deliverables/prototype%20pictures/1%20opening%20screen.png"/>

One of the suggestions that I got in class was to make it so I could save favorited recipes, or to discard disliked recipes so they don't show up again.
The option to discard a recipe would be lower, but I believe if I put a favorite recipe in, it should be displayed here for easy access as soon as possible.

<img src="https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-schweinsbergs/D3/Deliverables/prototype%20pictures/2%20entry%20mode.png"/>

There's been suggestions to add in the amount of ingredients here. I'm not sure how well that would translate, especially since I would have to factor in conversions, but I'd like to document it nonetheless.

If there is an option for favorite recipes, there should either be a back button to be located here, or the favorites button exists on this screen as well.

<img src="https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-schweinsbergs/D3/Deliverables/prototype%20pictures/3%20results.png"/>


The option for favorite recipes can exist here as well. I would imagine it would be something like editing or creating the pkl file it could read from for that.

<img src="https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-schweinsbergs/D3/Deliverables/prototype%20pictures/4%20recipe%20screen.png"/>

This screen contains a return button so that the user can browse other recipes if they want to (IE: they don't like this one.)

# Data flow // ER graph
## Original Prototype

<img src="https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-schweinsbergs/D3/Deliverables/prototype%20pictures/flow%20chart.JPG"/>

My original graph was lacking in design because I wasn't quite sure on how to format it. While I'm still shaky on it, especially with the actual symbols and what they mean,
I feel better after seeing everyone else's and getting an idea of how I want to set it up. I used the class feedback to revamp my design so it wasn't so simple.

# ER graph

<img src="https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-schweinsbergs/D3/Deliverables/prototype%20pictures/er%20diagram.JPG"/>

The first thing I did in the revamp was include an ER graph. Upon doing this and gathering the types of data my recipe scraper collects,
I realized that I'm going to need to somehow populate it, because it doesn't necessarily scrape by site. So, I figured there could be some sort of text document
that might pull URLs from websites, or something, because this scraper uses URLS. Which can then be put to the dataframe, which will then be saved as the pkl
and can be accessed by the app.

# Data Flow

<img src="https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-schweinsbergs/D3/Deliverables/prototype%20pictures/data%20flow%20diagram.JPG"/>

My dataframe includes my ER graph-- I wanted to more or less consider it a black box here, but I wanted to also show there was a relationship between the dataflow and the ER graph. So I just
tossed it in for good measure.

Here we can see how the user interacts with the app, and the app creates, fetches, and compares data to then display to the user.


# Process Reflection

* How was the process of creating your prototype?

Creating the actual paper prototype was easy. It was the ER graph and data flow that I had some trouble with, but I think I feel a little
better about them now. The paper prototype was essentially "what's the most functional and intuitive thing to do here?", while the
graphs were a constant "what am I missing?"

* How did this process guide you?

I realized (which I should have sooner...) that my webscraper only really intakes URLs, so I'll need to find a way to
go ahead and feed the urls. I also found the different types it returns, and how I can work with them, along with how to store
information into a dataframe. All in all, I think I learned a lot about the meat of my app.

* What lingering questions do you have?

I think I'd just like feedback on the ER graph in particular, since I think it was a little tricky.

* How prepared do you feel to tackle what you've created here?

On a scale of 1-10, with 1 being "I have next to no idea what I'm doing" and 10 being "I could make this in my sleep",
I think I'm feeling about a 4. I'm going to be working with a lot of new systems and doing things I don't think I've done before,
which is equally exciting and intimidating. I don't think there's a lot of this that's going to be familiar or easy for me,
but what's a Capstone project if you're overly comfortable? 