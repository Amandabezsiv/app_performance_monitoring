# 📊 Application Performance Monitoring System

The **Performance Monitoring App** is a system designed to track, monitor, and visualize key performance metrics of an application, such as response time, latency, CPU usage, memory usage, active sessions, and page load time. The application includes an alerting system managed exclusively through the **Django admin panel**, allowing for manual review of alerts when metrics exceed predefined thresholds. It also supports generating reports with graphical data representations.

## Features

- **Performance Metrics Monitoring**: Track various performance metrics such as CPU usage, memory usage, response time, and latency.
- **Access Logs**: Record and visualize the last 10 accesses to the application, including timestamps and URLs.
- **Report Generation**: Generate reports with graphs visualizing key performance metrics and access logs.
- **Alert System**: Send alerts based on monitored metrics.

## Stack

- **Backend**: Django (Python)
- **Database**: MongoDB
- **Frontend**: HTML, CSS
- **Visualization**: Matplotlib for generating graphs

## Setup

### Prerequisites

- Python 3.x
- MongoDB
- Django

### 🚀 How to Run the Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-repo/application-monitoring-platform.git
    cd application-monitoring-platform
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up MongoDB and configure it in `settings.py`:**

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'your_database_name',
        }
    }
    ```

5. **Apply migrations and run the server:**

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

---

### 📩 Alerts

The alert system is currently configured to send alerts only through the Django admin interface, but can be extended to send emails or integrate with Slack. You can configure the alert system by adding additional methods in the alert views.

---

### 📊 Usage

- **Monitoring Metrics:** Performance metrics are automatically tracked and can be visualized in the reports section.
- **Generating Reports:** Go to the reports section to generate performance reports, which include CPU usage graphs and access logs.
- **Alerts:** Set up alert thresholds in the Django admin panel for key metrics.

---

### 🌟 Future Improvements

- Integrate email notifications for alerts.
- Add support for Slack notifications.
- Extend the visualization to include more metrics, such as disk I/O and network traffic.
