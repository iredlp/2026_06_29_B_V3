from database.DB_connect import DBConnect
from model.movie import Movie


class DAO:
    @staticmethod
    def getAllMovies():
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select * \
                from movie m """

        cursor.execute(query)

        for row in cursor:
            results.append(row)

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """  select distinct genre  from genre g """

        cursor.execute(query)

        for row in cursor:
            results.append(row["genre"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllNodes(genere):
        conn = DBConnect.get_connection()
        results = []
        movies_map = {}

        cursor = conn.cursor(dictionary=True)
        query = """  SELECT distinct m.id, m.title, m.year, r.avg_rating
                    FROM role_mapping rm, movie m, genre g, ratings r 
                     where rm.category IN ('actor', 'actress')
                    and m.id=g.movie_id and m.id =rm.movie_id 
                    and r.movie_id =m.id 
                    and g.genre =%s """

        cursor.execute(query,(genere,) )

        for row in cursor:
            results.append(
                Movie(
                    id=row["id"],
                    title=row["title"],
                    year=row["year"],
                    avg_rating=float(row["avg_rating"]) if row["avg_rating"] is not None else None
                ))
               # movies_map[m.id] = m

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getCastFilm(genere):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
                    select m.id AS movie_id, n.id AS actor_id
                    from role_mapping rm,movie m, genre g, names n 
                    where rm.category IN ('actor', 'actress') and rm.name_id =n.id 
                    and m.id=g.movie_id and m.id =rm.movie_id
                    and g.genre =%s  """

        cursor.execute(query, (genere,))

        for row in cursor:
            results.append((row["movie_id"], row["actor_id"]))

        cursor.close()
        conn.close()
        return results