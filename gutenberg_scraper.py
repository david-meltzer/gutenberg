import requests
from bs4 import BeautifulSoup
import csv
import argparse

def parse_args():
    argparser=argparse.ArgumentParser(
        description='Process URL and book data'
    )

    argparser.add_argument(
        '--URL',
        type=str,
        default=None,
        help='URL of book'
    )
    argparser.add_argument(
        '--book_title',
        type=str,
        default=None,
        help='book title'
    )
    argparser.add_argument(
        '--author',
        type=str,
        default=None,
        help='author'
    )

    return argparser.parse_args()

def scrape(url,book_title,book_author):

    if url is None:
        raise Exception('Need to include URL of book')

    # The URL of the book on Project Gutenberg
    #url = 'https://www.gutenberg.org/files/2814/2814-h/2814-h.htm'

    # Make a request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the book title
    if book_title is None:
        book_title = soup.find('h1').text.strip()

    if book_author is None:
        # Find the book author
        book_author = soup.find('h2').text.strip()

    # Find the book text and remove the table of contents and other metadata
    book_text = ''
    for element in soup.find_all('p'):
        #if element.text.startswith(('Chapter ', 'CHAPTER ')):
        #    print('found chapter')
        #    continue
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
    url,book_title,book_author=args.values()
    scrape(url,book_title,book_author)
