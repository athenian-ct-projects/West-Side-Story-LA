print("""
This is a game/quiz for the West Side Story focus day. 
You will be asked some general questions and some personal questions. 
For the general questions (like answer yes or no, or answer 1 or 2) you will need to type it exactly how it is presented, 
capital letters are not needed and don't use them. At the end there will be a collective list of the questions you answered. 
Feel free to take a picture with a phone or iPad. This information is very useful and a good thing to study. If there is a 
syntax error you will need to restart. Thanks and enjoy!

by LA '23
""")

def lineyn():
    print("Do you know all your lines?")
    knowlines = input("Answer yes or no: ")
    return knowlines
#---Today is November 19
endlist = ["You will enter on: ","You will be feeling: ","You will be exiting on: ","One of your lines is:","Your cue for this line is: "]
#^This is the base of the end list, many more things will be added to this later on
print("Hey performer! The big day is coming up and we are going to get prepared! Let's go!")
knowlines = lineyn()
#---Today is November 20
while knowlines == "no":
    print("Wrong answer. Charlie won't be happy, tisk tisk.")
    knowlines = lineyn()
#This is a continuous loop that keeps asking you if you know your lines until you say yes. On the day of WSS hopefully everyone will know all their lines
if knowlines == "yes":
    print("Alright, go you. Here is a very important question:")
    print("Do you know when you have to say each line? Like who says what before your line?")
knowques = input("Answer yes or no: ")
#---This is now pt. 2 so I'm ahead of schedule. I will probably come back later and add a function and add things to a endlist
if knowques == "no":
    print("This part of line memorization is almost more important than the lines its self. Learn these well!") 
    print("\n")
    proveit = input("Type out one of your lines (maybe choose your longest one or one that you often forget if you have multiple): ")
if knowques == "yes":
    print("Wow you are very prepared! Prove it.")
    print("\n")
    proveit = input("Type out one of your lines (maybe choose your longest one or one that you often forget if you have multiple): ")
#These if statements are for two different responses to how they answer to the cue question. Both responses go to the same spot in the end
endlist.insert(4,proveit)
#This is the first addition to the end list
print("Nice. Now, in general, tell me what comes before this line.")
proveque = input("This could be the end of a number or song or the actual line that comes before: ")
endlist.insert(6,proveque)
print("Good job. Do you want to practice more lines or continue? I highly recommend practicing more if you have lots of lines.")
#---Today is November 21
morepractice = input("Answer 1 to continue or 2 to practice more lines: ")
while morepractice == "2":
    endlist.insert(7,"One of your lines is: ")
    proveit2 = input("Type out another line: ")
    endlist.insert(8,proveit2)
    endlist.insert(9,"Your cue for this line is: ")
    proveque2 = input("In general, tell me what comes before this line: ")
    endlist.insert(10,proveque2)
    morepractice = input("Do you want to practice more lines or continue? Answer 1 to continue or 2 to practice more lines: ")
    if morepractice == 2:
        endlist.insert(11,"One of your lines is: ")
        proveit2 = input("Type out another line: ")
        endlist.insert(12,proveit2)
        endlist.insert(13,"Your cue for this line is:")
        proveque2 = input("In general, tell me what comes before this line: ")
        endlist.insert(14,proveque2)
        morepractice = input("Do you want to practice more lines or continue? Answer 1 to continue or 2 to practice more lines: ")
    if morepractice == 2:
        endlist.insert(15,"One of your lines is:")
        proveit2 = input("Type out another line: ")
        endlist.insert(16,proveit2)
        endlist.insert(17,"Your cue for this line is:")
        provecue2 = input("In general, tell me what comes before this line: ")
        endlist.insert(18,proveque2)
        morepractice = input("Do you want to practice more lines or continue? Answer 1 to continue or 2 to practice more lines: ")
    if morepractice == 2:
        endlist.insert(19,"One of your lines is:")
        proveit2 = input("Type out another line: ")
        endlist.insert(20,proveit2)
        endlist.insert(21,"Your cue for this line is:")
        provecue2 = input("In general, tell me what comes before this line: ")
        endlist.insert(22,proveque2)
        morepractice = input("You have practiced enough lines. Go you! Now let's move on. Type 1 to continue: ")
