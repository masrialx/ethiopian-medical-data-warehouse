from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, database, crud, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/data", response_model=list[schemas.DataSchema])
def read_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_data(db, skip, limit)
