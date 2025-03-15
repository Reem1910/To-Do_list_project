# Use the official Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Expose the port the app runs on (change 5000 if your app uses a different port)
EXPOSE 5000

# Command to run the app
CMD ["python3", "TODO_List_Manager_Project.py"]