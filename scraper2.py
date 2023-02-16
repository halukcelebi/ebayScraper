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
url = 'https://www.ebay.de/itm/225130612124?hash=item346ad4859c:g:Nn0AAOSwmiJi3lnv';
#url = "https://www.ebay.de"
driver.get(url);

book_title=driver.find_element(By.CLASS_NAME,"x-item-title__mainTitle").text;
print(book_title);
#search = driver.find_element(By.CLASS_NAME, "prcIsum_bidPrice");
price =  driver.find_element(By.CLASS_NAME, "notranslate").text;
print(price);
about_item =  driver.find_element(By.ID, "viTabs_0_is");
#print(about_item.text);
print('----about item---')

text = about_item.text;
print(text)
ISBN = textProcess.parseTitle(text)

print(ISBN);
print('-------------')




divs = about_item.find_elements(By.CLASS_NAME, "ux-layout-section__row")

#divs = about_item.find_elements(By.NAME, "class")
ISBN        = [];
# check if booktitle contains ISBN 

# search ISBN in product descriptions 

Labels      = [];
Values      = [];



for dv in divs :
   # print(type(dv));
    dv_label    = dv.find_elements(By.CLASS_NAME,"ux-labels-values__labels");
    for dvl in dv_label:
        #print(dvl.text)
        Labels.append(dvl.text);
    dv_val      = dv.find_elements(By.CLASS_NAME,"ux-labels-values__values");
    for dvv in dv_val : 
        #print(dvv.text)
        Values.append(dvv.text)

i = 0;
while i < len(Labels):
    if '978' in Values[i]:
        ISBN = Values[i];
        
    #print( '{} \t {}'.format(Labels[i],Values[i] ));
    i= i + 1;
#print('length label = {} length val = {}'.format(len(Labels),len(Values)) );    
 
print('ISBN = {}'.format(ISBN));   
 
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
