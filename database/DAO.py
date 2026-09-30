from database.DB_connect import DBConnect


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
