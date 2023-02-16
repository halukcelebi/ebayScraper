# -*- coding:utf-8 -*-

#title = 'Der Konzernabschluss | Buch | 9783791037301';
#title = "Der Konzernabschluss | Buch | 978-37910373-01";
#title = 'Sterne: die Suche nach den Wurzeln von England, Michael Holz - 9780563205005';
#title = 'Rondo 7/8, Sch�lerbuch Karl-Heinz Keller, Mildenberger, ISBN 3-619-77700-4';
#title = 'Rondo 7/8, Sch�lerbuch Karl-Heinz Keller, Mildenberger,  3-619-77700-4';
title = 'Artikelmerkmale\nArtikelzustand:\nGut:\nHinweise des Verkäufers:\n“Wir haben diesen Artikel sorgfältig für Sie geprüft!”\nISBN:\n9783464571446\nEAN:\n9783464571446\nReihe:\nDas Große Tafelwerk Interaktiv\nFach:\nPhysik, Chemie, Mathematik\nProduktart:\nLehrbuch\nFormat:\nGebundene Ausgabe\nErscheinungsjahr:\n2003\nAnzahl der Seiten:\n168\nAutor:\nMatthias Felsch, Rolf Winter, Wolfgang Pfeil, Wolfgang Kricke, Karlheinz Martin\nVerlag:\nCornelsen Verlag Gmbh\nPublikationsname:\nDas große Tafelwerk interaktiv - Allgemeine Ausgabe / Tafelwerk Mathematik, Informatik, Astronomie, Physik, Chemie, Biologie von Karlheinz Martin, Matthias Felsch, Rolf Winter, Wolfgang Kricke und Wolfgang Pfeil (2003, Gebundene Ausgabe)\nSprache:\nDeutsch\nGewicht:\n518g'

#title = 'Artikelmerkmale\nArtikelzustand:\nGut:\nHinweise des Verkäufers:\n“Wir haben diesen (2003, Gebundene Ausgabe)\nSprache:\nDeutsch\nGewicht:\n518g'




ISBN = [];



title2  = title.replace('\n',' ');
title2  = title2.replace('-','');
title2  = title2.replace('/','');
title2  = title2.split(" ",-1);

#i = 0;
#while i < len(title2) : 
#    
#    
#    title2[i]=title2[i].replace('-','');
#    title2[i]=title2[i].replace('/','');
#   
#    i= i+1;


i   =  0;
while i < len(title2):
    print(i)
    
    if '978' in title2[i]:
        ISBN = title2[i];
        print('ISBN contains 978');
        
        break;
    elif 'ISBN' in title2[i]:
        if i + 1 < len(title2) :
            ISBN = title2[i+1]; 
            print('text has ISBN word');
            break;
        
    else :
        if title2[i].isnumeric() :
            ctr = 0;
            for ch in  title2[i]:
                if ch.isdigit():
                    ctr = ctr + 1;
                else :
                    print('String has non-numeric characters');
                    break;
            
            if ctr >= 10:
                print('Text has ASIN/EAN number');
                ISBN = title2[i];
                break;
    i = i+1;
       

print('ISBN: {}'.format(ISBN));
