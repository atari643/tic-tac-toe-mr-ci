# Tic-Tac-Toe with Merge-Request and Continuous Integration

Epreuve R4.02 sur machine en temps limité et en binôme.

> **Note**
> Si votre groupe est composé d'un nombre impair d'étudiants, un seul monôme sera choisi et jouera à la fois le rôle de **O** et **X**.

L'objectif de cette épreuve est de montrer votre capacité à maitriser le 'workflow' **GitLab** avec des *Merge-Requests* (*MR*) et des *Issues*, en particulier, ainsi que la mise en place d'une *Intégration Continue* (*CI*) dans **GitLab**.

Pour cela, vous allez jouer au jeu 'Git-Tac-Toe' (*Morpion* en **Git**) dans un fichier texte 'game.txt' contenant une grille de caractères 3x3. A chaque action de jeu, une *MR* devra être envoyée dans le dépôt, et la mise en place de votre *CI* devra s'assurer que les règles ont bien été respectées.

> **Note**
> Le code Python de ces tests est donné à la fin de ce document.

Tout au long de cette épreuve, vous n'aurez pas besoin d'échanger entre vous 'oralement'. Vous devez juste choisir qui jouera le rôle du joueur **O** et **X**.

## Organisation

- Constituer un groupe de 2 participants : **O** et **X**
> **Warning**
> **O** et **X** seront disposés dans la salle de contrôle de manière à ne pas pouvoir communiquer oralement !
- **O** *fork* ce dépôt (en mode `private` !) et donne les droits `maintainer` à **X**.
- **O** invite l'enseignant correcteur de son groupe en tant que `reporter`.
> **Note**
> Afin de pouvoir créer des *MR* à partir d'*Issues* gérées dans votre tableau de bord **GitLab**, on vous demande également de supprimer la relation avec le projet à l'origine du fork (voir /settings/general/advanced/ Remove fork relationship).
- **O** et **X** clonent le dépôt **GitLab**.

## Principe

- **O** et **X** doivent jouer chaque coup en remplaçant un '.' par leur lettre ('O' ou 'X') et pousser (`push`) le résultat sur le dépôt **GitLab**.
> **Warning**
> Il est interdit de commiter dans la branche `main` directement !
- Le but du jeu est d'aligner 3 lettres. A chaque tour, chacun joue une seule fois. On ne peut pas jouer sur une case occupée et il est interdit de rejouer la même case au coup suivant.
- **O** est le joueur qui débute.
- Pour jouer, vous devrez créer une *MR* afin de saisir votre coup dans le fichier 'game.txt' représentant le jeu.
- On joue dès que l'on est prêt, mais après avoir récupéré (`pull`) les modifications de l'autre joueur.
- Une *CI* sera mise en place pour s'assurer de la validité du coup saisie, c'est **O** (respectivement **X**) qui fusionnera la *MR* proposée par **X** (respectivement **O**).

## Mise en place des règles

- Le fichier 'game.txt' contenant 3 lignes de 3 caractères '.' est déjà présent dans le dépôt **GitLab**.
- **O** et **X** vont mettre en place la *CI* pour tester la validité des coups (chacun séparément dans une *MR* associée à une *Issue* : nommée `rules-O` et `rules-X`) :
  - **X** s'occupe d'écrire un script dans la *CI* pour vérifier que #('O') == #('X') ou #('O') == #('X') + 1, et que la grille ne comporte que des 'O', 'X' ou '.',
  - **O** s'occupe de vérifier qu'un coup a bien été joué (en regardant la différence entre 'game.txt' de la version `main` et celle de la branche courante, c.f. la note en fin de sujet pour connaitre la commande à exécuter).
- **O** devra ajouter un *job* `test-O` dans le fichier '.gitlab-ci.yml' qui instancie le *stage* `test`. De même pour **X** avec un *job* `test-X`. Ces *jobs* produiront un *artifact* contenant le fichier 'game.txt' en cas de succès.
- Fusionnez vos 2 *MR* `rules-O` et `rules-X` dans l'ordre que vous voulez.

## Début de partie

- **O** joue son premier coup dans une *MR* `first-valid` (sans passer par une *Issue*), et **X** vérifie que les tests de la *CI* passent avant de fusionner la *MR* `first-valid` de **O**
> **Note**
> Si nécessaire, **X** demande à **O** de corriger la *CI* dans la revue de code.
- **X** joue ensuite un coup invalide dans une *MR* `first-fail` (sans passer par une *Issue*), et **O** vérifie que les tests de la *CI* échouent
> **Note**
> Si nécessaire, **O** demande à **X** de corriger la *CI* dans la revue de code.
- **X** corrige son coup pour qu'il soit valide dans sa *MR* et pousse à nouveau ses modifications. **O** la fusionne si tout a bien.
> **Warning**
> On vous demande de conserver tous les *pipelines* dans votre dépôt **GitLab**, et en particulier ceux qui échouent !

