# pylint: disable=C0183
'''
The MIT License (MIT)

Copyright (c) 2014 Andreas "Akki" Nitsch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

from flask import Flask
from flask import render_template
from flask import redirect
from flask_bootstrap import Bootstrap

import logging
import operator
import os

logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s: %(message)s', level=logging.DEBUG)

GENRES = []

SPORT = {'id':'SPORT', 'name':'Sport', 'channels':[('sport1fm', 'Sport1FM')]}
GENRES.append(SPORT)

SEVENTIES = {'id':'70s', 'name':'70s', 'channels':[('bigrradio', 'Big R Radio - Classic Rock'), ('softrockradio', 'SoftRockRadio.net')]}
GENRES.append(SEVENTIES)

BLUEGRASS = {'id':'BLUEGRASS', 'name':'Bluegrass', 'channels':[('bluegrassmix', 'BluegrassMix')]}
GENRES.append(BLUEGRASS)

BOP = {'id':'BOP', 'name':'Bop', 'channels':[('allegrojazz', 'Allegro Jazz'), ('neworleansradio', 'New Orleans Radio'), ('radioskymusic', 'RadioSky Music')]}
GENRES.append(BOP)

CLASSICROCK = {'id':'CLASSICROCK', 'name':'Classic Rock', 'channels':[('fmclassicalternativerock', '181.FM - Classic Buzz -=- Classic Alternative Rock'), \
('fouru70s', '4U 70s'), \
('eightiesmixtape', '80sMixTape'), \
('abetterclassicrockstation', 'A Better Classic Rock Station'), \
('cityfmclassicrock', 'CITY FM Classic Rock') ,
('classicdeepcuts', 'Classic Deep Cuts') ,
('cocktelerablues', 'Cocktelera Blues') ,
('gdradio', 'GDRADIO.NET') ,
('novaclassicrock', 'novaclassicrock.nl') ,
('planetrockbelgium', 'Planet Rock Belgium') ,
('softclassicrock', 'Soft Classic Rock')]}
GENRES.append(CLASSICROCK)

FOLKROCK = {'id':'FOLKROCK', 'name':'Folk Rock', 'channels':[('aolmradio', 'AOLMRadio'), ('bleh', 'Bleh'), ('dylanradio', 'DylanRadio.com')]}
GENRES.append(FOLKROCK)

HESSISCHERRUNDFUNK = {'id':'hr', 'name':'Hessischer Rundfunk', 'channels':[('hrinfo', 'HR Info')]}
GENRES.append(HESSISCHERRUNDFUNK)

ROCKABILLY = {'id':'ROCKABILLY', 'name':'Rockabilly', 'channels':[('radiobilly', 'Radiobilly'), ('rockabillyradio', 'Rockabilly Radio')]}
GENRES.append(ROCKABILLY)

SWING = {'id':'SWING', 'name':'Swing', 'channels':[('radioswingworldwide', 'Radio Swing Worldwide'), ('ratpackmusicradioworldjazzfederation', 'RAT PACK MUSIC RADIO Worldjazzfederation.com')]}
GENRES.append(SWING)


GENRES.sort(key=operator.itemgetter('name'))

STATION = ""

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

@app.route("/")
def hello():
    """Render index-page."""
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation=STATION)

@app.route("/sport1fm")
def sport1fm():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh Sport1FM http://77.67.34.21/SPORT1FM_24_7.mp3')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Sport1FM")

#70s
@app.route("/bigrradio")
def bigrradio():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh bigrradio http://107.155.126.42:8010')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Big R Radio")

@app.route("/softrockradio")
def softrockradio():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh softrockradio http://173.236.21.250:8032')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Soft Rock Radio")

#Bluegrass
@app.route("/bluegrassmix")
def gluegrassmix():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh bluegrassmix http://192.81.248.194:8072/stream ')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="BluegrassMix")

#Bop
@app.route("/allegrojazz")
def allegrojazz():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh allegrojazz http://listen.radionomy.com/Allegro-Jazz')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Allegro Jazz")

@app.route("/neworleansradio")
def neworleansradio():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh neworleansradio http://listen.streamonomy.com/neworleansradio')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="New Orleans Radio")

@app.route("/radioskymusic")
def radioskymusic():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh radioskymusic http://listen.radionomy.com/RadioSky-Music')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Radio Sky Music")

#ClassicRock
@app.route("/fmclassicalternativerock")
def fmclassicalternativerock():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh 181fmclassicalternativerock http://108.61.73.117:14038')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="181 Fm Classic Alternative Rock")

@app.route("/fouru70s")
def fouru70s():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh 4U\ 70s http://listen.radionomy.com/4U-70s')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="4U 70s")

@app.route("/eightiesmixtape")
def eightiesmixtape():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh 80sMixTape http://listen.radionomy.com/80sMixTape')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="80s Mix Tape")

@app.route("/abetterclassicrockstation")
def abetterclassicrockstation():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh abetterclassicrockstation http://listen.radionomy.com/a-better-classic-rock-STATION')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="A better classicrock STATION")

@app.route("/cityfmclassicrock")
def cityfmclassicrock():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh cityfmclassicrock http://91.221.151.240:8043')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="City Fm Classic Rock")

@app.route("/classicdeepcuts")
def classicdeepcuts():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh classicdeepcuts http://208.85.240.10:8134')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Classic Deep Cuts")

@app.route("/cocktelerablues")
def cocktelerablues():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh cocktelerablues http://listen.radionomy.com/Cocktelera-Blues')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Cocktelera Blues")

@app.route("/gdradio")
def gdradio():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh gdradio http://216.119.152.213:8019')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Gd Radio")

@app.route("/novaclassicrock")
def novaclassicrock():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh novaclassicrock http://173.236.29.52:80')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Nova Classicrock")

@app.route("/planetrockbelgium")
def planetrockbelgium():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh planetrockbelgium http://91.121.219.80:8330')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Planet Rock Belgium")

@app.route("/softclassicrockRadio")
def softclassicrock():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh softclassicrock http://64.71.133.122:8000')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Soft Classic Rock")

#FolkRock
@app.route("/aolmradio")
def aolmradio():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh aolmradio http://listen.radionomy.com/AOLMRadio')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Aolm Radio")

@app.route("/bleh")
def bleh():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh bleh http://listen.radionomy.com/Bleh')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Bleh")

@app.route("/dylanradio")
def dylanradio():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh dylanradio http://173.192.198.244:8138')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Dylan Radio")

#Hessischer Rundfunk
@app.route("/hrinfo")
def hrinfo():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh HR\ Info http://www.metafilegenerator.de/HR/hrinfo/mp3/webm.m3u')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="HR Info")

#Rockabilly
@app.route("/radiobilly")
def radiobilly():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh Radiobilly http://184.154.202.243:8150')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Radiobilly")

@app.route("/rockabillyradio")
def rockabillyradio():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh Rockabilly\ Radio http://209.9.238.6:6042')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Rockabilly Radio")

#Swing
@app.route("/radioswingworldwide")
def radioswingworldwide():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh Radion\ Swing\ Worldwide http://208.53.158.48:8100')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Radio Swing Worldwide")


@app.route("/ratpackmusicradioworldjazzfederation")
def ratpackmusicradioworldjazzfederation():
    """Function for setting radiostream."""
    os.system('/usr/local/bin/chooseChanel.sh RAT\ PACK\ MUSIC\ RADIO\ Worldjazzfederation.com http://74.55.244.98:6900')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation="Rat Pack Music Radio Worldjazzfederation")

#Control
@app.route("/volume0")
def volume0():
    """Function for setting volume."""
    os.system('vol 0')
    logging.debug('Mute')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation=STATION)

@app.route("/volume75")
def volume75():
    """Function for setting volume."""
    os.system('vol 75')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation=STATION)

@app.route("/volume80")
def volume80():
    """Function for setting volume."""
    os.system('vol 80')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation=STATION)

@app.route("/volume85")
def volume85():
    """Function for setting volume."""
    os.system('vol 85')
    return render_template('fmberryremote.html', GENRES=GENRES)

@app.route("/volume90")
def volume90():
    """Function for setting volume."""
    os.system('vol 90')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation=STATION)

@app.route("/volume95")
def volume95():
    """Function for setting volume."""
    os.system('vol 95')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation=STATION)

@app.route("/volume100")
def volume100():
    """Function for setting volume."""
    os.system('vol 100')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation=STATION)

@app.route("/reboot")
def reboot():
    """Function for rebooting the raspberry pi."""
    os.system('reboot')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation=STATION)

@app.route("/shutdown")
def shutdown():
    """Function for shuting down the raspberry pi."""
    os.system('shutdown -h now')
    return render_template('fmberryremote.html', GENRES=GENRES, choosenStation=STATION)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
