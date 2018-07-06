# A Small Web Application Form

##### This is a small application form that takes the Registration data inputs and saves it in MongoDB.


For anything, [Gitter here](https://gitter.im/SERlyInterns/web-dev-application-form?utm_source=share-link&utm_medium=link&utm_campaign=share-link) with the wonderful developers, and me :D

[Click here](https://gitter.im/SERlyInterns/web-dev-application-form?utm_source=share-link&utm_medium=link&utm_campaign=share-link) to contact me SPECIFICALLY FOR THIS PROJECT.

***

## Step-wise guide to run this application on your localhost:

### Requirements:
1. mongoDB
2. python 3.0 (or higher) and some python packages
3. Any browser

### 1. Install mongoDB
* Check out your OS Architecture (by right-clicking on "My PC" or "This PC" on your desktop and select properties.
It should be listed in system type.


  If it is 64bit OS and x64 based processor, go to **Step A**
  
  
  If it is 32bit OS and x86 based processor, go to **Step B**
  

##### Step A (to download mongoDB for 64 x64 PC):
* Go [here](https://www.mongodb.com/dr/fastdl.mongodb.org/win32/mongodb-win32-x86_64-2008plus-ssl-4.0.0-signed.msi/download) and it will be downloaded.
* **NOTE**: If this does not work, go to [https://www.mongodb.com/download-center#community] -> select "Community Server", -> select "*yourOperatingSystem*" -> "download .msi"

##### Step B (to download mongoDB for 32 x86 PC): ** *THIS IS INCOMPLETE,  PLEASE DO NOT FOLLOW* **
* Go [here](http://downloads.mongodb.org/win32/mongodb-win32-i386-v3.2-latest-signed.msi?_ga=2.41016992.361794817.1530858094-91234175.1530858094) and it will be downloaded.
* **NOTE**: If this does not work, go to [http://downloads.mongodb.org/win32/mongodb-win32-i386-v3.2-latest-signed.msi?_ga=2.41016992.361794817.1530858094-91234175.1530858094] -> select "win32/mongodb-win32-i386-v3.2-latest-signed.msi"

##### Install mongoDB by double-clicking on the software you just downloaded, and follow the instructions.

> NOTE: Remember to CHECK "INSTALL mongoDB Compass" at the last page of the installation in order to get a GUI to handle the input data.

##### Add mongoDB to path:

1. Navigate to the folder where you installed mongoDB. Then move to the ```bin``` directory. (see below)  
It will be somewhere like:  
```
	C:\Program Files\MongoDB\Server\4.0\bin
```
2. Copy this path, and use it as follows.
3. Go to ```Control Panel\System and Security\System``` and click on ```Advanced System Settings``` in the left panel.
4. Click on 	```Environment Variables```
5. Find the variable ```Path``` in both the frames. Then,  for both the Path variables:
	* Click on ```Path```
	* Click ```Edit``` just below that frame
	* Go to the end of the ```Variavle Value```
	* Paste the path after the semicolon (```;```). If there is no semi-colon in the end, insert one yourself before pasting.
	* Open a new Command Prompt and type ```path``` (IMPORTANT: type only ```path``` with no spaces,  otherwise you'll be in trouble)
	* Check that the path ```C:\Program Files\MongoDB\Server\4.0\bin``` is somewhere inside that output or not.
	* If YES, continue. If NO,  [post a messege here](https://gitter.im/SERlyInterns/web-dev-application-form?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

***

### 2. Install python 3.0 or above