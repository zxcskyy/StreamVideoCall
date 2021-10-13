

<h1 align="centre">Woofie Video Stream  🎵</h1>

### A bot that can play music on Telegram Group and Channel Voice Chats
#### POWERED BY [PYTGCALLS](https://github.com/pytgcalls/pytgcalls)
### Available on telegram as [@mailmusicbot](https://t.me/mailmusicbot)

## ✨ Features
- Stable video streaming
- Clear video & audio quality
- Support youtube live streaming
- Support youtube video streaming
- Support streaming video from mp4 video/file video
- Join & Leave command for assistant
- Support inline search video
- Support youtube search video link
- Support PornHub direct link streaming 🔞
- Video downloader feature
- Song downloader feature
- Have many other interesting features

## 🛠 Commands:
- ``/vplay`` (reply to video/give yt url) - to start video streaming
- ``/vstop`` - to stop video streaming
- ``/song`` (song name) - to download song
- ``/vsong`` (video name) - to download video
- ``/lyric`` (query) - lyric scrapper
- ``/alive`` - check the bot alive status
- ``/ping`` - check the bot ping status
- ``/uptime`` - check the bot uptime status
- ``/sysinfo`` - show the bot system information

## 🧙🏻‍♂️ Sudo Only:
- ``/rmd`` - clear all downloaded files
- ``/rmw`` - clear all downloaded raw files

📝 Note: From now, /vstream & /vstop command can only be used by group admins.

## 🧪 Get SESSION_NAME from below:

TAP THIS: [![Run on Repl.it](https://repl.it/badge/github/ChankitSaini/GenerateStringSession)](https://replit.com/@ChankitSaini/GenerateStringSession)

## 💜 Deploy To Heroku
The easy way to host this bot, deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/W29F/WoofVideoStream)

## 🌀 Run On Workflows

- fork this repository
- Go to your forked repository settings
- Scroll down and select the `secrets` tab
- Click on `New repository secret` button
- Add the environmental vars as mentioned here
- Then create new file with structure `.github/workflows/run.yml`
- Now in `run.yml` file, fill with this code below, just copy it and paste in `run.yml` file


<details>
  <summary>
    <b>View code</b>
  </summary>  

```sh
name: Run on workflows
on:
    schedule:
      - cron: "0 */6 * * *"
    push:
      branches: [ main ]
    workflow_dispatch:
    
env:
  API_ID: "${{ secrets.API_ID }}"
  API_HASH: "${{ secrets.API_HASH }}"
  SESSION_NAME: "${{ secrets.SESSION_NAME }}"
  BOT_USERNAME: "${{ secrets.BOT_USERNAME }}"
  ASSISTANT_NAME: "${{ secrets.ASSISTANT_NAME }}"
  DURATION_LIMIT: "${{ secrets.DURATION_LIMIT }}"
  BOT_TOKEN: "${{ secrets.BOT_TOKEN }}"
  SUDO_USERS: "${{ secrets.SUDO_USERS }}"
  CHANNEL_NAME: "${{ secrets.ASSISTANT_NAME }}"
  GROUP_NAME: "${{ secrets.ASSISTANT_NAME }}"
  OWNER_NAME: "${{ secrets.ASSISTANT_NAME }}"

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
       - uses: actions/checkout@v2
         with:
            ref: beta
       - uses: styfle/cancel-workflow-action@0.9.0
         name: "Cancelling duplicate workflow runs"
         with:
            all_but_latest: true
            access_token: ${{ github.token }}
       - uses: actions/setup-node@v2
         with:
            node-version: '16'
       - name: Set up Python 3.9
         uses: actions/setup-python@v2.2.2
         with:
           python-version: 3.9
       - name: cloning repo and install

         continue-on-error: true
         run: |
           sudo apt -qq update && sudo apt -qq install -y --no-install-recommends ffmpeg neofetch
           pip3 install -r requirements.txt
          #  echo "API_ID=${{ secrets.API_ID }} | tee .env
          #  echo "API_HASH=${{ secrets.API_HASH }} | tee -a .env
          #  echo "BOT_USERNAME=${{ secrets.BOT_USERNAME }} | tee -a .env
          #  echo "ASSISTANT_NAME=${{ secrets.ASSISTANT_NAME }} | tee -a .env
          #  echo "SESSION_NAME=${{ secrets.SESSION_NAME }} | tee -a .env
          #  echo "DURATION_LIMIT=${{ secrets.DURATION_LIMIT }} | tee -a .env
          #  echo "SUDO_USERS=${{ secrets.SUDO_USERS }} | tee -a .env
          #  echo "CHANNEL_NAME=${{ secrets.ASSISTANT_NAME }} | tee -a .env
          #  echo "GROUP_NAME=${{ secrets.ASSISTANT_NAME }} | tee -a .env
          #  echo "OWNER_NAME=${{ secrets.ASSISTANT_NAME }} | tee -a .env
          #  echo "BOT_TOKEN=${{ secrets.BOT_TOKEN }} | tee -a .env || echo "processing with bot"
          #  cat .env
       - name: Running
         timeout-minutes: 350
         continue-on-error: true
         run: |
           python3 -m bot
           echo "Bot Died"
```
</details>


- After adding all, Go to the Actions tab and start/run the workflows

## VPS Deployment
```sh
- sudo apt update && upgrade -y
- sudo apt install python3-pip -y virtualenv
- sudo apt install ffmpeg -y
- nvm install v16.5.0
- npm i -g npm
- git clone https://github.com/W29F/WoofVideoStream
- cd video-stream
- virtualenv venv #Create Virtual Environment.
- source venv/bin/activate #Activate Virtual Environment
- pip3 install --upgrade pip
- pip3 install -U -r requirements.txt
- cp -r sample.env local.env
- nano local.env #Fill it with your variables value.
- python3 -m bot
```

# Special Credits 💖

- [Levina](https://github.com/levina-lab) 
- [Sammy-XD](https://github.com/Sammy-XD) 
- [Zxce3](https://github.com/Zxce3) 
- [DoellBarr](https://github.com/DoellBarr) 
- [tofikdn](https://github.com/tofikdn) 
- [Laky's](https://github.com/Laky-64) for [``py-tgcalls``](https://github.com/pytgcalls/pytgcalls)
- [Dan](https://github.com/delivrance) for [``Pyrogram``](https://github.com/pyrogram)

### Support & Updates 🎑
<a href="https://t.me/VeezSupportGroup"><img src="https://img.shields.io/badge/Join-Group%20Support-blue.svg?style=for-the-badge&logo=Telegram"></a> <a href="https://t.me/levinachannel"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
