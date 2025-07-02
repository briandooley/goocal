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
goocal
## Detailed Setup Instructions for Novice Users

Follow these steps carefully to get the script up and running.

### Step 1: Get the Script

1.  **Create a folder** on your computer where you want to store this script. Name it something simple and descriptive, like `google_calendar_script`.
2.  **Create a new file** inside this folder. You can use any plain text editor (like Notepad on Windows, TextEdit on Mac, or [VS Code](https://code.visualstudio.com/) which is highly recommended for coding).
3.  **Name the file `goocal.py`**.
4.  **Copy all the code** from the "**Python Script (`goocal.py`)**" section at the very end of this README and paste it into your `goocal.py` file. Save the file.

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
    * **Move `credentials.json`:** Place this renamed `credentials.json` file into the **same folder** (`google_calendar_script`) where you saved your `goocal.py` script.

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
    python3 goocal.py
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
    python3 goocal.py
    ```
* **To list events for a specific number of days (e.g., next 7 days):**
    ```bash
    python3 goocal.py 7
    ```
* **To list events for 60 days:**
    ```bash
    python3 goocal.py 60
    ```
    *(Remember to replace `python3` with `python` if that's what works on your system.)*

## Customization (Optional)

You can open the `goocal.py` file in a text editor to make minor adjustments to its behavior:

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
