import requests
from bs4 import BeautifulSoup

# Nice list of binary crates
req = requests.get('https://lib.rs/command-line-utilities')
soup = BeautifulSoup(req.content, 'html.parser')
crates = map(lambda c: c.get_text(), soup.find(id='category-crates').find_all('h4'))

print(*crates, sep='\n')