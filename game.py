# -*- coding: utf-8 -*-
"""
Created on Sun May  2 09:36:42 2021

@author: corey
This program takes user input, validates user input before running, and updates values based on user interaction.
Instructions are placed throughout.
"""
import random
import time
def main():
    print('     FFFFF  IIIIIII      SSS     H    H         ')
    print('    F         I        S   S    H    H    ')
    print('   FFF       I         S       HHHHHH        ')
    print('  F         I           S     H    H    ')
    print(' F         I        S   S    H    H   ')
    print('F      IIIIIII     SSSS    H    H    ')
    gas=random.randint(10,20)
    money=random.randint(0,12)+random.randint(0,3)
    capacity=500.0
    fishInboat=[]
    Quit=False
    gift_of_the_merman=False
    docked=False
    has_docked=False
    fish_list=[{'name':'seaweed','max_weight':4,'min length':3,'max_length':42,'price per pound':0},
               {'name':'green seaweed','max_weight':4,'min length':1,'max_length':42,'price per pound':.01},
               {'name':'brown seaweed','max_weight':6,'min length':2,'max_length':79,'price per pound':.10},
               {'name':'bass','max_weight':30,'max_length':36,'min length':3,'price per pound':.75},
               {'name':'perch','max_weight':8,'max_length':18,'min length':2,'price per pound':1.10},
               {'name':'croppy','max_weight':9,'max_length':19,'min length':2,'price per pound':.69},
               {'name':'trout','max_weight':25,'max_length':63,'min length':2,'price per pound':1.34},
               {'name':'catfish','max_weight':50,'max_length':71,'min length':2,'price per pound':.89,'extras':{'quills'}},
               {'name':'sunfish','max_weight':11,'max_length':24,'min length':2,'price per pound':.69},
               {'name':'carp','max_weight':160,'max_length':120,'min length':4,'price per pound':1.50},
               {'name':'merman','max_weight':135,'max_length':87,'min length':29,'price per pound':50,'extras':{'Amulet of the Deep Queen'}}]
    
    
    def luck():
        return float(random.randint(60,100)/100)
    
    def mermanizer():
        mermen=[{'mername':'Aglaophonus','type':'Wizard','title':'Wizard of the Bog'},
                {'mername':'Molpe','type':'Drowner'},
                {'mername':'Scilpion','type':'Screecher'},
                {'mername':'Sclaxion','type':'Slicer'},
                {'mername':'Thelzion','type':'Wizard','title':'Master of Fish'},
                {'mername':'Bilgo','type':'gift giver'},
                {'mername':'Goriel','type':'Drowner'}]
        roll=randint(0,len(mermen)-1)
        return mermen[roll]
    def catch():
        roll=int(random.randint(0,len(fish_list)-1)*fishLuck)
        return fish_list[roll]
    def weight(FISH):
        return round(random.randint(0,FISH['max_weight'])*fishLuck,2)
    def length(fish):
        return round(random.randint(0,fish['max_length'])*fishLuck,2)
    def Length(Fish):
        return round((Fish['min length']*(Fish['max_weight']-heft)+Fish['max_length']*heft)/Fish['max_weight'],2)
    
    def dock():
        pass
        
    
    #simulates the reality of fishing in a lake. Not every spot is the same
    fishLuck=luck()
    while Quit==False:
        
        query= input("I love fishing. Here we are on a boat.Type a command and press enter.\n C into the terminal to cast your line,\n M to move the boat,\n L to look in the boat,\nG to check how much gas we have left,\nD to go back to the dock and sell the fish \n or type Q and press enter to quit.  ")

