
# Transcript of third interview recorded. Transcribed with the assistance of Fireflies.ai and then corrected by hand

## Date of interview 10/03/2022


<font size="4">*Benjamin:*</font> Je vais commencer l'enregistrement aussi, si ça ne vous dérange pas. Je vais lancer un partage d'écran, je pense on va s'y prendre un peu comme on a fait jusqu'à maintenant. Oui, voilà, parfait. La première chose qui vient en tête depuis la dernière fois, j'ai changé les icônes ici pour avoir quelque chose d'un peu plus parlant. J'ai aminci la colonne des pokerScore. Ici, toutes les dates de remise  des sprints, j'ai tout enlevé. J'ai rajouté un petit icon qui dit ici on peut avoir les sprints potentiels des futures. J’ai remplacé les dates intermédiaires par les dates de création des sprints comme ça on a une idée assez générale quand le sprint a été créé.

<font size="4">*Matton:*</font> Oui, c'est très bien.

<font size="4">*Benjamin:*</font> Oui, donc après ici j'ai rajouté, il n'est pas encore fini mais c'est un prototype d'un burn-in-chart.

<font size="4">*Matton:*</font> Oui, très bien.

<font size="4">*Benjamin:*</font> Avec une petite option pour regarder en fonction du sprint, juste pour un sprint, qu'est-ce qui reste comme tâche, avec l’option to-do, done et doing. Après, l'implémentation n'est pas encore complètement finie mais j'ai rajouté une fonctionnalité pour envoyer des demandes. Maintenant, si on clique sur Team. Ici, on a une liste d' utilisateurs qui sont déjà sur le projet. Ici, on a un petit bar qui permet alors d'envoyer une demande pour rejoindre un projet à un autre utilisateur.

<font size="4">*Matton:*</font> ok super.

<font size="4">*Benjamin:*</font> Je vais faire ça directement et puis aussi de par après juste ici en dessous. Toutes les tables sont déjà dans la base de données mais je vais juste encore remplir la fonctionnalité d'avoir une liste d'amis.
Comme ça, ça serait une manière de rapidement choisir les personnes qu'on connaît déjà pour les rajouter à un projet.

<font size="4">*Matton:*</font>Oui.

<font size="4">*Benjamin:*</font> Donc là, vous allez juste voir un tout petit problème que j'ai qui est l' aspect ratio du burn-in-chart que je vais fixer. Mais après, ici, j'ai mis une petite cloche de notification qui permet alors de regarder les demandes pour rejoindre un projet ou bien les demandes d'amis ou on peut alors les accepter et les refuser. Furthermore, la dernière fois, on avait parlé aussi d'une liste de tous les user stories quand on crée un sprint. Et donc en fait, j'ai changé la fonctionnalité pour créer un sprint, ou maintenant, en fait, il va afficher tous les user stories qui ne sont pas encore associés à un sprint.
Et donc après, on peut juste cliquer sur la ligne pour les sélectionner et puis les rajouter à un nouveau sprint qui apparaît alors ici. Sur la timeline.
Qu'est-ce qu'il y a d'autres? Oui, donc ça c'est pour les user stories, ça c'est fait, les burn-in-chart… Excusez-moi, j'ai juste mon doc ici avec la transcription de ce que nous avons fait là d'une fois. Et puis, je pense que c'était surtout le principal pour ce sprint ici.
Excusez-moi, une seconde, je vais juste envoyer un screenshot, je vais juste faire un push pour vous montrer ce qui manque encore des user stories. Ok, parfait. Oui, donc ici le premier sprint effectué, le deuxième, alors, et fait en majorité, il aurait juste, alors, une des fonctionnalités que je déciderais de bouger au sprint d'après. Et en fait, c'est juste l'envoi de notification. Donc ce dont on avait parlé, par exemple, si on ne confirme pas qu'on a été un daily scrum pendant plus que deux jours, alors de recevoir une petite notification automatique.
Et donc, oui, donc ça c'est les Reminder, le fait de pouvoir prioritiser, aussi le fait, en fait, parce que pour l'instant, on a un moyen de...
Au niveau de la création des user stories, d'implémenter le poker score.

<font size="4">*Matton:*</font> Oui.

<font size="4">*Benjamin:*</font> Mais c'est encore une fonctionnalité qui est très... très personnelle, j'ai envie de dire. Donc, c'est-à-dire, pour l’instant, il y a seulement une personne qui peut choisir le poker score, en fait. Et donc là, j'hésite, en fait, ou bien à créer une espèce de fonctionnalité, ou c'est à un vote en ligne où le user story est ajouté dès le moment où tout le monde dans l'équipe à voter son score, ou bien de le laisser comme il est, en fait, et d' assumer que le poker score a été fait sur une autre application, en fait.

<font size="4">*Matton:*</font> Ben, pour l'instant,  on peut éditer chaque user story et adapter la valeur du poker score. Ah Non, on ne sait pas l'éditer.

<font size="4">*Benjamin:*</font> Je peux rajouter ça, en fait.

