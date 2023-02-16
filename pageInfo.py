from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
from textProcess import textProcess 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class pageInfo():

    def __init__(self,url):
        
        self.url    = url;
        self.price  = [];
        self.title  = [];
        self.ISBN   = [];
        self.set_page_Params();
        
    @staticmethod    
    def processPage(url):    
        #url = self.url;
        
        
        
        driver = webdriver.Chrome(ChromeDriverManager().install());
        #driver.implicitly_wait(10);
        driver.get(url);
        
        #book_title=driver.find_element(By.CLASS_NAME,"x-item-title__mainTitle").text;
        
        #book_title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "x-item-title__mainTitle")))
        
        try:
            book_title = WebDriverWait(driver,10).until( EC.presence_of_element_located((By.CLASS_NAME, "x-item-title__mainTitle"))).text;
        except: 
            print('unable to find title')
        
        
        #price =  driver.find_element(By.CLASS_NAME, "notranslate").text;
        try: 
            #price =  driver.find_element(By.CLASS_NAME, "x-price-primary").text;
            price = WebDriverWait(driver,10).until( EC.presence_of_element_located((By.CLASS_NAME, "x-price-primary"))).text;
        except: 
            print('cant find price')
        #about_item =  driver.find_element(By.ID, "viTabs_0_is");
        
        ISBN = [];
        ISBN_title      = textProcess.parseTitle(book_title);

        if not ISBN_title :
            
            try :
                #about_item =  driver.find_element(By.ID, "viTabs_0_is");
                about_item = WebDriverWait(driver,10).until( EC.presence_of_element_located((By.ID, "viTabs_0_is")));
            except :
                print('cant find item descriptions');
                
            
            text            = about_item.text;
            ISBN_aboutitem  = textProcess.parseTitle(text);
    
            if not ISBN_aboutitem : 
        
                print('[Err pageInfo]look at other descriptions');
            else:
                ISBN =  ISBN_aboutitem;
        else : 
            ISBN = ISBN_title;
    
        #print('ISBN:\t {}'.format(ISBN));
        
        #self.price = price;
        #self.title = book_title;
        #self.ISBN = ISBN;
         
        driver.close();
        
        return [book_title, price,  ISBN];
        
        
    def set_page_Params(self):
        
        [A, B, C]   = pageInfo.processPage(self.url)
        self.title  = A;
        self.price  = B;
        self.ISBN   = C;
        
    def get_page_Params(self):    
        return [self.title, self.price, self.ISBN];    




