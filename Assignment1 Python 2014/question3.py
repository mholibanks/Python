#A programe that generates a personalized spam message
#26/02/2014
#Mholi Mncube

first_name=(input("Enter first name:\n"))
last_name=(input("Enter last name: \n"))
USD=eval(input("Enter sum of money in USD: \n"))
country=(input("Enter country name: \n"))
print()
import math
print("Dearest", first_name)
print("It is with a heavy heart that I inform you of the death of my father,\n"
      "General Fayk ", last_name, ", your long lost relative from Mapsfostol.\n"
      "My father left the sum of ",USD,"USD for us, your distant cousins.\n"
      "Unfortunately, we cannot access the money as it is in a bank in ", country,sep='', end='.')
print("\nI desperately need your assistance to access this money."
      "\nI will even pay you generously, 30% of the amount - ",USD*30/100,"USD,",
      "\nfor your help.  Please get in touch with me at this email address asap.",
      "\nYours sincerely"
      "\nFrank ", last_name, sep='')