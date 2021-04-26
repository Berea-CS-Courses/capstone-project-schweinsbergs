import pandas as pd # for dataframe
import pickle # to save dataframe
from recipe_scrapers import scrape_me # recipe scraper
import openpyxl # for working with excel files

# Assistance with the pickle code from:
# https://www.youtube.com/watch?v=WkIW0YLoQEE&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&t=507s&ab_channel=sentdex

# Assistance with sitemap scraping from:
# https://github.com/dsottimano/xmlsitemap-extractor-google-sheets/blob/master/xmlscript.js
#######################################################################################################################


class testScrape:
    """
    The class for scraping and storing recipes into a dataframe, and then pickling them.
    """

    def __init__(self, scraper, recipeInfo, df, title, totaltime, yields, ingredients, recipeLoad, user_ingredients,
                 instructions):
        """
        self.scraper = the web scraper
        :param scraper:
        self.recipeInfo = data pulled from scraper for data frame
        self.df = data frame
        self.totaltime = total time to create recipe
        self.yields = the yields of the recipe
        self.ingredients = the ingredients of the recipe
        self.recipeLoad = loaded pickle file contents
        self.user_ingredients = the user's inputted ingredients
        self.instructions = the user's inputted instructions
        """

        self.scraper = scraper
        self.recipeInfo = recipeInfo
        self.df = df
        self.title = title
        self.totaltime = totaltime
        self.yields = yields
        self.ingredients = ingredients
        self.recipeLoad = recipeLoad
        self.user_ingredients = user_ingredients
        self.instructions = instructions


    def dataframe(self):
        """
        This sets up the dataframe. It opens up the excel sheet that contains all of the recipes URLS, reads it cell
        by cell, and populates the dataframe with each recipe.
        :return:
        """

        # Assigns each column of the data frame with a value.
        self.recipeInfo = {'Title': [self.title],
                           'Total Time': [self.totaltime],
                           'yields': [self.yields],
                           'ingredients': [self.ingredients],
                           'Instructions': [self.instructions]}

        # Actually creates the dataframe based on those values.

        self.df = pd.DataFrame(self.recipeInfo, columns=['Title', 'Total Time', 'yields', 'ingredients', 'Instructions'])
        # Now we have an empty dataframe with only titles, so we're going to open up the excel sheet. readurls is what
        # we use to actually READ the sheets.
        excellsheet = openpyxl.load_workbook("xmlinfo.xlsx")
        readurls = excellsheet.active

        # This iterates down the excel sheet and feeds urls to the web scraper. The web scraper then scrapes that url,
        # and places the data into the dataframe.
        for i in range(250, readurls.max_row + 1):   # changing the number @ range will change where the program reads
            recipeurls = readurls.cell(row=i, column=1)

            self.scraper = scrape_me(recipeurls.value)
            self.title = self.scraper.title()
            self.totaltime = self.scraper.total_time()
            self.yields = self.scraper.yields()
            self.ingredients = self.scraper.ingredients()
            self.instructions = self.scraper.instructions()

            addition = {'Title': self.title , 'Total Time' : self.totaltime , 'yields' : self.yields,
                        'ingredients' : self.ingredients, 'Instructions' : self.instructions}

            self.df = self.df.append(addition, ignore_index=True)
            print("Succeeded scrape at row", recipeurls)  # feedback so I'm not sitting in idle hell

        print(self.df)


    def pickle_jar(self):
        """
        Function to "pickle" my dataframe, which saves it as a pickle file.
        :return:
        """

        pickle_out = open('pickleRecipe.pickle', 'wb') # Creates pickleRecipe.pickle file, wb = write bytes
        pickle.dump(self.df, pickle_out) # dumps dataframe into pickle_out, the pickle file
        pickle_out.close()

    def open_pickle_jar(self):
        """
        Opens the pickle! This lets the program read from the pickle file so that the data can be used later.
        :return:
        """

        pickle_in = open('pickleRecipe.pickle', 'rb') # opens the pickle, now rb = read bytes
        self.recipeLoad = pickle.load(pickle_in) # reads pickle file
        # print(self.recipeLoad) # prints it for me to prove it happened lol

    def user_input(self):
        """
        Takes the user input and makes it a list of strings.
        TODO: Make all of the input lower case
        :return:
        """

        userinput = input("Enter your ingredients separated by a space.")

        self.user_ingredients = userinput.split() # splits each ingredient up
        # print("ingredients:", self.user_ingredients)

    def compare_ingredients(self):
        """
        Compares the dataframe's ingredients list and the user's.
        This might be helpful: https://towardsdatascience.com/dealing-with-list-values-in-pandas-dataframes-a177e534f173
        :return:
        """

        for ind in self.recipeLoad.index: # for however big the dataframe is:
            ingredientlist = list(self.recipeLoad['ingredients'][ind])  # the ingredients column is now a list per row
            matches = set(ingredientlist) & set(self.user_ingredients)  # a match is if it's in user and ingredients
            totalMatchLength = len(matches) # how many matches we have total
            userLength = len(ingredientlist) # how many ingredients has the user given?
            percentageMatched = totalMatchLength / userLength # matches divided by original number is the % matched
            if percentageMatched > 0: # If the percentage matched is over 0
                print(self.recipeLoad['Title'][ind])
                print(list(self.recipeLoad['ingredients'][ind]))
                print("Percentage matched:", percentageMatched * 100) # tell me how much it matched by and the recipe
            else:  # else, you got no food bud
                print("No match!")


def main():
    """
    Currently calls everything so I can test it.
    :return:open('pickleRecipe.pickle', 'wb')
    """
    test = testScrape('scraper', 'recipeInfo', 'df', 'title', 'totaltime','yields','ingredients', 'recipeLoad',
                      'user_ingredients', 'Instructions')

    #test.dataframe()  uncomment this if you wanna add more info to the dataframe. on god dont do it otherwise.
    test.pickle_jar()
    test.open_pickle_jar()
    test.user_input()
    test.compare_ingredients()


main()