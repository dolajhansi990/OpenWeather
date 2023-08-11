# Open Weather Project

The **Open Weather** project is a versatile application that provides weather information for a given location, offering both current weather conditions and a 5-day forecast. Additionally, the project includes an integrated chatbot powered by the OpenAI API. The application leverages the OpenWeatherMap API for weather data and utilizes a machine learning model to predict temperature variations throughout the day.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Obtaining API Keys](#obtaining-api-keys)
  - [Setting up OpenAI API](#setting-up-openai-api)
  - [Running the Application](#running-the-application)
- [Machine Learning Model](#machine-learning-model)
- [UI Framework](#ui-framework)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Open Weather project combines weather information and AI-driven chat capabilities. It utilizes the OpenWeatherMap API to provide accurate weather forecasts for up to 5 days and employs a machine learning model to predict hourly temperature variations. The integrated chatbot, powered by the OpenAI API, enables users to interact and inquire about weather conditions.

## Features

- Current weather information for a specified location
- 5-day weather forecast for the given location
- Integrated chatbot powered by OpenAI API
- Machine learning model for predicting hourly temperature variations

## Requirements

- Python 3.9
- Required libraries:
  - PyQt5
  - scikit-learn
  - TensorFlow
  - matplotlib
  - plotly
  - datetime
  - pandas
  - numpy
- Qt Designer for UI framework creation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/open-weather.git
   cd open-weather
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Obtaining API Keys

1. Visit the [OpenWeatherMap API](https://openweathermap.org/api) website and create an account.
2. Once logged in, generate an API key.

### Setting up OpenAI API

1. Create an account on the [OpenAI platform](https://beta.openai.com/signup/).
2. Obtain your OpenAI API key.

### Running the Application

1. Open the `config.py` file and replace `YOUR_OPENWEATHER_API_KEY` with your actual OpenWeatherMap API key, and replace `YOUR_OPENAI_API_KEY` with your OpenAI API key.

2. Launch the application:

   ```bash
   python main.py
   ```

3. The application GUI will appear, allowing you to input the desired location and interact with the chatbot.

## Machine Learning Model

The machine learning model included in this project predicts the temperature variations for each hour of the day. It is trained using historical weather data and utilizes scikit-learn and TensorFlow libraries for model development and training. The trained model is integrated into the application to provide accurate hourly temperature predictions.

## UI Framework

The UI for the Open Weather application is designed using the PyQt5 library. The Qt Designer tool can be used to create and modify the user interface layout. The designed `.ui` files are then converted into Python code using the `pyuic5` utility, which can be included in the project seamlessly.

## Contributing

Contributions to the Open Weather project are welcomed and encouraged. If you find any issues or have suggestions for improvements, please feel free to create a pull request or open an issue on the project's GitHub repository.



Feel free to modify this `README.md` template to fit your project's specific details and requirements. Good luck with your Open Weather project!
