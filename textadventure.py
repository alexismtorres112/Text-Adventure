s = "Student"

yes = "yes"

no = "no"


print("You're in your last class of the day when suddenly, a classmate asks if you've finished the 15-page, double spaced research paper you have due tonight, at 11:59 pm. You freak out and realize you've been pushing it off for a month now. Knowing your teacher, anything sent after 12:00 is late and points will be deducted. You can't wait for school to end at 3:20 and for you to get home and start writing.")
print("As you're getting ready to go home, you get a text from the president of the debate teamm that there's a mandatory meeting. It's from 3:30 to 4:30. If  you go, you won't be home till 5:00, but if you don't go, you won't be able to compete for the tournament on Saturday.")

answer1 = input("Should you go to the mandatory debate meeting? Yes or No?: ")
if answer1 == (yes):
    print("The meeting went well and you've secured a spot in the tournament, but now it's 5:00 and you JUST got home. Gotta start that 15-page research paper now!")
if answer1 == (no):
    print("The president of the debate team sees you leaving. He says that if you can't come to today's mandatory meeting, then you won't be able to participate in Saturday's tournamnent. You tell them that you'll be fine, since it's just one tournamnent anyways. You get home at 3:50! You eat first and start your essay at 4:00.'\n\n'")

print("You suddendly realize you can't find the prompt. You go on your phone and text your friend if they can send you a picture. '\n\n'")

answer3 = input("While waiting for your friend to send you a picture, should you stay on your phone and check your social medias? Yes or No?: ")
if answer3 == (yes):
    print("You check all your social medias and get so distracted that you forget that your friend already sent you the picture. You check the time and see that you wasted half an hour checking snaps and liking posts on instagram. You put your phone away and start typing your essay. \n\n")
if answer3 == (no):
    print("You decide to put on music to help you focus. After getting a picture of the prompt, you go straight to work. '\n\n'")

if answer1 == (yes) and answer3 == (yes):
    print("It's now 8:00 pm and you have only 4 pages done. Still have a long way to go.")
if answer1 == (no)and answer3 == (yes):
    print("It's now 8:00 pm and you have 6 pages done. That's almost halfway to go! ")
if answer1 == (yes) and answer3 == (no):
    print("It's now 8:00 and you have 5 pages done. That's not that bad.")
if answer1 == (no) and answer3 == (no):
    print("It's now 8:00 and you have 7 pages done! Halfway there!")


answer2 = input("Your dad calls you and tells you that dinner is ready. Should you take a break and eat dinner? Yes or No?: ")
if answer2 == (yes):
    print("You eat dinner with your family for about 30 minutes and go straight back to work.")
if answer2 == (no):
    print("Your mom brings you dinner and then asks you how you're doing. You tell them that you're busy working on a paper and they ask when you were given the assignment. They start lecturing you on time management and then compares their highschool self to you. After about what feels like forever, they leave you alone and you realize that you lost 10 minutes.")
    print("After eating your dinner, you bring your dirty dishes to the kitchen. While about to leave, your mom sees you and gets mad that you didn't wash your dishes. You tell her that you'll do it tomorrow morning because you're really busy, but she gets mad and makes you do it now. You get so mad that you drop a glass cup. You lose an extra five minutes after having to both wash the dishes and clean the glass off the floor.")

if answer2 == (yes) and answer1 == (yes) and answer3 == (yes):
    print("You've wasted so much time! It's 10:00 and you only have 7 pages done. You're finally halfway done but you only have two hours to go.")
if answer2 == (no) and answer1 == (no) and answer3 == (no):
    print("You may have procrastinated till the last minute to this research ppaer, but you're on your way to being done. It's 10:00 and you have 10 pages! Only five more to go!")

answer4 = input("'\n\n'Oh no! Your phone is buzzing with a million texts from your best friend. You try to ignore her so you can focus on your work. It's almost 11. You're under time pressure! Then, she calls you. She never calls unless major drama is happening. You pick up the phone and you hear her crying. Her boyfriend of two years was cheating on her and they just broke up. You try and type as you talk to her but you can't focus. Should you stay on the phone with her and comfort her? Yes or No?: ")

if answer4 == (yes):
    print("'\n\n'You stay on the phone and comfort your best friend. She explains to you the whole story and then midway, she says that she can't say anymore and just wants to sleep. You promise her that tomorrow, you and her will hang out and do anything she wants. She thanks you for being such an amazing best friend. During your phone call with her, you were only able to write one page.")
if answer4 == (no):
    print("'\n\n'You tell your friend that you're writing your paper. She cries even harder and you decide to stay on the phone but while continuing your paper. Your best friend explains to you what happened, but you become so focused on writing your paper that you're not even listening to her. She gets mad that you're not listening and says that she'll go talk to someone else if she's being such a bother. You try and go back to listening but she hangs up.")
print("'\n\n'As the time gets closer to 11:59pm, you work even harder and type faster than before. This research paper is 15 percent of your grade!")

if answer2 == (no) and answer1 == (no) and answer3 == (no) and answer4 == (no):
    print("'\n\n'You finished! All 15 pages complete with even the work cited page and you have 20 minutes till it's due. You try and look over as many pages as you can to make sure it all makes sense. You submit your paper in at 11:56 pm! CONGRATULATIONS!Although, you should probably call your best friend now.")

if answer2 == (yes) and answer1 == (yes) and answer3 == (yes) and answer4 == (yes):
    print("'\n\n'It's 11:59 pm and you don't have all 15 pages done. You can't submit an incomplete assignment so you accept the fact that your paper will be late and that half a letter grade will be taken off. Since it's already late, you no longer rush and just take your time. You'd rather submit an amazing essay late than a crappy essay on time! At least you have were there for her best friend when she needed you the most!")

if answer2 == (no) and answer1 == (yes) and answer3 == (yes) and answer4 == (no):
    print("'\n\n'It's 11:57 and all you need is to finish citing your last source and submit your paper! CONGRATULATIONS! You made it with just seconds to spare. You should probably call your best friend now, though...")
if answer2 == (no) and answer1 == (no) and answer3 == (no) and answer4 == (yes):
    print("'\n\n'You finished in time! You submitted it with five minutes left till 11:59 pm! You may not have gone to the mandatory debate meeting and got a lecture from your mom, at least you finished in time! That, and you were able to be there for your best friend when she needed you most.")
