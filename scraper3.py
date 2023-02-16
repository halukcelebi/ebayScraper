from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By

from textProcess import textProcess 

driver = webdriver.Chrome(ChromeDriverManager().install())



#url = "https://www.ebay.de/b/Fachbucher-Lehrbucher-Nachschlagewerke/184644/bn_203448?LH_Auction=1&rt=nc&_sop=5";
#url = "https://www.ebay.de/itm/195292013249?epid=88917132&hash=item2d784fa2c1:g:2jIAAOSw64xi~K4x"
#url = "https://www.ebay.de/itm/265840993009?epid=12054111196&hash=item3de55ba2f1:g:9fQAAOSwsZ5jAQYZ"
#url = "https://www.ebay.de/itm/372638383010?epid=161543935&hash=item56c2fa7ba2:g:pHYAAOSwotZcm9p8&amdata=enc%3AAQAHAAAA0PfeVhpmMVrALXctCgZu3%2BStHB5jrrfw%2FB%2BPy2WYJhKC4rFwSCU4wTdtKy6vCSvE4GjyRB8xVJqFZGBrG93zSKZMv3wV%2B7Eta8jA0%2FWcp7NkzWBPvGzLA6u1rOiz%2FNqvH54Na5FUton6f9pFYjtNLKEZuZjC3AJZAQ8VMKcDIgX6tj5z5KDgRO2vvwnP0LDgAFuXM3eHLk2OOAIgWDyPbemf3gS8oeq7f3ZW5QvxpDndf7A%2BTku1TSqnyLfzcZ1B4kam7%2Fuw%2F4UF4wEE8X32BAI%3D%7Ctkp%3ABFBMoLvo7Ntg"

#url = 'https://www.ebay.de/itm/225130612124?hash=item346ad4859c:g:Nn0AAOSwmiJi3lnv';
#url = 'https://www.ebay.de/itm/403849612452?hash=item5e07500ca4:g:FzEAAOSwiT9jBqop' ; 
#url = 'https://www.ebay.de/itm/125482188007?hash=item1d37523ce7:g:xrcAAOSw9~5jB-LD';
#url = 'https://www.ebay.de/itm/374223862860?epid=21042176923&hash=item57217afc4c:g:7EgAAOSwGl1jA5tP';

#url = "https://www.ebay.de"
url = "https://www.ebay.de/itm/314124722597?hash=item49234ae1a5:g:3OAAAOSwmBFjA6CN"

driver.get(url);

book_title=driver.find_element(By.CLASS_NAME,"x-item-title__mainTitle").text;
print('Book title:\t {}'.format( book_title));
#search = driver.find_element(By.CLASS_NAME, "prcIsum_bidPrice");
price =  driver.find_element(By.CLASS_NAME, "notranslate").text;
print('Price: \t {}'.format(price));



#item_descr = driver.find_elements(By.CLASS_NAME,"merch-tile-container");
#for itm in item_descr:
#    print(itm.text)

#print(item_descr);
#print(len(item_descr))


# --------------------------- find ISBN ---------------------------
#1 check if title contains ISBN number 
ISBN = [];
ISBN_title      = textProcess.parseTitle(book_title);

if not ISBN_title :
    about_item =  driver.find_element(By.ID, "viTabs_0_is");
    text            = about_item.text;
    ISBN_aboutitem  = textProcess.parseTitle(text);
       
    if not ISBN_aboutitem :       
        print('look at other descriptions');      
    else:
        
        ISBN =  ISBN_aboutitem;
else : 
    ISBN = ISBN_title;
    
print('ISBN:\t {}'.format(ISBN));
         
         
         
#divs = about_item.find_elements(By.CLASS_NAME, "ux-layout-section__row")

#divs = about_item.find_elements(By.NAME, "class")
#ISBN        = [];
# check if booktitle contains ISBN 

# search ISBN in product descriptions 

#Labels      = [];
#Values      = [];



#for dv in divs :
#   # print(type(dv));
#    dv_label    = dv.find_elements(By.CLASS_NAME,"ux-labels-values__labels");
#    for dvl in dv_label:
#        #print(dvl.text)
#        Labels.append(dvl.text);
#    dv_val      = dv.find_elements(By.CLASS_NAME,"ux-labels-values__values");
#    for dvv in dv_val : 
#        #print(dvv.text)
#        Values.append(dvv.text)
#
#i = 0;
#while i < len(Labels):
#    if '978' in Values[i]:
#        ISBN = Values[i];
        
    #print( '{} \t {}'.format(Labels[i],Values[i] ));
#    i= i + 1;
#print('length label = {} length val = {}'.format(len(Labels),len(Values)) );    
 
#print('ISBN = {}'.format(ISBN));   
 
    #dv_cnt      = dv.find_element(By.CLASS_NAME,"ux-labels-values__values-content");
    #dv_cnt2 = dv.find_elements(By.CLASS_NAME,"ux-textspans");
    #print(dv_cnt2.text)

    #print('{} \t {}'.format(  dv_label.text,dv_val.text ))
#for dv in divs:
#    print(dv.text);
    
#search.send_keys('notebooks')
#search.send_keys(Keys.RETURN)
#print( driver.page_source)
#print( driver.title);

driver.quit();
