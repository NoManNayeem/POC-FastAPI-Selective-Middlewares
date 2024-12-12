
# POC: FastAPI Selective Middlewares

This project demonstrates how to implement selective middlewares in a FastAPI application. Specific routes and methods bypass middleware processing, while others are processed as usual.

## Project Structure

```
SelectiveMiddlewareAPI_FastAPI/
├── venv/                # Python virtual environment directory
├── __pycache__/         # Compiled Python files (auto-generated)
├── .gitignore           # Git ignore file
├── app.py               # FastAPI application with selective middleware logic
├── requirements.txt     # Python dependencies
├── test_app.py          # Test cases for the application
```

## Features
- Bypass middleware for specific routes and HTTP methods.
- Middleware logic for logging or processing all other requests.
- Fully tested with comprehensive test cases.

## Repository
GitHub: [POC-FastAPI-Selective-Middlewares](https://github.com/NoManNayeem/POC-FastAPI-Selective-Middlewares)

---

## Getting Started

Follow the instructions below to set up and run the project on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/NoManNayeem/POC-FastAPI-Selective-Middlewares.git
cd POC-FastAPI-Selective-Middlewares
```

### 2. Set Up Virtual Environment
Create and activate a Python virtual environment:
```bash
python -m venv venv
# For Windows Command Prompt
venv\Scripts\activate
# For Windows PowerShell
.\venv\Scripts\Activate
```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Run the Development Server
Start the FastAPI development server:
```bash
uvicorn app:app --reload
```
The server will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 5. Run Test Cases
Execute the test cases to ensure everything works as expected:
```bash
python test_app.py
```

You should see the output indicating that all tests have passed.

---

## Example Usage
### Routes
1. **GET** `/without-middleware`: Bypasses middleware.
2. **POST** `/without-middleware`: Bypasses middleware.
3. **GET** `/with-middleware`: Processes through middleware.
4. **POST** `/with-middleware`: Processes through middleware.

### Middleware Behavior
- Logs processing for routes not in the exclusion list.
- Skips logging for excluded routes and methods.

---

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or suggestions.

## License
This project is licensed under the MIT License.
