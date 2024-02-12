# Basic Three-Tier Application Simulation - Frontend Overview

This project includes a front-end built with Vue.js, designed to display data in a table format. Initially, it uses placeholder data, which will later be replaced with data fetched from a Flask API, demonstrating a simple data flow from a MariaDB database to the front-end through the API.

## Front-End (Vue.js)

The front-end part of this application is developed using Vue.js. It is responsible for presenting the user interface and interacting with the middle-tier Flask API to retrieve and display data.

### Key Features

- **Data Display:** Utilizes Vue.js to render data in a table format. Initially set up with placeholder data.
- **API Integration:** Prepared to integrate with a Flask API to fetch real-time data from a MariaDB database.
- **Reactivity:** Leverages Vue's reactivity system to update the UI dynamically as new data is fetched.

### Setup Instructions

1. **Ensure Node.js and npm are installed:** Node.js and npm must be installed on your machine to set up the Vue.js project.

2. **Project Setup:**
   - Clone the repository and navigate to the front-end directory.
   - Run `npm install` to install dependencies, including Vue.js and Axios for making HTTP requests.

3. **Development:**
   - Modify the `HelloWorld.vue` component to include a table structure with placeholders for data.
   - The component fetches data from the API using Axios and updates the UI with the fetched data.

4. **Running the Application:**
   - Execute `npm run dev` to start the Vue.js development server.
   - Access the application through the URL provided in the terminal (usually `http://localhost:5173/`).
   - For production deployment, run `npm run build` to generate a production-ready build.
   - You can then deploy the generated files to a web server or hosting service.
   - Some hosting services, such as Netlify, Vercel, or GitHub Pages, allow you to deploy Vue.js applications easily.
   - Otherwise, you can host your own server using Nginx, Apache, or any other web server on your own infrastructure.

### Development Tips (In a professional production environment, consider the following best practices and tools to enhance the application further.)

- **Vue DevTools:** Utilize Vue DevTools for Chrome or Firefox to inspect and debug the Vue application.
- **Component Structure:** Keep your components modular and reusable to simplify maintenance and future enhancements.
- **State Management:** For larger applications, consider using Vuex for state management to handle data fetched from the API more efficiently.
- **Testing:** Write unit tests for your components and end-to-end tests for your application to ensure it works as expected. You can use tools like Jest, Mocha, or Cypress for testing.
- **Environment Variables:** Use environment variables to manage API URLs and other configuration settings. This allows you to switch between development, staging, and production environments easily. The `.env` file can be used to store environment-specific variables.
Here is an example of a `.env` file:

```VITE_API_URL=http://localhost:5000/api```

environment variables are always prefixed with `VITE_` in Vue.js applications. This is a security feature to prevent sensitive data from being exposed to the client-side code.

- **Error Handling:** Implement error handling for API requests and other operations to provide a better user experience. You can use Axios interceptors to handle errors globally in your application.

- **CI/CD:** Set up a continuous integration and continuous deployment (CI/CD) pipeline to automate the build, test, and deployment process. This can be done using tools like GitHub Actions, GitLab CI/CD, or Jenkins. For instance, you can configure the pipeline to run tests on every commit and deploy the application to a staging environment. Once the tests pass, it can be deployed to the production environment. You can automaticallly deploy the application to a web server or hosting service on every push to the main branch. You can also set up a staging environment to test the application before deploying it to production. You can do a lot of things with CI/CD, such as running linters, security checks, and performance tests.

- **Performance Optimization:** Optimize the performance of your application by using code splitting, lazy loading, and tree shaking. You can also use tools like Webpack Bundle Analyzer to analyze the size of your bundles and identify opportunities for optimization. Additionally, you can use performance monitoring tools like Lighthouse, WebPageTest, or Google PageSpeed Insights to identify performance bottlenecks and improve the user experience.

- **Security:** Ensure that your application is secure by following best practices for authentication, authorization, and data protection. You can use tools like OWASP ZAP, SonarQube, or Snyk to identify and fix security vulnerabilities in your application. You can also use security headers, content security policy, and other security measures to protect your application from common attacks.

