# Machine Learning-Based Solar Panel Performance Monitoring and Anomaly Detection

This project leverages IoT sensors and machine learning to monitor the performance of solar panels in real-time. It collects data on voltage, current, and temperature, and uses machine learning to predict performance and detect anomalies. The goal is to provide actionable insights for optimizing solar energy systems and enabling proactive maintenance.

## Features

- **Real-time data collection** from solar panels using a Raspberry Pi.
- **Monitoring of key parameters**: voltage, current, and temperature.
- **Machine learning-based anomaly detection** for identifying faults or inefficiencies.
- **Performance prediction** using regression models.
- **Visualization of data trends** and system efficiency.

## Components Required

- **Raspberry Pi** (any model with GPIO support).
- **Two solar panels or cells** (small-scale, e.g., 5W or 10W).
- **Voltage sensor** (e.g., INA219 or voltage divider).
- **Current sensor** (e.g., INA219 or ACS712).
- **Temperature sensor** (e.g., DHT11 or DHT22).
- **Wires and breadboard** (for circuit connections).
- **SD card** (16GB or more) with Raspberry Pi OS installed.
- **Power supply** (USB-C or micro-USB power adapter).

## Run the Code in Google Colab

All data processing and machine learning tasks are performed using Google Colab. Follow the steps below to set up and execute the scripts.

#### Prerequisites

- A Google account to access Google Colab.
- Ensure your Raspberry Pi is collecting and saving data to `solar_panel_data.csv`.

#### Steps

1. **Upload Data to Google Drive**

    - After collecting data with your Raspberry Pi, upload the `solar_data.csv` file to your Google Drive for access in Colab.

2. **Open Google Colab**

    - Navigate to [Google Colab](https://colab.research.google.com/) and create a new notebook.

3. **Mount Google Drive**

    In the first cell of your Colab notebook, mount your Google Drive to access the uploaded data:

    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```

4. **Set Working Directory**

    ```python
    import os
    os.chdir('/content/drive/My Drive/solar-panel-monitoring/')
    ```

5. **Upload Python Scripts**

    Ensure the following Python scripts are uploaded to your Google Drive in the `solar-panel-monitoring` directory:

    - `anomaly.py`
    - `performance_prediction.py`
    - `visual.py`

6. **Run the Scripts Procedurally**

    Execute each script sequentially within the Colab notebook.

    #### a. Anomaly Detection

    ```python
    %run anomaly.py
    ```

    **Description**: This script loads the `solar_data.csv`, applies the Isolation Forest model to detect anomalies, and saves the results.

    #### b. Performance Prediction

    ```python
    %run performance_prediction.py
    ```

    **Description**: This script uses Random Forest Regression to predict solar panel performance based on the collected data and saves the prediction results.

    #### c. Data Visualization

    ```python
    %run visual.py
    ```

    **Description**: This script generates visualizations of the data trends, efficiency metrics, and detected anomalies.

7. **Review Outputs**

    - **Anomaly Detection**: Check for any flagged anomalies indicating potential faults or inefficiencies.
    - **Performance Prediction**: Review predicted performance metrics to assess system efficiency.
    - **Visualizations**: Analyze the generated plots to gain insights into the solar panel performance under various conditions.
