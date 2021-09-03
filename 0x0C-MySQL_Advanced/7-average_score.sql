-- 7. Average score
-- SQL script that creates a stored procedure ComputeAverageScoreForUser
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMETER |
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
begin
declarate PROM float;
SET prom = (SELECT AVG(score) FROM corrections AS newTable WHERE newTable.user_id=user_id);
UPDATE users SET average_score=prom WHERE is=user_id;

END;
|
