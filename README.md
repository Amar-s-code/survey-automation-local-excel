# Survey Automation
Survey Automation using Qualtrics API you can use either a local excel sheet or google sheets by passing a flag while running main.py. 

# Requirements

## Download/Clone repository
Would prefer you clone the repository, in case there are any changes in the code. 

`git clone https://github.com/Amar-s-code/survey-automation-local-excel.git`

## Create Virtual Environment and install dependencies
* Inside repository create environment (e.g. `python -m venv env`)
* Activate environment (e.g. `source env/bin/activate`)
* Install dependencies (e.g. `pip install -r requirements.txt`) Note: Only need to do this step once.
* If you are having issues installing openpyxl the source folder is also present '/openpyxl-3.0.2' in the cloned repository

## Images
* Place all the image folders which contain the files inside them, inside a folder called 'Images' and place it in the cloned repo.
* Run `python image_resize.py height(default = 400) width (default = 340)` (will resize all images to corresponding height and width)

# If you are running with google sheets:
## Creating the appropriate credentials 
* Go to Google Cloud Platform and create project through the Console.
* Once project is created go to 'API & Services' then 'Credentials'
* Go to 'OAuth Consent Screen' and set 'Application Name' and save (will essentially give consent)
* Go to 'Credentials' tab select 'Create Credentials', select 'OAuth client ID', select 'Other' and set 'Name' and finally create 
* Under the 'Credentials' tab there should be a new ID, select the Download option at the right side 
* Place the downloaded file in the project folder and rename 'credentials_web.json'

## Enabling Googl Sheets API
* Under APIs & Services select 'Enable APIs and Services'
* Search for 'Google Sheets APIs' and Enable

## API Key & Datacenter
* Data Center
Once in your Qualtrics account the data center will be the pre-fix of the link (e.g. https://noe.co1.qualtrics.com/ControlPanel/ 'noe.co1' is the datacenter)
* API Key
Under Account Settings go to Qualtrics IDs. Under API, either generate token or copy the Token. 
* Set the appropriate values in credentials.py

## Spreadsheet ID
* Open the Hire Salary on Google Drive and Open as Google Sheets. Then select 'Save as Google Sheets' under 'File'
* Obtain the sheet ID
Can do this by opening the sheet and obtaining the ID from the browser link. For example:
https://docs.google.com/spreadsheets/d/1234ABC/edit
Spreadsheet ID = 123ABC 
* Add a sheet named 'images' in the 'Hire Salary' spreadsheet (this is where the image ids will be stored)
* Set the appropriate value in credentials.py 

# Running the script
# If you're using a spreadsheet from a local machine pass in the flag value as 1:
## Uploading all images to Qualtrics
* Place excel workbook in .xlsx format, containing data in the same folder as main.py.
* The sheet containing data should be names as 'item assignment'
* Replace the value of DATASHEET in credentials.py to the workbook name.
* Run `python main.py upload 1` 

## Create Survey
* Run `python main.py 1`
* Once survey is created, the survey link will be printed and will be ready to use!

# If you're using a spreadsheet from a local machine pass in the flag value as 0:
## Uploading all images to Qualtrics
* Run `python main.py upload 0` 
* If the web browser prompts you, select the account where the 'Hire Salary' sheet is located and Allow. 

## Create Survey
* Run `python main.py 0`
* Once survey is created, the survey link will be printed and will be ready to use!


