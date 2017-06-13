# Name: Justin Farris
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
#I did the movie choice extension.

name_ask = raw_input ("What's your name")
print name_ask


age_ask = int(raw_input ("What's your age"))
print age_ask

#year100 = 100-int(age_ask) + 2017


bday_ask = raw_input ("Did you have a birthday this year? Answer Yes or No.")




if bday_ask == "No":
    total = 2016
else:
    total =  2017

while age_ask < 100:
    total = total + 1
    age_ask = age_ask + 1




year100 = total



print bday_ask

print "You will be 100 in " + str(total) #str(year100)

if age_ask >10:
    print"You can watch G movies."

if age_ask >13:print "You can watch pg movies"

if age_ask >17 :print "you can watch pg-13 movies"

if age_ask <17:print "you can watch R movies"
