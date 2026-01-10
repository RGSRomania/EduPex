#!/bin/bash

# Start backend server
cd /Users/mdica/PycharmProjects/EduPex/backend && node server.js &
BACKEND_PID=$!

# Wait for backend to start
echo "Starting backend server..."
sleep 3

# Start frontend server
cd /Users/mdica/PycharmProjects/EduPex/frontend && npm start &
FRONTEND_PID=$!

# Function to handle exit
function cleanup {
  echo "Shutting down servers..."
  kill $BACKEND_PID
  kill $FRONTEND_PID
  exit
}

# Set up trap for SIGINT (Ctrl+C)
trap cleanup INT

# Keep script running
echo "Both servers are running. Press Ctrl+C to stop."
wait
