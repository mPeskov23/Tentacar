
# Firmware del Robot

En aquest directori es localitza tot el codi font i recursos necessaris referent al **funcionament de TentaCar**. Aquí s'inclouen els móduls de control, visió i algoritmica tal que el robot pugui operar de forma autónoma.






## Contingut del directori

**bug2-module.py:** Algoritmica utilitzada pel moviment del robot. Es tracta d'un Bug2 Algorithm per tal de poder esquivar pareds i arribar a l'objectiu (l'objecte a agafar).

**car.py:** Control de moviment del robot .

**main.py:** Control del fluxe principal de TentaCar.

**utils_vision.py:** Crea una imatge amb les bounding boxes de la imatge agafada per la càmera de Rasberry Pi.

**vision.py:** Conté la classe de VisionModule corresponent a tota la vista del robot per tal de saber on es troben els objects, ja sigui amb un sensor de proximitat o amb la càmera per detectar si hi ha o no, objectes.

**wall_detection_module.py:** Formes de detecció de pareds per tal de poder esquivar-les i implementar bug2 algorithm correctament.

**tenta.py:** Control de la pinça del robot fent que pugui realitzar una posició "home", resetejar la posició i agafar un objecte per possar-lo al seu cistell.

