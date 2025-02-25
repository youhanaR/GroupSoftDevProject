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

## Running the Minigames
At the moment, the minigames are not connected to the webapp as they have been developed using pygames. However, these 2 minigames are fully functional and can acccessed by:
1. Navigating to technical-documents/media
2. There will be 2 minigames, each in a zip file: 'CatchTheRubbish.zip' and 'SortTheRecycling.zip'.
3. Unzip the files.
4. For Catch the Rubbish minigame, run CatchTheRubbish.py in your IDE.
5. For Sort The Recycling. run Match3.py in your IDE.

