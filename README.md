# Clonus - Your Digital Health Twin

### Team Name: TechTogether 

### Team Members:
* Roshan Patil (Team Leader)
* Neha Chandele
* Shreya Nikam
* Bhagyashree Mistari

---

## 📖 Project Abstract

Clonus is an innovative health-tech prototype designed to combat the growing issue of lifestyle-related chronic diseases. Many people struggle to understand the slow, cumulative impact of their daily habits on their long-term health. Clonus addresses this by creating a personalized **"Digital Twin"**—an AI-powered projection of a user's future health.

By inputting their daily lifestyle and health data, users receive a dynamic, visualized health score and a projection of their physical well-being over time. The application features an interactive simulation model that allows users to see how positive changes (like improved sleep or diet) can alter their future health trajectory. Clonus isn't just a predictor; it's a proactive health companion that provides actionable, AI-driven recommendations to empower users to take control of their health today for a better tomorrow.

---

## 🛠️ Tech Stack

### Backend
* **Python:** The core programming language.
* **Django:** The web framework used to structure the application.

### Frontend
* **HTML5:** For the structure of all web pages.
* **CSS3:** For all custom styling, layouts, and responsiveness.
* **JavaScript (ES6):** For client-side interactivity, including the multi-step form, sliders, and dynamic chart updates.
* **Chart.js:** For data visualization of the health score gauge.
* **Font Awesome:** For icons used throughout the UI.

### Database
* **SQLite:** The default Django database used for rapid prototyping and storing user profile data.

---

## 📊 Dataset Used

This project does not use any external, pre-existing datasets. For the "Health Trajectory" demonstration featuring the user "Roshan," a **static, pre-assumed dataset** was created within the application's frontend. This dataset was designed to realistically simulate a 10-month health progression based on factors like poor diet and lack of exercise.

---

## 🚀 Getting Started

### Installation & Setup

Follow these steps to get the project running on your local machine.

**Prerequisites:**
* Python 3.8 or higher

**Steps:**

1.  **Clone or Unzip the Project:**
    Download and unzip the project folder.

2.  **Navigate to the Project Directory:**
    Open a terminal and navigate into the project's root folder (the one containing `manage.py`).
    ```bash
    cd path/to/clonus_project
    ```

3.  **Create and Activate a Virtual Environment:**
    * Create the environment:
        ```bash
        python -m venv venv
        ```
    * Activate it:
        * On Windows: `venv\Scripts\activate`
        * On macOS/Linux: `source venv/bin/activate`

4.  **Install Dependencies:**
    Install all required packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run Database Migrations:**
    This command sets up the necessary database tables.
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (for Admin Access):**
    This allows you to log in to the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Development Server:**
    You're all set!
    ```bash
    python manage.py runserver
    ```
    The project will be available at **http://127.0.0.1:8000/**.

---

## 📋 How to Use the Application

1.  **Visit the Landing Page:** The main page provides an overview of the project.
2.  **Enter the App:** Click on **"Try Model"** to go to the main application hub.
3.  **Register a New User:** Click **"Register New User"** and fill out the interactive, multi-step form with health details.
4.  **View Personalized Dashboard:** After submission, you'll be redirected to a personal dashboard showing your calculated **Health Score**, key impact factors, and AI-driven recommendations.
5.  **Explore the User List:** Navigate to the main dashboard to see a list of all registered users.
6.  **View the "Roshan" Demo:** From the user list dashboard, click **"Show Health Model"** to see the interactive 10-month health trajectory simulation.
7.  **Edit a Profile:** Click on any user to view their dashboard, then click the **"Edit Details"** button to update their information using the pre-filled form.

---

## 📸 Screenshots


**1. Main Landing Page**
<img width="1975" height="4300" alt="screencapture-127-0-0-1-8000-2025-10-05-19_54_47" src="https://github.com/user-attachments/assets/9e7a1af9-7345-41a0-b680-032ef5d4291a" />


**2. Multi-Step Registration Form**
<img width="675" height="917" alt="image" src="https://github.com/user-attachments/assets/bc7ff127-5451-4461-a317-b59467df14ae" />


**3. Personalized Health Dashboard**
<img width="1919" height="1778" alt="screencapture-127-0-0-1-8000-dashboard-7-2025-10-05-19_55_50" src="https://github.com/user-attachments/assets/3f1e30bc-2024-4712-98df-40becad31158" />


**4. Interactive "Health Trajectory" Model**
<img width="1024" height="960" alt="image" src="https://github.com/user-attachments/assets/643e73e0-991c-48ba-9026-2c9c971c4482" />


**5. User List Dashboard**
<img width="823" height="884" alt="image" src="https://github.com/user-attachments/assets/cbe991d0-b802-4fa8-a7f5-500afce8bea3" />

