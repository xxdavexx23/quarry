# Basic Three-Tier Application Simulation - DB Setup Overview

This section outlines how the MariaDB database is set up for the three-tier application simulation. It includes the database schema, table creation, and example data insertion. It also includes how we set up the database with AWS RDS for integration with the Flask API.

## Database Setup

The database for this application is a simple MariaDB database. It includes a single table called `heroes` with two columns: `id` and `name`. The `id` column is an auto-incremented integer and the primary key of the table. The `name` column is a variable character string that stores the names of DC superheroes.
The databse is created in AWS RDS through the following steps:

1. **Create a Database Instance:**
   - Log in to the AWS Management Console.
   - Navigate to the RDS service.
   - Click on "Create database."
   - Select "Standard Create" and choose "MariaDB" as the database engine.
   - Choose the appropriate version of MariaDB.
   - Select the "Free tier" template for the instance class.
   - Connect the ec2 instance to the RDS instance. This is very important because the ec2 instance will be used to connect to the RDS instance.
   - Set the DB instance identifier, master username, and master password.
   - Click "Create database."

2. **Connect to the Database:**
   - Once the database is created, you can connect to it using a MariaDB client such as MySQL Workbench or the MySQL command-line client.
   Here is an example to connect to the databsae through a MariaDB client:

        ```bash
            mysql -h <endpoint> -u admin -p
        ```

   - Use the endpoint provided by AWS RDS to connect to the database.
   - Use the master username and password to authenticate.
   - For best security practices, I have created a read-only user and password for the database. This is the user and password that will be used to connect to the database from the Flask API. The master username and password are used to connect to the database from the MySQL client. I will outline how to create a read-only user in the next section.
   - Once connected to the database, you can create the `heroes` table and insert example data into it.

3. **Create the database and the table:**
   - Once connected to the database, you can create the `heroes` table using the following SQL command:

        ```sql
            CREATE DATABASE dcheroes;
            USE dcheroes;
            CREATE TABLE heroes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );
        ```

   - This will create a new database called `dcheroes` and a table called `heroes` with two columns: `id` and `name`.
   - The `id` column is an auto-incremented integer and the primary key of the table.
   - The `name` column is a variable character string that stores the names of DC superheroes.

4. **Insert Example Data:**
    - Once the table is created, you can insert example data into it using the following SQL command:
          ```sql
                INSERT INTO heroes (name) VALUES
                ('Superman'),
                ('Batman'),
                ('Wonder Woman'),
                ('The Flash'),
                ('Green Lantern'),
                ('Aquaman'),
                ('Cyborg');
            ```
    - This will insert the names of seven DC superheroes into the `heroes` table.
    - You can verify that the data has been inserted by running a `SELECT` query on the table.
    - Once you have inserted, you are ready to connect the Flask API to the database.

5. **Create a Read-Only User:**
    - It is best practice to create a read-only user for the database. This user will be used to connect to the database from the Flask API. This is done to ensure that the Flask API does not have full access to the database. It only has read access to the database. This is a security best practice.
    - To create a read-only user, you can use the following SQL command:

        ```sql
            CREATE USER 'your_user'@'<ec2_internal_ip>' IDENTIFIED BY 'password';
            GRANT SELECT ON dcheroes.* TO 'your_user'@'<ec2_internal_ip>';
            FLUSH PRIVILEGES;
        ```

    - This will create a new user called `your_user` with the password `password`. The user will have read-only access to the `dcheroes` database.
    - Note that the IP provided is not the public IP of the ec2 instance. It is the internal IP of the ec2 instance. This is because the Flask API will be running on the ec2 instance and will need to connect to the RDS instance. We used the internal IP since both services are running on the same VPC. The VPC is your virtual private cloud. It is a virtual network that is dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS cloud. It is a best practice to use the internal IP of the ec2 instance to connect to the RDS instance. This is because it is more secure than using the public IP of the ec2 instance.
    - Now that the database is set up, you can connect the Flask API to the database.
    - You can confirm that your user is set up by running the following command:

        ```sql
            SELECT user, host FROM mysql.user;
        ```

    - Now, on your EC2 instance you can try connecting through the command line:

        ```bash
            mysql -h <endpoint> -u your_user -p
        ```

    - You will be prompted to enter the password. Once you enter the password, you will be connected to the database. This will confirm that the user has been set up successfully and connect from the ec2 instance to the RDS instance.

6. **Database Configuration in Flask API:**
    - For your flask server, we are using SQLAlchemy to connect to the database. SQLAlchemy is a popular SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language. It is particularly useful for the Flask API because it allows us to interact with the database using Python code. The URI for connecting to the database should be in the following format:

     ```sql
            mysql+pymysql://your_user:password@<db_endpoint>/database_name
    ```

    Or in our case:

    ```sql
            mysql+pymysql://your_user:password@<db_endpoint>/dcheroes
     ```

    - The URI is used to connect to the database from the Flask API. It includes the username, password, endpoint, and database name. This is the URI that will be used to connect to the database from the Flask API. The URI is used to create the database engine in SQLAlchemy. The database engine is used to connect to the database and execute SQL commands. The URI is passed to the `create_engine` function in SQLAlchemy to create the database engine. The database engine is then used to connect to the database and execute SQL commands. This is how the Flask API connects to the database.
    Note that it is not recommended to connect the root user to the database from the Flask API.  Instead, you should connect through the read-only user we configured.

## Conclusion

With this, you can now fetch the data from the Flask server directly from the database and develop REST APIs to serve the data to the front-end. This is a basic overview of how the database is set up for the three-tier application simulation