#These were all for the lines and cues. Not all will necessarily be used but they are here if the player chooses to type out many lines
print("\n")
print("Good job with your lines!! Now let's talk about another thing that is very important. This is your entrances and exits.")
print("Quiz!! Think of your first scene. This could be a scene with only lines or this could be the opening number.")
firstscene = input("What is the first time you go on stage? ")
#---Today is over and this is the end if pt.2 I am exactly on schedule. Go me!
#---Today is Sunday and I'm going to work a bit so I get ahead.
endlist.insert(0,"Your first scene is: ")
endlist.insert(1,firstscene)
print("If there is a scene before this you should be ready, in costume, and prepared to go on stage while that scene is going on.")
enter = input("What side do you enter from? ")
endlist.insert(3,enter)
#---End of pt. 3
#---Today is Dec. 3 and I'm continuing to work on pt. 3/4 because they overlap a bit
print("What emotions is your character feeling in this scene/number?")
emotions = input("This could be like frustration, excitement, love etc. ")
endlist.insert(5,emotions)
exit0 = input("Where do you exit? ")
endlist.insert(7,exit0)
morescenes = input("Do you have any more scenes? yes or no: ")
#This is the first scene, entrance, emotion, and exit they enter. All this information is added to the end list
if morescenes == "yes":
    endlist.insert(8,"Your next scene is: ")
    scene2 = input("Your next scene is: ")
    endlist.insert(9,scene2)
    enter2 = input("You will enter at: ")
    endlist.insert(10,"You will enter on: ")
    endlist.insert(11,enter2)
    emotions2 = input("What will you be feeling? ")
    endlist.insert(12,"You will be feeling:")
    endlist.insert(13,emotions2)
    exit2 = input("You will be exiting on: ")
    endlist.insert(14,"You will be exiting on: ")
    endlist.insert(15,exit2)
    morescenes2 = ("Do you have any more scenes? yes or no: ")
    if morescenes2 == "yes":
        endlist.insert(16,"Your next scene is: ")
        scene2 = input("Your next scene is: ")
        endlist.insert(17,scene2)
        enter2 = input("You will enter at: ")
        endlist.insert(18,"You will enter on:")
        endlist.insert(19,enter2)
        emotions2 = input("What will you be feeling? ")
        endlist.insert(20,"You will be feeling:")
        endlist.insert(21,emotions2)
        exit2 = input("You will be exiting on: ")
        endlist.insert(22,"You will be exiting on:")
        endlist.insert(23,exit2)
        morescenes3 = ("Do you have any more scenes? yes or no: ")
        if morescenes3 == "yes":
            endlist.insert(24,"Your next scene is:")
            scene2 = input("Your next scene is: ")
            endlist.insert(25,scene2)
            enter2 = input("You will enter at: ")
            endlist.insert(26,"You will enter on:")
            endlist.insert(27,enter2)
            emotions2 = input("What will you be feeling? ")
            endlist.insert(28,"You will be feeling:")
            endlist.insert(29,emotions2)
            exit2 = input("You will be exiting on: ")
            endlist.insert(30,"You will be exiting on:")
            endlist.insert(31,exit2)
#They have the option of adding/practicing more scenes. Again these will be added to the end list
#---End of pt.4 I won't be working tomorrow so I'm on schedule
print("Good job! Be sure to keep your costume on for bows.")
print("\n")
print("Very important question,")
jetshark = input("Are you a jet or a shark? ")
if jetshark == "jet":
    print("Right answer! Jets until your last dying day!!")
    print("\n")
if jetshark == "shark":
    print("Wow. I don't know if I will be able to look past that. Moving on.")
    print("\n")
#This is just a fun interactive part to get the student into the rival-mood for the show
#---This is the end of pt.5 I am very ahead of schedule
print("Be sure to have as much hatred as you")
print("can for the other gang. You must believe")
print("you are superior even if you are a Shark.")
print("Imagine that person you hate the most is")
print("the other gang. Have this mindset the")
print("the whole show.")
#More advice/mood setting
goon = input("Type 1 to go on: ")
print("\n")
print("Ok. The time is near and you are going to do great! Here are a few things to remember: ")
print("\n")
y = len(endlist)
x = 0
while x < y:
    print(endlist[x])
    x = x + 1
print("\n")
#That is where the end list is printed vertically so you can see it without needing to scroll. This is so you can take a picture and study this
goodluck = "good luck"
x = 0
for i in goodluck:
    x = x + 1
    print(goodluck[0:x])
for i in goodluck:
    x = x - 1
    print(goodluck[0:x])
#This is just a fun graphic wishing good luck

