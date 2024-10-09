# Description du projet
Le projet consiste en une To-do list qui permet de créer, modifier, annuler des tâches. On peut également mettre des états aux différentes tâches : Fait ou Pas fait. Une base de données sqllite gérée avec Flaskalchemy permet la sauvegarde de données des utilisateurs. Il y a aussi une certaine gestions des inputs pour le nom des identifiants et des tâches.

## Détails des routes HTTP
1. 127.0.0.1:5000/ : application principale
2. 127.0.0.1:5000/delete/<string:key> : utilisé pour supprimer des tâches grâce au bouton delete. Prend l'identifiant de la clé à supprimer en paramètre
3. 127.0.0.1:5000/newTask/ : utilisé pour l'onglet servant à créer une nouvelle tâche
4. 127.0.0.1:5000/modify/<string:key> : permet la modification du nom d'une tâche grâce au bouton Modify. Prend en paramètre l'identifiant de la tâche à modifier
5. 127.0.0.1:5000/check_uncheck/<string:key> : permet de changer une tâche de l'état ToDo à Done. Prend également en paramètre l'identifiant de la tâche concernée
6. 127.0.0.1:5000/register/ : utilisé lors de l'inscription d'un nouvel utilisateur
7. 127.0.0.1:5000/login/ : permet a l'utlisateur d'entrer ses donnees et au system de check si l'utilisateur existe bien
8. 127.0.0.1:5000/logout/ : permet a l'utlisateur de logout de son compte sans perdre ses donnees
9. 127.0.0.1:5000/bloc_user/<string:user1> : permet à l'admin de bloquer des utilisateurs problematiques  
10. 127.0.0.1:5000/admin : permet de voir la liste des utilisateurs. On peut bloquer des utilisateurs qui ne sont pas des admins.
11. 127.0.0.1:5000/change_group/<string:user1> : permet à l'admin de changer le groupe (normal ou admin) d'un utilisateur.
12. 127.0.0.1:5000/profile : permet de pouvoir consulter la base de données pour afficher les informations d'un compte ainsi que de les changer si l'utilisateur le souhaite.

```mermaid
  graph TD;
      127.0.0.1:5000/ --> 127.0.0.1:5000/delete/<string:key>;
      127.0.0.1:5000/ --> 127.0.0.1:5000/newTask/;
      127.0.0.1:5000/ --> 127.0.0.1:5000/modify/<string:key>;
      127.0.0.1:5000/ --> 127.0.0.1:5000/check_uncheck/<string:key>;
      127.0.0.1:5000/ --> 127.0.0.1:5000/register/;
      127.0.0.1:5000/ --> 127.0.0.1:5000/login/;
      127.0.0.1:5000/ --> 127.0.0.1:5000/logout/;
      127.0.0.1:5000/ --> 127.0.0.1:5000/bloc_user/<string:user1>;
      127.0.0.1:5000/ --> 127.0.0.1:5000/admin;
      127.0.0.1:5000/ --> 127.0.0.1:5000/change_group/<string:user1>;
      127.0.0.1:5000/ --> 127.0.0.1:5000/profile;

```

# Comment lancer le projet ? 
Il suffit de se mettre dans le répertoire principal, de créer un environnement virtuel (virtualenv ou conda) qui contient Flask, et de lancer le fichier run.py ($ python3 run.py)


# Pour accéder à la page administrateur :
Sur la page Log-in (la page sur laquelle on commence lors du run.py):
Username : admin
Password : admin123


# Changements par rapport au TP03
Les principales fonctionnalités supplémentaires sont : 
- Une base de données sqllite pour enregistrer les données de utilisateurs à la place d'un simple dictionnaire python
- Une section "Profile" dans la Taskbar pour voir ses infos et les modifier
- La possibilité pour un utilisateur de changer son mot de passe