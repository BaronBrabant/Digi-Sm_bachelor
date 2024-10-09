
# Transcript of second interview recorded. Transcribed with the assistance of Fireflies.ai and then corrected by hand

## Date of interview 06/12/2022

<font size="4">*Benjamin:*</font> Voilà. Je voulais juste commencer, vite fait, par vous demander, parce qu'on a eu un cours sur les licences, est-ce que vous voulez qu'elle soit permissive, ou non permissive?

<font size="4">*Matton:*</font> Du MIT ou du GPLv3

<font size="4">*Benjamin:*</font> Ok, c'est parfait, parce que j'ai déjà utilisée quelques composants, mais c'était tous des MIT,

<font size="4">*Matton:*</font> c'est très bien.

<font size="4">*Benjamin:*</font> Merci, alors je vais faire une petite démonstration de ce que j'ai déjà commencé. Voilà, d'abord j'ai fait une interface assez basique de login, un petit message, de manière à pouvoir login et se registrer comme de l'utilisateur.
Puis j'ai fait une page intermédiaire en fait où on peut gérer tous les projets qui sont en cours ou bien qui sont finis. Et puis une fois qu'on clique sur un projet, ça ouvre cette page, où nous avons ici en bas à gauche, une petite boîte qui contient alors le nom des user stories que nous avons déjà établi. Et une fois qu'on clique dessus, en fait, il y a un petit pop-up qui contient la description, donc le texte lui-même du user story en fait. De manière à ce que ça ne prenne pas trop de place.

<font size="4">*Matton:*</font> Ok

<font size="4">*Benjamin:*</font> Le user story ici, je veux pouvoir l'utiliser comme une checklist aussi et pouvoir regarder les tâches qui sont encore à accomplir du point de vue des user stories et pas directement des tâches individuelles. Donc aussi l'habileté de changer de statut en done, doing ou to do. De plus, il y avait le user story qui disait que, en tant que développeur junior, je voudrais aussi l'utiliser comme un outil d'apprentissage. Et donc pour ça, en fait, j'ai ajouté des petites icônes d'aide ou quand on clique dessus quelque chose se passe qui ne devrait pas se passer. Ok, excusez-moi, il y a une petite erreur avec la base de données pour l'instant, mais en fait ça affiche au-dessus de toute l’interface.
Oui, juste un petit boite avec écrit, OK, poker score, c'est a ca que ca sert, c'est comme ça qu'on l’utilise.

<font size="4">*Matton:*</font> Très bien, oui.

<font size="4">*Benjamin:*</font> Et bien oui, donc ça, c'est pas encore implémenté, mais donc l'idée c'est qu'en fait, cette timeline est toujours là. Et en fait, quand on vient cliquer sur Sprint 1, Sprint 2, Sprint 3, ça va charger la liste des tâches individuels pour chaque Sprint.

<font size="4">*Matton:*</font> Ok.

<font size="4">*Benjamin:*</font> Et puis après, c'est surtout des fonctionnalités de base, donc c'est-à-dire le login, regarder son profil, ou bien rajouter des nouveaux users stories. Et aussi une user list, afin de pouvoir regarder tous les utilisateurs qui travaillent sur le projet en cours, mais ça je ne suis pas encore sûr de le laisser une page à côté ou bien de rajouter une petite boîte ici.

<font size="4">*Matton:*</font> Ca tu peux le mettre dans une page à côté parce que ce n'est pas vraiment quelque chose qu’on va aller voir régulièrement, donc...
<font size="4">*Benjamin:*</font> Ok. ...

<font size="4">*Matton:*</font> Ça peut être une page indépendante.

<font size="4">*Benjamin:*</font> Ok. C'est ce que je pensais, donc... Ouais. Et donc les prochaines étapes, par rapport à au user stories qui a déjà établie pour ce Sprint, donc c'est le fait d'avoir une checklist qui est presque finie. Le fait d'avoir des... que ça soit aussi un outil d'apprentissage. Donc au fur et à mesure du développement du code, je vais rajouter à chaque fois que c'est pertinent des petites bulles un peu partout, de manière à ce qu'on puisse...

<font size="4">*Matton:*</font> Ouais, très bien.

