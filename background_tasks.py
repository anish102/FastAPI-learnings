from typing import Annotated

from fastapi import BackgroundTasks, Depends, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}:{message}"
        email_file.write(content)


def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(get_query)]
):
    if q:
        message = f"message to {email}\n"
        background_tasks.add_task(write_log, message)
        return {"message": "Message sent"}
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
