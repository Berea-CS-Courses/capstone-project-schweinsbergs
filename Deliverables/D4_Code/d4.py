import pandas as pd
import pickle
from recipe_scrapers import scrape_me

# Assistance with the pickle code from:
# https://www.youtube.com/watch?v=WkIW0YLoQEE&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&t=507s&ab_channel=sentdex

class testScrape:
    """
    The class for scraping and storing recipes into a dataframe, and then pickling them.
    """

    def __init__(self, scraper, recipeInfo, df, title, totaltime, yields, ingredients, recipeLoad):
        """
        self.scraper = the web scraper
        :param scraper:
        self.recipeInfo = data pulled from scraper for data frame
        self.df = data frame
        self.totaltime = total time to create recipe
        self.yields = the yields of the recipe
        self.ingredients = the ingredients of the recipe
        self.recipeLoad = loaded pickle file contents
        """

        self.scraper = scraper
        self.recipeInfo = recipeInfo
        self.df = df
        self.title = title
        self.totaltime = totaltime
        self.yields = yields
        self.ingredients = ingredients
        self.recipeLoad = recipeLoad


    def scraping(self):
        """
        Scrapes the information from the web scraper.
        :return:
        """
        self.scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
        self.title = self.scraper.title()
        self.totaltime = self.scraper.total_time()
        self.yields = self.scraper.yields()
        #print(self.scraper.title())

    def dataframe(self):
        """
        Sets up the data frame?
        :return:
        """

        #self.title = []
        #self.totaltime = []
        #self.yields = []

        self.recipeInfo = {'Title': [self.title],
                           'Total Time': [self.totaltime],
                           'yields': [self.yields]}

        self.df = pd.DataFrame(self.recipeInfo, columns=['Title', 'Total Time', 'yields'])
        #print(self.df)

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
        print(self.recipeLoad) # prints it for me to prove it happened lol


def main():
    """
    Currently calls everything so I can test it.
    :return:open('pickleRecipe.pickle', 'wb')
    """
    test = testScrape('scraper', 'recipeInfo', 'df', 'title', 'totaltime','yields','ingredients', 'recipeLoad')
    test.scraping()
    test.dataframe()
    test.open_pickle_jar()


main()