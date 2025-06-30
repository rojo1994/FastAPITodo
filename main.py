from fastapi import FastAPI
import models
import database
from controllers import tasks, users
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Maja Test API",
    description="API para gestión de tareas",
    version="1.0.0"
)

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(users.router, prefix="/users", tags=["users"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Maja Test API"}

@app.get("/health")
def health_check():
    return {"status": "OK", "message": "API funcionando correctamente"}