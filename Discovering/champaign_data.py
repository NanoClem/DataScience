from urllib.request import urlopen
import bs4 as BeautifulSoup
import re



def main() :
    html = urlopen("http://capsules.musa.free.fr/Caves02.html?fbclid=IwAR32Nqicxl6L2InZ6gjCO73PS_dtcgCBQwZC01dDPokE1aTCV9CcrdGpn28")
    soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')

    #ESSAYER DE TROUVER UN REGEX PATTERN
    ref   = soup.findAll('b')
    ref = list(set(ref))
    print(ref)




if __name__ == '__main__':
    main()
