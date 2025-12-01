-- Write your PostgreSQL query statement below
-- Self join would be good here because we can check duplicates. If the p1.id != p2.id its a different entity, check if they have duplicate emails with the other entity --

SELECT DISTINCT p1.email AS Email
FROM Person p1, Person p2
WHERE (p1.id != p2.id AND p1.email = p2.email)