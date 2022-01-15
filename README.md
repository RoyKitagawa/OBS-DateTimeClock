For English ReadMe, please view [README_EN.md](./README_EN.md)

<a id="anchor1"></a>
# OBS用時計の概要  
こちらはOBSを用いた配信などで配信画面に現在の時刻を表示するための時計となっています  

※表示サンプル  
![時計1](https://user-images.githubusercontent.com/78025620/149194479-4bdffcfa-c8d3-41a4-879f-2fd036b9a10f.png)   

また現状は以下の各種カスタマイズ機能に対応しております
追加の要望等ございましたら、Issueに起票をお願いいたします。
  
## 対応カスタマイズ機能一覧
1. 表示内容の調整（日付のみの表示、時間のみの表示、ミリ秒表記など複数パターンがあります）  
2. フォントファイルの調整  
3. タイムゾーン（時差）の調整  
4. 文字の色やサイズ、縁取りの太さや色の調整  
5. 年月日の表示形式（yyyy年mm月dd日, mm/dd/yyyy, dd/mm/yyyy）
   

# 目次
1. [OBS用時計の概要](#anchor1)
7. [OBS上でソースコードを取り込む方法](#anchor2)
2. [各種カスタマイズについて（概要）](#anchor3)
3. [日時の表記パターンの設定について](#anchor4)
4. [時差の設定について](#anchor5)
5. [フォントの設定について](#anchor6)
6. [その他各種設定について](#anchor7)
  
   
<a id="anchor2"></a>
## OBS上でソースコードを取り込む方法
それではまずは本プロジェクトをOBS上で表示させる方法をご紹介します。  
インストールされているフォントによっては見栄えがサンプルと違う風に表示される可能性もありますが、そちらは後述の[フォントの設定について](#anchor6)をご確認お願いいたします。  
  
### 本プロジェクトのダウンロード、及びOBSへの取り込む手順
1. [プロジェクトページ](https://github.com/RoyKitagawa/OBS-DateTimeClock)からZipファイルをダウンロードし、任意の場所に解凍する
![image](https://user-images.githubusercontent.com/78025620/149198154-ad08545f-f9af-44ca-9786-64862252949e.png)  
2. OBS上で「ブラウザ」のソースを追加  
![OBS-1](https://user-images.githubusercontent.com/78025620/149194173-b8f09038-f792-4be9-ad82-53452c1fa352.png) ![OBS-2](https://user-images.githubusercontent.com/78025620/149194272-326b6820-42d5-42da-b103-b049bc077f21.png)
3. 追加したブラウザソースの設定画面で「ローカルファイル」のチェックを入れる
4. 「参照」ボタンからダウンロードしたこちらのプロジェクトの```html```フォルダ内にある```clock.html```を指定する
5. 「表示されていないときにソースをシャットダウン」、及び「シーンがアクティブになったときにブラウザの表示を更新」にチェックを入れる
![OBS-4](https://user-images.githubusercontent.com/78025620/149194357-fb0ade5c-e0dc-4ba7-8898-3306444145b5.png)
  
  
<a id="anchor3"></a>
## 各種カスタマイズ項目について（概要）
前述の通り、本ソフトウェアでは複数のカスタマイズが可能となっています。
また配信者の方になるべく気軽に使っていただくため、変更が必要なファイルを以下の2ファイルのみに絞らせていただいています。
1. ```js/settings.js```: 主に表示パターンや色コード、文字サイズ等を指定する場合に使用します  
2. ```css/fontSettings.css```: フォントを指定する場合に使用します

<a id="anchor4"></a>
## 日時の表記パターンの設定について
本ソフトウェアでは数パターンの日時の表記が選択できます  
### 表示タイプ  
0: 基本セット（年月日、曜日、時間、分、秒）  
1: 曜日無し（年月日、時間、分、秒）  
2: 日付けのみ＋曜日（年月日、曜日）  
3: 日付けのみ（年月日）  
4: 時間のみ（時間、分、秒）  
5: 時間のみ＋ミリ秒付き（時間、分、秒、ミリ秒）  
※年月日の表記方法の指定は後述の[年月日の表記フォーマットを指定する方法](#anchor8)をご参照ください  
  
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
  
<a id="anchor5"></a>
## 時差の設定について    
本ソフトウェアでは任意の時差を指定することができます  
  
### 時差の設定方法  
```js/settings.js```内の```const timeDiffsInHour = 9```という文章の0を任意の表示タイプに変更してください。  
※日本の時差はUTC+9なため、デフォルトの設定は9となっています  
![image](https://user-images.githubusercontent.com/78025620/149195197-41f0bf39-5a84-40a3-a4cc-6d36fde096f0.png)  

<a id="anchor6"></a>
## フォントの設定について  
本ソフトウェアでは任意のフォントを指定することができます  
※サンプル画像ではにくまるフォント様を使用させていただいています  
  
本ソフトウェアでフォントを指定する際、以下の2つの方法があります  
1. PCにインストール済みのフォントを指定  
2. フォントファイル（ttf,otf等）を直接プロジェクト内にコピーして指定   

基本的には1番の「PCにインストール済みのフォントを指定」が楽なため、開発に不慣れな方はそちらを推奨します。
※また、フォントの設定を行う場合は```css/fontSettings.css```というファイルを編集します

### PCにインストール済みのフォントを指定する方法について
```css/fontSettings.css```内の以下の記述を確認、及び必要に応じて調整します。  

```css/fontSettings.css```の初期内容
![image](https://user-images.githubusercontent.com/78025620/149371745-534c0476-9685-4fe7-9571-7560f85b5e01.png)

以下の内容ですと、「07にくまるフォント」がPCにインストールされていれば「07にくまるフォント」が適用されます。  
また、もし「07にくまるフォント」が未インストールの場合は「HGP創英角ﾎﾟｯﾌﾟ体」を確認、それも未インストールなら「けいふぉんと」を、  
という風に左から順にみてインストール済みのフォントがあればそのフォントが適用されます。

そのためサンプル画像の通りの見た目表示する場合は、以下のサイトからにくまるフォントをダウンロード、インストールいただく必要があります。

にくまるフォント様公式サイト  
http://www.fontna.com/freefont/1651/  

#### 別のインストール済みのフォントを指定したい場合
にくまるフォント以外のフォントを優先したい場合、また別の任意のフォントを指定したい場合、記述を編集する必要があります。
仮に「カスタムフォント」という名前のフォントを使用したい場合、以下のような記述に変更します。

![image](https://user-images.githubusercontent.com/78025620/149373008-4488b22f-58d2-408d-ab06-b2a0b1f98663.png)

### 未インストールのフォント・フォントファイルを直接指定する方法について
何らかの事情でPCにフォントがインストールできない場合、またフォントファイルを本プロジェクト内で管理する方法も可能です。  
  
#### フォントファイルを直接している手順
1. 指定したいフォントファイル(ttf, otf等）を用意し、本プロジェクト内の「fonts」フォルダに配置する  
2. 設定を有効にするため、50行、58行目の記号を削除しコメントアウト状態を解除する  
3. 53行目の「<fontsフォルダに配置したファイル名>」を配置したフォントファイル名に変更  
   例）「07にくまるフォント.otf」をfontsファイルに配置した場合、以下のように変更します  
       -> 「src: url(./../fonts/07にくまるフォント.otf);」  
4. 27～29行のソースコードを全てコメントアウト、もしくは削除する  
  
手順2の初期状態のサンプル  
![image](https://user-images.githubusercontent.com/78025620/149373880-34512ac7-217d-4317-b8da-7858825fced5.png)  
  
手順3のコメントアウト解除、及びファイルの指定のサンプル  
![image](https://user-images.githubusercontent.com/78025620/149374233-c9ce6013-4491-4494-903d-451165e951d2.png)  

手順4のサンプル  
![image](https://user-images.githubusercontent.com/78025620/149374398-6ed77437-1b33-47c1-9290-800505dd2d13.png)  

<a id="anchor7"></a>  
## その他各種設定について
フォント以外の設定は全て```js/settings.js```ファイルにまとめられています。  
  
```js/settings.js```に記述されている設定可能項目一覧  
![image](https://user-images.githubusercontent.com/78025620/149374804-0b675ba2-e4df-46f8-9c70-6d3fbfb2cf45.png)  

### 1. 日付や時間の表示フォーマット設定
前述の[日時の表記パターンの設定について](#anchor4)をご確認ください。  

### 2. 時差の設定
前述の[時差の設定について](#anchor5)をご確認ください。  
  
### 3. 文字の縁取り（縁の太さ）設定
こちらの数値を指定することで縁取りの太さを変更することができます  
![image](https://user-images.githubusercontent.com/78025620/149375419-907e023a-743e-4e0c-a48a-5dbc74c79a4f.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
例）縁のサイズを30に指定した場合  
![image](https://user-images.githubusercontent.com/78025620/149375572-407ad2af-9cc9-4290-9e20-a582398da0f4.png)
![image](https://user-images.githubusercontent.com/78025620/149375765-78042441-6cfa-4f41-954e-c8c3d6c52646.png)  

### 4. 文字の縁取り（縁の色）設定
こちらの数値を指定することで縁取りの色を変更することができます  
![image](https://user-images.githubusercontent.com/78025620/149376109-184e828d-c846-436a-88ca-02aab3832619.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
例）縁の色を```RGB(128, 64, 32)```に指定した場合  
![image](https://user-images.githubusercontent.com/78025620/149376208-dcdb3251-a9e9-448c-aad6-5aa3b69eef1c.png)
![image](https://user-images.githubusercontent.com/78025620/149376176-94d6913f-d8e1-4a63-9c1c-33f1e6f9cb0b.png) 

### 5. 文字色の設定
こちらの数値を指定することで文字色を変更することができます  
![image](https://user-images.githubusercontent.com/78025620/149376392-8432bb4d-0266-4c01-9cb7-c1c41f5f7ddf.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
例）縁の色を```RGB(255, 150, 150)```に指定した場合  
![image](https://user-images.githubusercontent.com/78025620/149376506-499ea4ad-d484-4de7-a835-ccff51eccfc8.png)
![image](https://user-images.githubusercontent.com/78025620/149376477-f102550c-470b-4f36-b0cb-371a0bcf1560.png) 

### 6. 日付の文字サイズを強制的に指定する
こちらの数値を指定することで日付の文字サイズを変更することができます  
※日付と時間の文字のバランスが崩れる可能性がありますのでご注意ください  
![image](https://user-images.githubusercontent.com/78025620/149376810-9d92b303-daa5-4b7f-9ff9-476d64e6f97e.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
例）フォントのサイズを50に指定した場合  
![image](https://user-images.githubusercontent.com/78025620/149377030-a8351464-3096-4aef-a6c0-622cefe3920f.png)
![image](https://user-images.githubusercontent.com/78025620/149376983-5dc25898-c2bc-4533-997d-3536427408b5.png)　　

### 7. 時間の文字サイズを強制的に指定する
こちらの数値を指定することで時間の文字サイズを変更することができます  
※日付と時間の文字のバランスが崩れる可能性がありますのでご注意ください  
![image](https://user-images.githubusercontent.com/78025620/149377254-7b59d086-3cb0-4a87-8fdc-2f734c317fdc.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
例）フォントのサイズを100に指定した場合  
![image](https://user-images.githubusercontent.com/78025620/149605070-bb42bc6d-5b29-4c47-837e-69d455b962d5.png)
![image](https://user-images.githubusercontent.com/78025620/149377370-d6c51f1a-97f0-474e-8d18-093fdf042b9b.png)　　

### 8. 日付の行と時間の行の間隔を指定する
フォントやサイズによって行の間隔の調整が必要な場合に指定してください   
![image](https://user-images.githubusercontent.com/78025620/149377551-ef4aa3e7-cb74-4f35-bfa0-9424ca860f43.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
例）行間隔を20に指定した場合  
![image](https://user-images.githubusercontent.com/78025620/149605032-faeedeb2-36b8-4076-a2a0-0d0a331f3167.png)
![image](https://user-images.githubusercontent.com/78025620/149377684-60f5b9b9-3052-43ad-bdb6-5e646e868c11.png)    

<a id="anchor8"></a>
### 9. 年月日の表記フォーマットを指定する
日付のフォーマットの表記を日本式、アメリカ式、イギリス式で変更することができます  
※デフォルトは日本式の「yyyy年mm月dd日（a）」が指定されています
![image](https://user-images.githubusercontent.com/78025620/149604958-e9f6b551-9f30-4ffd-b2ec-660d6228af77.png)
![image](https://user-images.githubusercontent.com/78025620/149605123-33578229-88a0-4979-8937-f480314a0ed8.png)    
    
例）年月日表記フォーマットを1に指定した場合（アメリカ式の「mm/dd/yyyy (a)」表記）  
![image](https://user-images.githubusercontent.com/78025620/149604974-506d42e6-27e0-42d8-93ea-9ac92530cc85.png)
![image](https://user-images.githubusercontent.com/78025620/149605133-eb99a61d-9c86-40ae-a907-7b463aaeaf79.png)    
  
例）年月日表記フォーマットを2に指定した場合（イギリス式の「dd/mm/yyyy (a)」表記）    
![image](https://user-images.githubusercontent.com/78025620/149605016-872da544-a823-4edf-beac-f1fb633ecf6d.png)
![image](https://user-images.githubusercontent.com/78025620/149605138-781ea8d6-39e5-4d4d-8991-d8a96d51842c.png)    
  
