import requests
from bs4 import BeautifulSoup
import csv

def scrape_imdb_top_movies():
    url = "https://www.imdb.com/chart/top"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    movie_list = []

    for movie in soup.select("td.titleColumn"):
        title = movie.find("a").get_text()
        year = movie.find("span").get_text()[1:5]
        rating = movie.find_next("td", class_="ratingColumn").get_text().strip()

        movie_list.append({"Title": title, "Year": year, "Rating": rating})

    return movie_list

def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Title", "Year", "Rating"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for movie in data:
            writer.writerow(movie)

if __name__ == "__main__":
    scraped_data = scrape_imdb_top_movies()
    save_to_csv(scraped_data, "top_movies.csv")
    print("Scraping and CSV creation completed!")
