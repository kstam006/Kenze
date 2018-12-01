mylist=[]
variables = ["an adjective", "a name", "a body part.", "an adjective", "a noun", "an article of clothing.", "a number greater than one.", "a plural noun.", "an adjective.", "your name.", "an adverb.", "a theme.", "a place.", "a day of the week.", "a time.", "a verb.", "an animal.", "a contact number."]

for x in variables:
	hustlethese = raw_input("Enter " + x + ". ")
	mylist.append(hustlethese)
	
print (mylist[2])

print "Signs point to a very " + (mylist[0])+ " yes. "
print "Signs point to a very " + (mylist[3]) + " no. "
print " Don't believe anything " + (mylist[1]) + " says." 
print "What does your " + (mylist[2])  + " tell you?" 
print "Picture a blue " + (mylist[4]) + ". That is your answer. "
print "You will find the answer in your " + (mylist[5]) + "." 
print "I see " + " big " + (mylist[7]) + " in your future. " 
print "The skies are " + (mylist[8]) + ". The future is uncertain. "
print " Dear " + (mylist[9]) + ", You are " + (mylist[10]) + " invited!"
print (mylist[9]) + (mylist[11]) + " party! "
print " It's going to be at " + (mylist[12]) + " on " + (mylist[13]) + ". " 
print " Please make sure to show up at " + (mylist[14]) + ", or else you will be required to " + (mylist[15]) + " a/an " + (mylist[16]) + " with your " + (mylist[2]) + "." 
print " RSVP at " + (mylist[17]) + "."
