import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
import pandas as pd  # type: ignore

def Undergrad(url_string, course):
    current_page = 1
    data = []

    proceed = True
    firstloop = True
    while proceed:
        if firstloop:
            url = url_string
            firstloop = False
        else:
            url = url_string+str(current_page)+"/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        if soup.title.text == "404 - Wits University":
            proceed = False
        else:
            all_books = soup.find_all("a", class_="search-result")
            for book in all_books:
                item = {
                    'Title': book.find("h3").text.strip(),
                    'Details': book.find("div", class_="details").text.strip(),
                    'Description': book.find("div", class_="description").text.strip()
                }
                data.append(item)

        current_page += 1

    df = pd.DataFrame(data)
    df.to_excel(course+".xlsx")



def main():
    Undergrad("https://www.wits.ac.za/undergraduate/academic-programmes/faculty-of-science/", "Science")
    Undergrad("https://www.wits.ac.za/undergraduate/academic-programmes/faculty-of-health-sciences/", "Health Science")
    Undergrad("https://www.wits.ac.za/undergraduate/academic-programmes/faculty-of-engineering-and-the-built-environment/", "Engineering")
    Undergrad("https://www.wits.ac.za/undergraduate/academic-programmes/faculty-of-commerce-law-and-management/", "Commerce, Law & Management")
    Undergrad("https://www.wits.ac.za/undergraduate/academic-programmes/faculty-of-humanities/", "Humanities")


if __name__ == "__main__":
    main()
