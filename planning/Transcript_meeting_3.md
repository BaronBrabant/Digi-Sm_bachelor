
# Transcript of fourth interview recorded. Transcribed with the assistance of Fireflies.ai and then corrected by hand

## Date of interview 24/03/2022

<font size="4">*Benjamin:*</font> On va faire, je pense, comme la dernière session, on va passer vite fait à travers les changements depuis la dernière session. J'ai pas réussi à finir le sprint 3, parce que le Drag and Drop m'a pris un peu plus de temps que ce que je pensais. Mais j'ai réussi à la fin et j'ai implémenté presque la plupart du reste. Vous avez accès?

<font size="4">*Matton:*</font> Oui.

<font size="4">*Benjamin:*</font> J'ai ma petite liste qui est à côté. Dans la première temps, vous avez dit qu’on doit pouvoir arranger la liste et que ça soit persistant. Ça m'a pris un  peu de temps, mais on peut faire du Drag and Drop sur les user stories. Si on ne change pas de page et qu'on revient, on peut voir. On va échanger le 7, le 3.
Mais en gros, j'ai fait une fonction à Ajax, qui reload la table et qui le renvoie au backend a chaque fois qu'on clique sur quelque chose d'autre. Après, il y avait le problème, à chaque fois qu'on se déconnectait, on rentrait dans la page, et le “aspect ratio” des charts partait dans tous les sens. Ça aussi, j’ai fixe.
Après, dans un prochain temps, on avait parlé de changements au niveau de la création.
Maintenant, j'ai enlevé les radio-buttons. J'ai mis en bas ce que ça devrait être, si on utilise la méthode agile, mais on peut rentrer n'importe quel integer.
Ok, donc aussi, après, je vais changer le code. Je vais devoir dire quand on crée un nouveau sprint. On peut sélectionner les user stories qu'on veut.
De plus j'ai changé en créant les sprints il fallait arriver directement dans le dernier sprint, au lieu de nous remettre toujours dans le premier sprint, et devoir cliquer par là.

<font size="4">*Matton:*</font> juste la je t'interrompt, mais la liste qui est affichée là, c'est la liste des... des user stories du sprint en cours.

<font size="4">*Benjamin:*</font> Oui, c'est ça. Donc, si on vient ici, alors, ça reload la liste des user stories (click sur le sprint).

<font size="4">*Matton:*</font> Et on voit où, à quel sprint on a cliqué, quel sprint on a sélectionné? Là, tu clic sur le sprint 2, et puis 4, mais je ne vois pas dans quel sprint on est faut peut être l’afficher.

<font size="4">*Benjamin:*</font> Ok donc si ça vous va je vais faire un petit highlight dans la timeline.

<font size="4">*Matton:*</font> Ouais par exemple ca suffit

<font size="4">*Benjamin:*</font> Mettre une petite couleur. Ok. C'est ça. Donc, après, poker score, champs de texte. Ok, oui, donc depuis la dernière fois, maintenant, il y a la possibilité de rajouter des utilisateurs en amis. Ici, on peut envoyer une demande a lonelyWorkerTest. On envoie la requête. Donc, après, ici, on va aller de l'autre côté, sur le compte de lonelyWorkerTest. Et donc la on a une petite notification qui apparaît avec après une notification qui dit, qu’on a été invité à ce projet-ci avec l'option alors de l'accepter ou de refuser. Et donc, je n'ai pas encore fini d'implémenter, parce que, en fait, je vais utiliser ici cette même page pour aussi... Pour aussi gérer, en fait, les listes d'amis et les requêtes demande d'amis, en fait.
Donc, pour accepter et ajouter quelqu'un. Il va y avoir une petite page ici en bas avec la liste d'amis où on pourra directement cliquer sur qui on va rajouter au projet. All right. Et, ouais, sinon, à part ça, c'était surtout beaucoup d'adaptation dans le back-end. Donc, c'est des choses qui ne se reflètent pas forcément dans le front-end directement. Sauf à travers le fait que ça ne crash pas autant. Mais, ouais, mais je pense que c'est plus ou moins ça. Donc, oui, il reste environ un peu plus d'une semaine. Donc, jusqu'à là, en fait, il reste plus que les notifications à rajouter. Et puis, de changer un tout petit peu le look, surtout, par exemple, des messages d'aides, qui sont encore un peu... un peu moche, on dirait.

<font size="4">*Matton:*</font> Ouais.