<font size="4">*Benjamin:*</font> Donc les tâches peuvent déjà être marquées, mais l'état des Sprints ne peut pas encore être changé, ça va arriver aussi à la fin de ce Sprints. Et puis, oui, le dernier user-stories, c'est celui qui requiert encore tout petit peu de travail, car pour l’instant j'ai établi une page de projet, une page de tâches et des Sprints individuels. Mais en fait, c'est juste des données pré-faites, push dans la base de données. Donc je dois juste faire des boutons pour pouvoir les rajouter.

<font size="4">*Matton:*</font> Ouais, ça va.

<font size="4">*Benjamin:*</font> Et, ouais, est-ce que vous voyez quelque chose d'absolument horrifique à ne pas faire?

<font size="4">*Matton:*</font> Il y à un truc, c'est dans la liste des projets, il y a une colonne due date et cette colonne la ne doit pas exister, puisque priori un projet, ce n'est pas de date de fin. Il continue de Sprints en Sprints, et puis à un moment,on dit ok, on s'arrête ici.

<font size="4">*Benjamin:*</font> Ok.

<font size="4">*Matton:*</font> Je veux dire le backlog, la liste des tâches à réaliser est vide et on s'arrête comme ça. Donc, du coup il n'y a vraiment pas de due date pour un projet. Donc,  là, on peut juste retirer la colonne. Sinon, non, pour le reste, c'est pas mal. On a parlé d’une intégration trello,  donc du coup on laisse tout à fait côté. Ta implémenter les différentes features la dessus donc…

<font size="4">*Benjamin:*</font> En fait, j'avais commencé un peu avec ça, et puis je me suis rendu compte de notre conversation, que ça ne servait pas vraiment de trello. Et donc, je pensais en fait juste compacter ça un peu petit peu, et au lieu de mettre, ouais, en fait, peut-être enlever le poker score, regarder ça juste avec les user stories, comme ça, au lieu d'avoir les tâches individuelles, ok, par exemple, le programme et la base de données, ou le programme et ça et ça, que ça soit plus vague avec les user stories. Donc, en tant qu' utilisateur, je voudrais pouvoir faire ça, et puis, alors que l'équipe puisse voir ok, cette user story a déjà été finie, même si elle est composée de 4 ou 5 tâches différentes, par exemple.

<font size="4">*Matton:*</font> J'ai pas saisi, donc, l'idée, c'est de garder cette liste-là, mais modifier la structure, alors.

<font size="4">*Benjamin:*</font> C'est de... C'est de... En fait, parce que c'est user stories qui sont ici, enfin, comme j'ai lu la théorie où vous m'avez appris, ça doit rester assez vague. Ça ne doit pas vraiment aller totalement dans les détails techniques.

<font size="4">*Matton:*</font> Non, ça ne va pas être technique, mais c'est pas pour autant que ça doit rester vague, et c'est que ça doit être lié à une fonctionnalité du logiciel, de ce qui est développé, mais ça ne va pas avoir des informations techniques dedans. Que quelqu’un non-techniques puisse le comprendre. Mais ça doit quand même être relativement précis et vraiment viser une fonctionnalité bien spécifique du projet.
Donc, mais c'est vrai que dans un sprint, on peut avoir une user story et après la découpe en tâche technique spécifique. Donc ça, c'est possible effectivement, mais... Mais du coup, faire ça, c'est un pic du coup de quand même regarder quand on fait des tâches, que ce soit toujours lié à une user story en particulier. Parce que le truc, pas qui m'inquiète, mais c'est que la liste de user story, enfin, la liste qui est représenté ici, et bien,ca va être compliqué de rajouter plein de fonctionnalité en plus, d'ajouter des éléments liés, enfin des listes de tâches on va dire lié à des user story, etc. Ça va être plus complexe à mettre en place.
Et donc, je resterai du coup à ce stade- ci de garder des user stories dans le tableau et rester au niveau user story.
Du coup il faudra l’adapter, si tu reviens sur l’interface. Parce que du coup, dans la colonne name, ca sera en fait la liste de user story en question. Donc, à mon avis la colonne doit être beaucoup plus large. Et en fait, je pense que ce que je ferai au niveau de l'interface, c'est soit élargir et que la petite boîte prend toute la largeur. Ou un truc qui pourrait être intéressant, c'est au lieu d'avoir une fenêtre qui prend toute la page pour l'aide, etc. Mais d'avoir vraiment sur la partie de droite, l'aide qui s'affiche.
Mais je réfléchis, voir un petit peu avec les user stories, je veux dire plus classique. Ça peut être celle que tu a écris ici pour le projet. C'est de les mettre dans la colonne name et voir comment ça se présente. si c'est sur 4 lignes, les user story classiques ca n’ira pas, il faut un truc plus large. La colonne poker, elle peut être réduite beaucoup plus, c'est juste un seul chiffre. Ou limite, même pas obligé d'avoir une colonne en elle-même, mais juste à côté du bouton to do, par exemple, juste un petit icone, avec un numéro avec le poker score, c'est tout quoi.

