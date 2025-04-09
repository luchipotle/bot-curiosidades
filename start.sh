#!/bin/bash
rasa run \
  --enable-api \
  --cors "*" \
  --port $PORT \
  --model models \
  --debug