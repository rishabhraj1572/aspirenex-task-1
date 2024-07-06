import cv2
from PIL import Image
import os
import pygame
import pyautogui
import pywhatkit
from datetime import datetime
from functions.emailsender import send_email
import subprocess 

email_addresses = {
    'myself': 'rishabhpao2012@gmail.com',
    }

def bot(msg):
    print("Bot :",msg)


def run():

    count = 0

    bot('Hello sir, I am Neo and How can i help you today?')

    while True:
        query = input('\nYou: ')
        # print('\nYou: ' + query)

        if 'open' in query:
            app_name = query.replace('open', '')
            bot('opening ' + app_name)
            pyautogui.press('super')
            pyautogui.typewrite(app_name)
            pyautogui.sleep(1)
            pyautogui.press('enter')
        
        if 'Hello' in query  or 'hello' in query or 'hi' in query or 'Hi' in query:
            bot('Hello! How can I assist you today?')

        elif 'write a note' in query or 'take a note' in query or 'take note' in query  or 'write note' in query:
            write_note()

        elif 'take picture' in query or 'take pictures' in query  or 'click pictures' in query or 'click picture' in query or 'take a picture' in query:
            bot('Taking Picture')
            bot('Smile Please')
            take_picture()
            bot('Done')
            y=input('Do you want to see the image ? (yes/no) : ')
            if 'yes' in y:
                open_image()
            elif 'no' in y:
                pass
            else:
                pass

        elif 'weather' in query or 'temperature' in query:
            from weather import weather,get_ip_location
            bot(f'current temperature in {get_ip_location()} is {weather(get_ip_location())}°C')
        
        elif 'show picture' in query or ' show image' in query or 'show pictures' in query or 'show my picture' in query:
            try:
                open_image()
            except:
                bot('No picture available')
            

        elif 'play' in query:
            song_name = query.replace('play', '')
            bot('Playing ' + song_name + ' in youtube')
            pywhatkit.playonyt(song_name)

        elif 'switch tab' in query:
            pyautogui.hotkey('ctrl', 'tab')

        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')

        elif 'close' in query:
            pyautogui.hotkey('alt', 'f4')
            bot('done sir')

        elif 'time' in query:
            current_time = datetime.now().strftime('%H:%M %p')
            bot(f'Current time is {current_time}')
        
        elif 'date' in query:
            current_date = datetime.now()
            formatted_date = current_date.strftime('%d %B, %Y')
            bot("Today's "+f'date is {formatted_date}')

        elif 'write an email' in query or 'compose an email' in query or 'send an email' in query or 'send email' in query:
            bot('Sure sir, Can you provide me the name of the user to whom you want to send email: ')
            name = input("Enter Name of the Contact : ")
            try:
                email_address = get_email_address_by_name(name)
                print("Email : "+email_address)
            except:
                bot(f"No Contact with contact name {name}")
            
            if email_address is not None:
                bot('What should be the subject of the email?')
                subject = input("Subject : ")
                bot('What should be the content?')
                email_prompt = input("Content : ")
            
                send_email(email_address, subject, email_prompt)
                
                bot(f'Done sir. Email sent successfully to {name}')
            else:
                try:
                    bot('Sorry, the provided name is not in the list. Please manually enter the email address.')
                    receiver = input('Enter the email address: ')
                    bot('What should be the subject of the email?')
                    subject = input("Subject : ")
                    bot('What should be the content?')
                    email_prompt = input("Content : ")
                    
                    send_email(receiver, subject, email_prompt)
                
                    bot(f'Done sir. Email sent successfully to {receiver}')
                except:
                    bot('Email not sent')
                    pass
       
        elif 'identify the object' in query or 'what is this' in query or 'identify' in query:
            bot('Sure sir, show item in the camera')
            from identify import detect_object_from_image

            if __name__ == "__main__":
                cap = cv2.VideoCapture(0)
                ret, frame = cap.read()
                cv2.imwrite("captured_image.jpg", frame)
                cap.release()

                detected_item = detect_object_from_image("captured_image.jpg")

                if detected_item:
                    bot(f"Detected Item: {detected_item}")
                else:
                    bot("No item detected.")  
                # sleep_mode = True  
            
        elif 'take screenshot' in query or 'screenshot' in query or 'screen shot' in query:
            bot('Taking Screenshot...')
            screenshot = pyautogui.screenshot()
            screenshot.save('screenshot.png')
            bot('Screenshot Saved successfully')
            bot('do you want to see thre screenshot?')
            q = input("Do you want to see the screenshot ? (yes/no) : ")
            if 'yes' in q:
                try:
                    from PIL import Image
                    bot('opening screenshot')
                    image_path = 'screenshot.png'

                    image = Image.open(image_path)

                    image.show()
                except:
                    bot('error in opening')
            # sleep_mode = True
    

        elif query == 'show screenshot' or query=='showscreenshot':
            try:
                from PIL import Image
                bot('opening screenshot')
                image_path = 'screenshot.png'

                image = Image.open(image_path)

                image.show()
            except:
                bot('error in opening')
            # sleep_mode = True

        elif 'good bye' in query or 'bye bye' in query or 'goodbye' in query or 'byebye' in query or 'bye' in query or 'exit' in query:
                bot('have a good day sir.')
                exit()

        else:
            count = count +1

            if(count<5):
                bot("sorry I don't know that one, Please try again...")
            else:
                bot("Number of wrong Attempts Exceeded")
                print("Exitting...")
                exit()


def get_email_address_by_name(name):
    return email_addresses.get(name, None)

def get_phone_num_by_name(name):
    return phone_numbers.get(name, None)

def write_note():
    bot("What would you like to write in the note?")
    
    note_content =  (input("Enter Note Content : "))
    
    note_filename = "note.txt"
    with open(note_filename, "w") as note_file:
        note_file.write(note_content + "\n")
    
    bot("Note written successfully. Opening notepad.")
    
    subprocess.Popen(["notepad.exe", note_filename])

def take_picture(file_path='captured_image.jpg'):
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    cv2.imwrite(file_path, frame)

    cap.release()

    bot(f"Picture taken and saved as {file_path}")

def open_image(file_path='captured_image.jpg'):
    image = Image.open(file_path)
    image.show()

run()
exit()
