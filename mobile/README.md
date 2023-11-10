# Setup de l'appli 

## Cloner le repo  

`git clone https://gitlab.com/InseeFr/social-statistics/budget.git`  


## Installation de flutter  

Téléchargez Flutter depuis https://docs.flutter.dev/release/archive
Actuellement,l'application utilise la version 3.10.6. Une mise à jour vers la dernière version est prévue avant les tests à plus grande échelle. 

1. **Extraction du fichier zip :**
   - Téléchargez le fichier zip de Flutter depuis [https://docs.flutter.dev/release/archive](https://docs.flutter.dev/release/archive).
   - Extrayez le contenu du fichier zip.

2. **Placement de Flutter dans l'emplacement d'installation souhaité :**
   - Choisissez l'emplacement d'installation souhaité pour le SDK Flutter (par exemple, `%USERPROFILE%\flutter` ou `D:\dev\flutter`).
   - Déplacez le contenu extrait de Flutter vers cet emplacement.

Assurez-vous que l'emplacement d'installation choisi est accessible et que vous avez les autorisations nécessaires.

3. **Mise à jour des variables d'environnement (si nécessaire) :**
   - Ajoutez le chemin vers le répertoire `bin` de Flutter à votre variable d'environnement `PATH`.
     - Exemple : Si Flutter est installé dans `%USERPROFILE%\flutter`, ajoutez `%USERPROFILE%\flutter\bin` à la variable d'environnement `PATH`.

Vous devriez maintenant avoir Flutter correctement extrait et installé à l'emplacement de votre choix. Pour vérifier que tout est configuré correctement, vous pouvez exécuter la commande `flutter doctor`.
    

Vérifiez que Flutter fonctionne correctement : `flutter doctor`. Résolvez tout problème détecté par cette commande 

## Configurer le périphérique Android
Avant de pouvoir utiliser l'application, vous devez activer le mode développeur et le debogage USB sur l'appareil. Pour cela, accédez aux paramètres de l’appareil, puis dans « À propos du téléphone »  ou équivalent
Tout en bas, tapotez 7 fois « numéro de build ».
Un message vous indique que les options pour les développeurs sont apparues dans le menu « Système » des paramètres. 
Le menu Options pour les développeurs apparaîtra dans la partie Système des Paramètres. Depuis ce menu, il vous sera possible d’accéder à différentes options notamment l’accès au débogage USB (il faudra surement défiler un moment avant de trouver l'option)

Connectez un appareil Android avec le débogage USB activé ou utilisez un émulateur (voir plus bas). Exécutez `flutter devices` pour vérifier que le périphérique est bien reconnu.

## Installer Android Studio
Flutter dépend d'une installation d'Android Studio pour fournir les dépendances Android même si ce n'est pas nécessaire pour le développement

Télécharger et installer [Android Studio](https://developer.android.com/studio). Normalement cela installera les dernières versions d'Android SDK, Android SDK Command-line Tools et Android SDK Build-Tools, nécessaires à Flutter.
Pour Windows, il faudra également installer [Google USB Driver.](https://developer.android.com/studio/run/win-usb)

Exécuter 'flutter doctor' pour confirmer la localisation d'Android Studio. Si Flutter ne peut pas le localiser, exécutez 
```bash
flutter config --android-studio-dir=<répertoire>` 
```
pour définir le répertoire où Android Studio est installé.

Ouvrez un terminal exécutez la commande suivante pour accepter les licences Android.
```bash
flutter doctor --android-licenses 
```

### Installer un simulateur Android
Si vous ne disposez pas d'appareil Android, vous pouvez passer par un émulateur. Ce n'est pas conseillé car les émulateurs ne gèrent pas la caméra et utilisent les ressources du PC pour fonctionner. 

1. Lancer Android Studio et ouvrir le projet (`budget/app`), cliquer sur l'icône Gestionnaire de périphériques, et sélectionner Créer un périphérique sous l'onglet Gestionnaire de périphériques... Sélectionnez "Créer un périphérique"
2. Choisir un type d'appareil et sélectionner Suivant
3. Sélectionner une ou plusieurs SDK pour les versions d'Android que vous souhaitez émuler, puis cliquer sur Suivant
4. Sous Emulated Performance, sélectionner Hardware - GLES 2.0 pour activer l'accélération matérielle
5. Vérifier que la configuration de l'émulateur, puis cliquer sur Terminer
6. Dans le Gestionnaire de périphériques virtuels Android, cliquer sur Lancer dans la barre d'outils


## Build et lancement l'application

Dans `budget/app` : `flutter build bundle` devrait fonctionner correctement (on peut ignorer les divers warnings).
Pour exécuter l'application : `flutter run`



