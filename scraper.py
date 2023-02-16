from bs4 import BeautifulSoup
import requests

#url = "https://www.ebay.de/b/Fachbucher-Lehrbucher-Nachschlagewerke/184644/bn_203448?LH_Auction=1&rt=nc";
#url = "https://www.pythonanywhere.com/forums/topic/12505/"
#url = "https://www.amazon.de/";
#url = "https://www.ebay.de";
url = "https://www.ebay.de/b/Fachbucher-Lehrbucher-Nachschlagewerke/184644/bn_203448?LH_Auction=1&rt=nc&_sop=5";


result = requests.get(url).text;
doc = BeautifulSoup(result,"lxml");

print(doc.prettify());
#tbody= doc.tbody
#print(tbody);