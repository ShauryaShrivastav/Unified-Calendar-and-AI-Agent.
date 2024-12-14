from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalendarEvent(BaseModel):
    title: str
    start_time: str
    end_time: str
    platform: str

@app.get("/calendar/events", response_model=list[CalendarEvent])
def get_combined_calendar():
    # Placeholder: Fetch and merge events from Gmail, Outlook, etc.
    return [
        {"title": "Meeting with John", "start_time": "10:00 AM", "end_time": "11:00 AM", "platform": "Google Calendar"},
        {"title": "Team Standup", "start_time": "2:00 PM", "end_time": "2:30 PM", "platform": "Outlook"},
    ]

if _name_ == "_main_":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)