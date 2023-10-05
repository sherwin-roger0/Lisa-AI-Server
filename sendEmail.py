from socket_module import socketio,session

def sendEmail(mail,mailHead,mailContent):

    print("mail",[mail,mailHead,mailContent])
    socketio.emit("mail",[mail,mailHead,mailContent],room=session["room"])
    return f"Email sent to {mail}"
    
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class emailToolInput(BaseModel):
    """Inputs for the EmailTool"""

    mail: list = Field(description="The list of emailIDs of the people to send the email, if the mailid of the people is not given add @gmail.com at the end of the people names")
    subject: str = Field(description="if the user did'nt give the subject of the mail ID then create a subject of the mail yourself")
    mailContent: str = Field(description="This is the content part of the mail to be sent to the mailID")


class emailTool(BaseTool):
    name = "emailTool"
    description = """
        Useful when you want to send a email to people.
        """
    args_schema: Type[BaseModel] =emailToolInput
    def _run(self, mail: list,subject: str,mailContent: str):
        email_response = sendEmail(mail,subject,mailContent)
        return email_response

    def _arun(self, mail: list,subject: str,mailContent: str):
        email_response = sendEmail(mail,subject,mailContent)
        return email_response