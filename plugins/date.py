
from pyrogram import Client , Filters , Message
import requests , time
import jdatetime
from db import r

@Client.on_message(Filters.regex("^[Tt]oday$")& Filters.me)
def today(app : Client , msg : Message):


    r = requests.get("https://api.keybit.ir/time/").json()

    time = r["time24"]["full"]["en"]
    date_shamsi = r["date"]["full"]["official"]["iso"]["en"]
    month =  r["date"]["month"]["name"]
    weekday = r["date"]["weekday"]["name"]

    days_left = r["date"]["year"]["left"]["days"]["en"]
    
    day = r["date"]["day"]["name"]
    days = r["date"]["year"]["agone"]["days"]["en"]
    date_gregorian = r["date"]["other"]["gregorian"]["iso"]["en"]

    text = f"""
Time : **{time}**
Shamsi : **{date_shamsi}** |  **{weekday}** **{day}** **{month}**
Gregorian : **{date_gregorian}**
Day : **{days}**
DaysLeft : **{days_left}**
#Tkar
    """
    app.edit_message_text(
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        text = text,
    )

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
