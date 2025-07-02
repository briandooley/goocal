import datetime
import os.path
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"] 

def get_combined_calendar_events(days_to_forecast=30):
    """
    Fetches and prints events from the 'ODiE' calendar and any calendar
    starting with 'Holidays in' for a specified number of days from today,
    excluding events with "PTO", "OOO", "half-day" in their summary,
    and excluding events on Saturdays or Sundays.
    Indicates the country for 'Holidays in' calendars.
    Adds a carriage return after each week (before the first event of a new week).
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

        target_calendar_names = ["ODiE"]
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
            
            filter_keywords = ["PTO", "OOO", "HALF-DAY"]
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
                # --- UPDATED LOGIC: Add carriage return for new week ---
                current_week_info = (event_start.year, event_start.isocalendar().week)
                
                # Print a blank line if it's not the very first event AND
                # the week number (or year) has changed
                if found_events_in_range and current_week_info != last_printed_week_info:
                    print("") # Print a blank line
                
                last_printed_week_info = current_week_info # Update last printed week info

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