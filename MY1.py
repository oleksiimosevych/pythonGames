#first programm in Py


famousProgrammers="Durov, Mosevych, Zukkerberg, Cuccerberg"

famousPersonsM=['Jobs','Musk']
famousPersonsW=['Opra Winfrie','Jessica Alba', 'Jennifer Aniston', 'Avril Lavigne']

puilo="Putin, Putyn, Puten, putin, putyn, pu, puten"

while(1==1): #break need
    #declaration of variables
    story='So here the story begins... '
    end="The End"
    nothing='nothing'
    timeNow = input('First of all we need to know what time is it now? Type from 0 to 24 \n')
    morningTime="5,6,7,8,9"
    dayTime="10,11,12,13,14,15,16,17"
    eveningTime = "18,19,20,21"
    nightTime= "22,23,24,00,1,2,3,4"
    bye="It is fantastic! Thanks for coming und using our program made by Alex/Oleksii Mosevych specially at 02.09.2019!\n"
    gameOver='Game Over... Try again later!\n'
    onceMore="Oh Wow! And what happen later?"

    #I will push it into function later
    if(timeNow in morningTime):
        time = 'Good morning! '
    elif(timeNow in dayTime):
        time = 'Good day! '
    elif(timeNow in eveningTime):
        time = 'Good evening! '
    elif(timeNow in nightTime):
        time = 'Good night! '
    else:
        print ("So it is impossible. \n", gameOver)
        break
        
    #the game
    print("Now we know the time! It is time for our Talk Show! Are you famous not? \n Lets start it! \n")
    name = input('What is your Surname? \n')
    if (name in famousProgrammers):
        print('Hello ', name, ' The greatest programmer of the world!\n Tell us your story')
        story+=input()
        
    i=0
    print(time , ' You are so famous!  \nPlease tell us about your life. \n \nIf you want to end the story you must write <The End>')
        
        
    while(i<99):
        if(name==famousPersonsM[i]):
            print('And what else can you tell us Mr. ', name, '? ')
            story+=input()
            
            if (end in story)or(nothing in story):
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
    if(name in puilo):
        print("Hell to you!")
        a=1
        while (a<10):
            print("PUTIN HUILO! LALA LLALA LAALA LALA!")
            a=a+1
            #playThatMusic
            #open youTube video agains pu)
    ending=input("If you want to know all the story type WHOLE STORY using UPPERCASE symbols. Thank you.")
    if(ending=='WHOLE STORY'):
        print(story)
        break
    elif(name=="exit"):
            break
    else:
        print('Who are you, Mr. '+name+'? This is the end of the game. Try again later!')
 

                
        
    