<font size="4">*Benjamin:*</font> Ok.

<font size="4">*Matton:*</font> Et alors pour action aussi, je mettrai aussi un icône qui est de modification genre un petit crayon, ou plutôt un de icônes classiques, motifs. Tu te veux qu'à avoir le texte modify aussi.

<font size="4">*Benjamin:*</font> Oui, là, je pense que peut-être faire une espèce de drop-down list, puisque de par après, il va y avoir plus d'action comme delete.

<font size="4">*Matton:*</font> Après oui, oui. Enfin, après, il ne va pas trop beaucoup d' actions, parce que ce qui va surtout changer c'est le statut, si c'est to-do, in progress, done. Mais voilà, je ne sais pas, même les supprimer, a priori, on ne supprime pas les user story.
Ou alors, tu peux garder aussi, je ne sais pas.
Alors, comment ta fait la relation entre le backlog de produits et celui des sprints? Parce que du coup, le backlog de produits c'est l’ensemble des user stories pour tout le produit et le backlogs des sprints, c'est le sous ensemble du backlog du produit. Est-ce qu' il y a un backlog de produits qui est du coup imaginé dedans ou pas du tout?

<font size="4">*Benjamin:*</font> Donc ça, c'était en fait... Je pense... Donc ça, c'était en fait pour le prochain sprint

<font size="4">*Matton:*</font> c'est vrai. Donc là, c'était... et tu l'imagines comment du coup.
<font size="4">*Benjamin:*</font> En fait, j'ai fait... Donc, à travers ma base de données, je peux juste filtrer à travers le projet avec l'ID et trouver tous les sprints pour...
Donc en fait, j'ai fait une table projet, sprints et puis tâches. Et donc, en fait, il suffirait de regarder avec l'ID du projet tous les sprints qui existent et puis de tous ces points là, sortir toutes ces tâches pour créer un backlog… enfin un burn-down chart général.

<font size="4">*Matton:*</font> Ok, mais pour l'instant, il n'y a pas encore l'interface vraiment pour créer, enfin, pour visualiser le backlog de produits.

<font size="4">*Benjamin:*</font> Oui c'est ça.

<font size="4">*Matton:*</font> Ok, ça sera pour la suite alors. Parce que du coup, l'idée, en fait, ce serait bien... D’une manière ou d’une autre, en sélectionnant un sprint de données, d’avoir une vue, par exemple, qui est de sélectionner les backlogs de enfin les user stories du produit backlog, en cochant ou ce genre de trucs la.
Typiquement, dans la phase de sprint planning, c'est un peu ça qui se fait: on rentre toutes les user stories et on sélectionne celles qu’on veut pour le sprint.

<font size="4">*Benjamin:*</font> Ok.

<font size="4">*Matton:*</font> Et donc du coup d’avoir une vue pour juste créer le backlog des user stories du produit.

<font size="4">*Benjamin:*</font> Ok. Donc, c'est-à-dire en gros juste une page où vous pouvez voir tous les backlogs, en créer de nouveau et après sélectionner et dire, ok, je veux celui-là, celui-là, celui-là, dans sprint 1, celui-là, dans sprint 2.

