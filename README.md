# UserAPI
I have Used Mysql Database to store the data of the user.<br>
The endpoint must pass the data with query parameter first_name. We need to search the first_name in the user table for all users with the beginning of first_name matching the param first_name <br>
If the first_name matches then it will return the matched data. Otherwise we call an external API with the query parameter and it will return some records.They will store in user table and as well return the response to the user <br>
Used Postman to test this API.
