from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse 
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, func, select #Allows for connecting to database, creating tables, executing functions, and using select statements
from sqlalchemy.orm import sessionmaker, Session #Confused but recommended for sqlalchemy?
from databases import Database #interface for interaction with databases
from pydantic import BaseModel #Provides a method data validation


class MovieInput(BaseModel): #Movie Model for data input validation
    title: str
    release_date: str
    runtime_in_min: int
    watch_status: str

class TVShowInputObject(BaseModel): #TVShow model for data input validation
    name: str
    release_date: str
    number_of_episodes: int
    watch_status: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #Allows requests from any origin
    allow_credentials=True, #Allows cookies?
    allow_methods=["*"], 
    allow_headers=["*"],
)

DATABASE_URL = "sqlite:///./m&t.db" #Location to access SQLite.db
engine = create_engine(DATABASE_URL) #Create DB based on database location

metadata = MetaData()

#Creation of Movies Table
movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String),
    Column("release_date", String),
    Column("runtime_in_min", Integer),
    Column("watch_status", String, default="Want to Watch")
)

#Creation of Shows Table
shows = Table(
    "shows",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String),
    Column("release_date", String),
    Column("number_of_episodes", Integer),
    Column("watch_status", String, default="Want to Watch")
)

metadata.create_all(engine) #Creates database tables based on the previous data

#Create a new session for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Creates a session used to interact with db.

def get_db(): 
    db = SessionLocal() #Database session assignment for fastAPI
    try:
        yield db #Holds the function until db's code is done being ran
    finally:
        db.close() #Closes database session

#CRUD operations for movies
@app.post("/movies/") #Endpoint for Posting
async def create_movie(movie: MovieInput, db: Session = Depends(get_db)): #Takes in MoveInput Pydantic model, and sets the session to get_db
    db.execute(movies.insert().values(  #uses insert statement to add the data for the movie
        title=movie.title,
        release_date=movie.release_date,
        runtime_in_min=movie.runtime_in_min,
        watch_status=movie.watch_status 
    )) 
    db.commit() #saves the changes
    return {"message": "Movie created successfully"}


#Read all movies
@app.get("/movies/")
async def read_movies(db: Session = Depends(get_db)):
    return db.execute(select(movies)).all()


@app.put("/movies/{movie_id}")
async def update_movie(movie_id: int, movie: MovieInput, db: Session = Depends(get_db)): #Updates DB based on movie_id
    db.execute(
        movies.update().where(movies.c.id == movie_id).values(
            title=movie.title,
            release_date=movie.release_date,
            runtime_in_min=movie.runtime_in_min,
            watch_status=movie.watch_status 
        )
    )
    db.commit()
    return {"message": "Movie updated successfully"}


@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int, db: Session = Depends(get_db)):  #Deletes movie based on movie_id
    db.execute(movies.delete().where(movies.c.id == movie_id))
    db.commit()
    return {"message": "Movie deleted successfully"}



#CRUD operations for TV shows
@app.post("/tvshows/")
async def create_show(show: TVShowInputObject, db: Session = Depends(get_db)):
    db.execute(shows.insert().values(
        name=show.name,
        release_date=show.release_date,
        number_of_episodes=show.number_of_episodes,
        watch_status=show.watch_status  # Add the watch_status field here
    ))
    db.commit()
    return {"message": "TV show created successfully"}

#Read all TV shows
@app.get("/tvshows/")
async def read_shows(db: Session = Depends(get_db)):
    return db.execute(select(shows)).all()


@app.put("/tvshows/{show_id}")
async def update_show(show_id: int, show: TVShowInputObject, db: Session = Depends(get_db)):
    db.execute(
        shows.update().where(shows.c.id == show_id).values(
            name=show.name,
            release_date=show.release_date,
            number_of_episodes=show.number_of_episodes,
            watch_status=show.watch_status
        )
    )
    db.commit()
    return {"message": "TV show updated successfully"}


@app.delete("/tvshows/{show_id}")
async def delete_show(show_id: int, db: Session = Depends(get_db)):
    db.execute(shows.delete().where(shows.c.id == show_id))
    db.commit()
    return {"message": "TV show deleted successfully"}

if __name__ == "__main__": #Runs if __main__ is ran as the driver
    import uvicorn 

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True) 
