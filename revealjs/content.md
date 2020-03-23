# Titre
__Sous-titre__



## Enchaînements


* Avec 2 lignes d'espacement, les diapo défilent __vers le bas__


* Avec 3 lignes d'espacement, les diapo défilent __vers la droite__



## Formatage


### Styles

\_\_gras\_\_ : __gras__  
\_emphase\_ : _emphase_  
\`code\` : `code`


### Puces

* rouge
* vert
* bleu
    * bleu marine
    * bleu ciel
* noir



## Images


* On peut préciser la _taille des images_ avec  
`<!-- .element: height="200px" -->`

![Logo SII](images/logo-sii.png)  <!-- .element: height="200px" -->
![Logo SII](images/logo-sii.png)  <!-- .element: height="100px" -->



## Liens

\[Nom de la ressource\](Url de la ressource)

\[GitHub SII\](https://github.com/groupe-sii)



## Code


Taille normale

```javascript
function toggle(elemID){
    var elem = document.getElementById(elemID);   
    if (elem.style.display === 'block') {
        elem.style.display = 'none';  
    }
    else {
        elem.style.display = 'block';
    }
}
```


Taille moyenne

`<!-- .slide: data-state="medium-code" -->`

<!-- .slide: data-state="medium-code" -->
```javascript
function toggle(elemID){
    var elem = document.getElementById(elemID);   
    if (elem.style.display === 'block') {
        elem.style.display = 'none';  
    }
    else {
        elem.style.display = 'block';
    }
}
```


Petite taille

`<!-- .slide: data-state="small-code" -->`

<!-- .slide: data-state="small-code" -->
```javascript
function toggle(elemID){
    var elem = document.getElementById(elemID);   
    if (elem.style.display === 'block') {
        elem.style.display = 'none';  
    }
    else {
        elem.style.display = 'block';
    }
}
```



## Tableaux


Taille normale

| Colonne 1 | Colonne 2 | Colonne 3 |
| -         | -         | -         |
| A1        | B1        | C1        |
| A2        | B2        | C2        |


Taille moyenne

`<!-- .slide: data-state="medium-table" -->`

<!-- .slide: data-state="medium-table" -->
| Colonne 1 | Colonne 2 | Colonne 3 |
| -         | -         | -         |
| A1        | B1        | C1        |
| A2        | B2        | C2        |


Petite taille

`<!-- .slide: data-state="small-table" -->`

<!-- .slide: data-state="small-table" -->
| Colonne 1 | Colonne 2 | Colonne 3 |
| -         | -         | -         |
| A1        | B1        | C1        |
| A2        | B2        | C2        |



## Fonctionnalités avancées


### Utilisation de balises HTML dans le Markdown

- La formule Chimique de l'eau est H<sub>2</sub>O.

- E=mc<sup>2</sup> !

- Voici du texte en <small>fonte réduite</small>. Cool non ?

<!-- .slide: data-state="small-code" -->
```
- La formule Chimique de l'eau est H<sub>2</sub>O.

- E=mc<sup>2</sup> !

- Voici du texte en <small>fonte réduite</small>. Cool non ?
```


### Background

<!-- .slide: data-background-color="#888888"  -->
Modifier le background des slides :

`<!-- .slide: data-background-image="http://example.com/image.png" -->`

`<!-- .slide: data-background-repeat="repeat" -->`

`<!-- .slide: data-background-size="100px" -->`

`<!-- .slide: data-background-color="#888888"  -->`


### Transitions

<!-- .slide: data-transition="concave" -->

Changer le type de transition :
* default
* cube
* page
* concave
* zoom
* linear
* fade
* none

`<!-- .slide: data-transition="concave" -->`


### Vitesse de transition

<!-- .slide: data-transition="concave" data-transition-speed="slow" -->

Changer la vitesse de la transition :
* default
* fast
* slow

`<!-- .slide: data-transition-speed="slow" -->`


### data-state
<!-- .slide: data-state="data-state-slide" -->

L'ajout de `data-state` sur une slide permet d'appliquer une *classe CSS* spécifique à une slide.

`<!-- .slide: data-state="data-state-slide" -->`

```css
.data-state-slide em {
  color: #951753 !important;
}
```


### Cheat-Sheet
<!-- .slide: data-state="cheat-sheet" -->

1. On peut afficher une liste ordonnée façon Cheat-Sheet  
`<!-- .slide: data-state="cheat-sheet" -->`

2. Afficher une vache  
`$ apt moo`

3.  Faire beugler une vache  
`$ echo "Meuhhhh" | cowsay`


### Masquer le logo

<!-- .slide: data-state="nologo-slide" -->
`<!-- .slide: data-state="nologo-slide" -->`
