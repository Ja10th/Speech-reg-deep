
# Speech Emotion Recognition System: Local Installation Guide

Welcome to the Speech Emotion Recognition System local installation guide. This guide will walk you through the steps required to set up the Speech Emotion Recognition System on your local PC. The system uses Deep Learning techniques to recognize emotions from audio recordings. Follow these steps to install and run the system locally:

## System Requirements:

	•	Python 3.6 or higher
	•	pip package manager
	•	Git (optional, for cloning the repository)

## Installation Steps:

### 1. Clone the Repository:
If you have Git installed, you can clone the repository using the following command:

git clone https://github.com/Ja10th/Speech-reg-deep

Alternatively, you can download the repository as a ZIP file and extract it to your desired location.

### 2. Set Up Virtual Environment (Optional but Recommended):
Navigate to the project directory and create a virtual environment:

cd speech-emotion-recognition

python3 -m venv venv

Activate the virtual environment:

	•	On Windows: venv\Scripts\activate
	•	On macOS and Linux: source venv/bin/activate
 
### 3. Install Dependencies:Install the required Python packages using pip:

pip install -r requirements.txt


### 4. Run the Application:
Start the Flask development server using the following command:

flask run

The application will be accessible at http://localhost:5000.

### 5. Access the Application:
Open a web browser and navigate to http://localhost:5000 to access the Speech Emotion Recognition System. You can upload audio files for analysis and receive predicted emotion labels.
