# A Small Web Application Form

##### This is a small application form that takes the Registration data inputs and saves it in MongoDB.


For anything regarding the internship and the project, [Gitter here](https://gitter.im/SERlyInterns/web-dev-application-form?utm_source=share-link&utm_medium=link&utm_campaign=share-link) with the wonderful developers, and me :D

[Click here to contact us](https://webchat.freenode.net/?channels=%23serly_internship_portal&uio=d4) (the ex-interns) SPECIFICALLY FOR ISSUES in THIS PROJECT.

***

## Step-wise guide to run this application on your localhost (Using Windows)(will not work on XP or earlier) :

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

##### Step B (to download mongoDB for 32 x86 PC): 
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
	* Go to the end of the ```Variable Value```
	* Paste the path after the semicolon (```;```). If there is no semi-colon in the end, insert one yourself before pasting.
	* Open a new Command Prompt and type ```path``` (IMPORTANT: type only ```path``` with no spaces,  otherwise you'll be in trouble)
	* Check that the path ```C:\Program Files\MongoDB\Server\4.0\bin``` is somewhere inside that output or not.
	* If YES, continue. If NO,  [post a messege here](https://webchat.freenode.net/?channels=%23serly_internship_portal&uio=d4)

***

### 2. Install python 3.0 or above

1. Go to [this link](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe)
2. If this DOES NOT work, then manually go to the following link:   
	https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe     

3. After the download completes, proceed for installation:	
	* double-click the .exe executable file that you downloaded
	* Follow the installation guide (use default installation if you are a beginner)
	* > Remember to CHECH the option "Add python to PATH"
	* done

4. Open a new Command Prompt and type ```path``` (IMPORTANT: type only ```path``` with no spaces,  otherwise you'll be in trouble)
5. Check that the path ```C:\Users\<<YOUR_USER_NAME>>\AppData\Local\Programs\Python\Python37-32``` is somewhere inside that output or not.
6. * If YES, continue. If No, then try to follow the same procedure to add ```C:\Users\<<YOUR_USER_NAME>>\AppData\Local\Programs\Python\Python37-32``` to the path. Follow the same steps as you did with mongoDB.
7. Check again that the path ```C:\Users\<<YOUR_USER_NAME>>\AppData\Local\Programs\Python\Python37-32``` is somewhere inside that output or not.
8. If YES, continue. If NO, [post a messege here](https://webchat.freenode.net/?channels=%23serly_internship_portal&uio=d4)



***
## ** *NEXT IS INCOMPLETE,  PLEASE DO NOT FOLLOW. Go to IRC chat frame given below for other issues* **

***
***

## Contact us here:
1. Pick a nickname.
2. Tick the "I am not a robot" checkbox.
3. Connect.

<iframe src="https://webchat.freenode.net?channels=%23serly_internship_portal&uio=d4" width="647" height="400"></iframe>
