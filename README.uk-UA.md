See the English version of the readme [here.](README.md)

# 🚀 Personal Dev Showcase
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/Python-v3.12-blue?logo=python)](https://www.python.org/)
[![Django 5.2.7](https://img.shields.io/badge/Django-v5.2.7-darkgreen?logo=django)](https://www.djangoproject.com/)
[![Node.js 18](https://img.shields.io/badge/Node.js-v18-green?logo=node.js)](https://nodejs.org/)
[![Vue 3](https://img.shields.io/badge/Vue.js-v3.4-brightgreen?logo=vue.js)](https://vuejs.org/)

[//]: # ([![Build]&#40;https://github.com/ychernyshev/portfolio--personal-suite/actions/workflows/ci.yml/badge.svg&#41;]&#40;https://github.com/ychernyshev/portfolio--personal-suite/actions/workflows/ci.yml&#41;)


Ласкаво просимо до мого `monorepository` програмних проєктів. Цей простір створений для демонстрації моїх навичок у `Full-stack` розробці з акцентом на чистий код, архітектурну гнучкість та автоматизацію.

## 🧾 Зміст
- [Структура проєкту](#-структура-проєкту)
- [Стек технологій](#-стек-технологій)
- [Список додатків](#-список-додатків)
- [Деталі Backend](#-деталі-backend)
- [Деталі Frontend](#-деталі-frontend)
- [Опис додатків](#-опис-додатків)
  - [Персональна сторінка](#1--персональна-сторінка)
  - [Solar Power Calculator V1 Legacy](#2--solar-power-calculator-v1-legacy) 
  - [Solar Power Calculator V2 Active](#3--solar-power-calculator-v2-active)
- [Локальний запуск](#-локальний-запуск)
- [Короткий довідник API](#короткий-довідник-api)
  - [Solar Power Calculator V2 API](#-solar-power-calculator-v2-api)
    - [Приклади запитів](#приклади-запитів)
- [Підтримка Docker](#-підтримка-docker)
- [Поточне розгортання](#-поточне-розгортання)
- [Контакти](#-контакти)
- [Ліцензія](#-ліцензія)

## 📂 [Структура проєкту](#-структура-проєкту)

```
├── backend/                # Проєкт Django (Python 3.12+)
│   ├── calculator/         # Логіка сонячного калькулятора та API
│   ├── personal/           # API портфоліо та сервіс електронної пошти
│   └── settings/           # Налаштування безпеки, CORS, CSRF та деплою
├── frontend/               # Проєкт Vue 3 (Vite + TypeScript)
│   ├── src/
│   │   ├── components/
│   │   │   ├── calculator/ # Компоненти дашборду, графіків та таблиць
│   │   │   └── personal/   # Hero-секція, Timeline та компоненти контактів
│   │   ├── store/          # Pinia (управління станом повідомлень та даних)
│   │   └── assets/         # Стилі (CSS), іконки та зображення
└── README.md               # Глобальна документація
```

## 🛠 [Стек технологій](#-стек-технологій)

| Domain                | Technologies                                                       |
|:----------------------|:---------------------------------------------------------------------|
| **Backend**           | Python 3.12, Django 5.2.7, Django REST Framework, Pandas, NumPy    |
| **Frontend**          | Node 20, Vue 3 (Composition API), TypeScript, Pinia, Vite, Vue Router |
| **DevOps & Tooling**  | Vercel, Render (PaaS), Gunicorn, CORS/CSRF Security, Yarn          |
| **База даних**        | PostgreSQL / SQLite                                                |
| **Візуалізація**      | Chart.js                                                           |
| **Стилізація**        | Bootstrap 5, Bootswatch, FontAwesome                               |
| **API/Дані**          | Open-Meteo API, Axios, Excel/CSV Export/Import                     |

## 📱 [Список додатків](#-список-додатків)
- Персональна сторінка (Personal Page)
- [Solar Power Calculator V1 Legacy](https://github.com/ychernyshev/portfolio--personal-suite/blob/v1-legacy/README.md)
- Solar Power Calculator V2 Active

## ⚙️ [Деталі Backend](#-деталі-backend)
### Основні обов'язки
- 🔌 **REST API**: Побудовано на DRF, підтримує повний цикл CRUD для записів генерації.
- 📈 **Обробка даних та агрегація** 
  - **Агрегації в реальному часі**:
    - Підрахунок сонячних днів, середньої температури, середньомісячної та загальної потужності, порівняння продуктивності з попереднім місяцем у відсотках (з обробкою NaN) тощо.
  - **Заплановано**: 
    - Глибша інтеграція Pandas та NumPy.
- 📑 **Звітність**: Ендпоінти для автоматизованого життєвого циклу даних `CSV/Excel`.

## 🎨 [Деталі Frontend](#-деталі-frontend)
### Основні обов'язки
- Адаптивний дашборд від **320px** і вище.
- Компоненти: `MonthStats.vue`, `Dashboard.vue`, `TopNav`, `WeatherIcon`, `RecordsTable`, `AddRecord`, `Settings`, `CodeAndVision`, Персональні сторінки, додаток `Calculator`.
- Графіки: генерація енергії, фінансова економія; модальні вікна з детальними таблицями та чартами.
- Стан: сховища Pinia (`useNotificationStore` тощо).
- Роутинг: модульні маршрути з лінивим завантаженням (lazy loading) та рендерингом на основі лейаутів.

### Примітки
- Змінні оточення повинні мати префікс `VITE_` (наприклад, `VITE_API_URL`).
- Асети: Bootstrap core, Bootswatch, FontAwesome, кастомні CSS (`personal.css`, `calculator.css`).
- `Axios` налаштований для API-запитів; для ендпоінтів калькулятора використовується префікс `calculator/`.

## 🚀 [Опис додатків](#-опис-додатків)
### 1. 🏠 [Персональна сторінка](#1--персональна-сторінка)
Центральний хаб мого портфоліо.

#### Десктопний вигляд
![personal-6-desctop-home.png](docs/pictures/screenshots/personal_page/personal-6-desctop-home.png)

#### Мобільний вигляд
![personal-6-mobile-home.png](docs/pictures/screenshots/personal_page/personal-6-mobile-home.png)

*   **Мета:** Презентація досвіду, технологічного стека та інструментів зв'язку.
*   **Останні оновлення:** 
    *   Реалізовано анімований `WakeUpLoader` для пом'якшення ефекту "холодного старту" на безкоштовних PaaS-платформах, таких як `Render` або `Vercel`.
    *   Контактну форму винесено в окремий сервіс `useContactForm` для кращої підтримки коду.

### 2. 🏛️ [Solar Power Calculator V1 Legacy](#2--solar-power-calculator-v1-legacy)
Попередня версія калькулятора у форматі "блокнота" з простим дизайном та логікою.

#### Десктопний вигляд
![sp_calculator_v1_dashboard.png](docs/pictures/screenshots/sp_calculator_v1/sp_calculator_v1_dashboard.png)

Аналітична платформа для моніторингу та розрахунку ефективності сонячних електростанцій. Базується на початковій монолітній ітерації системи, побудованій з фокусом на надійну логіку бекенда та `Server-Side Rendering (SSR)`.
- **Монолітна архітектура**: Побудована повністю в екосистемі Django з використанням `Django Templates` та `Django Forms`.
- **Автоматизована фінансова логіка**: Математичні алгоритми для розрахунку згенерованої потужності (Вт) та економії в реальному часі, включаючи компенсацію розряду батареї.
- **Серверний дашборд**: Орієнтований на десктоп інтерфейс на Bootstrap з використанням `Chart.js` для візуалізації генерації та витрат.

### 3. ☀️ [Solar Power Calculator V2 Active](#3--solar-power-calculator-v2-active)
Друга ітерація додатка, розроблена як сервіс з адаптивним дизайном, реактивним шаблоном та розширеним функціоналом.

#### Десктопний вигляд
![4_widget_new.png](docs/pictures/screenshots/sp_calculator_v2/4_widget_new.png)

#### Мобільний вигляд
![4_widget_new_mobile.png](docs/pictures/screenshots/sp_calculator_v2/4_widget_new_mobile.png)

*   **Мета:** Збір даних про генерацію, фінансовий облік та аналітика продуктивності.
*   **Ключові особливості:**
*   **Дашборд:** Віджет `MonthStats`, який порівнює поточну генерацію з попереднім місяцем у реальному часі у відсотках.
*   Реалізовано систему закріплених повідомлень (`MessagesStack`) з іконками для різних типів подій.
*   **Розумна таблиця:** Таблиця записів з інтелектуальними статусами (`NOT TRACKED`, `NO GENERATION`) та колірною індикацією залежно від контексту.
*   **Бекенд-аналітика:** Розрахунок сонячних днів, середніх температур та вартості енергії на стороні Django за допомогою методів моделей.


## 💻 [Локальний запуск](#-локальний-запуск)
### Backend
```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate for Windows
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

## [Короткий довідник API](#короткий-довідник-api)
Стисла таблиця ендпоінтів та приклади curl.

## 📡 [Solar Power Calculator V2 API](#-solar-power-calculator-v2-api)

| Method | Endpoint | Purpose | Notes                                                                                                            |
|--------|----------|--------|------------------------------------------------------------------------------------------------------------------|
| GET    | /api/calculator/entries/ | Список усіх записів | Підтримує пагінацію                                                                                              |
| GET    | /api/calculator/weather-conditions/ | Дані про погоду | Кешований погодинний прогноз                                                                                           |
| GET    | /api/calculator/current-tariff/ | Поточний тариф | Повертає ціну за кВт·год та встановлює нову                                                                           |
| GET    | /api/calculator/stats/ | Статистика за місяць| К-сть сонячних днів, сер. темп., сер. потужність, економія, порівняння з минулим місяцем |
| GET    | /api/calculator/forecast/ | Денний прогноз | кВт·год, економія, пікова година                                                                                          |
| GET    | /api/calculator/forecast/details/ | Погодинний прогноз | Температура, стан неба                                                                                       |
| GET    | /api/calculator/data-export/ | Експорт записів | Завантаження файлу Excel                                                                                                   |
| POST   | /api/calculator/data-import/ | Імпорт записів | Завантаження файлу CSV                                                                                                       |

#### [Приклади запитів](#приклади-запитів)
```bash
# Get current monthly stats
curl -s https://api.example.com/api/calculator/stats/

# Import CSV
curl -X POST https://api.example.com/api/calculator/data-import/ \
  -F "file=@records.csv"
```

## 🐳 [Підтримка Docker](#-підтримка-docker)
#### Заплановані можливості
- `docker-compose up` запуск backend (Gunicorn) + frontend (Nginx) + PostgreSQL.
- Redis + Celery (заплановано для додатка Post Flow Controlling App)


## 🌐 [Поточне розгортання](#-поточне-розгортання)
 -**Frontend**: 'Vercel' (авто-деплой з репозиторію)
- **Backend**: 'Render' ('Gunicorn' + 'PostgreSQL', авто-деплой з репозиторію)
- **Домен**: 'ychernyshev.vercel.app'

## 📫 [Контакти](#-контакти)
Ви можете зв'язатися зі мною через контактну форму на моїй [Персональній сторінці](https://ychernyshev.vercel.app/) або через [LinkedIn](https://www.linkedin.com/in/ychernyshev/).

## 📜 [Ліцензія](#-ліцензія)
[MIT License](LICENSE) — вільно для використання, модифікації та розповсюдження.