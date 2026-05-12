Team Task Manager Project Documentation
A full-stack Django-based Team Task Management application designed to help teams manage projects, assign
tasks, monitor workflow, and track task progress efficiently.
Project Features
• User authentication and login/logout system
• Role-based access control (Admin and Member)
• Project creation, editing, and deletion
• Task creation, editing, updating, and deletion
• Task assignment to team members
• Task status workflow (Pending, In Progress, Completed)
• Dynamic dashboard analytics
• Task search and filtering
• Responsive Bootstrap-based frontend UI
• Success alert messages and notifications
Technologies Used
• Python
• Django
• Django ORM
• SQLite Database
• HTML
• CSS
• Bootstrap 5
• Django Templates
Database Models
• User Model - handles authentication and roles
• Project Model - stores project details and team members
• Task Model - stores task details, status, due dates, and assignments
Authentication System
• Admin creates user accounts through Django Admin Panel
• Users login using secure session-based authentication
• Role-based permissions restrict unauthorized access
• Members can only view/update assigned tasks
Dashboard Functionalities
• Total Projects Count
• Total Tasks Count
• Completed Tasks Count
• Pending Tasks Count
• In Progress Tasks Count
• Recent Tasks Display
CRUD Operations Implemented
• Create Project
• Read Project
• Update Project
• Delete Project
• Create Task
• Read Task
• Update Task
• Delete Task
Workflow Explanation
• Admin logs into the system
• Admin creates projects
• Admin assigns team members to projects
• Admin creates tasks and assigns them to users
• Members log in and view assigned tasks
• Members update task status
• Dashboard reflects updated project progress
Security Features
• Protected routes using authentication checks
• Role-based authorization
• Admin-only task/project creation
• User-specific task visibility
• Secure session handling
Future Improvements
• Dashboard charts and analytics
• Priority-based task management
• Email notifications
• Dark mode UI
• File attachments
• Task comments and collaboration
• Cloud deployment
Learning Outcomes
• Full-stack web development using Django
• Database relationships and ORM
• Authentication and authorization
• Frontend and backend integration
• CRUD operations
• Dynamic template rendering
• Responsive UI design
Installation Steps
1. Clone the repository.
2. Navigate to the project folder.
3. Create and activate a virtual environment.
4. Install Django using pip.
5. Run migrations.
6. Create a superuser.
7. Start the Django development server.
8. Open the application in browser.
