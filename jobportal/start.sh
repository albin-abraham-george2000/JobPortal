#!/bin/bash

# Navigate to the jobportal directory
cd jobportal

# Function to apply migrations
apply_migrations() {
    echo "Applying migrations..."
    python manage.py migrate
    echo "Migrations applied successfully."
}

# Ask user if they want to apply migrations
read -p "Do you want to apply migrations before starting the server? (y/n): " apply_migrations_choice

if [ "$apply_migrations_choice" == "y" ] || [ "$apply_migrations_choice" == "Y" ]; then
    apply_migrations
fi

# Start the Django development server
echo "Starting Django server..."
python manage.py runserver