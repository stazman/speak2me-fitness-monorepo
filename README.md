# Speak2Me Fitness - Meal Logging Feature Prototype

## Overview

**Speak2Me Fitness** is an innovative AI-powered fitness application designed to enhance the way users track their calorie intake, fitness activities, and overall well-being. The application leverages natural language processing (NLP) to enable users to interact with the app through voice commands, providing a seamless and hands-free experience.

This repository contains the prototype for the **Meal Logging Feature**, which is a core component of the Speak2Me Fitness app. The prototype focuses on allowing users to log their meals via voice commands and receive instant nutritional feedback.

## Tech Stack

- **Backend**: Django with SQLite3
  - **Django**: Web framework used to manage backend logic, including API endpoints and database interactions.
  - **SQLite3**: Lightweight, file-based database used during the prototype phase for simplicity and ease of setup.

- **AI & NLP**: 
  - **Google Cloud Speech-to-Text**: Service used to transcribe voice commands into text.
  - **Hugging Face Transformers**: Pre-trained NLP models used to process and classify text input for food items and nutritional data.

- **Frontend Prototype**: Streamlit
  - **Streamlit**: Used for rapid prototyping of the user interface, allowing users to interact with the meal logging feature in a simple, web-based environment.

## Features

- **Voice-Activated Meal Logging**: Users can log their meals using voice commands, which are processed and transcribed into text.
- **Nutritional Feedback**: The application analyzes the logged meal and provides immediate feedback on the nutritional content, including calories and macronutrients.
- **Data Storage**: Meals are stored in an SQLite3 database during the prototype phase, with plans to migrate to PostgreSQL for production.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)
- **Virtualenv** (optional but recommended)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/speak2me-fitness.git
    cd speak2me-fitness
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Run Streamlit for the Frontend Prototype**:
    ```bash
    streamlit run frontend/app.py
    ```

### Usage

- Access the web application by navigating to `http://127.0.0.1:8000` for the Django backend.
- Access the frontend prototype by navigating to the URL provided by Streamlit after running the command above.
- Use the interface to log meals via voice commands and receive nutritional feedback in real-time.

## Roadmap

- **Phase 1**: Develop and refine the voice-activated meal logging feature.
- **Phase 2**: Integrate habit formation tracking and personalized coaching features.
- **Phase 3**: Migrate from SQLite3 to PostgreSQL for production.
- **Phase 4**: Expand AI capabilities and improve user interaction through continuous learning models.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. Make sure to follow the contribution guidelines and maintainers will review your PR.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

This repository contains an early prototype of the Speak2Me Fitness app, focusing on the meal logging feature. The project is under active development and may not represent the final product.

