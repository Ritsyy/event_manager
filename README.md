## Project Description
A Flask Application(only REST APIs, no front end part) with CRUD operations of Event Management. Please use mysql to store the events. Events can be anything like technical event, meetup event, celebration event, etc.

### Setup Information
1. Install requisite packages:
```shell
$ pip install -r requirements.txt
```
2. Create tables:
```shell
$ ./models.py
```
3. Run service:
```
$ python app.py
```
4. Give it a try:
```shell
>> import requests, json
>> requests.get('http://localhost:5000/events').json()
[]
>> requests.post('http://localhost:5000/events',
                 headers={'Content-Type': 'application/json'},
                 data=json.dumps({"name":"test3"
"description":"test description"
"venue":"phoenix"
"organizer":"richa"
"registeration_fees":"2000"})).json()

response : {
    "description": "test description",
    "end_date_time": null,
    "id": 1,
    "name": "test3",
    "organizer": "richa",
    "registeration_fees": 2000,
    "start_date_time": null,
    "venue": "phoenix"
}
>> requests.get('http://localhost:5000/events/1').json()
{
    "description": "test description",
    "end_date_time": null,
    "id": 1,
    "name": "test3",
    "organizer": "richa",
    "registeration_fees": 2000,
    "start_date_time": null,
    "venue": "rm204"
}
>> requests.put('http://localhost:5000/events/1',
                headers={'Content-Type': 'application/json'},
                data=json.dumps({"name":"test_new"})).json()
{
    "description": "test description",
    "end_date_time": null,
    "id": 1,
    "name": "test new",
    "organizer": "richa",
    "registeration_fees": 2000,
    "start_date_time": null,
    "venue": "rm204"
}
>> requests.delete('http://localhost:5000/event/1')
>> requests.get('http://localhost:5000/event/1').json()
[]
```

Don't forget that you must pass a "Content-Type: application/json" header along with your request!
