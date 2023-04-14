# Job Portal Project Using Python Django 

We have developed a fully functional web application using python as backend with SQL Server database and HTML and bootstrap for frontend.
We have created several views for all functions in views.py.
Testing are done and all the test cases for user master, candidate and company models are added tests.py file.

## Modules and basic functions:
	Employee – View the Job posts and can apply for the jobs.
	Employer – Post Jobs and view them.
	Admin   - Delete and update users.
	
## Steps to be followed to run the application :

- Before running the application make sure that you installed all the requirements given in requirement.txt <br />
- Go to settings.py and change the database connection details to your server.<br />
	```
	 DATABASES = {
    	  'default': {
          'ENGINE': 'mssql',
          'NAME': 'Database Name',
          'USER': 'User Name',
          'PASSWORD': 'Password',    
          'HOST': 'Server Name',
          'PORT': '',

          'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
                     },
    	            },
	           }
	```
- For running the application: <br />
	```
	python manage.py runserver
	```
## Commands for Database Migrations if any changes needed(Optional):

```
python manage.py makemigrations <app-name>
python manage.py migrate
```

## Command for Test the application :
```
python manage.py test

```
## Dive into application features :

- Either select as company or candidate and register with details, if you are already registered go with login. <br />
- Login to the application either as company or candidate with user credentials.<br />
- If loggined as candidate(employee) :
	- Update profile if needed which includes updation of resume, profile photo,contact,address etc
	- Candidate can check the Job listing and can apply for interested jobs.
- If loggined as Company(Employer)
	- View the dashboard
	- Update profile if required which includes updation of company contact,address,company logo etc
	- Can post jobs by using Post a Job option in the sidebar
	- View application lists by checking the Application List option in the sidebar
	- View the posted jobs by selecting the Job Lists option
- If the admin want to login,go to /adminloginpage and have to use admin credentials(username : admin, password : admin)
	- Admin can view the dashboard
	- View the users list by selecting the Users List option in the sidebar and can manage(delete) the users if needed
	- Admin can view the company list by selecting the Company List option in the sidebar and can manage(delete,update) campanies if needed 




