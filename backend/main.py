from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TaskDescription(BaseModel):
    text: str

@app.post("/generate_user_story")
def gerar(description: TaskDescription):
    story = description.text
    return {"user_story": story}
