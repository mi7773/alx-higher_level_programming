-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.name AS genre, COUNT(c.show_id) AS number_of_shows
FROM tv_genres g
RIGHT JOIN tv_show_genres c ON c.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC;
