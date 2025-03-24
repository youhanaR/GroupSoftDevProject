# Napoleon's Adventure

## Installation
Before running the project, install the required dependencies using the requirements.txt file.

## Using a Virtual Environment (Recommended)
To keep the project environment isolated, follow these steps
1. Create a virtual environment
```
python -m venv venv  
```
2. Activate the Virtual Environment
   - On macOS/Linux
   ```
   source venv/bin/activate
   ```
   - On Windows
   ```
   venv\Scripts\activate
   ```
## Install dependencies
   ```
   pip install -r technical-documents/requirements.txt
   ```

### What is requirements.txt?
The requirements.txt file contains a list of all dependencies needed to run the project. Installing these ensures that all required Python packages are set up correctly.

## Running the Project
After setting up the virtual environment and installing dependencies, navigate to the project root directory (technical-documents) and run:
```
python manage.py runserver
```
The server will now be running at http://127.0.0.1:8000/.

## Environment Variables
Make sure you have your .env file set up, containing the automated email account credentials in the following format:
- User_Email = user_email  
- User_Password = user_password

