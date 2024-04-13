SELECT
Y.ID,
X.FISH_NAME,
X.LENGTH
FROM
(SELECT
FI.FISH_TYPE,
FN.FISH_NAME,
MAX(FI.LENGTH) AS LENGTH
FROM FISH_INFO FI
JOIN FISH_NAME_INFO FN
ON FI.FISH_TYPE = FN.FISH_TYPE
GROUP BY FI.FISH_TYPE, FN.FISH_NAME) X
JOIN FISH_INFO Y
ON X.FISH_TYPE = Y.FISH_TYPE
AND X.LENGTH = Y.LENGTH
ORDER BY 1