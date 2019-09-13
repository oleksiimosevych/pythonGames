#first programm in Py
#ARE YOU FAMOUS? TALK SHOW v.3.0

#functions
class ShowTime:
    self.story='So here the story begins...' 
    self.end="The End"
    self.nothing='nothing'
    self.bye="It is fantastic! Thanks for coming und using our program made by Alex/Oleksii Mosevych specially at 02.09.2019!\n"
    self.gameOver='Game Over... Try again later!\n'
    self.onceMore="Oh Wow! And what happen later?"
    self.famousProgrammers=['Durov', 'Mosevych', 'Zukkerberg', 'Cuccerberg']
    self.famousPersonsM=['Jobs','Musk']
    self.famousPersonsW=['Opra Winfrie','Jessica Alba', 'Jennifer Aniston', 'Avril Lavigne']
    self.puilo=['Putin', 'Putyn', 'Puten', 'putin', 'putyn', 'pu', 'puten']    

    
    def autoSetTime(self):
        morningTime="5,6,7,8,9"
        dayTime="10,11,12,13,14,15,16,17"
        eveningTime = "18,19,20,21"
        nightTime= "22,23,24,00,1,2,3,4"

    def __init__(self):
        print('I am A of the class. I was called..from Time as test')

    def setTime(self, timeNow):
        timeNow = input('First of all we need to know what time is it now? Type from 0 to 24 \n')

        
    def whatTimeIsItNow(self, timeNow):
        if(timeNow in morningTime):
            time = 'Good morning! '
        elif(timeNow in dayTime):
            time = 'Good day! '
        elif(timeNow in eveningTime):
            time = 'Good evening! '
        elif(timeNow in nightTime):
            time = 'Good night! '
        else:
            print ("There is no such time. \n")
            setTime()    
            #restart here but how... I know . I have to call a function. I need to learn how to create functions...
        print("Now we know the time! It is time for our Talk Show! Are you famous or not? \n Lets start it! \n")

        return time
    
f=ShowTime()
print(f)
#f.setTime()


#print(a)
#declaration of variables
    
    
    

#loop...
while(1==1): #break need
    

    #I will push it into function later
    #I want to create another file for this... is it possible?)
            
    #the game
    #settime(timeNow)
    
    
    name = input('What is your Surname? \n')
        
    i=0
    print(time , ' You are so famous!  \nPlease tell us about your life. \n \nIf you want to end the story you must write <The End>')
        
        
    while(i<99):
        if name == famousProgrammers[i]:
            print('Hello ', name, ' The greatest programmer of the world!\n Tell us your story')
            #REPLACE.. this must be a callable function.. else too much code.
            story+=input()
            if (end in story)or(nothing in story):
                break
            else:
                print(onceMore)
                story+= input()
            #until here
                
        elif name==famousPersonsM[i]:
            print('And what else can you tell us Mr. ', name, '? ')
            story+=input()
            
            if end in story or nothing in story:
                break
            else:
                print(onceMore)
                story+= input()
        elif(name==famousPersonsW[i]):
            print('And what else can you tell us Mrs. ', name, '? Have I already told you how goodlooking you are today? So tell us more! ')
            story=input()
            if (end in story):
                print("It was fantastic! Thanks for coming und using our program made by Alex/Oleksii Mosevych specially at 02.09.2019!")
                break
            else:
                print('It is very interesting, Mrs. ', name, '! So tell me more! ')
                story=input()
        elif name == puilo[i]:
            print("Hell to you!")
            a=1
            while (a<10):#9 times
                print("PUTIN HUILO! LALA LLALA LAALA LALA!")
                a=a+1
                #playThatMusic
                #open youTube video agains pu)

    ending=input("If you want to know all the story type WHOLE STORY using UPPERCASE symbols. Thank you.")
    if ending=='WHOLE STORY':
        print(story)
        break
    elif(name=="exit"):
        break
    else:
        print('Who are you, Mr. '+name+'? This is the end of the game. \nTry again later!')
        break

            
