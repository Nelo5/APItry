import uvicorn
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
@app.post("/translate")
def translate(lang:str,text: str):
    result = model(lang,text)
    return result

#uvicorn.run('Fast:app',host='localhost',port = 8080,reload=False)
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
# in terminal to start server
# uvicorn Fast:app --reload
