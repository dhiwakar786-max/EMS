from notify.interface import BaseNotificationSender
import pywhatkit as kit

class Whatsappsender(BaseNotificationSender):
    def send(self, recipient: str, message: str) -> None:
        kit.sendwhatmsg(recipient,message)
        print(f"📱  Message sended :  {message}")
        
