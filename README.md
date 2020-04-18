# Motor-con-rele
Aprenderemos una especie de módulo de interruptor especial, Módulo de relé.

En este proyecto, usaremos un botón para controlar un relé y conducir el motor..

Relé

El relé es un interruptor seguro que puede utilizar un circuito de baja potencia para controlar el circuito de alta potencia. Consiste en electroimán
y contactos. El electroimán es controlado por circuito de baja potencia y los contactos se utilizan en circuitos de alta potencia.
Cuando el electroimán está energizado, atraerá los contactos.
Los adjuntos son unos diagramas principal de relé común y la característica y el símbolo de circuito del relé de 5V utilizado en
este proyecto
El pin 5 y el pin 6 están conectados entre sí en el interior. Cuando el pin de bobina3 y 4 se conectan a la potencia de 5V
suministro, el pin 1 se desconectará al pin 5&6 y el pin 2 se conectará al pin 5&6. Así que el pin 1 se llama contacto
cerrado, el pin 2 se llama contacto abierto.

Inductor

La unidad de inductancia (L) es el henry (H). 1H-1000mH, 1mH-1000-H.
Inductor es un dispositivo de almacenamiento de energía que convierte la energía eléctrica en energía magnética. Generalmente, consiste en
de bobinado, con una cierta cantidad de inductancia. El inductor obstaculizará el cambio de corriente
el inductor. Cuando el paso actual a través del inductor aumenta, intentará obstaculizar el aumento de la
tendencia actual; y cuando la corriente que pasa a través del inductor disminuya, intentará obstaculizar la
tendencia decreciente de la corriente. Así que la corriente que pasa a través del inductor no es transitoria.
El circuito de referencia para el relé (imagen 1). La bobina de relé puede ser equivalente a inductor, cuando el transistor
desconecta la fuente de alimentación del relé, la corriente en la bobina del relé no puede detenerse inmediatamente,
impacto en la fuente de alimentación. Así que un diodo paralelo se conectará a ambos extremos del pasador de la bobina de relé en reversión
dirección, entonces la corriente pasará a través del diodo, evitando el impacto en la fuente de alimentación.

Preste atención a la tensión de alimentación necesaria para los componentes en circuito, en el que el relé necesita
tensión de alimentación 5V, y el motor necesita 3.3V. Además, se utiliza un LED como indicador para el relé
(activado o desactivado).