<font size="4">*Matton:*</font> Non, parce qu' en fait, ça se fait de manière incrémentale.
Ici là, tu vois, il est à plusieurs, si tu reviens sur ta vue, en gros la telle que c'est le projet il est dans le sprint 4. Parce qu'en gros, tu n'anticipes pas normalement les sprint suivants. Ici là, tu fais, en gros, je vais faire un premier sprint, un deuxième sprint etc. Mais ce n'est pas le genre de choses qui ce dont. C'est vraiment, on commence un nouveau sprint, on commence, supposons ici, on commence le sprint 4.

On va choisir, ok, quels sont les différents items du backlog qu’on va sélectionner et puis on arrive à faire le sprint 4, on va commencer le nouveau sprint. Donc on va faire la même chose à ce moment-là, ok, on va commencer le sprint 5, qu'est-ce qu'on va mettre dans le backlog du sprint 5. Mais on ne va pas, genre se retrouver 3 sprints plus loin, on va faire sprint par sprint.

<font size="4">*Benjamin:*</font> Ok.

<font size="4">*Matton:*</font> Et donc du coup, en fait là, est la vue de pouvoir voire ce qu’on a fait dans le sprint précédent. Mais finalement, la seule partie vraiment intéressante,c'est ce qu’il y a après le sprint 4.

<font size="4">*Benjamin:*</font> Ok

<font size="4">*Matton:*</font> Et donc, du coup, dans les buttons au-dessus il doit y avoir un button produit backlogs. Donc, on a vraiment toutes les user-stories du backlog de produit, et qui sont en fait les user-stories qui sont encore à faire.

<font size="4">*Benjamin:*</font> Ok. Ok. Donc une page bien claire comme ça, on peut construire les sprints.

<font size="4">*Matton:*</font> Oui, c'est ça, enfin mon, par forcément pour le sprint mais pour le backlog du projet entier, et où il y a un bouton ou on peut alors commencer le sprint planning, qui est donc la partie où on va  cocher les différentes user-stories du backlog de produit, qu'on va réaliser dans ce sprint.

<font size="4">*Benjamin:*</font> Ok. Ok, ça c'est clair. Ok. Je pense que, alors, je vais juste vous montrer ce que je comptais faire pour le prochain sprint. Donc, après, le premier, c'était de l'utiliser comme un log pour scrums et les évents afin de communiquer avec l'équipe. Et donc, ça, je pensais créer littéralement juste un historique de ce qui est fait, et de reprendre ces données-là pour après dire ok l'évolution du projet au fur et à mesure du temps. Peut-être regarder en fonction du poker score, s' il a augmenté ou réduit petit à petit. Le deuxième, c'était d'accéder à toutes les user-stories main, donc ça c'est ce que vous venez de dire. Comme ça, ça peut m'aider à choisir le prochain sprint.
Ça, c'est pour les métriques, ça veut dire, avant des petits burn-down charts, de pouvoir sélectionner pas seulement le sprint dans lequel on est, mais peut-être, de dire, ok, a quoi ça ressemble pour les 4 derniers sprints qu’on a fait. Et finalement, ça, c'était aussi en relation avec l'apprentissage, donc, avoir un système de notification qui dit, ok, vous n'avez pas coché la petite boîte que vous étiez au daily sprint pendant deux jours. Peut-être avec une petite explication, pourquoi c'est mauvais pour essayer de développer les habitudes de l'utilisateur.

<font size="4">*Matton:*</font> Moi, ça va très bien.

<font size="4">*Benjamin:*</font> Ok. Vous avez encore une question?

<font size="4">*Matton:*</font> Non, c'est tout. Non, c'est pas mal, ca donne bien, c'est déjà une bonne base. Ça va dans le bon sens.

<font size="4">*Benjamin:*</font>  Ok, enfin, juste une petite dernière question de ma part alors. Donc le meilleur, c'est quand même de travailler en pourcentage, en point de vue position HTML, ou je mets des pixels fixe.

<font size="4">*Matton:*</font> Ouais, ouais, effectivement. Tu veux avoir du plus responsif possible, c'est mieux en pourcentage, ou de manière générale, ou en pourcentage, ou en relatif.

<font size="4">*Benjamin:*</font> Ok. Ok, merci beaucoup alors.

<font size="4">*Matton:*</font> Pas de soucis.

<font size="4">*Benjamin:*</font> J'ai un peu de travail pour l'hiver, alors.
