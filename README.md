<img src="https://github.com/mPeskov23/Tentacar/blob/master/documents/Tentacar.jpeg" align="right" width="300" alt="header pic"/>

# Tentacar Project
[![Build status](https://ci.appveyor.com/api/projects/status/sb279kxuv1be391g?svg=true)](https://github.com/mPeskov23/Tentacar/tree/master/testval)

# Taula de Continguts
## [/3D](https://github.com/mPeskov23/Tentacar/tree/master/3D) 
Directori amb tots el models 3D utilitzats durant la creació del robot

## [/documents](https://github.com/mPeskov23/Tentacar/tree/master/documents)  

Documents necessaris per comprendre l'estructura de TentaCar, comprès per la proposta de projecte, els components del robot, el diseny del circuit i l'esquema dels móduls de software.


## [/firmware](https://github.com/mPeskov23/Tentacar/tree/master/firmware) 

Tot el codi font i recursos necessaris referent al funcionament de TentaCar. S'inclouen els móduls de control, visió i algoritmica tal que el robot pugui operar de forma autónoma.

## [/testval](https://github.com/mPeskov23/Tentacar/tree/master/testval) 

Conjunt de proves utilitzades per poder provar la funcionalitat del robot. S'ha utilitzat una simulació en un escenari controlat per tal de comprobar que totes les funcions escrites funcionen correctament.

## [/models](https://github.com/mPeskov23/Tentacar/tree/master/models)

Codi per l'utilització dels models preentrenats per la detecció d'objectes i el seu setup. 

# Qué és TentaCar?

Algún cop se us ha caigut algún objecte al terra? Clar que sí, no? I que heu fet? Us heu ajupit, l'heu agafat i heu seguit fent el que estaveu fent. 
**Però**, ara bé, i si fossiu una persona gran amb problemes a les cames que no us podeu ajupir. Qué passa si us cau el móvil o una forquilla i no el podeu agafar perque les vostres cames no responen?

Per aquest motiu, **TentaCar** és una realitat. Es tracta d'un robot amb complex de Roomba que dona voltes per la casa en busca d'algún objecte a recollir. Aquests objectes són almacenats dins el cubell que porta a sobre per poder ser agafats per l'usuari. 


# "How To Run"

Per tal de fer funcionar TentaCar és necessaria la connexió amb una rasberry pi 0 (recomanem el SO "Bullseye" per evitar els conflictes de dependències) i la seva càmera a més de les funcionalitats i llibreries necessaries per ejecutar el codi. Aquestes es troben dins del fitxer [*Requeriments.txt*](https://github.com/mPeskov23/Tentacar/blob/master/requirements.txt) o de manera més ràpida executant un [init.sh](https://github.com/mPeskov23/Tentacar/blob/master/init.sh) de la següent manera:
```bash
bash init.sh
```

# Localització d'objectes
<p>L'objectiu principal d'aquest robot és la localització dels objectes pel terra per tal de, seguidament, agafar-los i possar-los al seu darrere. Per tant la tasca principal de Tentacar recau sobre els seus ulls. Es tracta d'una càmera integrada a la Rasberry Pi 0 on a partir de la llibrería PiCamera2 i un model preeentrenat anomenat efficientdet_lite0 es poden extreure tots els objectes presents en un frame. Per tant, cada X segons, Tentacar va agafant imatges del seu voltant i les passa per un procès per tal de trobar algún objecte vàlid que pugui agafar (ja que el model detecta també objectes grans com neveres)</p>

![2](https://github.com/mPeskov23/Tentacar/blob/master/models/test_data/table.jpg)  

![3](https://github.com/mPeskov23/Tentacar/blob/master/documents/Resultats%20visio.png)  


<p>Com es pot veure en aquestes dues fotos, es detecten tots els objectes relacionats en la imatge. Però, hi ha un problema i és que les pareds no són detectades, per tan a partir d'un algorisme de contorns Canny i el càlcul del nivell de suavitat de la superficie de davant podem detectar si es tracta d'una pared o d'un objecte. Per tant, un cop tenim un objecte o pared detectats el cotxe s'ha de moure cap al seu objectiu. Quan no hi ha una pared es mou amb ajuda del sensor de proximitat controlant la orientació fent trigonometría bàsica i la distància fins a la qual s'ha de apropar. Però que passa si hi ha una pared o un pilar davant? Doncs s'utilitza bug2 algorithm, que el que fa és esquivar l'objecte intentant anar cap a la dreta d'aquest fins que trobi un camí cap endavant com en el següent exemple, on es veu un escenari extrem (ja que li em donat les coordenades del objecte, per a veure com funciona amb pareds llargues)</p>

![4](https://github.com/mPeskov23/Tentacar/blob/master/testval/videos/Bug2.png)  
![5](https://github.com/mPeskov23/Tentacar/blob/master/testval/videos/Bug2Algo.gif)  

<h1> Funcionalitat de la pinça </h1>

<p>Un cop tenim l'objecte detectat i ens em situat davant, agafem un frame per tal de localitzar l'objecte en relació a la posició on possar la pinça. Més tard, es fan els càlculs d'inverse cinemàtic per possar els angles corresponents a cada servo (tenint en compte una relació 1:2 al servo de rotació) i posicionar la pinza just a sobre del objecte per seguidament tancar-la, tornar a posició inicial, girar 90 graus (relació 1:2) el servo de rotació i deixar anar l'objecte cap a dins del cubell del robot. Aquests moviments es poden veure ens els següents passos:</p>

### Pas 1

![6](https://github.com/mPeskov23/Tentacar/blob/master/testval/videos/pinza.gif)  

### Pas 2

![7](https://github.com/mPeskov23/Tentacar/blob/master/testval/videos/coger_objeto.gif)  

  
# Autoría

Adrián Margarit 1665218 (Test Lead) 

Biel Alavedra 1666110 (HW Lead)

Mikhail Peskov 1534227 (SW Lead)





