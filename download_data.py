import re
from newspaper import Article
from bs4 import BeautifulSoup

url = "https://www.tagesschau.de/newsticker/liveblog-ukraine-donnerstag-111.html"
all_done = False

with open("ukraine.txt", "a") as f:
    while not all_done:
        a = Article(url, language='de')
        a.download()
        soup = BeautifulSoup(a.html, "lxml")
        divs = soup.find_all("div", {"class": "columns twelve liveblog--anchor"})

        for i, div in enumerate(divs):
            if i <= 1:
                continue
            elif i == len(divs)-1:
                a = div.find("a", href=re.compile("liveblog"))
                if a is None:
                    all_done = True
                else:
                    url = a["href"]
            else:
                try:    
                    result = {}
                    result["meta"] = div.find("div", {"class": "liveblog__datetime columns twelve m-ten m-offset-one l-eight l-offset-two"}).text.strip()
                    result["title"] = div.find("h2", {"class": "meldung__subhead columns twelve m-ten m-offset-one l-eight l-offset-two"}).text.strip()
                    result["text"] = " ".join([t.text.replace("\n","").strip() for t in div.findAll("p", {"class": "m-ten m-offset-one l-eight l-offset-two textabsatz columns twelve"})])

                    if i == 2:
                        print(result["meta"], url)
                    
                    if result["title"] != "Ende des Liveblogs":
                        f.write(f"{str(result)}\n")
                except AttributeError:
                    continue
