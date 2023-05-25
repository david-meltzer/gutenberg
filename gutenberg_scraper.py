import requests
import csv
import argparse
from bs4 import BeautifulSoup

def parse_args():
    """
    Parses user defined inputs.
    
    --URL: URL of book being scraped from Project Gutenberg.
    --book_title: Title of the book. User defined, does not have to be actual title.
    --author: Author of the book. User defined and does not have to be full author name.
    """
    argparser = argparse.ArgumentParser(
        description = 'Process URL and book data'
    )

    argparser.add_argument(
        '--URL',
        type = str,
        default = None,
        help = 'URL of book'
    )
    argparser.add_argument(
        '--book_title',
        type = str,
        default = None,
        help = 'book title'
    )
    argparser.add_argument(
        '--author',
        type = str,
        default = None,
        help = 'author'
    )

    return argparser.parse_args()

def scrape(url,
           book_title,
           book_author):
    """
    Scrapes book from ProjectGutenberg and saves resulting file in a csv file.

    Inputs:
    -------
    - url (str): URL of book being scraped from Project Gutenberg.
    - book_title (str): Title of the book. 
    - book_author (str): Author of the book. 

    Outputs:
    --------
    None, but Pandas dataframe is saved locally.
    """
    
    if url is None:
        raise Exception('Need to include URL of book')

    # Make a request to the URL and get the HTML content
    response = requests.get(url,
                            timeout=300)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 
                         'html.parser')

    # Find the book title
    if book_title is None:
        book_title = soup.find('h1').text.strip()

    # Find the book author
    if book_author is None:
        book_author = soup.find('h2').text.strip()

    # Find the book text and remove the table of contents and other metadata
    book_text = ''
    for element in soup.find_all('p'):
        book_text += element.text

    file_name=book_title+'_'+book_author+'.csv'
    # Create a CSV file to save the book data
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'Text'])

        # Write the book data to the CSV file
        writer.writerow([book_title, book_author, book_text])


if __name__ == "__main__":
    args=vars(parse_args())
    url_args,book_title_args,book_author_args=args.values()
    scrape(url_args,book_title_args,book_author_args)
