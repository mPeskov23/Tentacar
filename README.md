<img src="https://github.com/mPeskov23/Tentacar/blob/master/documents/TentaCar.png?raw=true" align="right" width="300" alt="header pic"/>

# Tentacar Project
![GitHub_Action_Linux_CI](https://github.com/AtsushiSakai/PythonRobotics/workflows/Linux_CI/badge.svg)
![GitHub_Action_Windows_CI](https://github.com/AtsushiSakai/PythonRobotics/workflows/Windows_CI/badge.svg)
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

Per tal de fer funcionar TentaCar és necessaria la connexió amb una rasberry pi 0 i la seva càmera a més de les funcionalitats i llibreries necessaries per ejecutar el codi. Aquestes es troben dins del fitxer [*Requeriments.txt*](https://github.com/mPeskov23/Tentacar/blob/master/requirements.txt) o de manera més ràpida executant un [init.sh](https://github.com/mPeskov23/Tentacar/blob/master/init.sh) de la següent manera:
```bash
bash init.sh
```

# Autoría


Adrián Margarit 1665218 (Test Lead) 

Biel Alavedra 1666110 (HW Lead)

Mikhail Peskov 1534227 (SW Lead)

Lucas Aviñó 1566876 (3D lead)




