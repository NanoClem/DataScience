"""
creator : decoopmc
"""
from urllib.request import urlopen
import bs4 as BeautifulSoup


def cleanData(refTab, guessWord) :
    ret = []
    for rf in refTab :
        if guessWord in str(rf) :
            ret.append(rf)

    return ret



def main() :
    html = urlopen("https://database.lichess.org")
    soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')

    ref       = soup.findAll('a')
    guessWord = "standard/lichess"

    #-------------------------------------------------
    #   PREMIER NETTOYAGE
    #-------------------------------------------------
    rfstand = cleanData(ref, guessWord)
    print(rfstand, end='\n')
    print("NOMBRES OCCURENCES :", len(rfstand))



if __name__ == '__main__':
    main()
