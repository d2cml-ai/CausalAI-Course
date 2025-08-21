# Flujo de Trabajo con Git

## Branches

Los branches en git son espacios de trabajo independientes entre sí. De esta manera, los cambios en uno no afectan a los demás.

![](_assets/git1.PNG)

Si deseamos que nuestros cambios sí afecten a otro *branch*, podemos hacer un *merge*

![](_assets/git2.PNG)

## Flujo de trabajo

![](_assets/git3.PNG)

## Algunas consideraciones

Tenemos dos tipos de branches:

1. Main branch:

Donde se guarda la versión "oficial" de nuestro trabajo.

2. Feature branch

Aquí tenemos los cambios antes de que hallamos probado que son apropiados para el Main

3. Develop branch

Este tipo de branch es utilizado para tareas complejas, y tiende a ser la base de varios feature branches

- Procurar que todos los commits sean suficientemente significativos para tener una descripción de una oración.

- Procurar no hacer merge al main antes de saber que el código funciona bien y que no provocará cambios no deseados.