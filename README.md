Smaart Helpdesk

A lightweight helpdesk support system built using Python (Django) with a simple and intuitive interface for users to create, view, and manage support tickets.

🚀 Overview

Smaart Helpdesk is a web application that provides basic helpdesk functionality — allowing users to:

📩 Create support tickets

🛠️ Track their issues

📋 View ticket history

🧑‍💻 Manage responses

It’s ideal for small teams or projects that need a simple ticketing/helpdesk system without heavy overhead.

📌 Features

✔️ Submit new support requests
✔️ View list of existing tickets
✔️ Update or modify tickets
✔️ Simple user interface (HTML + CSS templates)
✔️ API serializers for easy integration
✔️ Built with Django’s standard MVC architecture

🛠️ Tech Stack
Layer	Technology
Backend	Python, Django
Frontend	HTML, CSS
API	Django REST-friendly serializers
📁 Repository Structure
Smaart_helpdesk/
├── admin.py
├── apps.py
├── models.py
├── views.py
├── urls.py
├── templates/
│   ├── home.html
│   ├── create.html
│   ├── update.html
├── static/
│   └── style.css
├── serializers.py
├── tests.py
├── settings.py
└── wsgi.py
📥 Installation

Clone the repository

git clone https://github.com/Sathvik1696/Smaart_helpdesk.git
cd Smaart_helpdesk

Create & activate a virtual environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies

pip install -r requirements.txt

Run database migrations

python manage.py makemigrations
python manage.py migrate

Start the development server

python manage.py runserver

Open in your browser
Visit: http://127.0.0.1:8000

🧪 Running Tests
python manage.py test
🧠 How It Works

Users land on a homepage listing the tickets.

They can create a new ticket using the form.

Each ticket can be viewed/updated using standard CRUD operations.

Templates render the UI for interactions with the ticket system.

📋 Contributing

Contributions are welcome! Here’s how you can help:

Fork the repository

Create a feature branch: git checkout -b feature-name

Commit your changes git commit -m "Add feature"

Push to your branch git push origin feature-name

Open a Pull Request

📜 License

This project is open-source and free to use — license details can be added here.
