# UNA HEALTH

### Task Done
- /api/v1/levels/ : Retrieve ( GET ) a list of glucose levels for a given
    user_id , filter by start and stop timestamps (optional). This endpoint
    should support pagination, sorting, and a way to limit the number of
    glucose levels returned.
- /api/v1/levels/<id>/ : Retrieve ( GET ) a particular glucose level by id .
- /api/v1/levels/ : Create ( POST )  endpoint to fill / pre-populate the model / database via an API
    endpoint.



## Installation
- Clone this repository ```git clone https://github.com/nouwatinjacob/UnaHealth.git```
- Navigate to the directoty ```cd unahealth```
- Install all depencies with ```pip install -r requirements.txt```
- Using ```make makemigrations``` and ```make migrate``` migrate the database
- Seed data in csv to database using ```make seed_csv_data```
- Start the server by running ```make runserver```

## Testing

- Run server-side test with `make test`


## Copyright

&copy; Nouwatin Jacob
