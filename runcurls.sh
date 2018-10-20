#!/usr/bin/env bash
echo "--------- Results of POST to /api/activities --------" > ./evidence/output.txt
curl -H "Content-Type: application/json" -X POST -d '{ "user_id": 3, "username": "frank", "details": "stuff here"}' http://0.0.0.0:5001/api/activities >> ./evidence/output.txt

echo "" >> ./evidence/output.txt
echo "--------- Results of GET to /api/activities/ --------" >> ./evidence/output.txt
curl http://0.0.0.0:5001/api/activities/ >> ./evidence/output.txt

echo "" >> ./evidence/output.txt
echo "--------- Results of GET to /api/activities/5bcbb7a03cfa483af554e041 --------" >> ./evidence/output.txt
curl http://0.0.0.0:5001/api/activities/5bcbb7a03cfa483af554e041 >> ./evidence/output.txt
