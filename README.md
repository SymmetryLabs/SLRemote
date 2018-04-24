# SLRemote
A small python web app with functionality to control a locally running SLStudio instance (mainly useful for instances of headless SLStudio).

### To run 
Should be running with Python 3.6
Dependancies included in requirements.txt
To change the OSC address you send messages to, look in the utils_light.py file and change the string manually
To run the app through a public ip, use ngrok (temporary) or serveo (permanent)
https://ngrok.com/
https://serveo.net/

```
pip install -r requirements.txt
python SLRemote.py
```
