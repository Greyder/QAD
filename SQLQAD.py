SELECT c.login,
       COUNT(o.”inDelivery”)
FROM “Couriers” AS c
RIGHT JOIN “Orders” AS o ON o.”courierId” =c.id
GROUP BY c.login
HAVING COUNT(o.”inDelivery”) = true;

SELECT track,
       finished,
       cancelled,
       “inDelivery”,
       CASE
           WHEN finished = true THEN status = 2
           OR WHEN finished = false AND cancelled = true THEN status = -1
           OR WHEN finished = false AND  “inDelivery” = true THEN status =1
           ELSE = 0
       END
FROM “Orders”;

