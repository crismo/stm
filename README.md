# stm
stm base project

Start
-----
Bruk: #Start: [navn]

Signaliserer starten på en ny scene.

[navn] er en identifikator som kan brukes med #Handling eller #Neste


Slutt
-----
Bruk: #Slutt

Signaliserer slutten på en scene.

Lyd
-----
Bruk: #Lyd: [filer..]

Setter opp en liste med lydfiler som starter å spille straks scenen er lastet.

Eks: #Lyd: hei.mp3,fortelling.mp3

Bilde
-----
Bruk: #Bilde: [navn]

Viser et bilde.

Eks: #Bilde: bakgrunn.png

Handling
-----
Bruk: #Handling: Gå til ... (lbl) / .. , bilde, lyd, state, x,y

Første parameter er altid Gå til eller en annen tekst (eks feil). Dersom labelet man ønsker å gå til ikke er et enkelt ord så setter man det i parantes etterpå.

Eks: #Handling: Gå til Den store grønne skogen (skogen)

Deretter angir man en bilde fil som skal vises som trigger for handlingen. Man kan også angi en lydfil som spilles av når man trykker på bildet. Siste parameterene er aldit x og y for bildet.

Eks: #Handling: Gå til slottet, slott.png, veientilslottet.mp3, 100, 200

En handling kan også medføre en state endring. Det gjøres ved å angi et nøkkel/verdi par.

Eks: #Handling: Gå til slottet, slott.png, veientilslottet.mp3, valgtSlott=grønne.png , 100, 200

State er ment å hjelpe å huske enkle ting for senere bruk. Se mer under #Lagre

Neste
-----

Lagre
-----
Bruk: #Lagre: key=value

Man kan bruke Lagre kommandoen til å lagre en verdi for seinere bruk
For å bruke verdien senere brukes en oppslags kommando.

Eks: 

#Lagre: bakgrunn=havet.png

#Bilde: [bakgrunn]

Tell
-----


Terning
-----

TerningPos
-----

Nedtelling
-----

Drag
-----

DragForbli
-----

DragRekt
-----

DragAlternativ
-----

DragMål
-----

<a href="https://heroku.com/deploy?template=https://github.com/crismo/stm">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
