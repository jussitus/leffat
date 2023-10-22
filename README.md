# Leffatus
Elokuvien arvostelusovellus
## Alkuperäinen suunnitelma
Sovelluksessa näkyy elokuvia ja käyttäjien arvosteluita niistä. Arvostelut näkyvät myös käyttäjien profiileissa.
- Käyttäjä voi luoda uuden tunnuksen ja kirjautua sisään tai ulos.
- Käyttäjä näkee listan elokuvista jonka voi järjestää eri tavoin.
- Käyttäjä voi etsiä elokuvia nimen, genren, vuosiluvun, jne. perusteella.
- Käyttäjä voi lisätä arvostelun jo sivulla olevaan elokuvaan tai lisätä elokuvan jos sitä ei ole vielä lisätty.
- Käyttäjä voi poistaa arvostelunsa tai muokata sitä. 
- Käyttäjä voi tarkastella toisen käyttäjän arvosteluita.
- Ylläpitäjä voi lisätä, muokata ja poistaa elokuvia ja arvosteluita. 

## Sovelluksen nykytilanne

Ominaisuuksia jotka toimivat joten kuten
- Tunnuksen luominen ja kirjautuminen sisään/ulos
- Listaukset elokuvista ja käyttäjistä
- Elokuvien ja käyttäjien sivuilla listaus arvosteluista
- Elokuvien sivuilla voi lisätä arvostelun
- Elokuvien listaan voi lisätä elokuvan
- Sovelluksen ulkoasu
- Elokuvien haku
- Elokuvalistauksen ja hakutulosten sivutus
- Ylläpitäjän toiminnot (elokuvien, arvostelujen ja käyttäjien poisto, genrejen lisääminen)

TODO
- ~~ohjaajat~~? ei tule  
## Sovelluksen testaaminen

Voit testata sovellusta paikallisesti näin:
1. Kloonaa repo
2. Suorita leffatus-hakemistossa

        $ python3 -m venv venv
        $ source venv/bin/activate
        (venv) $ pip install -r requirements.txt

3. Luo tietokanta ja sitten suorita

        $ psql sun_tietokanta < schema.sql
        
4. Määritä tarvittavat ympäristömuuttujat tiedostoon .env näin

        SECRET_KEY=jotain_ihan_mitä_vaan
        DATABASE_URL=postgresql:///sun_tietokanta

5. Suorita

        $ flask run

Lisäksi voit lisätä pääkäyttäjän (tunnus: admin, salasana: admin) testaamista varten näin (tarvitsee .env tiedoston toimiakseen): 

        $ python3 ./admin_adder.py

Sivutusta voi testata ajamalla (tarvitsee myös .env tiedoston, generoi elokuvia tietokantaan):

        $ python3 ./db_populator.py