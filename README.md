# AUTOCOMP Python Version

## Overview
AUTOCOMP Python Version is the Python implementation of the automated competitive analysis tool, offering similar functionality to the JavaScript version but with Python's data science capabilities.

## Features
- Competitor data collection and analysis
- Machine learning-based market predictions
- Advanced data visualization
- Automated reporting
- Integration with Python data science libraries

## How It Works
The application leverages Python's ecosystem for data analysis, including libraries like Pandas, NumPy, Scikit-learn, and Matplotlib. It uses web scraping tools like BeautifulSoup and Scrapy to collect data, and Flask or FastAPI for the backend API.

## Code Structure
- `app/`: Main application directory
  - `scrapers/`: Web scraping modules
  - `analysis/`: Data analysis and machine learning models
  - `api/`: API endpoints
  - `models/`: Data models
  - `utils/`: Utility functions
- `frontend/`: Frontend application (may use a JavaScript framework)
- `notebooks/`: Jupyter notebooks for data exploration

## How to Run the Application
1. Clone the repository:
```bash
git clone https://github.com/AWERDdev/AUTOCOMP_PYVersion.git
```

2. Navigate to the project directory:
```bash
cd AUTOCOMP_PYVersion
```

3. Create and activate a virtual environment:
```bash
python -m venv venv
```

4. On Windows:
```bash
venv\Scripts\activate
```

5. On macOS/Linux:
```bash
source venv/bin/activate
```

6. Install dependencies:
```bash
pip install -r requirements.txt
```

7. Start the backend server:
```bash
python run.py
```

8. If there's a separate frontend, navigate to its directory and install dependencies:
```bash
cd frontend
npm install
```

9. Start the frontend development server:
```bash
npm run dev