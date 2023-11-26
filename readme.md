# Notes CRUD + summary using Langchain Project

## Description

This project is based on the Notes Model and has a CRUD built on top of it, Also, for summarizing the content of notes we are utilizing Langchain

## Setup and Installation

### Prerequisites

- Python 3.x
- pip
- Virtual environment (recommended)

### Installation Steps

1. **Clone the Repository:**

2. **Create and Activate a Virtual Environment (optional but recommended):**

3. **Install Required Packages:**


4. **Set Environment Variables:**
- Set `OPENAI_API_KEY` in your environment. You can do this by adding it to your virtual environment's `activate` script or using an environment variable management tool like `dotenv`.

5. **Database Setup:**
- Run migrations to set up the database:
  ```
  python manage.py migrate
  ```

6. **Run the Server:**


## API Endpoints

This project provides the following API endpoints:

1. **List Notes:**
- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Returns a list of all notes.

2. **Note Detail:**
- **Endpoint:** `/<int:pk>/`
- **Method:** `GET`
- **Description:** Returns details of a specific note by ID.

3. **Summarize Text:**
- **Endpoint:** `/summarize/<int:notes_id>/`
- **Method:** `GET`
- **Description:** Returns a summarized version of the note content for the given ID.

### Example Usage

- To list notes, make a `GET` request to `http://localhost:8000/`.
- To view details of a note, make a `GET` request to `http://localhost:8000/1/`, where `1` is the note ID.
- To get a summarized text of a note, make a `GET` request to `http://localhost:8000/summarize/1/`.

### Langchain Issues Faced
For langchain, I did not faced any issue and it worked smoothly. Although, there were some errors when passing the text directly in chain.run() but then after some RnD I found a solution on Github Pages and implemented that, afterwards the solution for summarizing worked fine.