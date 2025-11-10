WITH A AS (SELECT ID,
                  TO_DATE(TO_CHAR(LOGINTIME, 'yyyy-mm-dd'), 'yyyy-mm-dd'
                  ) AS LOGINDATE
           FROM LOGIN1
           GROUP BY ID,
                    TO_DATE(TO_CHAR(LOGINTIME, 'yyyy-mm-dd'),
                            'yyyy-mm-dd')),
     B AS (SELECT ID,

                  LOGINDATE,
                  LOGINDATE - LAG(LOGINDATE, 1) OVER (
                      PARTITION BY
                          ID
                      ORDER BY LOGINDATE
                      ) AS 天数差值
           FROM A),
     C AS (SELECT ID,
                  LOGINDATE,

                  SUM(
                          CASE
                              WHEN 天数差值 IS NULL
                                  OR 天数差值 > 2 THEN 1
                              ELSE 0
                              END
                  ) OVER (
                              PARTITION BY
                                  ID
                              ORDER BY LOGINDATE
                              ) AS 组
           FROM B),
     D AS (SELECT ID, 组, MAX(LOGINDATE) - MIN(LOGINDATE) + 1 AS 连续天数
           FROM C
           GROUP BY ID,
                    组)

SELECT ID, MAX(连续天数) AS 最大连续天数
FROM D
GROUP BY ID;