import requests
import bs4
userInput = input("Enter a wikipedia webage to get the headlines: ")
r = requests.get(userInput)
type(r)
soup = bs4.BeautifulSoup(r.text, 'lxml')
type(soup)
soup.select('.mw-headline')
for word in soup.select('.mw-headline'):
    print(word.text)
