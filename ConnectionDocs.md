# Connection Services (1.8)

## Methods and uses:
|Method  |Result  | Common Use |
|--|--| -- |
|[`.__init__` & `dataconnect(connection, password)`](#database-init-method)|Creates the Database| ___Required___ |
|`.append(key, content)` & `.read(key)`| writes or reads content on a key |Base Methods |
|`.point` & `.catch`|points or catches a pointer associated with a key, storing content| Medium Methods
| `.change_` Methods | changes kname, pointer or content of a key. | Medium Methods
| `__enter__` & `__exit__` | calls a temporary database using `with... as`|Advanced Methods
| `__len__` & `__contains__` | check the length `len()`, or if the database/keywords database contains a kname content or pointer `Any in dataconnect`| Advanced Methods
---


### Database `.__init__` Method


```py
class dataconnect(self, name: Any, password: Any) -> None
```

Connection services come integrated within the services **OOP** test. Connection Services can store in a Database (`Dict[Str, Any]`) any tipe of obj counting with the fact the key-name is a string. Can also store using keywords (`Dict[Str, Str]`), that will call a Key once they are pointed.



Keywords call Database Keys to call content.

`Keywords -> Keys -> Content`

You can't have a keyword without a key, neither a key without a content.



The `.__init__` Method will create a new `network`/`connection` with custom password and name. (Name is recommended to be a `str`). After that, the other methods will be enabled for use. 

---
### Database `.append` & `.read` Methods
```py
def append(self, kname: str, content: Any) -> None
```

Store using `.append` after connecting to a `network` (using the `__init__` function). It will write down a **new** object part with a `key name` (which must be a string) and any type of **content** as a `Any` type. 

Append will be used most of the time in your **code**, check this example out:
```py
e = dataconnect("myConnection", 1234)
e.append("myKey", "myData")
# database -> {'myKey': 'myData'}
e.append("mySecondKey", "myContent")
# database -> {'myKey': 'myData', 'mySecondKey': 'myContent'}
```
---

```py
def read(self, kname: str) -> Any
```

The `.read` calls a key to return it's content. It's very simple and mainly can be used to `print()` out a content or simply just use it's value.
Check this example:
```py
e = datacontent("net", 1234)
e.append("myKey",  "myData")
# database -> {'myKey': 'myData'}
e.read("myKey")
# returns -> "myData"
```
---
### Database `.point` & `.catch` Methods

```py
def point(self, keywords: str, kname: str) -> None
```

The `.point` method associates a `key` with it's name, it's kind of like storing the same value with 2 different names, this can be useful to have a **safe** name, that will not corrupt and one that you can play with and possibily corrupt it.
Check out this example:
```py
e = datacontent("net", 1234)
e.append("myKey",  "myData")
# database -> {'myKey': 'myData'}
e.read("myKey")
# returns -> "myData"
e.point("myPointer", "myKey")
```
---
```py
def catch(self, keyword: Any) -> Any
```
The `.catch` method simply calls the pointer and returns the `key` content, not it's name.  Works like read, but transformed into the pointer version. 

```py
e = datacontent("net", 1234)
e.append("myKey",  "myData")
# database -> {'myKey': 'myData'}
e.read("myKey")
# returns -> "myData"
e.point("myPointer", "myKey")
e.catch("myPointer")
# returns -> "myData"
```
---
 ### Database `.log` & `.catchLog` Methods
 ```py
 def log(self, kname: Any) -> None
 ```
 
The `.log` function reads the data in your Key and prints it out, while also returning it's value. 
The `.catchLog` does the same, except it works based on Keywords and not Keys.

```py
e = datacontent("net", 1234)
e.append("myKey",  "myData")
e.point("myPointer", "myKey")
e.catchLog("myPointer")
# Terminal: myKey
```
---
### Database `.change_` Methods
```py
def change_content(self, kname, new_content):  
  self.database[kname] = new_content  
  return "result: " + str(self.database)  
  
def change_key(self, kname, new_name):  
  self.database[new_name] = self.database[kname]  
  del self.database[kname]  
  return "result: " + str(self.database)  
  
def change_pointer(self, old_pointer, new_pointer):  
  self.keywords[new_pointer] = self.keywords[old_pointer]  
  del self.keywords[old_pointer]  
  return "result: " + str(self.keywords)
```

The `.change_` operators (`content`, `key`, `pointer`) create a new object of each specified keys and delete the old ones. The result is returned, in the other hand, you can change the content of your keys manually using only... `1 line` of code!
```py
e.database["myKey"] = "myNewContent"
```
But, the `.change_content` method is better within uses of `.__enter__` & `.__exit__` methods.

---

### Database `With... as` , `.__enter__` & `.__exit__` Methods

```py
def __enter__(self) -> dataconnect | None

def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> dataconnect
```
---
Creating temporary databases is perfect within those commands, they do not save your database when you sucessfuly exit a `with... as`. They are simple to call and yet very clean and **readable**. The Database surely gets improved while combined with those methods. The `.__enter__` method gives the `as` call a value, in this case, the self value (this means that it is directly connected to the value you called before).
To call a Database with those built-in magical methods, simply use a `with... as` statement:
```py
with dataconnect("myConn", 1234) as client:  
	client.append("myText", "hello!")  
	client.point("myKeyword", "myText")  
	client.catchLog("myKeyword")
	# TERMINAL: hello!
	
client.read("myText")
# The database got erased, therefore, this won't read anything
```
---
This can also result into creating 2 Databases called `client` that won't clash with each other and have their own special contents. Transforming the Database into a Local Temporary Dict can be really useful while using it's not-complicated functions to have a cleaner and **less-typing** code.

---
### Database `.__len__` & `.__contains__`
Database comes with an integrated `.__len__` function, which means that using `len(database)` will return the actual number and not an error.
```py 
e = dataconnection("myConn", 1234)
# len(e) = database length + keywords database length

e.append("myFile", "content!!!")
e.point("myPointer", "myFile")
print(len(e))
# TERMINAL: 4 (key + content + keywords)
```
---
The Database also comes with an integrated `.__contains__` method, that will read through the Keywords and Database to find the item. In case of success, return bool `True` or `False`. The operation is a built-in function of python that administers customly using the `.__contains__` method.
```py 
e = dataconnection("myConn", 1234)

e.append("myFile", "content!!!")
e.point("myPointer", "myFile")
if "myFile" in e:
	print(True)
else:
	print(False)
# TERMINAL: True
```
This only works if the string is full, if you get half a string. 
By example `"myF" in e` will return False. Since it only reaches out for complete (and case sensitive) strings.

---

--- Connection Services (1.8), MewPlush.
