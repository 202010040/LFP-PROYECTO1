##### Universidad de San Carlos de Guatemala
##### Facultad de ingenieria
##### Ingenieria en Ciencias y Sistemas
##### Laboratorio Lenguajes Formales y de Programacion
#
#
**Nombre** : Evelio Marcos Josue Cruz Soliz
####
**Carnet** : 202010040
#
#
#

<h1 align="center">
   MANUAL TECNICO PROYECTO 1
</h1>

#
#
**Auxiliar** : Pablo Fernando Cabrera Pineda
####
**Catedratico** : Ing. Kevin Adiel Lajpop Ajpacaja
#
#
#
#
<p align="center">
   FECHA DE ENTREGA: 18/6/2022 
</p>

#
#
#
#
### Generacion de afd por medio del metodo del arbol:
#### AFD para el tipo de dato Int: DD*
###
**Construccion del arbol de expresion regular:**
#
<p align="center">
   <img src = "Grafo Arbol int.png" />
</p>

### 
**Enumeracion de las hojas:**
<p align="center">
   <img src = "Grafo Arbol int 2.png" />
</p>

### 
**Calculo de los anulables:**
<p align="center">
   <img src = "Grafo Arbol int 3.png" />
</p>

### 
**Calculo de los first:**
<p align="center">
   <img src = "Grafo Arbol int 4.png" />
</p>

### 
**Calculo de los last:**
<p align="center">
   <img src = "Grafo Arbol int 5.png" />
</p>

### 
**Calculo de los follow:**
| Nodo     | Numero (i)               | Follow (i)                 |
| --------- | ------------------------- | ---------------------- |
| D     | 1               | 2,3                 |
| D     | 2               | 2,3                 |
| #     | 3               | -                 |

### 
**Calculo de los follow:**
| Estado     | Simbolo               | Siguiente estado                 |
| --------- | ------------------------- | ---------------------- |
| S0     | D               | S1              |
| S1     | D               | S1               |

### 
**AFD:**
<p align="center">
   <img src = "Grafo Arbol int 6.png" />
</p>



#### AFD para el tipo de dato String: (")([a-zA-z0-9][a-zA-z0-9]*)(")(#)
###
**Construccion del arbol de expresion regular:**
#
<p align="center">
   <img src = "Grafo Arbol str.png" />
</p>

### 
**Enumeracion de las hojas:**
<p align="center">
   <img src = "Grafo Arbol str 2.png" />
</p>

### 
**Calculo de los anulables:**
<p align="center">
   <img src = "Grafo Arbol str 3.png" />
</p>

### 
**Calculo de los first:**
<p align="center">
   <img src = "Grafo Arbol str 4.png" />
</p>

### 
**Calculo de los last:**
<p align="center">
   <img src = "Grafo Arbol str 5.png" />
</p>

### 
**Calculo de los follow:**
| Nodo     | Numero (i)               | Follow (i)                 |
| --------- | ------------------------- | ---------------------- |
| "    | 1               | 2,3,4                 |
| [a-zA-z0-9]     | 2               | 2,3,4                |
| [a-zA-z0-9]     | 3               | 2,3,4                |
| "     | 4               | -               |

### 
**Calculo de los follow:**
| Estado     | Simbolo               | Siguiente estado                 |
| --------- | ------------------------- | ---------------------- |
| S0     | "               | S1              |
| S1     | [a-zA-z0-9]              | S2               |
| S2     | [a-zA-z0-9]              | S2               |
| S2     | "               | S3               |
| S3     | #               | -               |
### 
**AFD:**
<p align="center">
   <img src = "Grafo Arbol str 6.png" />
</p>
