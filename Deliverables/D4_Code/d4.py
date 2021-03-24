import pandas as pd
from recipe_scrapers import scrape_me


class testScrape:
    """
    The class for scraping and storing recipes into a dataframe, and then pickling them.
    """

    def __init__(self, scraper, recipeInfo, df, title, totaltime, yields, ingredients):
        """
        self.scraper = the web scraper
        :param scraper:
        self.recipeInfo = data pulled from scraper for data frame
        self.df = data frame
        """

        self.scraper = scraper
        self.recipeInfo = recipeInfo
        self.df = df
        self.title = title
        self.totaltime = totaltime
        self.yields = yields
        self.ingredients = ingredients


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
        print(self.df)


def main():
    """
    Currently calls everything so I can test it.
    :return:
    """
    test = testScrape('scraper', 'recipeInfo', 'df', 'title', 'totaltime','yields','ingredients')
    test.scraping()
    test.dataframe()


main()