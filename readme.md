<a id="anchor1"></a>
# OBS用時計の概要  
こちらはOBSを用いた配信などで配信画面に表示する用の時計となっています  
日付や曜日、ミリ秒表記、任意のフォントファイルや任意のタイムゾーンの指定も可能となっています。  
   
※表示サンプル  
![時計1](https://user-images.githubusercontent.com/78025620/149194479-4bdffcfa-c8d3-41a4-879f-2fd036b9a10f.png)   

# 目次
1. [OBS用時計の概要](#anchor1)
2. [OBS上でソースコードを取り込む方法](#anchor2)
3. [表示内容の調整について](#anchor3)
4. [時差の設定について](#anchor4)
5. [フォントの設定について](#anchor5)


<a id="anchor2"></a>
## OBS上でソースコードを取り込む方法
1. [プロジェクトページ](https://github.com/RoyKitagawa/OBS-DateTimeClock)からZipファイルをダウンロードし、任意の場所に解凍する
![image](https://user-images.githubusercontent.com/78025620/149198154-ad08545f-f9af-44ca-9786-64862252949e.png)  
2. OBS上で「ブラウザ」のソースを追加  
![OBS-1](https://user-images.githubusercontent.com/78025620/149194173-b8f09038-f792-4be9-ad82-53452c1fa352.png) ![OBS-2](https://user-images.githubusercontent.com/78025620/149194272-326b6820-42d5-42da-b103-b049bc077f21.png)
3. 追加したブラウザソースの設定画面で「ローカルファイル」のチェックを入れる
4. 「参照」ボタンからダウンロードしたこちらのプロジェクトの```html```フォルダ内にある```clock.html```を指定する
5. 「表示されていないときにソースをシャットダウン」、及び「シーンがアクティブになったときにブラウザの表示を更新」にチェックを入れる
![OBS-4](https://user-images.githubusercontent.com/78025620/149194357-fb0ade5c-e0dc-4ba7-8898-3306444145b5.png)

<a id="anchor3"></a>
## 表示内容の調整について
本ソフトウェアでは数パターンの日時の表記が選択できます

### 表示タイプ  
0: 基本セット（年月日、曜日、時間、分、秒）  
1: 曜日無し（年月日、時間、分、秒）  
2: 日付けのみ＋曜日（年月日、曜日）  
3: 日付けのみ（年月日）  
4: 時間のみ（時間、分、秒）  
5: 時間のみ＋ミリ秒付き（時間、分、秒、ミリ秒）  

### 表示サンプル  
※実際の背景は透過となっています

0: 基本セット（年月日、曜日、時間、分、秒）  
![時計1](https://user-images.githubusercontent.com/78025620/149194479-4bdffcfa-c8d3-41a4-879f-2fd036b9a10f.png)  

1: 曜日無し（年月日、時間、分、秒）  
![image](https://user-images.githubusercontent.com/78025620/149194569-d9110e0d-1955-45ee-8747-d4db1d6bfb7a.png)  

2: 日付けのみ＋曜日（年月日、曜日）  
![image](https://user-images.githubusercontent.com/78025620/149194709-7a057b2e-cb4a-40b9-a5c6-e1ca1e8e4f87.png)  

3: 日付けのみ（年月日）  
![image](https://user-images.githubusercontent.com/78025620/149194754-525057e3-b3ca-4f0b-b469-53cf5f08afd2.png)  

4: 時間のみ（時間、分、秒）  
![image](https://user-images.githubusercontent.com/78025620/149194911-3f66b45b-5f01-46d8-97b1-892bce3e1b24.png)


5: 時間のみ＋ミリ秒付き（時間、分、秒、ミリ秒）  
![image](https://user-images.githubusercontent.com/78025620/149194804-2e07cdb6-fa03-42c7-a10d-866d4782787a.png)  


### 表示タイプの変更方法
```js/settings.js```内の```const showPattern = 0```という文章の0を任意の表示タイプに変更してください。  
![image](https://user-images.githubusercontent.com/78025620/149195153-18081562-c3a0-4db2-9570-8311dda97579.png)  
  
<a id="anchor4"></a>
## 時差の設定について    
本ソフトウェアでは任意の時差を指定することができます  
  
### 時差の設定方法  
```js/settings.js```内の```const timeDiffsInHour = 9```という文章の0を任意の表示タイプに変更してください。  
※日本の時差はUTC+9なため、デフォルトの設定は9となっています  
![image](https://user-images.githubusercontent.com/78025620/149195197-41f0bf39-5a84-40a3-a4cc-6d36fde096f0.png)  

<a id="anchor5"></a>
## フォントの設定について  
本ソフトウェアでは任意のフォントを指定することができます  
※サンプル画像ではにくまるフォント様を使用させていただいています  
※また、フォントの再配布を防ぐためにフォントファイル自体は配布プロジェクトから削除しています  
※にくまるフォントを反映させるためには以下の公式サイトからフォントをダウンロードし、以下の設定を行ってください  
  
にくまるフォント様公式サイト  
http://www.fontna.com/freefont/1651/  
  
### にくまるフォントの設定方法について  
1. 上記サイトからにくまるフォントをダウンロード  
2. ```fonts```フォルダ内にダウンロードした「07にくまるフォント.otf」を配置  
3. ```css/clock.css```の23行目の```/* font-family: "clockFont"; */```を```font-family: "clockFont";```に変更する  
  
```css/clock.css```のサンプル  
![image](https://user-images.githubusercontent.com/78025620/149195665-ea3ce0c5-b98f-457e-bb18-54bc35e677c3.png)  
  
```css/clock.css```変更後のソースコード  
![image](https://user-images.githubusercontent.com/78025620/149196335-908e2557-63f6-4385-b171-a00fa406ac79.png)  
  
### その他任意のフォントの設定について  
1. 任意のフォントファイルを```fonts```フォルダに設置  
2. ```css/clock.css```の19行目の```./../fonts/07にくまるフォント.otf```のフォント名部分を変更する  
※以下の画像サンプルでは「サンプルフォント.ttf」というフォントファイルに差し替える変更を行っています  
  
元々のソースコード   
![image](https://user-images.githubusercontent.com/78025620/149196792-4d0775f4-fe51-40c8-b0c7-7c53982a7f4a.png)   
  
```サンプルフォント.ttf```用に変更後（```font```フォルダにこちらのファイルを設置するのを忘れないようご注意ください）  
![image](https://user-images.githubusercontent.com/78025620/149196605-c904f618-d877-4d1b-baa8-48df3597bf44.png)  

  
