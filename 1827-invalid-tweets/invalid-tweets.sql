-- Write your PostgreSQL query statement below
SELECT t1.tweet_id
FROM Tweets t1
WHERE LENGTH(t1.content) > 15