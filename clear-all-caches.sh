#!/bin/bash

# Clear all caches and restart the app
echo "🧹 Clearing all caches..."

# 1. Clear npm cache
npm cache clean --force
echo "✅ Cleared npm cache"

# 2. Clear React cache (if exists)
rm -rf node_modules/.cache 2>/dev/null
echo "✅ Cleared React build cache"

# 3. Clear browser service worker
echo "⚠️  You MUST manually clear browser cache:"
echo "   - Chrome/Edge: Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)"
echo "   - Firefox: Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)"
echo "   - Safari: Develop > Empty Web Storage"

# 4. Kill any running Node processes
pkill -f "react-scripts" 2>/dev/null
pkill -f "node" 2>/dev/null
echo "✅ Killed running processes"

echo ""
echo "🚀 To complete the cache clear:"
echo "1. Open your browser"
echo "2. Press Cmd+Shift+Delete (Mac) or Ctrl+Shift+Delete (Windows)"
echo "3. Select 'All time' and clear cache"
echo "4. Hard refresh: Cmd+Shift+R (Mac) or Ctrl+F5 (Windows)"
echo "5. Restart the dev server: npm start"
echo ""
echo "✅ The app will now show REAL content!"

