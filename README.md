# UserAPI
I have Used Mysql Database to store the data of the user.<br>
The first_name query parameter is passed through endpoint. It will search the first_name in the user table for all users with the beginning of first_name matching the param first_name <br>
If the first_name matches then it will return the matched data. Otherwise It will call an external API with the query parameter and if we get records from API then records will store in user table and as well return the response to the user <br>
Used Postman to test this API.<br>

Here are the some snapshots.<br>
I just inserted two records manually into users table:<br>
![Screenshot 2023-07-14 122257](https://github.com/bhargav2550/UserAPI/assets/106314092/13962226-8242-4d82-bf1d-102d9d12dfdb)

If we search for "will" it will return all the records with first_name beginning with "will".<br>
![Screenshot 2023-07-14 122418](https://github.com/bhargav2550/UserAPI/assets/106314092/876d7266-cf3f-4eb9-af5b-5dd540edf53c)

If first_name not matched in users table it will call an external API and store the records in the database.<br>

We can develop Restful API using Django and Django REST.<br>
userAPI project is developed with Django only.<br>
restful is developed with Django REST.
