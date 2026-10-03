from notify.interface import BaseNotificationSender
import pywhatkit as kit

class Whatsappsender(BaseNotificationSender):
    def send(self, recipient: str, message: str, time_hour: int, time_min: int) -> None:
        kit.sendwhatmsg(recipient,message,time_hour,time_min)
        print(f"📱  Message sended :  {message}")
        