- **Accessibility:** Make your application accessible to users with disabilities by following best practices for web accessibility. You can use tools like Axe, Lighthouse, or Wave to identify and fix accessibility issues in your application. You can also use ARIA roles, semantic HTML, and other accessibility features to improve the user experience for all users.

- **Documentation:** Document your code, APIs, and architecture to make it easier for other developers to understand and contribute to the project. You can use tools like Swagger, Postman, or Redoc to document your APIs. You can also use tools like JSDoc, VuePress, or Docusaurus to document your code and architecture. I personally prefer JSDoc for documenting both JavaScript and Vue.js code. It's a great way to keep your codebase well-documented and maintainable.

### Deploying the Application with Nginx on EC2:
# Deploying a Vue.js Application on AWS EC2 with Nginx

This guide provides a comprehensive overview of deploying a Vue.js application on an AWS EC2 instance running Ubuntu, utilizing Nginx as the web server. Part of the setup includes creating a configuration file for Nginx to correctly serve the Vue.js application. Here's a detailed explanation of the configuration steps and the significance of each directive within the Nginx configuration file.

## 1. Connecting to Your AWS EC2 Instance

Connect to your EC2 instance via SSH. Replace `your-public-dns-name` with your instance's public DNS and `/path/to/your-key.pem` with the path to your SSH key.

```bash
ssh -i /path/to/your-key.pem ubuntu@your-public-dns-name
```

## 2. Installing Nginx on Ubuntu

Update package lists and install Nginx:

```bash
sudo apt-get update
sudo apt-get install nginx -y
```

## 3. Configuring Nginx to Serve Your Vue.js Application

After installing Nginx, the next step is to configure it to serve your Vue.js application. This involves creating a new configuration file in the `/etc/nginx/conf.d/` directory. For this example, we named the file `vueapp.conf`.

### Detailed Explanation of `vueapp.conf`

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # Server name is optional since you're accessing via IP address
    # server_name _;

    root /home/ubuntu/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

- `listen 80 default_server;` and `listen [::]:80 default_server;`: These lines tell Nginx to listen on port 80 for IPv4 and IPv6 requests, respectively. The `default_server` parameter designates this server block as the default for requests that do not match any other server blocks.

- `# server_name _;`: This line is commented out because the server name is optional when accessing the application via an IP address. If you were using a domain name, you would uncomment this line and replace `_` with your domain name.

- `root /home/ubuntu/dist;`: Specifies the root directory for requests, which is the location of your Vue.js application's `dist` folder. Nginx will serve files from this directory.

- `index index.html;`: Defines `index.html` as the index file. When a directory is requested, Nginx will serve the `index.html` file from that directory.

- `location / {`: Begins the location block, which is used to define how to respond to requests for resources within the server.
  
  - `try_files $uri $uri/ /index.html;`: This directive attempts to serve the requested file or directory. If Nginx cannot find the file or directory, it falls back to serving `/index.html`, enabling SPA (Single Page Application) routing. This is crucial for Vue.js applications, where you want to handle routing on the client side.

## 4. Adjusting File Permissions

Change the ownership and permissions of the `dist` directory to ensure Nginx can read the files and directories:

```bash
sudo chown -R www-data:www-data /home/ubuntu/dist
sudo find /home/ubuntu/dist -type d -exec chmod 755 {} \;
sudo find /home/ubuntu/dist -type f -exec chmod 644 {} \;
```

## 5. Opening Firewall (If UFW is Enabled)

If you're using UFW, allow Nginx:

```bash
sudo ufw allow 'Nginx Full'
```

## 6. Configuring Security Group in AWS

Adjust your EC2 instance's security group settings to allow inbound traffic on port 80 (HTTP) and optionally on port 443 (HTTPS) from your desired sources. This step is performed in the AWS Management Console.

This guide outlines each step required to deploy a Vue.js application on an EC2 instance, from setting up the server with Nginx to ensuring the application is accessible to users. The `vueapp.conf` configuration file plays a crucial role in directing Nginx to serve your Vue.js application correctly, facilitating both the serving of static files and support for SPA routing.

### Conclusion

The front-end part of this application is built with Vue.js and is responsible for presenting the user interface and interacting with the middle-tier Flask API to retrieve and display data.
