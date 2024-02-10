# Basic Three-Tier Application Simulation - Backend Overview

This project includes a backend built with Flask, designed to serve data through RESTful APIs. It interacts with a MariaDB database to fetch and manipulate data, which is then consumed by a Vue.js frontend.

## Backend (Flask)

The backend part of this application is developed using Flask. It is responsible for handling HTTP requests, interacting with the database, and serving data to the frontend.

### Key Features

- **RESTful API Design:** Implements RESTful APIs to handle CRUD operations on the database. CRUD refers to Create, Read, Update, and Delete operations. These operations are mapped to HTTP methods such as POST, GET, PUT, and DELETE. For example, creating a new record is done using the POST method, reading records is done using the GET method, updating records is done using the PUT method, and deleting records is done using the DELETE method.
- **Database Integration:** Utilizes Flask-SQLAlchemy for ORM and interacts with a MariaDB database. SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access.
- **Environment Configuration:** Manages application configuration through environment variables using `python-dotenv`.
- **Security:** Implements security measures such as CORS (Cross-Origin Resource Sharing) and secure secret key generation. CORS is a security feature that restricts web pages from making requests to a different domain than the one that served the web page. It is a critical security mechanism that protects web applications from cross-origin attacks.

### Setup Instructions

1. **Ensure Python and pip are installed:** Python and pip must be installed on your machine to set up the Flask project.

2. **Project Setup:**
   - Clone the repository and navigate to the backend directory.
   - Run `pip install -r requirements.txt` to install dependencies, including Flask and Flask-SQLAlchemy.

3. **Secret Key Generation:**
   - Run `python generate_secret_key.py` to generate a secure secret key.
   - Update the `FLASK_SECRET_KEY` environment variable in the `.env` file with the generated key.

4. **Running the Application:**
   - Execute `flask run` to start the Flask development server. Or simply run `python app.py`.
   - The API will be accessible through the URL provided in the terminal (usually `http://localhost:5000/`).
   - Note that the bind address is set to 0.0.0.0 in the `app.py` file, allowing the server to be accessible from other devices on the same network. This is useful for testing the API on different devices.

5. **Running the 
6. **Running the Application in the Cloud:**
   - **Setting up an EC2 Instance:** To begin, navigate to the AWS Management Console and launch a new EC2 instance. This instance will act as the cloud server for hosting our Flask application. Choose an appropriate Amazon Machine Image (AMI) that comes pre-installed with Ubuntu Server. This choice is crucial as Ubuntu is widely supported and comes with a robust package ecosystem.
   - **Configuring Security Group:** It is imperative to configure the security group associated with your EC2 instance correctly. Navigate to the security group settings and add an inbound rule to open port 5000. This step is critical because our Flask server listens on port 5000 for incoming HTTP requests. By opening this port, we ensure that the Flask server is exposed to the outside world, allowing users to interact with our application via the internet.
   - **Bind Address Configuration:** Within your Flask application's `app.py` file, ensure that the bind address is explicitly set to `0.0.0.0`. This configuration is not arbitrary; it instructs the Flask server to be accessible on all network interfaces of the EC2 instance. This level of accessibility is essential for making the server reachable from any location on the internet, thereby facilitating global access to your application.
   - **Connecting to the Instance:** AWS provides multiple methods for connecting to your EC2 instance. For a seamless connection experience, you can use EC2 Instance Connect, which allows you to connect directly through the browser. Alternatively, for a more traditional approach, you can use SSH. Both methods are secure and efficient, ensuring that you can easily manage your instance.
   - **Environment Setup:**
     - After establishing a connection to your EC2 instance, proceed to set up the environment. Begin by updating the package lists for upgrades and new package installations by running `sudo apt-get update`.
     - Install Python3 and pip, essential tools for running Python applications, by executing `sudo apt-get install python3 python3-pip`. This step ensures that your EC2 instance has the necessary software to run the Flask application and manage Python packages.
     - Navigate to your project directory and install the project dependencies by executing `pip install -r requirements.txt`. Additionally, install `gunicorn` by running `pip install gunicorn`. Gunicorn is a Python WSGI HTTP Server for UNIX environments. It is chosen for its ability to handle multiple requests simultaneously with its pre-fork worker model, making it vastly superior for production environments compared to the default Flask server, which is designed for development purposes.
   - **Running the Server:** To launch the Flask application on the cloud, use the command `gunicorn --workers 3 --bind 0.0.0.0:5000 app:app`. This command starts the Gunicorn server with three worker processes, hosting our Flask application. The `--bind` option specifies the IP address and port number where Gunicorn will listen for requests, ensuring that the application is accessible over the internet.
   - **Accessing the Application:** With the server running, your application is now accessible at `http://<ec2_public_ip>:5000/`. Replace `<ec2_public_ip>` with the actual public IP address of your EC2 instance. This URL serves as the gateway for users worldwide to interact with your Flask application, hosted securely and efficiently on an AWS EC2 instance. 
  


### Real-World Scenario: Bind Address, Security Measures, and Authentication