<font size="4">*Matton:*</font> Parce que ce qu'il faudrait alors, du coup, c'est ne pas le mettre quand on crée un user story qu’il ny ai pas de pokerscore. Enfin, si on peut le laisser, mais avoir la possibilité de laisser vide. Et puis après, dans l'édition de là, pouvoir ajouter un score. Et par contre, je vais mettre pas spécialement, parce que je sais plus quelle valeur il y avait, si tu crées, si tu retournes sur la page création user story il y a 1, 2, 3, 5, 8, 13… Parce que là, moi, j'aime bien aussi avoir le 0 et le ½.
Ouais, mais du coup, ce que je proposerais comme alternative, peut-être plus générique, c'est finalement de pas mettre des boutons radio, mais juste un champ texte d'entrée. Et juste avec l’instruction que c'est des valeurs numériques qui peuvent être décimales. Mais voilà, je ne sais pas si ça change grand chose après dans la présentation derrière, mais à l'utilisation, je pense que c'est plus simple. Et pareil, je pense qu'on a parlé à du “due date”, c'est un champ vraiment qu'on peut retirer complètement.

<font size="4">*Benjamin:*</font> Oui, oui, oui, ça c'est... On est fait, ça je dois l'enlever. Oui, ok. Et puis donc, ouais, et donc en fait, les deux grosses étapes, ça serait... En dernière étape en fait, je voudrais aussi regarder comment je peux communiquer alors avec Trélo pour potentiellement faire ce qu'on avait parlé au début, un import potentiel d'un projet Trélo, mais si ça vous va, je garderai ça comme dernière étape une fois que le reste du site marche en fait.

<font size="4">*Matton:*</font> Dans l'état ou comment développer les choses, je n'implémenterai même pas la partie Trélo parce que finalement, il y a beaucoup de gros éléments de Trélo qui surviennent ici, et c'est essentiellement la liste avec le poker et le statut.
La seule chose que je pense qu'il manque vraiment, je sais plus si on en a parlé ou pas, où s' il y a moyen de faire ou pas, mais de pouvoir en fait réorganiser l'ordre de vos éléments dans la liste. Ca c'est un truc important parce qu'on a en gros de grosses notions de priorité et quelles sont les tâches qui sont plus importantes par rapport aux autres. Et donc il faudrait potentiellement mettre la tâche “test 11” qui soit tout en haut de la liste et test 7 plus bas, enfin, pouvoir réorganiser et que cette organisation soit persistante et visible partout où il y a une liste de tâches comme celle-là.
Et donc là, on a une liste qui serait organisée, mais quand on crée par exemple un nouveau sprint, il faudrait avoir cette liste avec le même ordre aussi qui soit toujours présente. On se dit vraiment, en fait, à la base, on crée un nouveau sprint, on sélectionne les user stories qui sont sur le dessus de la liste. Et comme ça, ça permet d'être sûr que l'ordre est bon et on commence par travailler avec la bonne chose.

<font size="4">*Benjamin:*</font> Et donc, dans ces cas, alors vous préférez une privatisation personnelle ou, enfin, une espèce de drag and drop pour réarranger...

<font size="4">*Matton:*</font> Un drag and drop, ou un bouton,ou peu importe, mais c'est une organisation qui est à l'échelle du projet. Donc, si il y a plusieurs membres dans le projet, organisation est la même pour tout le monde



<font size="4">*Benjamin:*</font> Oui, ok, donc je communique avec la base de données et garder ça quelque part.

<font size="4">*Matton:*</font> Oui, là, c'est ça. Ok, ok.

<font size="4">*Benjamin:*</font> Donc, c'est pas exactement la même chose que de faire un filtre où on peut, alors, par exemple, le filtre et cliquer sur pokerscore.

<font size="4">*Matton:*</font> Oui, non, non, c'est vraiment, c'est pas un sort, vraiment une organisation qui est personnelle et complètement, enfin, dire, qui n'a pas de relation avec un score. C'est un choix arbitraire, d'ordre de trucs, et qui lui est persistant dans le temps.

<font size="4">*Benjamin:*</font> Ok, et donc après, je vais penser alors aux deux plus grosses étapes, entre guillemets.
Je pense que je vais implémenter alors toutes les données des sprints que nous avons fait ensemble comme data dummy. Je pourrais avoir un projet démo. Oui. Et bah, ça serait en fait une fois que les fonctionnalités de base sont finies d'être implémenter, de travailler un peu sur le look du site.

<font size="4">*Matton:*</font> Ouais, très bien, ça ne me parle très bien dans cet ordre aussi

<font size="4">*Benjamin:*</font> ouais. Je vais changer les couleurs, réimplémenter les aspects ratio qui changent dans tous les sens comme ça. Ouais. Les détails pour que ça soit un peu plus plaisant aux yeux, quoi.

<font size="4">*Matton:*</font> Ouais, très bien.

<font size="4">*Benjamin:*</font> Ok, après ça, je sais pas, ça serait plutôt une question ouverte puisqu' on arrive vers la fin.
Est-ce que ça ressemble plus ou moins à ce que vous attendiez ou bien, est-ce qu'il y a quelque chose que vous aimeriez bien avoir différemment, à part bien sûr ici le Drag and Drop de la liste?

<font size="4">*Matton:*</font> Non, sinon globalement, ça rend pas mal. Non, c'est bien. C'est sympa, les grosses fonctionnalités sont dedans, après, il y a toujours moyen de rajouter et d'améliorer le truc, mais je pense qu' ici on arrive à un stade qui est pas mal. Alors, c'est un beau résultat, c'est un beau travail.

<font size="4">*Benjamin:*</font> Ok, alors super. Merci beaucoup. C'est très marrant en tout cas de se lancer dans un projet où, d'un coup, on est un peu en full stack, front end back end.

<font size="4">*Matton:*</font> Ouais, c'est a ca que ca sert aussi.
