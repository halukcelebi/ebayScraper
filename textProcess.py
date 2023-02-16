class textProcess():
    
    @staticmethod
    def parseTitle(text):
    #this function extracts ISBN from text. It first removes \n, - and / from string and splits it 
        
        ISBN = [];
    
        title2= text.replace('\n',' ');
        title2  = title2.replace('-','');
        title2  = title2.replace('/','');
        title2 = title2.split(" ",-1);
        

        #i = 0;
        #while i < len(title2) : 
        #    
        #    title2[i]=title2[i].replace('-','');
        #    title2[i]=title2[i].replace('/','');
        #    i= i+1;

        i = 0;
        while i < len(title2):
    
            if '978' in title2[i]:
                ISBN = title2[i];
                
                #print('ISBN contains 978');
                break;
            elif 'ISBN' in title2[i]:
        
                if i + 1 < len(title2):
                    ISBN = title2[i+1];
                    
                    #print('text has ISBN word');
                    break;
            else :
                
                if title2[i].isnumeric() :
                    ctr = 0;
            
                    for ch in  title2[i]:
                        if ch.isdigit():
                            ctr = ctr + 1;
                        else :
                            break;
            
                    if ctr >= 10:
                        #print('Text has ASIN/EAN number');
                        ISBN = title2[i];
     
            i = i+1        

        #print('ISBN: {}'.format(ISBN));
        
        return ISBN;   
        


    