# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class FormData(BaseModel):
    name: str
    email: str
    message: str

@app.post("/submit")
async def submit_form(form_data: FormData):
    try:
        # Here you can handle the form data, e.g., save it to a database
        return {"message": "Form submitted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="There was an error processing your request.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
