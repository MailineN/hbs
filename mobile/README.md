# Mobile

## Setup

1. Clone repos  

`git clone https://gitlab.com/tabi/projects/budget.git`  

depends on https://gitlab.com/tabi/projects/packages/questionnaire which should be cloned also and it should be in `../../packages/questionnaire` relative to `budget/app` folder.  

`git clone https://gitlab.com/tabi/projects/packages/questionnaire.git`  

directory structure should look like this :  

```
budget
  app  
packages
  questionnaire
```

Budget and questionnaire have incompatible versions requirements since https://gitlab.com/tabi/projects/packages/questionnaire/-/commit/a26ff195a1bb3fc1757e739cbf2ea2497bc4b3f4 leading to error `Because every version of questionnaire from path depends on font_awesome_flutter ^9.1.0 and budget_onderzoek depends on font_awesome_flutter ^8.11.0, questionnaire from path is forbidden.`.  
Quick fix is downgrading questionnaire to 787db612955a798f6f0380e226984930d3bbb418 (`git checkout 787db612955a798f6f0380e226984930d3bbb418`) 

2. Setup flutter  

Download flutter from https://docs.flutter.dev/release/archive  
Currently latest working version is 2.8.1 (12/16/2021 !) due to a file (https://gitlab.com/tabi/projects/budget/-/blob/master/app/lib/features/menu/menu.dart#L316) in budget being incompatible with https://github.com/flutter/flutter/commit/0a2227c286568674fb72106f277d3b04a5ac75c5 changes

Check flutter is ok : flutter doctor`. Solve any issue detected by this command (likely : install Android SDK).  

3. Setup android device  

Connect an Android device with USB debugging enabled or an emulator.  
Run `flutter devices` to check that device is set up.  

4. Build / run the app

In `budget/app`  : `flutter build bundle` should run fine.  
To run the app : `flutter run` which may lead to error `path may not be null or empty string. path='null'`.  
To solve that, comment out the block `signingConfigs` from `budget/app/android/app/build.gradle` L51 to 58 (https://gitlab.com/tabi/projects/budget/-/blob/master/app/android/app/build.gradle#L51) and uncomment `signingConfig signingConfigs.debug` (https://gitlab.com/tabi/projects/budget/-/blob/master/app/android/app/build.gradle#L62), comment the rest of the block L63 to 65 (https://gitlab.com/tabi/projects/budget/-/blob/master/app/android/app/build.gradle#L63).   
Run `flutter run` again and ... voila


