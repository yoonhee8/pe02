#!/usr/bin/env bash

PORT=5000
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "data":[[0,0],
    [1,1]
    ]
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict