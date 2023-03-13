import requests
from bs4 import BeautifulSoup

banner = """

         ,MMM8&&&.
    _...MMMMM88&&&&..._
 .::'''MMMMM88&&&&&&'''::.
::     MMMMM88&&&&&&     ::
'::....MMMMM88&&&&&&....::'
   `''''MMMMM88&&&&''''`
   sah   'MMM8&&&'  meran
  
        Key Genius        by Sahmeran
                     Telegram: https://t.me/istiklal_team                                                                                           

  
"""
print(banner)




query = input("Axdarmaq istədiyin dorku yaz : ")

num_pages = 4

filename = 'dorklist.txt'

url = f"https://www.google.com/search?q={query}&num=10"

with open(filename, 'w') as f:
    for page in range(num_pages):
        # Arama sayfasının URL'si
        page_url = f"{url}&start={page*10}"
        # Arama sayfasını al
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for a in soup.select('a'):
            href = a.get('href')
            if href.startswith('/url?q='):
                url = href.split('/url?q=')[1].split('&')[0]
                f.write(url + '\n')
                print(url)

print(f"{filename} adlı faylda nəticələr yazıldı.")
