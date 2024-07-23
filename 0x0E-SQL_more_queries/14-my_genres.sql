-- uses the hbtn_0d_tvshows database to list all genres of the show Dexter
SELECT g.name
FROM tv_genres g
INNER JOIN tv_show_genres c ON c.genre_id = g.id
INNER JOIN tv_shows s ON s.id = c.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name;
