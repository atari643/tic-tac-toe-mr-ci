# Tic-Tac-Toe with Merge-Request and Continuous Integration

Epreuve R4.02 sur machine en temps limité et en binôme.

## Organisation

- Constituer un groupe de 2 participants : **O** et **X** (**O** et **X** seront disposé dans la salle de contrôle de manière à ne pas pouvoir communiquer oralement !)
- **O** fork le dépôt cet dépôt et donne les droits `maintainer` à **X**
- **O** invite l'enseignant correcteur de son groupe en tant que `reporter`
- chacun clone le dépôt

## Principe

- **O** et **X** doivent jouer chaque coup en remplaçant un '.' par leur lettre ('O' ou 'X') et pousser le résultat (sans jamais commiter dans la branche `master` directement !)
- le but du jeux est d'aligner 3 lettres
- à chaque tour, chacun joue une fois
- on ne peut pas jouer sur une case occupée et il est interdit de rejouer la même case au coup suivant
- **O** est le joueur qui débute
- pour jouer, vous devez créer une *MR* afin de saisir votre coup dans le fichier 'game.txt' représentant le plateau
- on joue dès que l'on est prêt, après avoir récupéré (`pull`) les modifications de l'autre
- une *CI* sera mise en place pour s'assurer de la validité du coup saisie, c'est **O** (resp. **X**) qui fusionnera la *MR* proposée par **X** (resp. **O**)

## Mise en place des règles

- le fichier 'game.txt' contenant 3 lignes de 3 caractères '.' est déjà présent dans le dépôt
- **O** et **X** vont mettre en place de la *CI* pour tester la valider des coups (chacun dans une *MR* : `rules-O` et `rules-X`) :
  - **X** s'occupe d'écrire le script dans la *CI* pour vérifier : $$0 <= #('O')-#('X') <= 1$$ (utiliser la commande bash `wc`), et que la grille ne comporte que des 'O', 'X' ou '.'
  - **O** s'occupe de vérifier qu'un coup a bien été joué (`diff` sur 'game.txt' entre la version dans `master`et celle de la branche courante)
- fusionnez vos 2 *MR* `rules-O` et `rules-X`

## Jouer une partie

- **O** joue son premier coup dans une *MR* `first-valid`, et **X** vérifie que les tests de la *CI* passent avant de fusionner la *MR* `first-valid` de **O** (**X** demande à **O** corriger la *CI* si nécessaire dans la revue de code)
- **X** joue ensuite un coup invalide dans une *MR* `first-fail`, et **O** vérifie que les tests de la *CI* échouent (**O** demande à **X** corriger la *CI* si nécessaire dans la revue de code)

## Bonus

- ajouter une règle dans la *CI* pour détecter la fin de partie (dans un `stage` supplémentaire)
