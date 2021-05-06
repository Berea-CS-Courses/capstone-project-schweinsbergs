from recipe_scrapers import scrape_me

scraper = scrape_me('https://www.acouplecooks.com/tofu-curry/', wild_mode=False)

print(type(scraper.ingredients()))

print(type(scraper.instructions()))

print(type(scraper.images)))

print(type(scraper.host()))

print(type(scraper.links()))

print(type(scraper.nutrients()))