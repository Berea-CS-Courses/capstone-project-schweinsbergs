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



    def scraping(self):
        """
        Scrapes the information from the web scraper.
        :return:
        """
        self.scraper = scrape_me('https://www.allrecipes.com/recipe/274974/lemon-ricotta-cornmeal-waffles/')
        self.title = self.scraper.title()
        self.totaltime = self.scraper.total_time()
        self.yields = self.scraper.yields()
        self.ingredients = self.scraper.ingredients()
        self.instructions = self.scraper.instructions()

    def dataframe(self):
        """
        Sets up the data frame?
        TODO: make all the data lowercase
        :return:
        """


        self.recipeInfo = {'Title': [self.title],
                           'Total Time': [self.totaltime],
                           'yields': [self.yields],
                           'ingredients': [self.ingredients],
                           'Instructions': [self.instructions]}

        self.df = pd.DataFrame(self.recipeInfo, columns=['Title', 'Total Time', 'yields', 'ingredients', 'Instructions'])
        ### TESTING ###
        # self.df.insert(1,"Ham for testing", 13, "5 cups") # remember to put in the number of the column
        # addition = {'Title': 'Tasty Test Ham', 'Total Time': 13, 'yields': "12 cups", 'ingredients':["ham", "cheese"]}
        # self.df = self.df.append(addition, ignore_index=True)
        # print(self.df)
        # https://www.geeksforgeeks.org/how-to-iterate-through-excel-rows-in-python/

        excellsheet = openpyxl.load_workbook("xmlinfo.xlsx")

        readurls = excellsheet.active

        for i in range(250, readurls.max_row + 1):
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
            print("Succeeded scrape at row", recipeurls)

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

        self.user_ingredients = userinput.split()
        # print("ingredients:", self.user_ingredients)

    def compare_ingredients(self):
        """
        Compares the dataframe's ingredients list and the user's.
        This might be helpful: https://towardsdatascience.com/dealing-with-list-values-in-pandas-dataframes-a177e534f173
        :return:
        """

        for ind in self.recipeLoad.index:
            # print(self.recipeLoad['ingredients'][ind]) # debugging
            ingredientlist = list(self.recipeLoad['ingredients'][ind])
            matches = set(ingredientlist) & set(self.user_ingredients)
            totalMatchLength = len(matches)
            userLength = len(ingredientlist)
            percentageMatched = totalMatchLength / userLength
            if percentageMatched > 0:
                print(self.recipeLoad['Title'][ind])
                print(list(self.recipeLoad['ingredients'][ind]))
                print("Percentage matched:", percentageMatched * 100)
            else:
                print("No match!")






def main():
    """
    Currently calls everything so I can test it.
    :return:open('pickleRecipe.pickle', 'wb')
    """
    test = testScrape('scraper', 'recipeInfo', 'df', 'title', 'totaltime','yields','ingredients', 'recipeLoad',
                      'user_ingredients', 'Instructions')
    test.scraping()
    test.dataframe()
    test.pickle_jar()
    test.open_pickle_jar()
    test.user_input()
    test.compare_ingredients()


main()