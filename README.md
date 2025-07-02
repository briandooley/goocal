# Google Calendar Event Lister

This Python script connects to your Google Calendar, fetches events from specified calendars, filters them based on various criteria, and outputs them in a clean, readable format. It's especially useful for getting a quick overview of your upcoming work events and holidays, excluding personal time off.

## Features

* **Multiple Calendar Support:** Fetches events from the "ODiE" calendar and any calendar starting with "Holidays in".
* **Customizable Forecast:** Lists events for a specified number of days from today (default is 30 days) via a command-line argument.
* **Intelligent Filtering:**
    * Excludes events containing "PTO", "OOO", or "half-day" in their titles.
    * Excludes events falling on Saturdays or Sundays.
* **Clean Output Format:**
    * Displays dates as "Weekday, Day Month" (e.g., "Wednesday, 2 July").
    * For holiday events, simplifies the source to just the country (e.g., "Independence Day (United States)").
    * Adds a blank line separator between events from different weeks for improved readability.

## Prerequisites

Before you begin, ensure you have the following:

* **Python 3.6 or higher:** You can download it from [python.org](https://www.python.org/downloads/).
* **A Google Account:** This will be used to access your Google Calendar.
* **Internet Connection:** To connect to Google's APIs.

## Detailed Setup Instructions for Novice Users

Follow these steps carefully to get the script up and running.

### Step 1: Get the Script

1.  **Create a folder** on your computer where you want to store this script. Name it something simple and descriptive, like `google_calendar_script`.
2.  **Create a new file** inside this folder. You can use any plain text editor (like Notepad on Windows, TextEdit on Mac, or [VS Code](https://code.visualstudio.com/) which is highly recommended for coding).
3.  **Name the file `calendar_lister.py`**.
4.  **Copy all the code** from the "**Python Script (`calendar_lister.py`)**" section at the very end of this README and paste it into your `calendar_lister.py` file. Save the file.

### Step 2: Set up Google Cloud Project & Get Credentials

To allow your script to talk to your Google Calendar, you need to set up a project in Google Cloud and get a special file called `credentials.json`.

1.  **Go to the Google Cloud Console:**
    Open your web browser and navigate to [https://console.cloud.google.com/](https://console.cloud.google.com/).
    * You might need to log in with your Google Account.

2.  **Create a New Project:**
    * In the top left corner, click on the project dropdown (it might say "My First Project" or the name of a previous project).
    * In the dialog box that appears, click **"New Project"**.
    * Give your project a name (e.g., "My Calendar Script"). You can leave the Organization field blank.
    * Click **"Create"**. Wait a moment for the project to be created.

3.  **Enable the Google Calendar API:**
    * Once your new project is selected (make sure its name is visible in the top left dropdown), use the **search bar** at the top of the Google Cloud Console.
    * Type `Google Calendar API` and select it from the search results.
    * On the "Google Calendar API" page, click the blue **"Enable"** button.

4.  **Configure OAuth Consent Screen:**
    * In the left-hand navigation panel, go to **"APIs & Services" > "OAuth consent screen"**.
    * For **"User type"**, select **"External"** (unless you are part of a Google Workspace organization and only want internal users to access this app).
    * Click **"Create"**.
    * **OAuth consent screen details:**
        * **App name:** Give it a name (e.g., "My Calendar Lister").
        * **User support email:** Select your email address.
        * **Developer contact information:** Enter your email address again.
        * Click **"Save and Continue"**
    * **Scopes:**
        * Click **"Add or Remove Scopes"**.
        * In the search bar, type `Google Calendar API`.
        * Select the scope: `.../auth/calendar` (This is the general calendar access scope needed for private calendars).
        * Click **"Add to table"**.
        * Click **"Save and Continue"**.
    * **Test users:**
        * Click **"Add Users"**.
        * Enter your Google Account email address.
        * Click **"Add"**.
        * Click **"Save and Continue"**.
    * **Summary:** Review and click **"Back to Dashboard"**.
    * **Important:** For testing, you can keep the "Publishing status" as "Testing". If you ever wanted others to use it, you'd need to go through Google's verification process, but for personal use, "Testing" is sufficient.

5.  **Create OAuth Client ID (Download `credentials.json`):**
    * In the left-hand navigation panel, go to **"APIs & Services" > "Credentials"**.
    * Click on **"+ Create Credentials"** at the top.
    * Select **"OAuth client ID"**.
    * For **"Application type"**, select **"Desktop app"**.
    * Give it a name (e.g., "My Calendar Desktop Client").
    * Click **"Create"**.
    * A dialog box will appear with your Client ID and Client secret.
    * Click the **"Download JSON"** button.
    * **Rename the downloaded file:** The file will likely have a long, generated name (e.g., `client_secret_YOUR_CLIENT_ID.apps.googleusercontent.com.json`). **You MUST rename this file to exactly `credentials.json`**.
    * **Move `credentials.json`:** Place this renamed `credentials.json` file into the **same folder** (`google_calendar_script`) where you saved your `calendar_lister.py` script.

### Step 3: Install Python Libraries

1.  Open your computer's **Terminal** (Mac/Linux) or **Command Prompt/PowerShell** (Windows).
2.  Navigate to the folder where you saved your script using the `cd` command. For example, if your folder is named `google_calendar_script` and it's in your Documents:
    ```bash
    cd Documents/google_calendar_script
    ```
3.  Then, run the following command to install the necessary Python libraries:
    ```bash
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```
    Wait for this command to finish. You should see messages indicating successful installation.

### Step 4: Run the Script for the First Time (Authentication)

Now you're ready to run the script.

1.  In your Terminal/Command Prompt (ensure you are still in your `google_calendar_script` folder), run the script using the Python 3 interpreter:
    ```bash
    python3 calendar_lister.py
    ```
    (If `python3` doesn't work, try `python` instead.)

2.  **Authentication Process:**
    * The **first time** you run it, a web browser window will automatically open.
    * It will prompt you to log in to your Google Account (if you're not already logged in).
    * It will then ask for your permission for "My Calendar Lister" (or whatever app name you chose) to "See, edit, share, and permanently delete all the calendars you can access using Google Calendar." **You must grant this permission** for the script to function correctly.
    * After you grant permission, the browser might show a message like "The authentication flow has completed." You can then safely close this browser tab.

3.  **`token.json` file:**
    * Back in your `google_calendar_script` folder, you will now see a new file named `token.json`. This file securely stores your authentication tokens so you don't have to go through the browser login process every subsequent time you run the script. **Do not delete or share this file.**

## Usage

Once setup is complete, you can run the script:

* **To list events for the default 30 days:**
    ```bash
    python3 calendar_lister.py
    ```
* **To list events for a specific number of days (e.g., next 7 days):**
    ```bash
    python3 calendar_lister.py 7
    ```
* **To list events for 60 days:**
    ```bash
    python3 calendar_lister.py 60
    ```
    *(Remember to replace `python3` with `python` if that's what works on your system.)*

## Customization (Optional)

You can open the `calendar_lister.py` file in a text editor to make minor adjustments to its behavior:

* **Change target calendars:** Modify the `target_calendar_names` list near the top of the `get_combined_calendar_events` function to include other specific calendar names you want to monitor.
    ```python
    target_calendar_names = ["ODiE", "My Team Calendar", "Project X Schedule"]
    ```
* **Adjust filter keywords:** Modify the `filter_keywords` list to add or remove words that cause an event to be skipped from the output.
    ```python
    filter_keywords = ["PTO", "OOO", "HALF-DAY", "VACATION", "SICK"]
    ```

## Troubleshooting

* **`ModuleNotFoundError: No module named 'google.auth'`**:
    * This means the Python libraries are not installed or are not accessible by your Python environment. Go back to **Step 3: Install Python Libraries** and run the `pip install` command again.

* **`An error occurred: <HttpError 403 ... accessNotConfigured ... Enable it by visiting ...>`**:
    * This means the Google Calendar API is not enabled for your project. Go back to **Step 2.3: Enable the Google Calendar API** and ensure it's enabled for the specific project you created.

* **`An error occurred: <HttpError 400 ... "Bad Request">`**:
    * This error was addressed during development. It usually means an API parameter is invalid for a specific calendar. The current script avoids the known `timeMin` issue by filtering client-side. If this error reappears, it might be due to a specific event within the calendar or a combination of `singleEvents=True` or `orderBy="startTime"` causing issues. You can try removing those parameters from the `service.events().list(...)` call if the error persists.

* **No events are listed / "No events found..."**:
    * **Check your Google Calendar manually** to ensure there are events in the specified calendar(s) within the date range you're asking for.
    * Ensure the calendar names in your script (e.g., `"ODiE"`) match the **exact names** in your Google Calendar (case-sensitive).
    * Increase `query_max_results` in the script to a higher number (e.g., `2500`) to fetch more events, in case your relevant events are further down the list fetched from Google.

---

### Python Script (`calendar_lister.py`)

```python
import datetime
import os.path
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["[https://www.googleapis.com/auth/calendar](https://www.googleapis.com/auth/calendar)"] 

def get_combined_calendar_events(days_to_forecast=30):
    """
    Fetches and prints events from the 'ODiE' calendar and any calendar
    starting with 'Holidays in' for a specified number of days from today,
    excluding events with "PTO", "OOO", "half-day" in their summary,
    and excluding events on Saturdays or Sundays.
    Indicates the country for 'Holidays in' calendars.
    Adds a carriage return after each week.
    Does not output event times.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        target_calendar_names = ["ODiE"] # Customize this list for other specific calendars
        holiday_calendar_prefix = "Holidays in"
        
        calendar_info_to_query = [] 
        
        print("--- Discovering Calendars ---")
        calendar_list = service.calendarList().list().execute()
        for calendar_list_entry in calendar_list["items"]:
            summary = calendar_list_entry.get("summary")
            id_val = calendar_list_entry.get("id")

            if summary in target_calendar_names or (summary and summary.startswith(holiday_calendar_prefix)):
                calendar_info_to_query.append({'id': id_val, 'name': summary})
                print(f"  Found '{summary}' calendar with ID: {id_val}")
        
        if not calendar_info_to_query:
            print("Error: No target calendars found. Please check names and permissions.")
            return

        print(f"--- Querying events from selected calendars ---")

        all_fetched_events = []
        query_max_results = 2500 

        for cal_info in calendar_info_to_query:
            cal_id = cal_info['id']
            cal_name = cal_info['name']
            print(f"  Fetching events for '{cal_name}'...")
            
            events_result = (
                service.events()
                .list(
                    calendarId=cal_id,
                    maxResults=query_max_results,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])
            for event in events:
                event['source_calendar_name'] = cal_name
            all_fetched_events.extend(events)

        if not all_fetched_events:
            print(f"No events found across all selected calendars within the {query_max_results} fetched events per calendar.")
            return

        all_fetched_events.sort(key=lambda x: x['start'].get('dateTime') or x['start'].get('date'))

        now_utc = datetime.datetime.now(datetime.timezone.utc)
        start_date_range = now_utc.date()
        end_date_range = (now_utc + datetime.timedelta(days=days_to_forecast)).date() 


        print(f"\n--- Combined Events for the next {days_to_forecast} days ({start_date_range.strftime('%A, %d %B')} to {end_date_range.strftime('%A, %d %B')}) ---")

        found_events_in_range = False
        last_printed_week_info = None # (year, week_number)

        for event in all_fetched_events:
            summary = event.get('summary', '') 
            source_cal_name = event.get('source_calendar_name', 'Unknown Calendar')
            
            filter_keywords = ["PTO", "OOO", "HALF-DAY"] # Customize filter keywords here
            if any(keyword in summary.upper() for keyword in filter_keywords):
                continue 

            start_str = event["start"].get("dateTime", event["start"].get("date"))
            
            if 'dateTime' in event['start']:
                event_start = datetime.datetime.fromisoformat(start_str)
                if event_start.tzinfo is None:
                    event_start = event_start.replace(tzinfo=datetime.timezone.utc)
                else:
                    event_start = event_start.astimezone(datetime.timezone.utc)
                
                display_date_time = event_start.strftime('%A, %d %B')
            else:
                event_start = datetime.datetime.strptime(start_str, '%Y-%m-%d').replace(tzinfo=datetime.timezone.utc)
                display_date_time = event_start.strftime('%A, %d %B')
            
            if event_start.weekday() == 5 or event_start.weekday() == 6: # 5 is Saturday, 6 is Sunday
                continue

            if start_date_range <= event_start.date() <= end_date_range:
                current_week_info = (event_start.year, event_start.isocalendar().week)
                
                if found_events_in_range and current_week_info != last_printed_week_info:
                    print("") 
                
                last_printed_week_info = current_week_info 

                output_line = f"{display_date_time} - {summary}"
                if source_cal_name.startswith(holiday_calendar_prefix):
                    country_name = source_cal_name[len(holiday_calendar_prefix + " "):]
                    output_line += f" ({country_name})"
                print(output_line)
                found_events_in_range = True
        
        if not found_events_in_range:
            print(f"No events found for the next {days_to_forecast} days ({start_date_range.strftime('%A, %d %B')} to {end_date_range.strftime('%A, %d %B')}) across selected calendars (after filtering).")

    except HttpError as error:
        print(f"An error occurred: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    days = 30
    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
            if days <= 0:
                print("Error: Number of days must be a positive integer.")
                sys.exit(1)
        except ValueError:
            print("Error: Invalid number of days. Please provide an integer.")
            sys.exit(1)
    
    get_combined_calendar_events(days)