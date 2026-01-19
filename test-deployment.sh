#!/bin/bash

echo "🧪 EduPex Deployment Testing Script"
echo "===================================="
echo ""

# Test 1: Backend Health Check
echo "Test 1: Backend Health Check"
echo "Checking: https://edupex-backend.onrender.com/api/health"
HEALTH_STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://edupex-backend.onrender.com/api/health)
echo "Status: $HEALTH_STATUS"
if [ "$HEALTH_STATUS" = "200" ]; then
    echo "✅ Backend is responding"
else
    echo "❌ Backend not responding (still deploying?)"
fi
echo ""

# Test 2: Lessons Endpoint (No Auth Required)
echo "Test 2: Lessons Endpoint"
echo "Checking: https://edupex-backend.onrender.com/api/lessons/materii"
RESPONSE=$(curl -s https://edupex-backend.onrender.com/api/lessons/materii)
echo "Response: $RESPONSE"

# Check if it's an array (successful) or error
if echo "$RESPONSE" | grep -q '\['; then
    echo "✅ Successfully fetching lessons (no 401 error!)"
elif echo "$RESPONSE" | grep -q 'Please authenticate'; then
    echo "❌ Still getting auth error - deployment in progress or old code running"
elif echo "$RESPONSE" | grep -q 'error'; then
    echo "⚠️  API error: $RESPONSE"
else
    echo "⚠️  Unexpected response"
fi
echo ""

# Test 3: Frontend Running
echo "Test 3: Frontend Status"
FRONTEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000)
if [ "$FRONTEND_STATUS" = "200" ]; then
    echo "✅ Frontend is running on localhost:3000"
else
    echo "❌ Frontend not accessible on localhost:3000"
fi
echo ""

# Test 4: CORS Preflight
echo "Test 4: CORS Preflight"
echo "Checking: CORS headers from backend"
CORS_HEADER=$(curl -s -I -X OPTIONS https://edupex-backend.onrender.com/api/lessons/materii | grep -i "Access-Control-Allow-Origin")
if [ -n "$CORS_HEADER" ]; then
    echo "✅ CORS headers present: $CORS_HEADER"
else
    echo "❌ No CORS headers found"
fi
echo ""

echo "===================================="
echo "Summary:"
echo ""
echo "If you see mostly ✅: Deployment was successful!"
echo "If you see ❌: Render is still deploying (wait 2-3 more minutes)"
echo ""
echo "Next step: Refresh http://localhost:3000 in your browser"

