 SELECT COUNT(title) FROM ratings JOIN
 movies ON ratings.movie_id = movies.id
 WHERE rating = 10.0;