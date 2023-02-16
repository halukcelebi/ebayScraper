from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By

from pageInfo import pageInfo

url = "https://www.ebay.de/b/Fachbucher-Lehrbucher-Nachschlagewerke/184644/bn_203448?LH_Auction=1&rt=nc&_sop=5";
#url = "https://www.ebay.de/itm/195292013249?epid=88917132&hash=item2d784fa2c1:g:2jIAAOSw64xi~K4x"
#url = "https://www.ebay.de/itm/265840993009?epid=12054111196&hash=item3de55ba2f1:g:9fQAAOSwsZ5jAQYZ"
#url = "https://www.ebay.de/itm/372638383010?epid=161543935&hash=item56c2fa7ba2:g:pHYAAOSwotZcm9p8&amdata=enc%3AAQAHAAAA0PfeVhpmMVrALXctCgZu3%2BStHB5jrrfw%2FB%2BPy2WYJhKC4rFwSCU4wTdtKy6vCSvE4GjyRB8xVJqFZGBrG93zSKZMv3wV%2B7Eta8jA0%2FWcp7NkzWBPvGzLA6u1rOiz%2FNqvH54Na5FUton6f9pFYjtNLKEZuZjC3AJZAQ8VMKcDIgX6tj5z5KDgRO2vvwnP0LDgAFuXM3eHLk2OOAIgWDyPbemf3gS8oeq7f3ZW5QvxpDndf7A%2BTku1TSqnyLfzcZ1B4kam7%2Fuw%2F4UF4wEE8X32BAI%3D%7Ctkp%3ABFBMoLvo7Ntg"

#url = 'https://www.ebay.de/itm/225130612124?hash=item346ad4859c:g:Nn0AAOSwmiJi3lnv';
#url = 'https://www.ebay.de/itm/403849612452?hash=item5e07500ca4:g:FzEAAOSwiT9jBqop' ; 
#url = 'https://www.ebay.de/itm/125482188007?hash=item1d37523ce7:g:xrcAAOSw9~5jB-LD';
#url = 'https://www.ebay.de/itm/374223862860?epid=21042176923&hash=item57217afc4c:g:7EgAAOSwGl1jA5tP';

#pg = pageInfo(url)
#print( pg.get_page_Params() )

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url);
 

#result_list =driver.find_element(By.ID,"s0-27_1-9-0-1\[0\]-0-0");
result_list =driver.find_element(By.ID,"s0-28_1-9-0-1\[0\]-0-0");

#book_list = result_list.find_elements(By.CLASS_NAME,"s-item__link");
book_list = result_list.find_elements(By.TAG_NAME,"a");

#book_list = result_list.find_elements(By.TAG_NAME,"href");


#print(result_list.text)
#print(type(result_list))
#print(type(book_list))


url_list = [];

for bl in book_list :
    url_ = bl.get_attribute("href");
    if 'https://www.ebay.de/itm/' in url_ :
        url_list.append(url_);
#remove duplicates     
url_list = list(dict.fromkeys(url_list));    


# print(book_list);
link_counter    =   0;
for rl in url_list : 
    print('Book[{}]'.format(link_counter))
    print( rl)
    try :
        print(pageInfo.processPage(rl) )
    except : 
        print('Error fetching the data');
    
    link_counter = link_counter + 1;   
    print(''); 
    
#print('number of books: {}'.format(link_counter))
driver.close();