## Fin de partie

- Ajouter une règle dans la *CI* pour détecter la fin de partie, dans un `stage` supplémentaire.
- Finir la séquence de jeu avec un minimum de *MR* en faisant apparaître la victoire de l'un des deux joueurs.
> **Note**
> Vous pouvez vous mettre d'accord sur la séquence à réaliser dans la discussion associée à l'une de vos *MR*.

## Base de code en Python

Pour vous aider dans l'écriture de vos tests, voici un exemple de code écrit en Python (essentiellement par l'IA *Copilot* !)

- Pour charger le fichier 'game.txt' dans une liste de caractères :

```python
# Load game from file
def load_game(name):
    game = [''] * 9
    file = open(name, "r")
    for i in range(1, 10):
        game[i-1] = file.read(1)
        if i % 3 == 0:
            file.read(1)  # end-of-line
    file.close()
    return game
```

- Pour le test à mettre en place par **X** :

```python
# Check if the game is valid
def valid_game(game):
    # 1. check if the game is a list of 9 characters
    if not isinstance(game, list):
        return False
    if len(game) != 9:
        return False
    # 2. check if the game contains only 'X', 'O' or '.'
    for i in range(0, 9):
        if game[i] != 'X' and game[i] != 'O' and game[i] != '.':
            return False
    # 3. check if #('O') == #('X') or #('O') == #('X') + 1
    x_count = 0
    o_count = 0
    for i in range(0, 9):
        if game[i] == 'X':
            x_count += 1
        elif game[i] == 'O':
            o_count += 1
    if o_count != x_count and o_count != x_count + 1:
        return False
    return True
```

- Pour le test à mettre en place par **O** :

```python
# Check if one turn has been made
def one_turn(game_old, game_new):
    move_count = 0
    for i in range(0, 9):
        if game_old[i] != game_new[i]:
            move_count += 1
    if move_count == 1:
        return True
    return False
```

Ce code a été testé avec le fichier 'game-new.txt' suivant :

```txt
X.O
XO.
X..
```

et avec le fichier 'game-old.txt' suivant :

```txt
..O
XO.
X..
```

et avec la séquence suivante :

```python
game_old = load_game("game-old.txt")
game_new = load_game("game-new.txt")

assert valid_game(game_old)
assert not valid_game(game_new)  # more 'X' than 'O'
assert one_turn(game_old, game_new)
```

- Pour le test de fin de partie :

```python
# Check game (return 'X' or 'O' or '.')
def check_game(game):
    # check rows
    for i in range(0, 9, 3):
        if game[i] == game[i+1] == game[i+2] and game[i] != '.':
            return game[i]
    # check columns
    for i in range(0, 3):
        if game[i] == game[i+3] == game[i+6] and game[i] != '.':
            return game[i]
    # check diagonals
    if game[0] == game[4] == game[8] and game[0] != '.':
        return game[0]
    if game[2] == game[4] == game[6] and game[2] != '.':
        return game[2]
    return '.'
```

Enfin, lorsque vous êtes sur une branche (associée à votre *MR* par exemple), pour récupérer le contenu du fichier 'game.txt' dans la branche `main` (dernière situation validée), vous pouvez utiliser la commande :

```sh
git cat-file -p origin/main:./game.txt > game-old.txt
```

> **Warning**
> Vous devez impérativement utiliser l'image *Docker* `python:3.10` ! De plus, la durée du *pipeline* pour ce projet étant normalement inférieure à **10 secondes**, vous ne devriez donc pas attendre plus d'**1 minute** pour que votre *CI* s'exécute. Ainsi, l'activité des 3 runners est enregistrée, et vous êtes responsable du contrôle des ressources allouées à vos tests d'intégration continue. Vous serez sanctionner dans la notation en cas d'abus !

## Barème indicatif

- [+2pt] pour le fork du dépôt initial et respect des consignes associées.
- [+8pt] pour mise en place des deux premières *MR* avec la *CI* associée aux deux *jobs* de validation. Montrez que vous avez effectué une relecture croisée.
- [+6pt] pour mise en place d'une *Issue* et de la *MR* associée pour chacun des coups joués. Le graphe des commits devra refléter un workflow **GitLab** propre.
- [+4pt] pour la séquence de fin de partie et terminaison.
- [-2pt] par commit direct dans la branche `main` ou par *pipeline* effacé manuellement, ou en cas de non respect des consignes du *fork* !
