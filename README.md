# scheduleAutoOOP# 
Schedule Automator

A Python-based workforce scheduling application that automatically assigns tasks to available workers while balancing workloads and supporting task rotation.

Built using object-oriented programming (somewhat lol), Streamlit, SQLite, and Docker.

## Features

- **Worker Management:** Add, edit, and delete workers and their weekly availability.
- **Task Management:** Create tasks with durations and optional rotation.
- **Automatic Scheduling:** Generate a seven-day schedule based on worker availability.
- **Workload Balancing:** Assign tasks to workers with the lowest assigned workload for the day.
- **Task Rotation:** Avoid assigning rotating tasks to the same worker on consecutive assignments when alternatives are available.
- **SQLite Persistence:** Save workers and tasks between application sessions.
- **Weather Integration:** Retrieve current temperature using the Open-Meteo API.
- **CSV Export:** Export generated schedules.
- **Docker Support:** Run the application locally in a container with persistent database storage.
- **Automated Testing:** Verify scheduling behavior using pytest.

## Technologies

- Python 3.12
- Streamlit
- SQLite
- Docker and Docker Compose
- Requests
- Open-Meteo API
- Pytest
- Git and GitHub

## Getting Started

### Prerequisites

Install Docker Desktop and make sure the Docker engine is running.

### Installation

Clone the repository:

```bash
git clone https://github.com/sea-breeeze/scheduleAutoOOP.git
cd scheduleAutoOOP
```

Build and start the application:

```bash
docker compose up --build
```

Open your browser:

http://localhost:8501

### Stopping the Application

```bash
docker compose down
```

Docker Compose preserves the SQLite database using a named volume. Avoid `docker compose down -v` unless you intend to remove the stored data.

## How the Scheduling Algorithm Works

1. Determine which workers are available for each day.
2. Sort tasks by duration, from longest to shortest.
3. Track the number of minutes assigned to each worker.
4. Assign each task to the eligible worker with the lowest workload.
5. For rotating tasks, avoid the worker who most recently performed that task when another available worker exists.
6. Repeat the process for all seven days.

The scheduler uses a greedy workload-balancing approach. It does not guarantee globally optimal assignments or assign specific clock-time slots.

## Running Automated Tests

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the scheduling tests:

```bash
python -m pytest tests/test_scheduler.py -v
```

## Project Structure

```text
scheduleAutoOOP/
├── Canvas.py
├── worker.py
├── task.py
├── scheduler.py
├── database.py
├── weather.py
├── tests/
│   └── test_scheduler.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

## Future Improvements

- Optional REST API using FastAPI


## Author

Juan Martinez

GitHub: https://github.com/sea-breeeze