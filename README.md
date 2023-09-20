# leffatus
Elokuvien arvostelusovellus

Sovelluksessa näkyy elokuvia ja käyttäjien arvosteluita niistä. Arvostelut näkyvät myös käyttäjien profiileissa.
- Käyttäjä voi luoda uuden tunnuksen ja kirjautua sisään tai ulos.
- Käyttäjä näkee listan elokuvista jonka voi järjestää eri tavoin.
- Käyttäjä voi etsiä elokuvia nimen, genren, vuosiluvun, jne. perusteella.
- Käyttäjä voi lisätä arvostelun jo sivulla olevaan elokuvaan tai lisätä elokuvan jos sitä ei ole vielä lisätty.
- Käyttäjä voi poistaa arvostelunsa tai muokata sitä. 
- Käyttäjä voi tarkastella toisen käyttäjän arvosteluita.
- Ylläpitäjä voi lisätä, muokata ja poistaa elokuvia ja arvosteluita. 

## sovelluksen testaaminen

Voit testata sovellusta paikalliseti näin:
1. Kloonaa repo
2. Suorita
``` 
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```
3. Luo tietokanta ja sitten suorita
```
$ psql sun_tietokanta < schema.sql
```
4. Määritä ympäristömuuttujat SECRET_KEY (mikä tahansa) ja DATABASE_URL (mallia postgresql:///sinun_tietokanta) esim. tiedostoon .env
5. Suorita
```
$ flask run
```
