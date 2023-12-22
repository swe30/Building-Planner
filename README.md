# Building-Planner
Web application for selecting, drawing, and annotating building plans can serve various purpose
# Building Plans Annotation Web Application

## Description

This web application allows users to select, draw, and annotate building plans. It provides a drawing area and a toolbar with various instruments for creating and manipulating drawings.

- **Draw Tools**: Lines, rectangles, circles, and other shapes.
- **Select Tool**: Allows moving, resizing, or deleting created shapes.
- **View Tool**: Show or hide annotations.

Annotations include length, breadth, and any other dimensions added by the user.

## Technologies Used

- Frontend: React
- Backend: Flask (Python)
- Database: SQLite
- ORM: SQLAlchemy

## Prerequisites

Before running the application, ensure you have the following installed:

- Node.js and npm (for React)
- Python 3.x
- Flask
- SQLite

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sweta30/building-plans-app.git
   cd building-plans-app



   ##Install Frontend Dependencies
   cd frontend
   npm install

   ##Install Backend Dependencies
   cd backend
   pip install -r requirements.txt

   ##Create the Database
   python app.py

   ##Start the Backend
   cd backend
   python app.py


   ##Start the Frontend
   cd frontend
   npm start

