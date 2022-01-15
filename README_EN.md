日本語版のReadMeは[README.md](./README.md)をご参照ください。

<a id="anchor1"></a>
# About this OBS-DateTimeClock  
This software is a clock aimed to show the current date and time on the stream screen using OBS.  

*Sample of the output  
![image](https://user-images.githubusercontent.com/78025620/149605123-33578229-88a0-4979-8937-f480314a0ed8.png)  
  
*The format of date display can be changed in below formats too.  
![image](https://user-images.githubusercontent.com/78025620/149605133-eb99a61d-9c86-40ae-a907-7b463aaeaf79.png)
![image](https://user-images.githubusercontent.com/78025620/149605138-781ea8d6-39e5-4d4d-8991-d8a96d51842c.png)  
  
Currently, this software allows following customization.  
If you have any additional requests, please feel free to raise up on the issue on this repository.  
  
## Customize target features
1. Adjust visual output (There are several pattern such as only date, only time, and millisecond display)    
2. Adjust font file  
3. Adjust time zone    
4. Adjust text size and color, text border width and color   
5. Adjust date display format (yyyy年mm月dd日, mm/dd/yyyy, dd/mm/yyyy)  
  
# Index
1. [About this OBS-DateTimeClock](#anchor1)  
7. [How to import this software into OBS](#anchor2)  
2. [About each customize feature (Summary)](#anchor3)  
3. [Setting date and time show patterns](#anchor4)  
4. [Setting time zone](#anchor5)  
5. [Setting fonts](#anchor6)  
6. [Other detailed settings](#anchor7)    
  
  
<a id="anchor2"></a>
## How to import this software into OBS
As start, let us introduce how to show this project in OBS for to use in streams.  
Depending on the fonts installed in your PC, initial display may differ, for the details to adjust fonts, please see the section for [setting fonts](#anchor6) later.  
  
### Steps to download this project, and import to OBS
1. Download Zip file from [this project's page](https://github.com/RoyKitagawa/OBS-DateTimeClock), and unzip to any place in your PC.  
![image](https://user-images.githubusercontent.com/78025620/149198154-ad08545f-f9af-44ca-9786-64862252949e.png)  
2. Add "Broser" source in OBS    
![OBS-1](https://user-images.githubusercontent.com/78025620/149194173-b8f09038-f792-4be9-ad82-53452c1fa352.png) ![OBS-2](https://user-images.githubusercontent.com/78025620/149194272-326b6820-42d5-42da-b103-b049bc077f21.png)
3. Set the check on "Local File" in the setting screen of added browser source  
4. From "Browse button", select ```clock.html``` file in ```html``` folder   
5. Also set check in 2 checkbox at below, "Shutdown source when not displayed" and "Refresh browser display when scene is in active"  
![OBS-4](https://user-images.githubusercontent.com/78025620/149194357-fb0ade5c-e0dc-4ba7-8898-3306444145b5.png)
  
  
<a id="anchor3"></a>
## About each customize feature (Summary)
As shared previoudly, this software allows multiple customizations.  
Also, to allow streamers to customize freely without less need of coding knowledge, user will ONLY need to see/update following 2 files to customize.  
1. ```js/settings.js```: For adjusting show patterns, color code and text size.  
2. ```css/fontSettings.css```: For adjusting fonts.  

<a id="anchor4"></a>
## Setting date and time show patterns
In this software, several patterns for date and time display can be selected.  
### Display format  
0: Basic set (Year/Month/Day, Weekday, Hour, Minutes, Seconds)  
1: No weekday (Year/Month/Day, Hour, Minutes, Seconds)   
2: Only date and weekday (Year/Month/Day, Weekday）  
3: Only date (Year/Month/Day）    
4: Only time (Hour, Minutes, Seconds)  
5: Only time and milliseconds (Hour, Minutes, Seconds, Milliseconds)  
*For adjustment of date formatl, please refer the section [Specify date display format](#anchor8)
  
### Display sample 
*Actual display will be transparent
  
0: Basic set (Year/Month/Day, Weekday, Hour, Minutes, Seconds)  
![時計1](https://user-images.githubusercontent.com/78025620/149194479-4bdffcfa-c8d3-41a4-879f-2fd036b9a10f.png)  
  
1: No weekday (Year/Month/Day, Hour, Minutes, Seconds)   
![image](https://user-images.githubusercontent.com/78025620/149194569-d9110e0d-1955-45ee-8747-d4db1d6bfb7a.png)  
  
2: Only date and weekday (Year/Month/Day, Weekday）  
![image](https://user-images.githubusercontent.com/78025620/149194709-7a057b2e-cb4a-40b9-a5c6-e1ca1e8e4f87.png)  
  
3: Only date (Year/Month/Day）   
![image](https://user-images.githubusercontent.com/78025620/149194754-525057e3-b3ca-4f0b-b469-53cf5f08afd2.png)  
  
4: Only time (Hour, Minutes, Seconds)  
![image](https://user-images.githubusercontent.com/78025620/149194911-3f66b45b-5f01-46d8-97b1-892bce3e1b24.png)
  
5: Only time and milliseconds (Hour, Minutes, Seconds, Milliseconds)  
![image](https://user-images.githubusercontent.com/78025620/149194804-2e07cdb6-fa03-42c7-a10d-866d4782787a.png)  
  
  
### How to specify display format  
From the file ```js/settings.js```, please change the value "0" in ```const showPattern = 0``` to the value of expected format. 
  
![image](https://user-images.githubusercontent.com/78025620/149195153-18081562-c3a0-4db2-9570-8311dda97579.png)  
  
<a id="anchor5"></a>
## Setting time zone    
In this software, timezone can be specified  
  
### How to specify time zone    
From the file ```js/settings.js```, please change the value "9" in ```const timeDiffsInHour = 9``` to the value of expected time zone.  
*As default, it is set to "9" since the Japan's time zone is UTC +9  
![image](https://user-images.githubusercontent.com/78025620/149195197-41f0bf39-5a84-40a3-a4cc-6d36fde096f0.png)    

<a id="anchor6"></a>
## Setting fonts  
In this software, any fonts can be specifed.  
*In sample font called "Nikumaru font (にくまるフォント)" is used.  
   
To specify fonts in this software, there are 2 choices.    
1. Specify font that is already installed in your PC *Recommended  
2. Specify font by directly placing font file in the project folder  
  
Since using the installed font will be more simple and easy, it will be more recommended to ones who are not very familiar with coding.  
*And when setting fonts, the file ```css/fontSettings.css``` needs be checked and updated.

### How to specify font that is already installed in your PC
For how the fonts are specified, please Check the contents in ```css/fontSettings.css```.  
  
Default content of ```css/fontSettings.css```  
![image](https://user-images.githubusercontent.com/78025620/149371745-534c0476-9685-4fe7-9571-7560f85b5e01.png)  
   
In the above content, if "07にくまるフォント" (which is Nikumaru font) is installed, it will be applied.  
If "07にくまるフォント" is not installed, the font on the right "HGP創英角ﾎﾟｯﾌﾟ体" will be appllied.  
If "HGP創英角ﾎﾟｯﾌﾟ体" is also not installed, the font on the right "けいふぉんと" will be applied, and so on.  
  
The font on left has higher priority, and whatever that is installed on more left, will be applied.  
So if you would like to use the same font with sample image, please visit website for Nikumaru font, to download and install Nikumaru font.  

Official website for Nikumaru font  
http://www.fontna.com/freefont/1651/  

#### How to specify other installed fonts
If you would like to specify other fonts, you will need to adjust the contents.  
For example, lets say you have installed font called "MyCustomFont" into your PC, and in that case the content will be as follows.  

![image](https://user-images.githubusercontent.com/78025620/149607451-062d1772-c4b5-427e-b5ec-92380e70103f.png)  
  
### How to specify fonts that are not installed / directly using font file  
If for any reason you cannot install desired font, you can also specify font directly by placing font file in project folder.   
  
#### Steps font files directly  
1. Place font file (like ttf, otf files) in the "fonts" folder in this project.  
2. To apply fonts delete symbols (```/*``` and ```*/```) in line 50 and 58, to undo comment out.  
3. In line 53, change the content ```<fontsフォルダに配置したファイル名>``` to uploaded font file name.  
   ie) if you place "MyCustomFont.otf" file in "fonts" folder, updated content will be as follow    
       -> "src: url(./../fonts/MyCustomFont.otf);"  
4. Comment out or delete source code in line 27 to 29.  
    
Sample of step 2 (Default status)  
![image](https://user-images.githubusercontent.com/78025620/149373880-34512ac7-217d-4317-b8da-7858825fced5.png)  
  
Sample of step 3, to undo comment out and specify target font file  
![image](https://user-images.githubusercontent.com/78025620/149607903-a65aec76-b462-48dd-a0ff-32aa23558b20.png)  

Sample of step 4  
![image](https://user-images.githubusercontent.com/78025620/149374398-6ed77437-1b33-47c1-9290-800505dd2d13.png)  

<a id="anchor7"></a>  
## Other detailed settings
Every setting other than font, is all placed in ```js/settings.js``` file.  
    
Each settings specified in ```js/settings.js``` are as follows.  
1. Specify display format of date and time    
2. Specify time zone    
3. Specify text border width  
4. Specify text border color  
5. Specify text color  
6. Specify text size of date  
7. Specify text size of time  
8. Specify margin between date row and time row  
9. Specify date display format  
  
  
### 1. Specify display format of date and time  
Please refer to previous [Setting date and time show patterns](#anchor4)    
  
### 2. Specify time zone  
Please refer to previous [Setting time zone](#anchor5)  
  
### 3. Specify text border size  
By changing below values, text border size can be adjusted.  
![image](https://user-images.githubusercontent.com/78025620/149375419-907e023a-743e-4e0c-a48a-5dbc74c79a4f.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
ie) Sample of changing text border size to 30  
![image](https://user-images.githubusercontent.com/78025620/149375572-407ad2af-9cc9-4290-9e20-a582398da0f4.png)
![image](https://user-images.githubusercontent.com/78025620/149375765-78042441-6cfa-4f41-954e-c8c3d6c52646.png)  

### 4. Specify text border color  
By changing below values, text border can be adjusted.    
![image](https://user-images.githubusercontent.com/78025620/149376109-184e828d-c846-436a-88ca-02aab3832619.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
ie) Sample of changing text border color to ```RGB(128, 64, 32)```.  
![image](https://user-images.githubusercontent.com/78025620/149376208-dcdb3251-a9e9-448c-aad6-5aa3b69eef1c.png)
![image](https://user-images.githubusercontent.com/78025620/149376176-94d6913f-d8e1-4a63-9c1c-33f1e6f9cb0b.png)   
  
### 5. Specify text color  
By changing below values, text color can be adjusted.    
![image](https://user-images.githubusercontent.com/78025620/149376392-8432bb4d-0266-4c01-9cb7-c1c41f5f7ddf.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
ie Sample of changing text color tp ```RGB(255, 150, 150)```.  
![image](https://user-images.githubusercontent.com/78025620/149376506-499ea4ad-d484-4de7-a835-ccff51eccfc8.png)
![image](https://user-images.githubusercontent.com/78025620/149376477-f102550c-470b-4f36-b0cb-371a0bcf1560.png) 

### 6. Specify text size of date  
By changing below values, text size of date can be adjusted.  
*Balance of date and time may not fit very nice dpending on the value set. Please be aware when you adjust these values.  
![image](https://user-images.githubusercontent.com/78025620/149376810-9d92b303-daa5-4b7f-9ff9-476d64e6f97e.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
ie) Sample of changing font size to 50.   
![image](https://user-images.githubusercontent.com/78025620/149377030-a8351464-3096-4aef-a6c0-622cefe3920f.png)
![image](https://user-images.githubusercontent.com/78025620/149376983-5dc25898-c2bc-4533-997d-3536427408b5.png)　　

### 7. Specify text size of time  
By changing below values, text size of time can be adjusted.  
*Balance of date and time may not fit very nice dpending on the value set. Please be aware when you adjust these values.  
![image](https://user-images.githubusercontent.com/78025620/149377254-7b59d086-3cb0-4a87-8fdc-2f734c317fdc.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
ie) Sample of changing font size to 100.   
![image](https://user-images.githubusercontent.com/78025620/149605070-bb42bc6d-5b29-4c47-837e-69d455b962d5.png)
![image](https://user-images.githubusercontent.com/78025620/149377370-d6c51f1a-97f0-474e-8d18-093fdf042b9b.png)　　

### 8. Specify margin between date row and time row  
By changing below values, margin between lines can be adjusted.  
Please use this setting if the line margin needs to be adjusted due to font or text size.  
![image](https://user-images.githubusercontent.com/78025620/149377551-ef4aa3e7-cb74-4f35-bfa0-9424ca860f43.png)
![image](https://user-images.githubusercontent.com/78025620/149375900-b4e0c1cb-39c5-4a86-8fc1-8a568a769f28.png)  
  
ie) Sample of changing line margins to 20.    
![image](https://user-images.githubusercontent.com/78025620/149605032-faeedeb2-36b8-4076-a2a0-0d0a331f3167.png)
![image](https://user-images.githubusercontent.com/78025620/149377684-60f5b9b9-3052-43ad-bdb6-5e646e868c11.png)    
  
<a id="anchor8"></a>
### 9. Specify date display format  
By changing below values, date display format can be set to either "Japan format", "US format", "UK format".    
*As default, it is set to "Japan format" (```yyyy年mm月dd日（a)```)  
![image](https://user-images.githubusercontent.com/78025620/149604958-e9f6b551-9f30-4ffd-b2ec-660d6228af77.png)
![image](https://user-images.githubusercontent.com/78025620/149605123-33578229-88a0-4979-8937-f480314a0ed8.png)    
      
ie) Sample of setting to 1, for "US format" (```mm/dd/yyyy (a)```)    
![image](https://user-images.githubusercontent.com/78025620/149604974-506d42e6-27e0-42d8-93ea-9ac92530cc85.png)
![image](https://user-images.githubusercontent.com/78025620/149605133-eb99a61d-9c86-40ae-a907-7b463aaeaf79.png)    
  
ie) Sample of setting to 2, for "UK format" (```dd/mm/yyyy (a)```)    
![image](https://user-images.githubusercontent.com/78025620/149608705-ba71b548-6cdd-4a3f-ba42-91f0bab7400f.png)
![image](https://user-images.githubusercontent.com/78025620/149605138-781ea8d6-39e5-4d4d-8991-d8a96d51842c.png)    
  
