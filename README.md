## Introduction
This project aims to create a web application that connects prospective tenants with property agents. Tenants can browse available properties and register their interest. Agents can log in to see the details of tenants interested in their properties.\
The application has two main parts:
For Prospective Tenants: A public page where tenants can view property listings and register their interest.
For Agents and Admins: A secure login system where agents and admins can view tenant details for the properties they manage.


## Technical Implementation
The project uses Flask (a Python web framework) and SQLite (a database). The front-end is built with HTML, CSS, and JavaScript to ensure it looks good and works well. The project is designed to be easy to update and maintain.


## Database Retrieval
The utils.py file contains functions responsible for interacting with the databases and fetching data as needed.

The get_properties() function gets all the properties from the properties.db database. It connects to the database, retrieves all properties, and then closes the connection before sending back the properties.

The get_property_info(property_id) function fetches specific details about a property based on its ID from properties.db. It connects to the database, gets the property's name, type, and agent name using the ID, and then closes the connection before sending back the details

The get_user(email, password, name) function retrieves user data from users.db. It connects to the database, gets user information based on the provided email, password, and name, and then closes the connection before sending back the user's details.

The get_tenant_requests(agent_name) function fetches tenant requests from tenant_request.db based on the agent's name. If no agent name is given, it fetches all requests. It connects to the database, retrieves tenant information, and then closes the connection before sending back the requests.


## Dependencies

Flask (I used a virtual environment to use flask on my laptop)
SQLite


## Configuration
For reviewers or anyone working with the code, if you need to clear the tenant requests database, you can follow these steps:

1.Delete the tenant_request.db file from the project directory.
2.Run database.py to create a new and empty database.
This process will reset the tenant requests database, allowing for a fresh start with no existing data.


## Running the App
Run app.py to start the application then type 'http://localhost:5000/' into your browser
Admin credentials: admin1@gmail.com , password: admin123 /admin2@gmail.com , password: admin456
Agent credentials: agent1@gmail.com / password: agent123


