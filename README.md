<p align="center">
  <img src="https://graph.org/file/d8a22e3cf962a098d2a6b.jpg" alt="File2Link-Bot Logo">
</p>
<h1 align="center">
  OP-File2Link-BOT
</h1>

![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=𝑊𝑒𝑙𝑐𝑜𝑚𝑒+𝑇𝑜+File2Link-Bot;𝐴+private+𝑎𝑛𝑑+𝑝𝑜𝑤𝑒𝑟𝑓𝑢𝑙+𝐵𝑜𝑡!;Send+𝐹𝑖𝑙𝑒𝑠+𝑎𝑏𝑜𝑣𝑒+2𝐺𝐵;𝐴+𝐵𝑜𝑡+𝑤𝑖𝑡ℎ+Stream+DL!;𝑆𝑡𝑎𝑟𝑡+𝑚𝑒𝑠𝑠𝑎𝑔𝑒+𝑤𝑖𝑡ℎ+𝑝𝑖𝑐!;𝐴𝑛𝑑+𝑚𝑜𝑟𝑒+𝑓𝑒𝑎𝑡𝑢𝑟𝑒𝑠!)
</p>

## 🍁 𝑨𝒃𝒐𝒖𝒕 𝑻𝒉𝒊𝒔 𝑩𝒐𝒕 :

<p align='center'>
    Tʜɪs ʙᴏᴛ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ sᴛʀᴇᴀᴍᴀʙʟᴇ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋs ғᴏʀ Tᴇʟᴇɢʀᴀᴍ ғɪʟᴇs ᴡɪᴛʜᴏᴜᴛ ᴛʜᴇ ɴᴇᴇᴅ ᴏғ ᴡᴀɪᴛɪɴɢ ᴛɪʟʟ ᴛʜᴇ ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴘʟᴇᴛᴇs.
</p>


## ♢ How to make your own :


#### ♢ Click on This Drop-down and get more details
<br>
<details>
  <summary><b>Deploy on Heroku:</b></summary>


<a href="https://youtu.be/lBJZdaA04Ig"><img src="https://img.shields.io/badge/Watch%20Tutorial%20On%20YouTube-red.svg?logo=Youtube"></a>

<h4> So Follow Above Video 👆 and then deploy other wise bot won't work</h4>

Press the below button to Fast deploy on Heroku/Raiwlay
Either you could locally host or deploy on [Heroku](https://heroku.com)
### 💜 Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy/)

<br>


then goto the <a href="#mandatory-vars">variables tab</a> for more info on setting up environmental variables. </details>

<details>
  <summary><b>Features:</b></summary>

<p>

🚀Features<p>
💥Superfast⚡️ download and stream links.<br>
💥No ads in generated links.<br>
💥Superfast interface.<br>
💥Along with the links you also get file information like name,size ,etc.<br>
💥Updates channel Support.<br>
💥Mongodb database support for broadcasting.<br>
💥Password Protection.<br>
💥User Freindly Interface.<br>
💥Ping check.<br>
💥User DC Check.<br>
💥Real time CPU , RAM , Internet usage. <br>
💥Custom Domain support. <br>
💥All unwanted code removed. <br>
💥A lot more tired of writing check out by deploying it.


and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

Setting up things

If you're on Heroku, just add these in the Environmental Variables
or if you're Locally hosting, create a file named `config.env` in the root directory and add all the variables there.
An example of `config.env` file:

```py
API_ID=12345
API_HASH=esx576f8738x883f3sfzx83
BOT_TOKEN=55838383:yourtbottokenhere
BIN_CHANNEL=-100
PORT=8080
FQDN=your_server_ip
OWNER_ID=your_user_id
DATABASE_URL=mongodb_uri
```
  </details>

<details>
  <summary><b>Vars and Details :</b></summary>

`API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`MY_PASS` : Bot PASSWORD

`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)

`BIN_CHANNEL` : Create a new channel (private/public), add [@missrose_bot](https://telegram.dog/MissRose_bot) as admin to the channel and type /id. Now copy paste the ID into this field.

`OWNER_USERNAME` : U should be knowing it afterall it's your username dont remember it? just go to settings!

`OWNER_ID` : Your Telegram User ID

`DATABASE_URL` : MongoDB URI for saving User IDs when they first Start the Bot. We will use that for Broadcasting to them. I will try to add more features related with Database. If you need help to get the URI you can click on logo below!

[![mongo](https://telegra.ph/file/fd68906852c71fdd68bef.jpg)](https://www.youtube.com/watch?v=HhHzCfrqsoE)

 Option Vars

`UPDATES_CHANNEL` : Put a Public Channel Username, so every user have to Join that channel to use the bot. Must add bot to channel as Admin to work properly.

`BANNED_CHANNELS` : Put IDs of Banned Channels where bot will not work. You can add multiple IDs & separate with <kbd>Space</kbd>.

`SLEEP_THRESHOLD` : Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds.

`WORKERS` : Number of maximum concurrent workers for handling incoming updates. Defaults to `3`

`PORT` : The port that you want your webapp to be listened to. Defaults to `8080`

`WEB_SERVER_BIND_ADDRESS` : Your server bind adress. Defauls to `0.0.0.0`

`NO_PORT` : If you don't want your port to be displayed. You should point your `PORT` to `80` (http) or `443` (https) for the links to work. Ignore this if you're on Heroku.

`FQDN` :  A Fully Qualified Domain Name if present. Defaults to `WEB_SERVER_BIND_ADDRESS` </details>

<details>
  <summary><b>How to Use :</b></summary>

:warning: **Before using the  bot, don't forget to add the bot to the `BIN_CHANNEL` as an Admin**

`/start` : To check if the bot is alive or not.

To get an instant stream link, just forward any media to the bot and boom, its fast af.

![image](https://user-images.githubusercontent.com/88939380/145798095-3cdad108-96b0-4391-a540-cad144d6b864.png)


### Channel Support
Bot also Supported with Channels. Just add bot Channel as Admin. If any new file comes in Channel it will edit it with **Get Download Link** Button. </details>

### Credits :

- [Adarsh Goel](https://github.com/adarsh-goel)
- [Me For Fix Errors](https://github.com/Angel-noori)
- Everyone In This Journey !
