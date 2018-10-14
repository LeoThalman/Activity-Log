#!/usr/bin/env bash
echo "--------- Results of POST to /api/activities --------" > ./evidence/output.txt
curl -H "Content-Type: application/json" -X POST -d '{ "user_id": 3, "username": "frank", "details": "stuff here"}' http://0.0.0.0:5000/api/activities >> ./evidence/output.txt

echo "" >> ./evidence/output.txt
echo "--------- Results of GET to /api/activities/ --------" >> ./evidence/output.txt
curl http://0.0.0.0:5000/api/activities/ >> ./evidence/output.txt

echo "" >> ./evidence/output.txt
echo "--------- Results of GET to /api/activities/2 --------" >> ./evidence/output.txt
curl http://0.0.0.0:5000/api/activities/2 >> ./evidence/output.txt
