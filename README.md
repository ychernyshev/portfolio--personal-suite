[Україномовна версія](README.uk-UA.md)

# 🚀 Personal Dev Showcase
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.11](https://img.shields.io/badge/Python-v3.11-blue?logo=python)](https://www.python.org/)
[![Django 5.2.7](https://img.shields.io/badge/Django-v5.2.7-darkgreen?logo=django)](https://www.djangoproject.com/)
[![Vue 3](https://img.shields.io/badge/Vue.js-v3.4-brightgreen?logo=vue.js)](https://vuejs.org/)
[![Docker](https://img.shields.io/badge/Docker-v24+-blue?logo=docker)](https://www.docker.com/)
[![Redis](https://img.shields.io/badge/Redis-v7-red?logo=redis)](https://redis.io/)

Welcome to my software projects `monorepository`. This space is designed to demonstrate my skills in `Full-stack development`, with a focus on clean code, production-ready containerization, asynchronous architectures, and automation.

## 🧾 Table of Contents
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [App List](#-app-list)
- [Backend Detailed](#-backend-detailed)
- [Frontend Detailed](#-frontend-detailed)
- [Apps Detailed](#-apps-detailed)
  - [Personal Page](#1--personal-page)
  - [Solar Power Calculator V1 Legacy](#2--solar-power-calculator-v1-legacy) 
  - [Solar Power Calculator V2 Active (v4.6.0)](#3--solar-power-calculator-v2-active-v460)
- [Local Launching](#-local-launching)
- [Docker Support](#-docker-support)
- [Short API reference](#short-api-reference)
- [Current deployment](#-current-deployment)
- [Contact](#-contact)
- [License](#-license)

## 📂 [Project Structure](#-project-structure)
```
├── backend/                # Django Project (Python 3.11+)
│   ├── calculator/         # Solar app logic, mathematical models, and API endpoints
│   ├── personal/           # Portfolio API, routing & WebSockets
│   ├── settings/           # Security, ASGI/WSGI, CORS & DB configurations
│   ├── Dockerfile          # Optimized backend containerization configuration
│   ├── docker-compose.yml  # Local orchestration stack (Daphne + Postgres + Redis)
│   └── requirements.txt    # Python dependencies
├── frontend/               # Vue 3 Project (Vite + TypeScript)
│   ├── src/
│   │   ├── components/
│   │   │   ├── calculator/ # Dashboard cards, multi-type charts, tables, and neomorphic modals
│   │   │   └── personal/   # Hero section, Interactive Timeline, and contact components
│   │   ├── store/          # Pinia (reactive state for cross-component management)
│   │   └── assets/         # Unified styles (CSS), neomorphic toolkit, and icons
└── README.md               # Global documentation
```

## 🛠 [Tech Stack](#-tech-stack)

| Domain | Technologies |
|:---|:---|
| **Backend** | Python 3.11, Django 5.2.7, Django Channels, DRF, Pandas, NumPy |
| **Frontend** | Node 20, Vue 3 (Composition API), Pinia, Vite, Vue Router, TypeScript |
| **Asynchronous Core** | Daphne (ASGI Server), WebSockets, Redis 7 (Channel Layer) |
| **DevOps & Infrastructure**| Docker, Docker Compose, Render (PaaS), Vercel (SaaS) |
| **Database** | PostgreSQL 15 (Production/Docker), SQLite (Local fallback) |
| **Visualization & UI** | Chart.js, Vue-Chart.js, Bootstrap 5, Bootswatch, FontAwesome |
| **API / Integration** | Open-Meteo API, Axios, Excel/CSV Lifecycle |

## 📱 [App List](#-app-list)
- Personal Page (Portfolio Hub)
- [Solar Power Calculator V1 Legacy](https://github.com/ychernyshev/portfolio--personal-suite/blob/v1-legacy/README.md)
- [Solar Power Calculator V2 Active](https://github.com/ychernyshev/portfolio--personal-suite/blob/v2-reborn-in-vue/frontend/README.md)

## ⚙️ [Backend Detailed](#-backend-detailed)
### Main responsibilities
- 🔌 **Unified ASGI Network Gateway:** Driven by `Daphne` and `Django Channels` to concurrently manage standard REST API request/response cycles alongside persistent WebSockets state.
- 📉 **Data Processing & Analytics (Pandas & NumPy):**
  - **Real-Time Aggregations:** Processes month-over-month performance ratios, sunny days calculations, peak trends, and averages with resilient NaN/zero‑fault safety guards.
  - **Empirical Calibration Engine:** Implemented specialized data-science workflows. The system automatically cross-references empirical production inputs against raw Open-Meteo radiation historical metrics to dynamically yield a custom `calibration_factor`.
- 🧮 **Single Source of Truth Calculations:** Refactored the core domain models to treat calculated daily generation in Watts as the absolute single source of truth. Financial computations (`_calculate_full_day_cost`) are dynamically bound to the generated power to guarantee perfect alignment with UAH values, preventing multi-line out-of-sync branching.
- 📊 **Resource & Schema Integration:** Added deep-level indexing and calculations accounting for a dedicated `Extra power` field (including USB loads) directly integrated across structural paths and charge delta balances.

## 🎨 [Frontend Detailed](#-frontend-detailed)
### Main responsibilities
- **Responsive Fluid Layouts:** Optimized for all viewport sizes starting from ultra-compact smartphones (**320px**) up to wide-screen displays.
- **Asynchronous Connectivity:** Seamlessly maintains connections with the backend server via HTTP and WebSockets for dynamic interfaces.
- **Neomorphic UI Toolkit:** Modular implementation with tactile micro-interactions, smooth soft-shadow states, and optimized touch target zones for controls.
- **Real-Time Reactivity:** Fully bound via Vue 3 script setup and Pinia state management. Scorecards, financial totals, and analytical indicators reflect data updates instantly upon mutation without requiring full-page reloads.

## 🚀 [Apps Detailed](#-apps-detailed)

### 1. 🏠 [Personal Page](#1--personal-page)
The centralized core of the portfolio showcase.
* **Purpose:** Production display of professional experience, stack competency, and client communications.
* **Key Mechanisms:** Features a specialized `WakeUpLoader` ensuring seamless platform transitions, asynchronous request pooling, and a dedicated `useContactForm` architecture.

### 2. 🏛️ [Solar Power Calculator V1 Legacy](#2--solar-power-calculator-v1-legacy)
Monolithic historical codebase focusing on Server-Side Rendering (SSR). Encapsulated entirely inside Django Templates with static tabular visual mappings.

### 3. ☀️ [Solar Power Calculator V2 Active (v4.6.0)](#3--solar-power-calculator-v2-active-v460)
The active responsive analytical platform for monitoring, calculating, and forecasting solar energy performance.
* **Dynamic Dual-Line Daily Chart:** Multi-layered `Chart.js` tracking actual user metrics against self-correcting generation forecasts, separated cleanly by an interactive "Today Timeline" boundary.
* **Advanced Monthly Analytics:** Introduced a modular `DifferenceMonthsChart.vue` component. It renders an elegant bar chart that visualizes and groups long-term generation vs. financial cost parameters side-by-side inside an asynchronous tooltip card.
* **Predictive Weather Calibration:** Auto-fetches 16-day forward metrics via Open-Meteo, scaling weather datasets against mathematical models calibrated to physical shading characteristics.
* **Bulletproof Integrity:** Native protection mechanisms handling edge cases like 31-day shifting layout anomalies or database-absence crashes.

## 🐳 [Docker Support](#-docker-support)

The backend infrastructure is fully containerized for local development, providing an environment identical to production.

Inside the `backend/` directory, the multi-container environment includes:
* **`backend`**: Custom Python 3.11 environment running the Daphne ASGI server.
* **`db`**: PostgreSQL 15 relational storage database.
* **`redis`**: Redis 7 serving as both the caching mechanism and message broker for Django Channels.

Data persistence is guaranteed via isolated named Docker volumes (`postgres_data`), ensuring records remain intact across infrastructure restarts.

---

## 💻 [Local Launching](#-local-launching)

### Option A: Complete Automated Stack (Recommended)
Ensure you have Docker and Docker Compose installed. Navigate to the backend folder and boot all services simultaneously:

```bash
cd backend
docker-compose up --build -d

# Apply DB tables structure & migrations inside the live container
docker-compose exec backend python manage.py migrate
```
> The backend API and WebSocket endpoints will become available at http://localhost:8001/.

### Option B: Manual Bare-Metal Installation
### 1. Backend Service
```
cd backend
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
daphne -b 0.0.0.0 -p 8001 settings.asgi:application
```

### 2. Frontend Application
```
cd frontend
npm install  # or yarn install
npm run dev  # or yarn dev
```

## 📡 Short API Reference
| Method | Endpoint | Purpose | Configuration Type |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/calculator/entries/` | Paginated records retrieval | REST API |
| `GET` | `/api/calculator/current_month_stats/` | Daily logs, summaries & current month performance | REST API |
| `GET` | `/api/calculator/difference_months_stats/` | Long-term historical data grouped by month for bar charts | REST API |
| `GET` | `/api/calculator/forecast/` | 16-Day forward empirical production metrics | REST API / Open-Meteo |
| `POST` | `/api/calculator/data-import/` | Bulk file lifecycle data intake | CSV Multipart Stream |
| `WS` | `/ws/personal/...` | Real-time bi-directional message streams | WebSocket Protocol |

## 🌐 Current Deployment
- Frontend Application Infrastructure: Hosted via Vercel pipeline directly connected to repository triggers.
- Backend Application Infrastructure: Scaled on Render hosting environments, utilizing persistent attached PostgreSQL database storage.
- Live Address: ychernyshev.vercel.app

## 📫 Contact
Feel free to reach out via the secure asynchronous contact channel on my Personal Portfolio Page or connect professionally via LinkedIn.

## 📜 License
Distributed under the AGPLv3 License to ensure the core platform remains open-source and free from cloud vendor-lock. Check the [LICENSE](LICENSE) file for additional terms.