In a real-world production environment, while setting the bind address to `0.0.0.0` allows the server to be accessible from any network interface, for enhanced security, it's advisable to bind the server to a specific IP address that limits access to a controlled environment, such as a private internal network or a secure VPN. For example, using `192.168.1.100` as the bind address would restrict server access to the local network only.

#### Security Measures for Bind Address Configuration:

1. **Firewall Configuration:** Configure the server's firewall to permit traffic only on essential ports and from trusted IP addresses, significantly mitigating the risk of unauthorized access.

2. **VPN Access:** Implement a Virtual Private Network (VPN) to secure access to the server. Binding the server to an IP address within the VPN ensures that only VPN-connected devices can access the server.

3. **Network Segmentation:** Use network segmentation to isolate the server from other network parts, reducing the potential impact of security breaches by limiting attackers' access to a specific network segment.

4. **Monitoring and Logging:** Actively monitor and log server access to identify and respond to unauthorized access attempts promptly.

5. **Regular Updates:** Maintain the server and all associated software with the latest security patches to close vulnerabilities that could be exploited by attackers.

#### Implementing Authentication:

In addition to the above security measures, implementing robust authentication mechanisms is crucial for protecting sensitive data and ensuring that only authorized users can access the application.

1. **User Authentication:** Implement user authentication using JWT (JSON Web Tokens) or OAuth 2.0. These methods provide secure and flexible options for managing user sessions and access controls.

2. **API Authentication:** Secure your API endpoints by requiring API keys or tokens for access. This ensures that only authorized applications can consume your API, protecting it from unauthorized use.

3. **Role-Based Access Control (RBAC):** Implement RBAC to define and enforce access controls based on user roles. This allows for fine-grained control over who can access specific resources and perform certain actions within the application.

4. **Two-Factor Authentication (2FA):** For highly sensitive applications, consider adding an extra layer of security by implementing 2FA. This requires users to provide two forms of identification before gaining access, significantly reducing the risk of unauthorized access.

By careful selecting the bind address, implementing these security measures, and ensuring robust authentication, you can significantly enhance the security posture of your Flask application in a production environment.

#### AWS: 

- On aws, the public IP of the aws instance currently running 18.234.52.80 (note that this is not an elastic IP).
- It has two ports open to all network interfaces (0.0.0.0), port 22 for SSH, and port 5000 for the flask server API access. 
- You can either run gunicorn when you ssh into the machine (You can  use EC2 connect, Putty, or OpenSSH), but since SSH sessions timeout, you can set up a system service where the server can run on boot. This is the recommended professional way since you don't have to worry about ssh disconnections, you simply boot up the instance and the service will start automatically.
- The username and password assigned to the instance to access the DB have read-only access for now (Refer to teh DB Overview section). 

For persistent access to your application, it's recommended to use an Elastic IP (EIP) with your EC2 instance. An Elastic IP is a static IPv4 address offered by AWS for dynamic cloud computing. Using an EIP can help you manage the mapping of this public IP address to any instance in your VPC, ensuring that the IP address for your application remains unchanged even if you stop and restart your EC2 instance.

#### Setting up an Elastic IP:
1. **Allocate New Elastic IP:** Navigate to the EC2 dashboard within the AWS Management Console. Under the "Network & Security" section, choose "Elastic IPs". Click "Allocate new address" and follow the prompts to allocate a new Elastic IP to your account.
2. **Associate Elastic IP with Your Instance:** After allocation, select the newly created Elastic IP from the list and click "Actions". Choose "Associate address" and select your EC2 instance. Confirm the association to ensure that your EC2 instance now uses the Elastic IP.
3. **Update DNS Records:** If you have a domain name associated with your application, update your DNS records to point to the new Elastic IP. This ensures that your domain name directs traffic to the correct IP address of your EC2 instance.

By following these steps, you can ensure that your application has a persistent public IP address, making it more reliable and accessible to your users.



### Development Tips

Here are best practices and tools to enhance the application further in a professional production environment:

- **Flask CLI:** Utilize the Flask CLI for running and managing the application more efficiently.
- **Database Migrations:** Consider using Flask-Migrate for handling database migrations.
- **Testing:** Write unit tests for your API endpoints using the Flask testing framework.
- **Error Handling:** Implement comprehensive error handling for your API endpoints to provide meaningful error messages. You can use Flask's error handling mechanisms to return appropriate HTTP status codes and error messages.
- **Logging:** Use Flask's built-in logging or integrate with external logging frameworks for better monitoring and debugging. You can use tools like Sentry, Loggly, or Logstash for centralized logging. By centralizing logs, you can easily monitor and analyze the application's behavior and performance.
- **API Documentation:** Document your API endpoints using tools like Swagger or Postman. A common practice is to use the OpenAPI Specification (OAS) to define and document your API. An example of this can be found in [the docker API documentation](https://docs.docker.com/engine/api/v1.44/). Docker uses redoc to render the OAS documentation. It's a great way to keep your API documentation up-to-date and easily accessible to other developers.
- **Security Practices:** Implement security best practices such as HTTPS, input validation, and rate limiting. You can use tools like OWASP ZAP, SonarQube, or Snyk to identify and fix security vulnerabilities in your application. You can also use security headers, content security policy, and other security measures to protect your application from common attacks.