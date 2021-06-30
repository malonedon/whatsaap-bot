
import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

import time
date_time=time.localtime()
year=date_time[0]
month=date_time[1]
day=date_time[2]
time=str(date_time[3])+":"+str(date_time[4])



load_dotenv()

app = Flask(__name__)
TWILIO_SID = "ACaffe33385ebba23a9fb41bd774e87d2e"
TWILIO_AUTHTOKEN = "c414743106c28a6c0d542c3a7dd425e5"
client = Client(TWILIO_SID,TWILIO_AUTHTOKEN)

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/message', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
    if message == "link":
        return respond(f"https://console.twilio.com/us1/billing/manage-billing/upgrade?frameUrl=%2Fconsole%2Fbilling%2Fupgrade%3F__override_layout__%3Dembed%26bifrost%3Dtrue%26x-target-region%3Dus1") 


    
    if message == "hy" or "hi" or "hello":
        return respond(f"Welcome to the official Ministry of Health and Child Care Zimbabwe Typhoid Conjugate Vaccine support service\n"+str(day)+" "+str(month)+" "+str(year)+" "+str(time)+"\nThe right infomation is important.This service provides infomation on the typhoid conjugate vaccination campaign\nWhat would you like to know typhoid vaccinnation?.\nReply with a key word in bold to get the  infomation you need\n vaccine\n child details\n vaccination centers \n symptoms \n basic infomation \n Wellness tips \n Covid19 \n Share this service.." )
    if message == "what is typhoid" or "typhoid":
        return respond(f"typhoid fever is a life threatning infection caused by the bacteriumsalmonella typhi.It is ussually spread through contanimated food or water.")
    header="Welcome to the official Ministry of Health and Child Care Zimbabwe Typhoid Conjugate Vaccine support service\n"
    date="+str(day)+" "+str(month)+" "+str(year)+" "+str(time)\n"
    header2="The right infomation is important.This service provides infomation on the typhoid conjugate vaccination campaign\n"
    question="What would you like to know about typhoid vaccinnation?.\n Reply with a key word in bold to get the  infomation you need\n"


    basic_infomation=header+header2+date
    if message == "vaccine\n":
        return respond("""1.Vaccines are safe and effective-Any licenced vaccine is rigously tested before it is approved for use
                        \n-It is reguraly reassed
                        \n-it is also monitored for side effects
                        \n2. Vaccines prevent deadly illnesses
                        \n-Vaccines protect children from diseases like measles(gwirikwiti
                        \n-polio
                        \n3.Vaccines provide better immunity than natural infections:
                        \n-the immune response to vaccines is similar to the one produced by natuarl infections but is less risky
                        \n4.Combined vaccines are safe and beneficial
                        \n-Giving several vaccines at the same time has no effects on the childs health
                        \n5. If we stop vaccination with better hygiene,diseases will return.
                        \nwhen people are not vaccinated,infectious diseases that have become uncommon will quickly reappear.
                        """) 
    if message == "symptoms":
        return respond(f"common signs and symptoms include\n persistent high fever\n sweeting \n headache \n abdominal discomfort \n loss of appetite \n diarrhea or constipation \n nausea \n general body weakeness \n if untreated typhoid can result life threatening intestinal bleeding and perfoation,hepatitis,mental problems and infections of the lungs and heart")
    if message == "vaccination centers":
        return respond(".......................................................")
    
    if message == "Hygine tips":
        return respond("wash your hands throughly with soup and running water\nTry to eat your whilst its hot\n") 
    if message == "covid19":
        return respond("Contact this number for mor infomation on Covid19 0714734593") 
    if message == "share_this_service":
        return respond("For all who want to know about Typhoid vaccination") 

    if  message == "what is typhoid vaccination" or "vaccination" or "immunisation":
        return respond(f"typhoid vaccination is vaccination against typhoid.it is given to prevent your child from typhoid in case/in cases where the child is exposed to contamneted food or water.")
    if message == "where can i get vaccinated" or "where can i get treated" or "treated":
        return respond(f"At any clinic or hospital near you.Where do you stay ?.")
    if message == "Vaccination is for what age" or "age of vaccination" or "age":
        return respond(f"it is for children aged between 9 months and below 15 years")
    if message == "what are the benefits of vaccination":
        return respond(f"your child is protected in the event of a typhoid outbreak")
    if message == "what are the side effects of this vaccine" or "effects of vaccine" or "effects":
        return respond(f"visit your nearest clinic or hospital for checkup if you suspect any side effects")
    if message == "how long does the vaccine last" or "vaccine duration":
        return respond(f"visit your nearest clinic or hospital for vaccine duration they will assist and give you more infomation")
    if message == "if i have been vaccinated before when do i need to get vaccinated again" or "when do i get vaccinated":
        return respond(f"You will be notified by the ministry of health and child care,or at your nearest clinic.")
    if message == "Are there any effects of being vaccinated twice" or "effects of being vaccinated":
        return respond(f"No but you should only be vacinated once.")
    if message == "what are the symptoms of typhoid fever" or "symptoms":
        return respond(f"common signs and symptoms include\n persistent high fever\n sweeting \n headache \n abdominal discomfort \n loss of appetite \n diarrhea or constipation \n nausea \n general body weakeness \n if untreated typhoid can result life threatening intestinal bleeding and perfoation,hepatitis,mental problems and infections of the lungs and heart")
    if message == "how is the vaccine administered" or "administered":
        return respond(f"it is administerd by injection into the left thigh for children under five years and left upper arm for children above five years.")

    if message == "what else do i need to do after vaccination" or "after vaccination":
        return respond(f"Remember after vaccination against typhoid it remains important to mantain good personal and food hygene by drinking boiled or treated water,washing hands with soup before eating and after using the toilet,eating food whilst hot and getting early treatment if you or family member is sick")
                
    if message == "i have been vaccinated for covid19 do i need to be vaccinated for typhoid" or "do i need to be vaccinated":
        return respond(f"Yes you need to be vaccinated")
    if message == "will the covid19 vaccine affect typhoid vaccine":
        return respond(f"No it does not")
    if message == "where can i get more infomation on vaccines" or "more infomation":
        return respond(f"At your nearest clinic or call the ministry of health toll free number 2019,393")


if __name__=="__main__":
    app.run()