#Cast the line

        if 'c' in query.lower():
            fish=catch()
            heft=weight(fish)
            LENGTH=Length(fish)
            time.sleep(random.randint(0,5))
            fishInboat.append({'name':fish['name'],'weight':str(heft)+'lbs','length':str(LENGTH)+'inches'})
            fishLuck=fishLuck*.9
            print('\n\n\n\n','You Caught', fishInboat[-1]['name'],fishInboat[-1]['weight'],fishInboat[-1]['length'],'\n\n\n\n')
            
            
            ###Merman Mini Game###
            
            if fishInboat[-1]['name']=='merman':
                merman_question=input('These fellas are pretty dangerous. Some of them can talk,\n but you made need to gaffe him or he\'s liable to escape, or worse.\n\n\n Enter T to try to talk to the creature, G to gaffe it, or L to let him go.')
                merman=mermanizer()
                if t in merman_question.lower():
                    if merman['type']=='Wizard':
                        print('\"I am the wise and powerful', merman['mername'],',', merman['title'],',','\n Let me go and I shall grant you a reward\"','\nF to free the ancient deep thing.')
                        decision=input('L to let go, or G to gaffe')
                        if 'g' in decision.lower():
                            print('You quickly raise your arm and nail the old fish man in the \nside of the head with your trusty gaffer.\n He falls dead in the middle of the boat,\ndark green blood fills the middle of the boat.\nYou look down and are surprised to find that you have a very hard erection.')
                            pass
                        if 'l' in decision.lower():
                            print('\"Thank you, human. I shan\'t forget you. Please accept this gift.\"')
                            gift_of_the_merman=True
                    if merman['type']=='Drowner':
                        print('The creature stares at you with lidless eyes. It springs forward and knocks you out of the boat. \n You struggle to keep your head above water,\nbut to no avail, the creature\n has pulled you underwater and ended your life.\nI told you these things were dangerous.\nMaybe next time you\'ll listen to me.')
                        Quit=True
                    if merman['mername']=='Scilpion':
                        print('A terrible screeching noise bursts forth from the terrible things gaping maw.\n (T)hrow the beast back, or (G)affe it,\n but do something quick.')
                    if merman['mername']=='Sclaxion':
                        print('The creature seems to be hiding something behind it\'s back, back says nothing when questioned.')
                    if merman['mername']=='Thelzion':
                        pass
                    if merman['mername']=='Bilgo':
                        pass
                    if merman['mername']=='Goriel':
                        pass
                    
                    
        if 'm' in query.lower():
            print('\n\n\n','Let\'s move','\n\n\n\n')
            time.sleep(random.randint(0,5))
            print('We\'ll find a good spot sooner or later. I like the look of this new spot')
            fishLuck = luck()
            gas-=1
        if 'l' in query.lower():
            looking=True
            
            while looking==True:
                count=0
                if fishInboat==[]:
                    print('Empty Boat')
                    looking=False
                    pass
                else:
                
                    for fish in fishInboat:
                        count+=1
                        print(count,fish['name'],'  ',fish['weight'],'  ',fish['length'],'\n')
                    ####Merman Mini Game###
                    
                    
                    
                    query1=input('Would you like Throw anything into the water? \nSimply type the number to the left of the the item you\'d\nlike to throw overboard, and press enter, else\ntype 0 type 0 to stop looking in the boat.')
                ##Validate user input before stuff fish away
                    try:
                        int(query1)
                    except:
                        print('Sorry, I didn\'t get that.')
                    else:
                    
                        if int(query1) in range(count+1):
                            if int(query1)>0:
                                fishInboat.pop(int(query1)-1)
                        
                            else:
                                looking=False
                        else:
                            print('\n\n\n','Sorry, I didn\'t get that.','\n\n\n')
                
                        
                        
        if 'g' in query.lower():
            print(str(gas/4.0),'Gallons of Gas left in the tank')
        if 'd' in query.lower():
            pass
            
        if 'q' in query.lower():
            Quit=True
                
        #game rules
        if gas==0:
            print('We ran out of gas and forgot to bring an oar. Stranded in the middle of the lake.\n It\'s getting dark too. At least we\n spent the day fishing.Let\'s look at them one more time.')
            print('You caught',len(fishInboat))
            for fish in fishInboat:
                 print(fish['name'],'  ',fish['weight'],'  ',fish['length'],'\n')
            input('thanks for playing...press enter to Quit')
            Quit=True
main()
                    
            
                
                
    




    
    