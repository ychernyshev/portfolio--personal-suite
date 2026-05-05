[україномовна версія](README.uk-UA.md)

## Table of Contents
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [App List](#app-list)
- [Backend Detailed](#backend-detailed)
- [Frontend Detailed](#frontend-detailed)
- [Apps Detailed](#apps-detailed)
  - [Personal Page](#personal-page)
  - [Solar Power Calculator V1 (Legacy)](#sp-calc-v1)
  - [Solar Power Calculator V2](#sp-calc-v2)
- [Local Launching](#local-launching)
- [Short API reference](#short-api-reference)
- [License](#licence)


# 🚀 Personal Dev Showcase

Welcome to my software projects `monorepository`. This space is designed to demonstrate my skills in `Full-stack development`, with a focus on clean code, architectural flexibility, and automation.

## 📂 [Project Structure](#project-structure)

```
├── backend/                # Django Project (Python 3.12+)
│   ├── calculator/         # Solar app logic and API
│   ├── personal/           # Portfolio API & email service
│   └── settings/           # Security, CORS, CSRF & deployment config
├── frontend/               # Vue 3 Project (Vite + TypeScript)
│   ├── src/
│   │   ├── components/
│   │   │   ├── calculator/ # Dashboard, charts, and table components
│   │   │   └── personal/   # Hero section, Timeline, and contact components
│   │   ├── store/          # Pinia (state management for messages and data)
│   │   └── assets/         # Styles (SASS/CSS), icons, and images
└── README.md               # Global documentation
```

## 🛠 [Tech Stack](#tech-stack)

| Domain               | Technologies                                                 |
|:---------------------|:-------------------------------------------------------------|
| **Backend**          | Python, Django, Django REST Framework, Pandas, NumPy         |
| **Frontend**         | Vue 3 (Composition API), TypeScript, Pinia, Vite, Vue Router |
| **DevOps & Tooling** | Vercel, Render (PaaS), Gunicorn, CORS/CSRF Security, Yarn    |
| **Database**         | PostgreSQL / SQLite                                          |
| **Visualization**    | Chart.js, Vue-chartjs                                        |
| **Styling**          | Bootstrap 5, Bootswatch, SASS, FontAwesome                   |
| **API/Data**         | Open-Meteo API, Axios, Excel/CSV Export/Import               |

## [App List](#app-list)
- Personal Page
- Solar Power Calculator V1 (Legacy)
- Solar Power Calculator V2

## [Backend Detailed](#backend-detailed)
### Main responsibilities
- REST API with DRF for records, weather, monthly stats, import/export.
- Models: DataEntryLineModel, WeatherDataModel, personal pages, calculator.
- Aggregations: sunny days count, average temperature, monthly average power, monthly total power.
- Percentage performance comparison current vs previous month with NaN handling.
- CSV import and Excel export endpoints.

## [Frontend Detailed](#frontend-detailed)
### Main responsibilities
- Responsive dashboard from **320px** upward.
- Components: `MonthStats.vue`, `Dashboard.vue`, `TopNav`, `WeatherIcon`, `RecordsTable`, `AddRecord`, `Settings`, `CodeAndVision`, `Personal pages`, `Calculator` app.
- Charts: power generation, cost savings; drill‑down modal with tables and charts.
- State: Pinia stores (`useNotificationStore`, etc.).
- Routing: modular routes with lazy loading and layout-based rendering..

### Notes
- Env variables must be prefixed with `VITE_` (e.g., `VITE_API_URL`).
- Assets: Bootstrap core, Bootswatch, FontAwesome, custom CSS (`personal.css`, `calculator.css`).
- Axios configured for API calls; calculator/ prefix used for calculator app endpoints.

## [Apps Detailed](#apps-detailed)
### 1. 🏠 [Personal Page](#personal-page)
The central hub of my portfolio.

#### Desktop view
![personal-6-desctop-home.png](docs/pictures/projects/personal_page/personal-6-desctop-home.png)

#### Mobile view
![personal-6-mobile-home.png](docs/pictures/projects/personal_page/personal-6-mobile-home.png)

*   **Purpose:** Presentation of experience, technical stack, and communication tools.
*   **Latest Updates:** 
    *   Implemented an animated `WakeUpLoader` to mitigate the "cold start" effect on free PaaS platforms like Render or Vercel.
    *   The contact form has been moved to a separate `useContactForm` service for better code maintainability.

### 2. [Solar Power Calculator V1 (Legacy)](#sp-calc-v1)
A previous version of the Calculator in the form of a notebook with a simple design and logic

#### Desktop View
![sp_calculator_v1_dashboard.png](docs/pictures/projects/sp_calculator_v1/sp_calculator_v1_dashboard.png)

An analytical platform for monitoring and calculating the efficiency of solar power plants. Based on the initial monolithic iteration of the system, built with a focus on robust backend logic and Server-Side Rendering (SSR).
- **Monolithic Architecture**: Built entirely within the Django ecosystem using Django Templates and Django Forms, with business logic encapsulated in a dedicated service layer (`handle_entry_form.py`).
- **Automated Financial Logic**: Implemented math algorithms for real-time calculation of generated power (Watts) and financial savings, including automated battery discharge compensation and precision rounding (2 decimal places).
- **Integrated Management**: Features a built-in `Add Entry` system with automated validation and a customized Django Admin interface for advanced record management.
- **Server-Side Dashboard**: Desktop-oriented UI using Bootstrap, featuring a tabbed interface for `Chart.js` visualizations (power generation vs. costs) and paginated data tables.
- **Data Integrity**: Specialized handling for missing "afternoon" data points and battery-level logic to ensure accurate accounting of net energy production.

### 3. ☀️ [Solar Power Calculator V2](#sp-calc-v2)
The second iteration of the Calculator APP was developed as a service with a responsive design,  a reactive template, friendlу user UI experience, and extended functionality

#### Desktop View
![4_widget_new.png](docs/pictures/projects/sp_calculator_v2/4_widget_new.png)

#### Mobile View
![4_widget_new_mobile.png](docs/pictures/projects/sp_calculator_v2/4_widget_new_mobile.png)

An analytical platform for monitoring and calculating the efficiency of solar power plants.
*   **Purpose:** Data collection on generation, financial accounting, and performance analytics.
*   **Key Features:**
    *   **Dashboard:** The `MonthStats` widget, which compares current generation with the previous month in real-time using percentages.
    *   Implemented a pinned notification system (`MessagesStack`) with icons for event types: success, info, warning, and error.
    *   **Smart Table:** A record table with intelligent status badges (`NOT TRACKED`, `NO GENERATION`) and context-aware color indication.
    *   **Backend Analytics:** Calculation of sunny days, average temperatures, total power, and generated energy costs on the Django side using model methods.

## 🚀 [Local Launching](#local-launching)
### Backend
```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # або venv\Scripts\activate для Windows
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
```

### Frontend
```bash
    cd frontend
    yarn install
    yarn dev --host 0.0.0.0 --port 5173
```

### [Short API reference](#short-api-reference)
Use a compact table for endpoints and short `curl` examples + a minimal sample response. Put full response examples in code blocks.

#### Solar Power Calculator V2 API:
| Method | Endpoint | Purpose | Notes |
|--|---|---|---|
| GET | api/calculator/entries |   |   |
| GET | api/calculator/weather-conditions |   |   |
| GET | api/calculator/current-tariff/ |   |   |
| GET | api/calculator/stats/ |   |   |
| GET | api/calculator/forecast/ |   |   |
| GET | api/calculator/forecast/details |   |   |
| GET | api/calculator/data-export/ |   |   |
| GET | api/calculatordata-import// |   |   |

### 📜 [License](#licence)
MIT License — free to use, modify, and distribute.