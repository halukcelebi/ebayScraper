from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
import  numpy as np
import socket;
import time;

from pageInfo import pageInfo
import  pandas as pd


from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


def is_webdriver_alive(driver):
    print('Checking whether the driver is alive')
    try:
        assert(driver.service.process.poll() == None) #Returns an int if dead and None if alive
        driver.service.assert_process_still_running() #Throws a WebDriverException if dead
        driver.find_element_by_tag_name('html') #Throws a NoSuchElementException if dead
        print('The driver appears to be alive')
        return True
    except (NoSuchElementException, WebDriverException, AssertionError):
        print('The driver appears to be dead')
        return False
    except Exception as ex:
        print('Encountered an unexpected exception type ({}) while checking the driver status'.format(type(ex)))
        return False


base_url        = "https://www.ebay.de/b/Fachbucher-Lehrbucher-Nachschlagewerke/184644/bn_203448?LH_Auction=1&rt=nc&_sop=5";
base_url_pg2    = "https://www.ebay.de/b/Fachbucher-Lehrbucher-Nachschlagewerke/184644/bn_203448?LH_Auction=1&rt=nc&_pgn=2&_sop=5"

pg_ct       = 49;
page_max    = 100;

fl_conn = False
fl_in = True;
ARR_list        = [];
arr_list_ct     = 0;

#creates two dimensional list without shallow copy 
rows, cols = (48 * (page_max - pg_ct +1)  ,  3 ) # 
# method 2b
ARR_list = [[0 for i in range(cols)] for j in range(rows)];

#url = "https://www.ebay.de/itm/195292013249?epid=88917132&hash=item2d784fa2c1:g:2jIAAOSw64xi~K4x"
#url = "https://www.ebay.de/itm/265840993009?epid=12054111196&hash=item3de55ba2f1:g:9fQAAOSwsZ5jAQYZ"
#url = "https://www.ebay.de/itm/372638383010?epid=161543935&hash=item56c2fa7ba2:g:pHYAAOSwotZcm9p8&amdata=enc%3AAQAHAAAA0PfeVhpmMVrALXctCgZu3%2BStHB5jrrfw%2FB%2BPy2WYJhKC4rFwSCU4wTdtKy6vCSvE4GjyRB8xVJqFZGBrG93zSKZMv3wV%2B7Eta8jA0%2FWcp7NkzWBPvGzLA6u1rOiz%2FNqvH54Na5FUton6f9pFYjtNLKEZuZjC3AJZAQ8VMKcDIgX6tj5z5KDgRO2vvwnP0LDgAFuXM3eHLk2OOAIgWDyPbemf3gS8oeq7f3ZW5QvxpDndf7A%2BTku1TSqnyLfzcZ1B4kam7%2Fuw%2F4UF4wEE8X32BAI%3D%7Ctkp%3ABFBMoLvo7Ntg"

#url = 'https://www.ebay.de/itm/225130612124?hash=item346ad4859c:g:Nn0AAOSwmiJi3lnv';
#url = 'https://www.ebay.de/itm/403849612452?hash=item5e07500ca4:g:FzEAAOSwiT9jBqop' ; 
#url = 'https://www.ebay.de/itm/125482188007?hash=item1d37523ce7:g:xrcAAOSw9~5jB-LD';
#url = 'https://www.ebay.de/itm/374223862860?epid=21042176923&hash=item57217afc4c:g:7EgAAOSwGl1jA5tP';

#pg = pageInfo(url)
#print( pg.get_page_Params() )


while pg_ct <= page_max:  
    
    if pg_ct ==  1: 
        url = base_url;
    else:
        url = "https://www.ebay.de/b/Fachbucher-Lehrbucher-Nachschlagewerke/184644/bn_203448?LH_Auction=1&rt=nc&_pgn="+str(pg_ct)+"&_sop=5";
    
    while not fl_conn:
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(url);
            fl_conn = True;
        except:
            print("Exception occured trying to connect again..\n"); 
            driver.close();
               
     
    #result_list =driver.find_element(By.ID,"s0-27_1-9-0-1\[0\]-0-0");
    result_list     = driver.find_element(By.ID,"s0-28_1-9-0-1\[0\]-0-0");
    
    #book_list = result_list.find_elements(By.CLASS_NAME,"s-item__link");
    book_list       = result_list.find_elements(By.TAG_NAME,"a");
    
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
    url_list = list( dict.fromkeys(url_list) );    
    
    # print(book_list);
    link_counter    =   0;
    
    for rl in url_list : 
        print('Book[{}/{}]'.format(link_counter,pg_ct))
        print( rl)
        try :
            [Title,Price,ISBN] = pageInfo.processPage(rl);
            
            print('{} {} {}'.format(Title, Price, ISBN) );
            if ISBN :
                
                print('ISBN exists {}\n'.format(ISBN));
                
                ARR_list[arr_list_ct][0] = Title;
                ARR_list[arr_list_ct][1] = ISBN;
                ARR_list[arr_list_ct][2] = Price;
                arr_list_ct = arr_list_ct + 1;
        
        except : 
            print('Error fetching the data, checking internet connection..');
            fl_in = False;
        
        # unable to connect wait until connection established
        while not fl_in : 
            
            IPaddress=socket.gethostbyname(socket.gethostname());
            #print('IPaddress'+IPaddress);
            if str(IPaddress) =="127.0.0.1":
                
                print("No internet, your localhost is "+ IPaddress);
                time.sleep(6); 
                #driver.close();
            else:
                print("Connected, with the IP address: "+ IPaddress );
                fl_in = True; 
                
                   
                
        
        link_counter = link_counter + 1;   
        print(''); 
        
    #print('number of books: {}'.format(link_counter))
    #if is_webdriver_alive(driver):
     #   driver.close();
    #driver.close();    
    # go to next page 
    
    print('page {} is scraped now going to page {}'.format(pg_ct,pg_ct+1)); 
    print('_____________________________________________________________');

    if arr_list_ct < rows :   
        ARR_list_ = np.delete( ARR_list, slice( arr_list_ct , rows  , 1 ), 0)    
        
    df = pd.DataFrame( ARR_list_ , columns= ["title", "ISBN", "Price"] )  
    with pd.ExcelWriter("scrape_results.ods") as writer:
        df.to_excel(writer); 
    
    
    pg_ct = pg_ct + 1; 
    fl_conn = False;
    

if arr_list_ct < rows :   
    ARR_list_ = np.delete( ARR_list, slice( arr_list_ct , rows  , 1 ), 0)    
    
df = pd.DataFrame( ARR_list_ , columns= ["title", "ISBN", "Price"] )  
with pd.ExcelWriter("scrape_results.ods") as writer:
    df.to_excel(writer); 
