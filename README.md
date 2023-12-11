# Django Receipt Tracker

## Overview

Django Receipt Tracker is a web application for tracking and managing receipts. Users can create accounts, log in, and keep a record of their store purchases, including details like store name, date of purchase, item list, and total amount.


## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/merwan32/Basic-Django-Receipt-Tracker.git
   cd Basic-Django-Receipt-Tracker

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt

4. **Apply Migrations:**

    ```bash
    python3 manage.py migrate # On macOS/Linux
    python manage.py migrate # On Windows

5. **Run the Development Server:**

    ```bash
    python3 manage.py runserver # On macOS/Linux
    python manage.py runserver # On Windows

Visit http://localhost:8000/ in your browser.

