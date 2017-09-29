![Aeros](pilotsplus/static/img/aeros2.png)
# Aeros
Know where you are, **_Airborne_**.
<br><br><br>
### Introduction
Ever wondered what’s that beautiful place while looking out of your flight window?

Aeros provides you complete information, along with the points of interest, about the place beneath you when you are airborne in a flight.
<br><br><br>
### Installation

```bash
git clone https://github.com/AnirudhGoel/aeros
cd aeros
pip install -r requirements.txt
python manage.py runserver
```
<br><br><br>
### Usage
This web-app has two types of inputs-

1. The user can enter his flight number.
The app automatically finds the current location of this flight and gives information about the place beneath it.
2. Just hit the "Locate Me" button. 
The app will locate you by your latitude and longitude and provide you information about the place corresponding to it.