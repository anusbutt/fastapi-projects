
---

# FastAPI Mini Projects

This repository contains a collection of small, real-world **FastAPI** projects, each focusing on different API design concepts and best practices.
They are built for learning, hands-on practice, and portfolio building.

---

## 📂 Projects Overview

### 1. **fastapi\_first**

* **Description:** A simple introductory FastAPI project to understand routing, request handling, and JSON responses.
* **Key Features:**

  * Basic `GET` and `POST` routes
  * Query parameters and path parameters
  * JSON response formatting

---

### 2. **zyphoria\_api**

* **Description:** Backend API for the *Zyphoria* perfume e-commerce concept.
* **Key Features:**

  * Product listing & details
  * Category filtering (Men/Women fragrances)
  * Placeholder data structure for future DB integration

---

### 3. **todo\_list\_api**

* **Description:** A basic task management API to practice CRUD operations.
* **Key Features:**

  * Add, update, delete, and retrieve tasks
  * Task completion status tracking
  * In-memory data storage

---

### 4. **taskflow\_api**

* **Description:** A task delegation and scheduling API inspired by the "TaskMate" concept.
* **Key Features:**

  * Create and assign tasks to team members
  * Set deadlines and priorities
  * Search & filter tasks

---

### 5. **book\_review\_api**

* **Description:** API for managing and retrieving book reviews.
* **Key Features:**

  * Add and view book reviews
  * Store reviewer name, rating, and review text
  * Retrieve reviews by book title

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-mini-projects.git
cd fastapi-mini-projects
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn
```

### 4️⃣ Run Any Project

```bash
cd project_name
uvicorn main:app --reload
```

---

## 🛠 Tech Stack

* **FastAPI** – Modern, fast (high-performance) web framework for building APIs
* **Uvicorn** – ASGI server for running FastAPI apps
* **Python** – Core language for implementation

---

## 📚 Learning Goals

These projects are designed to:

* Practice **API design principles**
* Improve **FastAPI routing & dependency injection** skills
* Prepare for **real-world backend development**
* Strengthen **GitHub portfolio** with practical examples

---

## 📜 License

This repository is open-source and free to use under the MIT License.

---
