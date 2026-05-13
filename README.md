# Team Task Manager

## Overview

Team Task Manager is a full-stack Django web application that helps teams manage projects, assign tasks, track task progress, and monitor workflow efficiently.

The application includes:

- Authentication system
- Signup/Login functionality
- Role-based access control
- Project management
- Task assignment & tracking
- REST APIs
- Dashboard analytics
- CRUD operations

This project demonstrates both frontend and backend full-stack development using Django and Django REST Framework.

---

# Features

## Authentication & Authorization

- User Signup
- User Login
- Logout Functionality
- Session-based Authentication
- Role-Based Access Control
- Admin & Member Roles
- Protected Routes

---

# Project Management

Admins can:

- Create Projects
- Edit Projects
- Delete Projects
- Manage Team Workflow
- View All Projects

---

# Task Management

Admins can:

- Create Tasks
- Assign Tasks to Members
- Edit Tasks
- Delete Tasks
- Track Task Progress

Members can:

- View Assigned Tasks
- Update Task Status

Task Status Workflow:

- Pending
- In Progress
- Completed

---

# Dashboard Features

The dashboard displays:

- Total Projects
- Total Tasks
- Completed Tasks
- Task Statistics
- Dynamic Task Updates

---

# Search & Filter

Users can:

- Search Tasks by Title
- Filter Tasks by Status

---

# REST APIs

The project includes REST API endpoints using Django REST Framework.

## API Endpoints

### Tasks API

```text
/api/tasks/
