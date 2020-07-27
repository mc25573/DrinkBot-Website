# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:23:19 2020

@author: Matthew
"""

def soft_search(pumps,extras,all_ingrs,ingrs_dict):
    
    temp_ingrs_dict = dict(ingrs_dict)
    
    if pumps.get('pineapple juice') and 'cream of coconut' in extras:
        temp_ingrs_dict['pina colada mix'] = (True,'pineapple juice and cream of coconut')          
    
    for ingr in all_ingrs:   
        if ingr == 'vodka' or ingr ==  'absolut vodka':
            temp_ingrs_dict['vodka'] = (True,ingr)
            temp_ingrs_dict['absolut vodka'] = (True,ingr)
            
        elif ingr == 'bourbon' or ingr == 'tennesse whiskey' or ingr == 'wild turkey' or ingr == 'jack daniels':
            temp_ingrs_dict['bourbon'] = (True,ingr)
            temp_ingrs_dict['tennesse whiskey'] = (True,ingr)
            temp_ingrs_dict['wild turkey'] = (True,ingr)
            temp_ingrs_dict['jack daniels'] = (True,ingr)
            temp_ingrs_dict['whiskey'] = (True,ingr)
            temp_ingrs_dict['blended whiskey'] = (True,ingr)
            
        elif ingr == 'scotch' or ingr == 'jim beam' or ingr == 'islay single malt scotch' or ingr == 'johnnie walker' or ingr == 'blended scotch' or ingr == 'whisky':
            temp_ingrs_dict['scotch'] = (True,ingr)
            temp_ingrs_dict['jim beam'] = (True,ingr)
            temp_ingrs_dict['islay single malt scotch'] = (True,ingr)
            temp_ingrs_dict['blended scotch'] = (True,ingr)
            temp_ingrs_dict['johnnie walker'] = (True,ingr)
            temp_ingrs_dict['whisky'] = (True,ingr)
            temp_ingrs_dict['whiskey'] = (True,ingr)
            
        elif ingr == 'whiskey' or ingr == 'blended whiskey':
            temp_ingrs_dict['whiskey'] = (True,ingr)
            temp_ingrs_dict['blended whiskey'] = (True,ingr)
            temp_ingrs_dict['scotch'] = (True,ingr)
            temp_ingrs_dict['jim beam'] = (True,ingr)
            temp_ingrs_dict['islay single malt scotch'] = (True,ingr)
            temp_ingrs_dict['blended scotch'] = (True,ingr)
            temp_ingrs_dict['johnnie walker'] = (True,ingr)
            temp_ingrs_dict['whisky'] = (True,ingr)
            temp_ingrs_dict['bourbon'] = (True,ingr)
            temp_ingrs_dict['tennesse whiskey'] = (True,ingr)
            temp_ingrs_dict['wild turkey'] = (True,ingr)
            temp_ingrs_dict['jack daniels'] = (True,ingr)
            temp_ingrs_dict['rye whiskey'] = (True,ingr)
            temp_ingrs_dict['irish whiskey'] = (True,ingr)
            temp_ingrs_dict['crown royal'] = (True,ingr)
            
        elif ingr == 'carbonated water' or ingr == 'soda water' or ingr == 'club soda' or ingr == 'tonic water':
            temp_ingrs_dict['carbonated water'] = (True,ingr)
            temp_ingrs_dict['soda water'] = (True,ingr)
            temp_ingrs_dict['club soda'] = (True,ingr)
            temp_ingrs_dict['tonic water'] = (True,ingr)
            
        elif ingr == 'simple syrup' or ingr == 'sugar syrup' or ingr == 'agave syrup':
            temp_ingrs_dict['simple syrup'] = (True,ingr)
            temp_ingrs_dict['sugar syrup'] = (True,ingr)
            temp_ingrs_dict['agave syrup'] = (True,ingr)
                    
        elif ingr == 'demerara sugar' or ingr == 'sugar' or ingr == 'powdered sugar':
            temp_ingrs_dict['demerara sugar'] = (True,ingr)
            temp_ingrs_dict['sugar'] = (True,ingr)
            temp_ingrs_dict['powdered sugar'] 
        
        elif ingr == 'dr. pepper' or ingr == 'cola' or ingr == 'coca-cola' or ingr == 'pepsi cola':
            temp_ingrs_dict['cola'] = (True,ingr)
            temp_ingrs_dict['coca-cola'] = (True,ingr)
            temp_ingrs_dict['pepsi cola'] = (True,ingr)  
            temp_ingrs_dict['dr. pepper'] = (True,ingr)
            
        elif ingr == 'lemon-lime soda' or ingr == '7-up' or ingr == 'sprite' or ingr == 'tonic water' or ingr == 'mountain dew':
            temp_ingrs_dict['lemon-lime soda'] = (True,ingr)
            temp_ingrs_dict['7-up'] = (True,ingr)
            temp_ingrs_dict['sprite'] = (True,ingr)
            temp_ingrs_dict['tonic water'] = (True,ingr)
            temp_ingrs_dict['mountain dew'] = (True,ingr)
            
        elif ingr == 'rum':
            temp_ingrs_dict['rum'] = (True,ingr)
            temp_ingrs_dict['light rum'] = (True,ingr)
            temp_ingrs_dict['white rum'] = (True,ingr)
            temp_ingrs_dict['dark rum'] = (True,ingr)
            temp_ingrs_dict['blackstrap rum'] = (True,ingr)
            temp_ingrs_dict['gold rum'] = (True,ingr)
            temp_ingrs_dict['spiced rum'] = (True,ingr)
            temp_ingrs_dict['coconut rum'] = (True,ingr)
            temp_ingrs_dict['malibu rum'] = (True,ingr)
            temp_ingrs_dict['151 proof rum'] = (True,ingr)
            temp_ingrs_dict['anejo rum'] = (True,ingr)
        
        elif ingr == 'white rum' or ingr ==  'light rum' or ingr ==  'cachaca':
            temp_ingrs_dict['white rum'] = (True,ingr)
            temp_ingrs_dict['light rum'] = (True,ingr)
            temp_ingrs_dict['cachaca'] = (True,ingr)
            temp_ingrs_dict['rum'] = (True,ingr)
        
        elif ingr == 'rye whiskey' or ingr ==  'crown royal':
            temp_ingrs_dict['rye whiskey'] = (True,ingr)
            temp_ingrs_dict['crown royal'] = (True,ingr) 
            
        elif ingr == 'coconut rum' or ingr ==  'malibu rum' or ingr == 'coconut liqueur':
            temp_ingrs_dict['coconut rum'] = (True,ingr)
            temp_ingrs_dict['malibu rum'] = (True,ingr)
            temp_ingrs_dict['coconut liqueur'] = (True,ingr)
            
        elif ingr == 'gold rum' or ingr == 'spiced rum' or ingr == 'anejo rum' or ingr == '151 proof rum':
            temp_ingrs_dict['gold rum'] = (True,ingr)
            temp_ingrs_dict['spiced rum'] = (True,ingr)
            temp_ingrs_dict['anejo rum'] = (True,ingr)
            temp_ingrs_dict['151 proof rum'] = (True,ingr)
            temp_ingrs_dict['rum'] = (True,ingr)
            
        elif ingr == 'dark rum':
            temp_ingrs_dict['dark rum'] = (True,ingr)
            temp_ingrs_dict['blackstrap rum'] = (True,ingr)
            temp_ingrs_dict['rum'] = (True,ingr)
            
        elif ingr == 'cherry liqueur' or ingr == 'cherry brandy' or ingr == 'maraschino liqueur' or ingr == 'cherry heering':
            temp_ingrs_dict['cherry liqueur'] = (True,ingr)
            temp_ingrs_dict['cherry brandy'] = (True,ingr)        
            temp_ingrs_dict['maraschino liqueur'] = (True,ingr)
            temp_ingrs_dict['cherry heering'] = (True,ingr)
            
        elif ingr == 'absinthe' or ingr == 'pernod' or ingr == 'ricard' or ingr == 'anise' or ingr == 'ouzo' or ingr == 'sambuca':
            temp_ingrs_dict['absinthe'] = (True,ingr)
            temp_ingrs_dict['pernod'] = (True,ingr)        
            temp_ingrs_dict['ricard'] = (True,ingr)
            temp_ingrs_dict['anise'] = (True,ingr) 
            temp_ingrs_dict['ouzo'] = (True,ingr)
            temp_ingrs_dict['sambuca'] = (True,ingr) 
            
        elif ingr == 'anise liqueur' or ingr == 'anisette':
            temp_ingrs_dict['anise liqueur'] = (True,ingr)
            temp_ingrs_dict['anisette'] = (True,ingr)        
     
        elif ingr == 'honey-whiskey liqueur' or ingr == 'yukon jack' or ingr == 'drambuie':
            temp_ingrs_dict['honey-whiskey liqueur'] = (True,ingr)
            temp_ingrs_dict['yukon jack'] = (True,ingr)        
            temp_ingrs_dict['drambuie'] = (True,ingr)
        
        elif ingr == 'orange liqueur' or ingr == 'triple sec' or ingr == 'curacao' or ingr == 'grand marnier' or ingr == 'cointreau' or ingr == 'blue curacao':
            temp_ingrs_dict['orange liqueur'] = (True,ingr)
            temp_ingrs_dict['curacao'] = (True,ingr)        
            temp_ingrs_dict['grand marnier'] = (True,ingr)
            temp_ingrs_dict['cointreau'] = (True,ingr) 
            temp_ingrs_dict['triple sec'] = (True,ingr)
            temp_ingrs_dict['blue curacao'] = (True,ingr)         
        
        elif ingr == 'grain alcohol' or ingr == 'everclear':
            temp_ingrs_dict['grain alcohol'] = (True,ingr)
            temp_ingrs_dict['everclear'] = (True,ingr)   
                    
        elif ingr == 'caraway liqueur' or ingr == 'kummel' or ingr == 'aquavit':
            temp_ingrs_dict['caraway liqueur'] = (True,ingr)
            temp_ingrs_dict['kummel'] = (True,ingr) 
            temp_ingrs_dict['aquavit'] = (True,ingr) 
        
        elif ingr == 'prosecco' or ingr == 'champagne':
            temp_ingrs_dict['champagne'] = (True,ingr)
            temp_ingrs_dict['prosecco'] = (True,ingr)
            
        elif ingr == 'lillet' or ingr == 'lillet blanc' or ingr =='dubonnet rouge':
            temp_ingrs_dict['lillet'] = (True,ingr)
            temp_ingrs_dict['lillet blanc'] = (True,ingr)
            temp_ingrs_dict['dubonnet rouge'] = (True,ingr)
            
        elif ingr == 'sweet vermouth' or ingr == 'red vermouth' or ingr == 'rosso vermouth':
            temp_ingrs_dict['sweet vermouth'] = (True,ingr)
            temp_ingrs_dict['red vermouth'] = (True,ingr)        
            temp_ingrs_dict['rosso vermouth'] = (True,ingr)
    
        elif ingr == 'root beer' or ingr == 'sarsaparilla':
            temp_ingrs_dict['root beer'] = (True,ingr)
            temp_ingrs_dict['sarsaparilla'] = (True,ingr)
    
        elif ingr == 'cinnamon liqueur' or ingr == 'firewater' or ingr == 'hot damn':
            temp_ingrs_dict['cinnamon liqueur'] = (True,ingr)
            temp_ingrs_dict['firewater'] = (True,ingr)  
            temp_ingrs_dict['hot damn'] = (True,ingr) 
       
        elif ingr == 'hawaiian punch' or ingr == 'fruit punch':
            temp_ingrs_dict['hawaiian punch'] = (True,ingr)
            temp_ingrs_dict['fruit punch'] = (True,ingr)
            temp_ingrs_dict['kool-aid']
            
        elif ingr == 'sweet and sour' or ingr == 'daiquiri mix' or ingr == 'sour mix':
            temp_ingrs_dict['sweet and sour'] = (True,ingr)
            temp_ingrs_dict['daiquiri mix'] = (True,ingr)
            temp_ingrs_dict['sour mix'] = (True,ingr)
    
        elif ingr == 'lemonade' or ingr == 'pink lemonade':
            temp_ingrs_dict['lemonade'] = (True,ingr)
            temp_ingrs_dict['pink lemonade'] = (True,ingr)   
            
        elif ingr == 'apple juice' or ingr == 'apple cider':
            temp_ingrs_dict['apple cider'] = (True,ingr)
            temp_ingrs_dict['apple juice'] = (True,ingr) 
        
        elif ingr == 'apple brandy' or ingr == 'applejack':
            temp_ingrs_dict['applejack'] = (True,ingr)
            temp_ingrs_dict['apple brandy'] = (True,ingr) 
            
        elif ingr == 'angostura bitters' or ingr == 'bitters':
            temp_ingrs_dict['angostura bitters'] = (True,ingr)
            temp_ingrs_dict['bitters'] = (True,ingr)
            
        elif ingr == 'brandy' or ingr == 'cognac':
            temp_ingrs_dict['brandy'] = (True,ingr)
            temp_ingrs_dict['cognac'] = (True,ingr)    
            
        elif ingr == 'melon liqueur' or ingr == 'midori melon liqueur':
            temp_ingrs_dict['melon liqueur'] = (True,ingr)
            temp_ingrs_dict['midori melon liqueur'] = (True,ingr)     
            
        elif ingr == 'chocolate liqueur' or ingr == 'godiva liqueur':
            temp_ingrs_dict['chocolate liqueur'] = (True,ingr)
            temp_ingrs_dict['godiva liqueur'] = (True,ingr)   
            
        elif ingr == 'aperol' or ingr == 'campari':
           temp_ingrs_dict['aperol'] = (True,ingr)
           temp_ingrs_dict['campari'] = (True,ingr)   
           
        elif ingr == 'peppermint schnapps' or ingr == 'rumple minze':
           temp_ingrs_dict['peppermint schnapps'] = (True,ingr)
           temp_ingrs_dict['rumple minze'] = (True,ingr)      
        
        elif ingr == 'frangelico' or ingr == 'amaretto':
           temp_ingrs_dict['frangelico'] = (True,ingr)
           temp_ingrs_dict['amaretto'] = (True,ingr)
        
        elif ingr == 'coffee liqueur' or ingr == 'kahlua' or ingr == 'tia maria':
           temp_ingrs_dict['coffee liqueur'] = (True,ingr)
           temp_ingrs_dict['kahlua'] = (True,ingr)
           temp_ingrs_dict['tia maria'] = (True,ingr)
        
        elif ingr == 'elderflower cordial' or ingr == 'st. germain':
           temp_ingrs_dict['elderflower cordial'] = (True,ingr)
           temp_ingrs_dict['st. germain'] = (True,ingr)
        
        elif ingr == 'banana liqueur' or ingr == 'pisang ambon':
           temp_ingrs_dict['banana liqueur'] = (True,ingr)
           temp_ingrs_dict['pisang ambon'] = (True,ingr)
           
        elif ingr == 'egg':
           temp_ingrs_dict['egg'] = (True,ingr)
           temp_ingrs_dict['egg white'] = (True,ingr)   
           temp_ingrs_dict['egg yolk'] = (True,ingr) 
             
        temp_ingrs_dict[ingr] = (True,ingr)
        
    return temp_ingrs_dict