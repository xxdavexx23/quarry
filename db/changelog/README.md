# MariaDB Database Setup

Assuming you have a MariaDB server running, you can create a new database and table to store the data for this application. The following SQL commands can be used to set up the database and table:

```CREATE DATABASE helloworld;
USE helloworld;
CREATE TABLE dc_heroes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);
```

And you can INSERT example data into the table:

```INSERT INTO dc_heroes (name) VALUES ('Superman'), ('Batman')
...
```

This will allow you to fetch data from the `dc_heroes` table using the Flask API and display it in the Vue.js front-end.

It is worthy to note that data insertion into the table directly from the database is not the best practice. It is recommended to use a form to insert data into the table. This is just an example to show how to insert data into the table. A form can be created in the front-end to insert data into the table. Data is usually inserted from apps to the database through the API.
