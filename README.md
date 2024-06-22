MakersBnB README

Project Overview:

Project Name: Engineering Project 1 (MakersBnB)

Introduction:

Objective: Build a web application (BnB clone) collaboratively.
Key Activities: Effective team communication, project breakdown, agile workflow implementation.

Getting Started:

Team Setup:

Create a private Slack channel with team members and coaches.
Fork the project's seed repository and add team members as collaborators.
Read and discuss the project specification together.

Project Setup:

Create a Trello board for task management.
Translate specifications into user stories.
Start the initial sprint.

Agile Workflow:

Sprints and Ceremonies:
Conduct short sprints (2 days) with defined goals.
Daily stand-ups for progress updates.
Retrospectives to reflect on teamwork and improvements.

Developer Workflow:

Minimum Viable Product (MVP):

Focus on implementing core features.
Iterate based on feedback for continuous improvement.
User Story Management:

Break down user stories into manageable tasks.
Create clear tickets with specific technical details and acceptance criteria.
Best Practices:

Team Collaboration:

Rotate pairs regularly to avoid burnout.
Prioritize team health and well-being.
Development Process:

Emphasize testing and TDD for robust code.
Avoid rushing to meet deadlines at the expense of quality.
Inclusivity and Communication:

Ensure every team member's voice is heard and valued.
Utilize stand-ups and retrospectives for feedback and discussion.
Additional Resources:

Leverage web development tools and guidance from previous modules.
Explore additional resources for building user-friendly applications.



Steps to start the project:

# Set up the virtual environment
; python -m venv makersbnb-venv

# Activate the virtual environment
; source makersbnb-venv/bin/activate 

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing
(makersbnb-venv); playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
(makersbnb-venv); createdb YOUR_PROJECT_NAME
(makersbnb-venv); createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser

