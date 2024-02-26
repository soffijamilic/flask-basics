# Flask

[Flask](https://flask.palletsprojects.com/en/3.0.x/) je python biblioteka za
programiranje servera.

Potrebno predznanje:

-   Osnove programskog jezika python
-   Poznavanje [HTTP](https://www.freecodecamp.org/news/what-is-http/) protokola

## Podesavanje radnog okruzenja

Na ovom kursu cemo se dotaci raznih upotreba HTTP protokola za realizaciju
razlicitih oblika veb aplikacija. Kada je rec o flask projektu, ili bilo kom
drugom python projektu koji koristi eksterne biblioteke i pakete, nepohodno je
da se svi paketi navedu u `requirements.txt` fajlu. Na ovaj nacin package
manager je u mogucnosti da instalira sve neophodne pakete koristeci taj fajl.

Naravno, kada instaliramo zavisnosti _(eng. dependancies)_, ne zelimo da
zagadimo globalni prostor imena _(eng. global namespace)_. Kako bismo to
postigli potrebno je da instaliramo nase zavisnosti u necemu sto se zove
**virtuelno okruzenje**.

Pocecemo tako sto cemo forkovati, a zatim i klonirati ovaj repozitorijum u nekom
praznom direktorijumu gde imamo potpune privilegije (uglavnom je to disk D: na
Windows sistemima). Kada uspesno kloniramo repozitorijum, otvoricemo instancu VS
Code editora koriscenjem komande `code <naziv repozitorijuma>`. Kada nam se otvori
VS Code, otvoricemo instancu terminala i iskucati sledece naredbe:

```shell
pip install virtualenv
python -m virtualenv env
Set-ExecutionPolicy Unrestricted -Scope Process
.\env\Scripts\activate
pip install -r requirements.txt
```

Ove komande rade sledece:

1. `pip install virtualenv` instalira paket za kreiranje virtuelnih okruzenja u
   globalnom prostoru imena
2. `python -m virtualenv env` kreira direktorijum u kom ce ziveti virtuelno
   okruzenje nazvano `env`
3. `Set-ExecutionPolicy Unrestricted -Scope Process` dozvoljava izvrsavanje
   skripti ukoliko nismo admin nalog samo u okviru trenutne shell sesije
4. `.\env\Scripts\activate` izvrsava skriptu koja aktivira virtuelno okruzenje
5. `pip install -r requirements.txt` installira sve pakete koji su navedeni kao
   zavisnosti u **virtualnom okruzenju**

Ukoliko ste uspesno izvrsili sve navedene komande, mozemo nastaviti sa
pravljenjem nase prve veb aplikacije.

## Razvoj flask aplikacije

[Dokumentacija flask paketa](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
kaze da minimalna flask aplikacija izgleda ovako:

```python
# app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Flask aplikacija se pokrece sledecom naredbom:

```shell
flask --app src.app run --debug
```

Ovde `--debug` flag sluzi da obavesti flask da cemo praviti izmene na aplikaciji
i da zelimo da se server ponovo pokrene cim se naprave izmene.

Naravno, mi necemo koristi minimalnu aplikaciju jer planiramo da koristimo i
paket za testiranje koda pod nazivom `pytest`.

Zato nas `app.py` fajl izgleda malo drugacije. Za bolje razumevanje flask paketa
treba procitati
[dokumentaciju](https://flask.palletsprojects.com/en/3.0.x/quickstart/).

## Testiranje aplikacije

U direktorijumu `tests` nalaze se python moduli koji treba da testiraju
funkcionalnost nase aplikacije. Mi cemo praktikovati metodologiju koja se zove
**TDD** _(eng. Test Driven Development)_, gde se prvo pisu testovi koji
odredjuju zahteve koda, a zatim se pise kod tj. funkcionalnost koja te testove
treba da polozi.
