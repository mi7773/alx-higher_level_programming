-- lists all comedy shows in the database hbtn_0d_tvshows
SELECT s.title
FROM tv_shows s
INNER JOIN tv_show_genres c ON s.id = c.show_id
INNER JOIN tv_genres g ON g.id = c.genre_id
WHERE g.name = 'Comedy'
ORDER BY s.title;
