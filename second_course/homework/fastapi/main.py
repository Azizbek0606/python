from fastapi import FastAPI
from database import showStudent 
app = FastAPI()

dict_data = {}

for i in showStudent():
    dict_data.update({i[0]:[i[1],i[2]]})
@app.get("/student")
def student():
    return dict_data
