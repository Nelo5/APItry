from fastapi import FastAPI
from ML import load_model

app = FastAPI()
model = None

# create a route
@app.get("/")
def index():
    return {"text": "Translation"}

# Register the function to run during startup
@app.on_event("startup")
def startup_event():
    global model
    model = load_model()

# Your FastAPI route handlers go here
@app.get("/translate")
def translate(lang:str,text: str, max_length = 1000):
    result = model(lang,text)
    return result

#uvicorn.run('Fast:app',host='localhost',port = 8080,reload=False)

# in terminal to start server
# uvicorn Fast:app --reload
