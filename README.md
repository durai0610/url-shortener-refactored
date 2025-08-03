1. 🧾 Project Title & Summary
# URL Shortener API

A simple Flask-based API that generates short codes for long URLs, tracks clicks, and provides analytics like bit.ly or tinyurl.

---

2. 🚀 Getting Started / Setup Instructions
## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.8+
- pip

### 📦 Installation
# Navigate to the project directory
```bash
cd url-shortener
```

# Install dependencies
```bash
pip install -r requirements.txt
```
🧪 Run the Application
python -m flask --app app.main run

The API will be available at:
👉 http://localhost:5000

---

### 3. 🔗 **API Endpoints**
## 🔗 API Endpoints

| Method | Endpoint                  | Description                   |
|--------|---------------------------|-------------------------------|
| POST   | `/api/shorten`            | Shortens a long URL           |
| GET    | `/<short_code>`           | Redirects to original URL     |
| GET    | `/api/stats/<short_code>` | Returns analytics info        |
| GET    | `/api/health`             | Health check for API          |
| GET    | `/`                       | Service health info           |

---

4. 🧪 Testing
## 🧪 Run Tests
- pytest

- The test suite includes:

- URL shortening

- Redirection

- Invalid URL handling

- Missing data handling

- Analytics check

---

### 5. 🛠️ **Project Structure**
## 🧱 Project Structure

```text
url-shortener/
├── app/
│   ├── main.py        # Main Flask app (routes & logic)
│   ├── utils.py       # URL validator & short code generator
│   └── models.py      # In-memory URL store
├── tests/
│   └── test_basic.py  # Pytest unit tests for core features
├── requirements.txt   # Project dependencies
├── README.md          # Project documentation
└── CHANGES.md         # AI usage notes & implementation summary
```
---

6. 🤖 AI Usage Declaration
## 🤖 AI Usage Declaration

- ChatGPT was used to clarify Flask, routing, thread safety, and test structuring.
- All code was manually reviewed and tested.
- No AI-generated code was copy-pasted blindly.

---

## ✅ Sample Curl Request

curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com"}'

Response:
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
