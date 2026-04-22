# Flask Docker App 
# Overview
This project demonstrates a simple Flask web application containerized using Docker and managed with Docker Compose. It showcases how to package applications into containers for consistent and portable deployment.

## Tech Stack

* Python (Flask)
* Docker
* Docker Compose

## Features

* Containerized Flask application
* Easy setup using Docker Compose
* Lightweight and beginner-friendly project
* Runs on any system with Docker installed

## Project Structure
flask-docker-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml

## API Endpoints

GET /messages
→ Fetch all messages

POST /add
→ Add a new message

Example:
curl -X POST http://localhost:5000/add 
-H "Content-Type: application/json" 
-d '{"message":"Hello"}'

## How to Run
docker compose up -d
Then open:
http://localhost:5000











Rishika Verma

