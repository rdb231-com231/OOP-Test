# Services OOP Test - GEN 1
08/03/2025 - First created by MewPlush

**This is just a test!**

## Summary
- ### Connection Services (1.8)
- ### PySocket (1.2.4)
- ### PyCharacter (0.8) - BETA
---
- PySort --- __Canceled__


This __"library"__ is consistent of codes that might actually not have a use, in general, this "library" was made as a __OOP Test__ for me to enhance my classes manipulations hability's and general python _skill_. After all, this really improved my general hability to ___code in python___ and __read__ code.
So, don't expect much from it!

## Importing this "Library"

To import this code, download this repo and open it in your __IDE__. This was made in PyCharm, but others IDE's will work just fine. After opening the folder in your __IDE__, create a new python file (the one that you will code in, `main.py` or `index.py`) simply import the files that you want to use. 
examples:
```py
from Services import connection
from Services import PySocket
```
You can define a custom name for your imports using `from Services import File as Custom_Name`, also import singular functions/classes using `from Services.File import send`. Examples:
```py
from Services import connection as conn
from Services.PySocket import send as socket
```
---
Remember that, if you change a filename (by example, PySocket to PySoK) you must change the **file** import name to the new one. Or else, the code will be importing nothing, since the file doesn't exist anymore/has a new name.

Importing using custom names might have you to type more, the majority of this library functions accept `with... as` statements and all classes can be converted into variables. 
If you don't feel like typing more, these are 2 ways to have a custom name set for this class:
```py
from Services import connection
data_save = connection.dataconnection("myConn", 1234)
data_save.append("File", "Hi!")
# this saves with a custom name: data_save

with connection.dataconnection("myConn", 1234) as client:
	client.append("myFile", "myContent")
	client.log("myFile")
# temporary database that has a custom name
```
---
Now, just follow the Documentation and you should be good to go! Any errors, report to me in:

- Discord: @mew.plush
- Email: mewplushyt@gmail.com

Thank you for reading and thank you even more if you tested the "library", I really spent some time working on it and if you think it could have improvements, send me some or edit the code yourself!
Stay good out there.
 
--- MewPlush


