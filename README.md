Simple FastApi apllication with mongoDb as database

The database has one collection messages which has channel,author and text attributes

Various endpoints are created using FastApi to demonstrate data retrieval from mongodb

**How to use the code?**

1.Clone the respository
```
git clone https://github.com/mdmudassir7/UserRolesActions.git
```
2.Create a virtual environment
```
python -m venv env
```
3.Install the requirements
```
pip install -r requirements.txt
```
4.Run the server
```
uvicron main:app --reload
```
5.Visit the localhost port 8000 
```
http://127.0.0.1:8000/
```
6.For the api documentation visit
```
http://127.0.0.1:8000/docs
```