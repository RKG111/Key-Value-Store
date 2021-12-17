#### Cloning the repository

```
 git clone https://github.com/RKG111/Key-Value-Store.git
 cd Key-Value-Store
```

#### Installation of dependencies
```
$ pip install -r requirements.txt
```
#### Performing necessary migrations
```
 python manage.py makemigrations
 python manage.py migrate
```
#### Running the project
```
 python manage.py runserver
```

#### To list all KEY VALUE pairs paste the following command in terminal
```
 curl -H “Accept: application/json” http://127.0.0.1:8000/get
```



#### To get the value of a particular KEY paste the following command in terminal
```
 curl -X GET -H "Content-type:application/json" --data "{\"key\":\"Key name\"}" http://127.0.0.1:8000/get/key
```
eg: to get the value of KEY= "xyz" type
```
 curl -X GET -H "Content-type:application/json" --data "{\"key\":\"xyz\"}" http://127.0.0.1:8000/get/key
```

#### To set a new pair of KEY-VALUE pair paste the following command in the terminal
```
 curl -X GET -H "Content-type:application/json" --data "{\"key\":\"Key name\",\"value\":\"Value of the key\"}" http://127.0.0.1:8000/set/key
```
eg: to set the Key="qwe" VALUE="QWE"
```
 curl -X GET -H "Content-type:application/json" --data "{\"key\":\"qwe\",\"value\":\"qwe\"}" http://127.0.0.1:8000/set/key
```
