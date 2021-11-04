import os
from collections import Counter
from email.parser import Parser
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#---------------Functions---------------#

#This funcitons analysys the emails and inputs to given lists
def email_analyse(inputfile, to_email_list, from_email_list, email_body):
    with open(inputfile, "r") as f:
        data = f.read()

    email = Parser().parsestr(data)
    if email['to']:
        email_to = email['to']
        email_to = email_to.replace("\n", "")
        email_to = email_to.replace("\t", "")
        email_to = email_to.replace(" ", "")

        email_to = email_to.split(",")

        for email_to_1 in email_to:
            to_email_list.append(email_to_1)
    from_email_list.append(email['from'])

    email_body.append(email.get_payload())

#Funciton to print given datasets to given filename to a CSV
def CSVPrint(filename,email_list):
   with open(filename, "w") as f:
    for to_email in email_list:
        if to_email:
            f.write(to_email)
            f.write("\n") 
#---------------Functions---------------#

#---------------Main Method---------------#

#Asks user for a specific name in the dataset, since going through the whole dataset whould take days
userinput = input("Please give us a user in the enron emails you will like to look at:")
rootdir = "maildir\\" + userinput #

print("\nBelow are the categorization of emails and how many were sent in each for " + userinput + "\n")
for directory, subdirectory, filenames in  os.walk(rootdir): #Used to see how many files each of the directories in the persons email dataset has
    print(directory, subdirectory, len(filenames))

#lists to show who the emails was sent, to who , and also the body
to_email_list = []      
from_email_list = []
email_body = []

for directory, subdirectory, filenames in  os.walk(rootdir):    #Analysys each of the emails
    for filename in filenames:
        email_analyse(os.path.join(directory, filename), to_email_list, from_email_list, email_body )


#Prints to the the CSV files 
CSVPrint("to_email_list.txt",to_email_list)
CSVPrint("from_email_list.txt",from_email_list)
CSVPrint("email_body.txt",email_body)


#Used to print the top 10 common email addresses that the given user send emails too
print("\nThese are the top 10 addresses that " + userinput + " sent emails to\n")
for x in Counter(to_email_list).most_common(10):
    print(x)

#Used to print the top 10 common email addresses that the given user received emails from
print("\nThese are the top 10 addresses that " + userinput + " received emails from\n")
for x in Counter(from_email_list).most_common(10):
    print(x)


#---------------Main Method---------------#
