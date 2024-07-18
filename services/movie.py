from models.movie import Movie as MovieModel
from schemas.movie import Movie

#creo la cclase con el metodo constructor
class MovieService():
    def __init__(self,dataB) -> None:
        self.dataB = dataB
        
    def get_movies(self):
        result = self.dataB.query(MovieModel).all()
        return result
    
    def get_movie(self,id):
        result = self.dataB.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movie_by_name(self,title):
        result = self.dataB.query(MovieModel).filter(MovieModel.title == title).first()
        return result
    
    def get_movie_category(self,category):
        result = self.dataB.query(MovieModel).filter(MovieModel.category == category).all()
        return result
        
    def create_movie(self, movie:Movie):
        new_movie = MovieModel(**movie.model_dump())
        self.dataB.add(new_movie)
        self.dataB.commit()
        return
        
    def update_movie(self, id:int, data: Movie):
        movie = self.dataB.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.dataB.commit()
        return
    
    def delete_movie(self,id=int):
        self.dataB.query(MovieModel).filter(MovieModel.id == id).delete()
        self.dataB.commit()
        return