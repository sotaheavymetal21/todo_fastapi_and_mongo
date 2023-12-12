from fastapi import FastAPI
from routers import route_todo

app = FastAPI()
app.include_router(route_todo.router)


@app.get("/")
def root():
    return {"message": "Welcome to Fast API"}
