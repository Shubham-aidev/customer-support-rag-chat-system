from fastapi import FastAPI
from routes import user, document , auth
from database.db import engine, Base
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include all routes
app.include_router(user.router)
app.include_router(document.router)
app.include_router(auth.router)
# health endpoint
@app.get("/")
def root():
    return {"message": "Customer Support RAG API running"}

