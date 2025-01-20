# Buy Now Pay Later - API

This project provides an API to manage users and their purchases, including credit management, using FastAPI. It allows users to register, make purchases, and check outstanding balances. The system supports credit limits and monthly installment purchases.

## Setup
### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/sameerkumar2907/buy-now-pay-later.git
cd buy-now-pay-later
```

### 2. Create a Virtual Environment
Create a virtual environment to manage your dependencies:

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment
On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies
Install the required dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 5. Set the PYTHONPATH
To ensure that the src folder is recognized as the root for imports, set the PYTHONPATH:

```bash
export PYTHONPATH=src
```

### 6. Run the Application
Run the FastAPI application using uvicorn:

```bash
uvicorn src.buy_now_pay_later.main:app --reload
```

Your app should now be available at http://127.0.0.1:8000