<font size="4">*Benjamin:*</font> Mais, sinon, je pense que c'est plus ou moins ça. Et j'allais juste rajouter aussi potentiellement, en tant que créateur du projet, d'avoir accès à des fonctionnalités un peu plus spécifiques pour pouvoir enlever un utilisateur ou des choses de ce genre-ci. Mais, normalement, c'est déjà un peu le cas, puisqu'on peut bloquer un utilisateur d'avoir accès au projet, en fait. Ce qui est un peu équivalent, je pense.
All right. Ben, je pense que c'était le grand... La grosse partie de ce qui a changé. Et donc, oui, enfin, on arrive vers la fin et je voulais juste en fait vous demander si, pour l'instant, le timeline, comme ça, ça vous va. Parce que je pensais juste un tout petit peu que si on a beaucoup de sprints, ça risque de devenir un peu chaotique.
Et donc, de peut-être aussi implémenter le système de era, en fait, de pouvoir regrouper des sprints ensemble.

<font size="4">*Matton:*</font> Moi j’imagine d'ajouter on va dire sur l'écran, jusqu'à une certaine limite, ou, par exemple, au-delà de... Tu sais dans le design du comment ça donne, à partir de je sais pas 6 ou 7 sprint, peut être même le 5ème, ça sera déjà trop. Et alors, à partir de là, on les rapproche quand on en rajoute, et puis quand on en rajoute encore des suivants, d'implémenter un système de scroll , qui avec un overflow qui va en dehors de l'écran à gauche, et si possible, une petite barre de défilement qui permet de revenir en arrière. 
Pour moi, ça me paraît le plus simple et le plus intuitif, et ça permet d'éviter de refaire une refonte graphique complète du système.

<font size="4">*Benjamin:*</font> Ok, ok. Et donc, après, j'avais juste une petite question par rapport surtout à l'organisation des fichiers. En fait, surtout pour les routes ici, enfin, je sais pas si c'est... Par rapport à des vrais projets professionnels, si c'est très approprié d'avoir des déficits de 1100 lignes, ou bien, si je devrais essayer de diviser ça et de mettre par exemple tout ce qui n'est pas du flask dans un fichier à part et de simplement les importer.
<font size="4">*Matton:*</font> Effectivement, l'idéal, ça aurait été d'avoir une distinction un peu plus... Une modularité, en quelque sorte, un peu plus importante. Après, honnêtement, oui, ça peut être pas mal de l'adapter, etc.
Si, si, tout te rend compte, parce que t'as quand même lister pas mal de trucs que tu veux encore faire cette semaine, si ça ne se fait pas, c'est  pas de dramatique, non plus. Après, c'est clair que la partie qualité du code a une importance aussi dans le projet. Mais essayer, peut-être, oui, essayer d'un peu mieux... Repartir, oui, sur différentes routes. Si tu dis, effectivement, qu’il a différentes parties qui sont… qu’il y a une fonction qui n'est pas forcément une route non plus, de les mettre dans des fichiers à côté. C'est effectivement un gros fichier, on a l’impression un petit peu du mélange et pas uniquement de la gestion de route.

<font size="4">*Benjamin:*</font> Mais donc, oui, donc, j'imagine séparer les routes, en fichier séparé, ça serait un peu plus délicat.

<font size="4">*Matton:*</font> Comment?

<font size="4">*Benjamin:*</font> De... enfin, ici, toutes les fonctions, tout ce qui n'est pas du flasks, c'est assez facile, on peut le mettre dans un autre fichier et les importer. Mais pour les routes flask dans des fichiers séparées, ça risque d'être un peu plus délicat.

<font size="4">*Matton:*</font> j'ai pas une suffisamment bonne expérience, sur le framework, donc ça je ne saurais pas directement te dire, ce qui est le plus compliqué ou pas, mais j'ai parlé de manière générale de... De... De... de modularité. Et donc, je pense au serveur node.js, aussi, où il y a beaucoup de routes. On va essayer vraiment de distinguer les différentes routes en fonction de... par thématiques, tout ce qui concerne les routes liées à la gestion d’utilisateurs, les routes purement liées au API, d'une telle partie. Enfin voilà, un peu distinguer par thématiques, ca permet aussi, après de se retrouver, et que finalement, quand on complète, et on enrichit l'application, on va rajouter une thématique, et donc, du coup, on rajoute un nouveau... Un nouveau fichier, de manière spécifique à la thématique en question, ou genre de choses, quoi. Mais voilà, mais je sais pas à quel point, c'est modulable, à ce point là aussi, avec ce framework là, donc voilà.



<font size="4">*Benjamin:*</font> Je vais faire comme vous avez dit, alors je vais me concentrer sur le plus important, et regarder si, et comment c'est faisable alors.

<font size="4">*Matton:*</font> Ok oublie pas de garder quand même un peu de temps, sur le debugging, etc. Et que ca reste toujours le plus important d’avoir des fonctionnalités, qui marchent et qui ne plombent pas à la moindre utilisation, qu’un truc qui est un peu plus riche, mais avec plein de bugs partout, quoi.