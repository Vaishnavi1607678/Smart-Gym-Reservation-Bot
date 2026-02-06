# Smart-Gym-Reservation-Bot


A simple, end-to-end **ML + Backend + Docker** project that predicts the **least crowded gym hours** and allows users to **reserve slots** via an API.

This project is beginner-friendly, fully runnable, and designed to demonstrate **real-world MLOps concepts** in a clean and practical way.

---

##  Project Overview

Going to the gym at peak hours can be frustrating. This bot helps by:

* Analyzing historical gym usage data
* Predicting the **least crowded time slots**
* Recommending optimal hours to users
* Allowing users to **book gym slots**
* Logging booking notifications

The entire system is **Dockerized** and ready for **CI/CD and cloud deployment**.

---

##  Key Features

*  **Crowd Prediction** using historical data
*  **Smart Recommendations** for least busy hours
*  **Gym Slot Booking API**
*  **SQLite Database** for storing bookings
*  **Dockerized Application**
*  **Swagger UI** for live API testing
*  Easily extendable to Twilio / Google Calendar

---

##  Tech Stack

| Layer            | Technology        |
| ---------------- | ----------------- |
| Backend API      | FastAPI           |
| Data Processing  | Pandas            |
| Containerization | Docker            |
| API Docs         | Swagger (FastAPI) |
| Language         | Python 3.10       |

---

## Project Structure

```
Smart-Gym-Reservation-Bot/
│
├── backend/
│   ├── __init__.py
│   ├── app.py
│   ├── model.py
│   ├── database.py
│   ├── notifier.py
│   └── requirements.txt
│
├── data/
│   └── gym_usage.csv
│
├── Dockerfile
└── README.md
```

---

## How It Works

1. Historical gym usage data is stored in `gym_usage.csv`
2. The model identifies the **least crowded hour**
3. FastAPI exposes endpoints for:

   * Getting recommendations
   * Booking slots
4. Bookings are stored in SQLite
5. Notifications are logged to the console

---

##  Run the Project Locally

### 1️⃣ Build Docker Image

```bash
docker build -t smart-gym-bot .
```

### 2️⃣ Run Container

```bash
docker run -p 8000:8000 smart-gym-bot
```

---

## 🌐 Access the Application

* **Home**: [http://localhost:8000](http://localhost:8000)
* **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  API Endpoints

###  Health Check

```
GET /
```

Response:

```json
{"status": "Smart Gym Bot Running"}
```

---

###  Recommend Least Crowded Hour

```
GET /recommend
```

Response:

```json
{
  "hour": 6,
  "expected_users": 10
}
```

---

### 📅 Book a Gym Slot

```
POST /book?name=Vaishnavi&hour=6
```

Response:

```json
{
  "message": "Slot booked successfully",
  "name": "Vaishnavi",
  "hour": 6
}
```

Console Output:

```
[NOTIFICATION] Gym slot booked for Vaishnavi at 6:00 hrs
```

---

##  Sample Dataset

`gym_usage.csv`

```
hour,users
6,10
7,18
8,45
9,60
10,40
17,55
18,80
19,90
20,70
21,35
```

---

##  Learning Outcomes

* Structuring a **production-ready FastAPI project**
* Avoiding common **Docker + Python import issues**
* Building a **complete ML-backed backend service**
* Using Swagger for API testing
* Git & GitHub workflow understanding

---

<img width="1920" height="1080" alt="Screenshot (1102)" src="https://github.com/user-attachments/assets/241172d4-a57a-49bd-9d0a-24c56097004a" />

<img width="1914" height="1030" alt="Screenshot 2026-02-06 164138" src="https://github.com/user-attachments/assets/02fcd459-c6fe-4789-bb88-e274e23b7b22" />



<img width="1920" height="1080" alt="Screenshot (1104)" src="https://github.com/user-attachments/assets/7f0ead77-db1c-4042-ab89-50adc6b4c23b" />

<img width="1920" height="1080" alt="Screenshot (1105)" src="https://github.com/user-attachments/assets/c8afe9af-f25b-4550-9ace-cc2daca1077f" />


<img width="1920" height="1080" alt="Screenshot (1103)" src="https://github.com/user-attachments/assets/aa25cb9c-4366-4995-bb75-604847f19ea5" />


<img width="1920" height="1080" alt="Screenshot (1106)" src="https://github.com/user-attachments/assets/904ceb5e-79a5-4840-938b-d846ae23098b" />

