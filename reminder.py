import datetime
from socket_module import socketio,session

current_datetime = datetime.datetime.now()

def send_reminder(date,hours,minutes,month,description):
    print("hi",datetime.datetime.now().day)
    if month==12: 
      month = datetime.datetime.now().month
    print(date,hours,minutes,month)
    socketio.emit("reminder",[date,hours,minutes,month,description],room=session["room"])
    return "Reminder is created"

from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class send_reminderInput(BaseModel):
    
    """Inputs send_reminder Tool  
    """

    date: int = Field(description=f"This is the date to be set as an input ,If the user didn't specify the date of the reminder then calculate the date yourself today's date is {datetime.datetime.now().day}")
    hours: int = Field(description=f"if the date is not provided set hours as {0} The hours input must be in Coordinated Universal Time (UTC) Set the hour (0-23)")
    minutes: int = Field(description=f"This is an minutes in input for the reminder,the default value is 0")
    month: int = Field(description=f"This is an month input for the reminder, if it is january the input must be 0 do like this for all the months(0-11), If the user didn't specify the month of the reminder then calculate the month yourself today's month is {datetime.datetime.now().month-1}")
    description: str=Field(description="The reason to set the reminder must be passed in this input")


class send_reminderTool(BaseTool):

    # Get the current date and time

    name = "send_reminderTool"
    description = """
        Useful when you want to send a reminder.
        If the user didn't give the reason for the reminder then ask the reason for the reminder
        """
    args_schema: Type[BaseModel] = send_reminderInput
    
    def _run(self, date: int,hours: int,minutes: int,month: int,description: str):
        reminder_response = send_reminder(date,hours,minutes,month,description)
        return reminder_response

    def _arun(self, date: int,hours: int,minutes: int,month: int,description: str):
        reminder_response = send_reminder(date,hours,minutes,month,description)
        return reminder_response