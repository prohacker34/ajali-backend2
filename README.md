# Ajali- backend
Ajali! is a web application that allows users to report accidents or emergencies, attach media files (images, videos), and notify emergency responders. Admins can view, manage, and analyze incident data in real-time.
## Features
User Registration & Login
JWT-based Protected Routes
Role-based Access Control (Admin vs Regular User)
Create, View, and Delete Incident Reports
Upload and Link Media to Incidents
Admin Panel to Manage Users and Incidents
## Project Structure
Ajali-backend/ ├── migrations
               ├── server/ │
               │            ├── models/ ├── __init__.py
               │            │            ├── incident.py
               │            │            ├── media.py
               │            │            ├── user.py
               │            │
               │            ├── routes/  ├── __init__.py
               │            │            ├── admin_routes.py
               │            │            ├── auth_routes.py
               │            │            ├── incident_routes.py
               │            │            ├── media_routes.py
               │            │            ├── user_routes.py
               │            │
               │            ├── utils/   ├── ___init___.py
               │            │            ├── auth.py
               │            │            ├── upload.py
               │            ├── __init__.py
               │            ├── seed.py
               │            ├── uploads
               │
               │
               ├── .env
               ├── config.py
               ├── generate_secret.py
               ├── pipfile
               ├── pipfile.lock
               ├── README.md
               ├── requirments.txt
               ├── run.py
               ├── secrets

## API Endpoints
### Auth
Endpoint	Method	Description
/auth/register	POST	Register a new user
/auth/login	POST	Login and get JWT
/auth/user	GET	Get current user info


### Incidents
Endpoint	Method	Description
/incidents/	GET	Get all incidents
/incidents/	POST	Report a new incident
/incidents/ PATCH   update an incident
/incidents/<id>	DELETE	Delete incident (admin only)
### Media
Endpoint	Method	Description
/media/	POST	Upload media file
/media/<incident_id>	GET	Get media for an incident

### Admin
Endpoint	Method	Description
/admin/users	GET	List all users


## Installation & Setup
1. Clone the repo
   git clone SSH git@github.com:munge124/Ajali-backend.git

2. Create a virtual environment
   pipenv install

3. Set environment variables
   .env

4. Run migrations
    $ flask db init
    $ flask db migrate -m "message"
    $ flask db upgrade

5. Seed the data
    $ python3 server/seed.py

6. Start the server
    $ python3 run.py
## Testing
### Thunder client
 You can make the following request:
1.    GET  http://127.0.0.1:5000/users to get all users
2. To register POST http://127.0.0.1:5000/auth/register in the body tag use JSON format to write the email,password, and username of the user
3. login POST http://127.0.0.1:5000/auth/login to login registered user go to the body tag and write the email and password of the user in JSON format
4. To acces admin routes you must login(step 2), copy the access token and got to the headers tab under the tab there are two dashes one short and another long, this is what to write Authorization for the short one and Bearer access token.
- Make sure you leave space between the word Bearer and the token.

- Make sure that the word Bearer starts with capital "B".

- Your answer should look something like this:
         Authorization    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
5. Once you are able to access admin routes the admin will be able to update status

## Author
- Habert Otieno.
- Munge Kariuki.
## License
MIT License