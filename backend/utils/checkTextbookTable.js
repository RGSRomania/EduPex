// Simple script to check Supabase textbook_content table
const { createClient } = require('@supabase/supabase-js');
require('dotenv').config();

console.log('Starting Supabase check...');

// Use the Supabase URL and key directly from environment or hardcoded value
const supabaseUrl = process.env.SUPABASE_URL || 'https://szbjppcmhshegyewsveu.supabase.co';
const supabaseKey = process.env.SUPABASE_SERVICE_KEY || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN6YmpwcGNtaHNoZWd5ZXdzdmV1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NjIwODg4NiwiZXhwIjoyMDcxNzg0ODg2fQ.9DFChq7KL_KhjyNxUkhlBWDXuMiRZkpuvAS-kS3SlH0';

// Log what we're using
console.log('Using Supabase URL:', supabaseUrl ? 'Found' : 'Missing');
console.log('Using Supabase Key:', supabaseKey ? 'Found' : 'Missing');

if (!supabaseUrl || !supabaseKey) {
  console.error('Supabase credentials missing. Cannot continue.');
  process.exit(1);
}

// Initialize Supabase client
const supabase = createClient(supabaseUrl, supabaseKey);
console.log('Supabase client initialized');

// Check for the textbook_content table
async function checkTextbookTable() {
  try {
    console.log('Checking for textbook_content table...');
    const { data, error } = await supabase
      .from('textbook_content')
      .select('count(*)')
      .limit(1);

    if (error) {
      console.error('Error querying textbook_content:', error.message);
      return;
    }

    console.log('Textbook content table exists!');
    console.log('Record count:', data[0].count);
  } catch (err) {
    console.error('Unexpected error:', err.message);
  }
}

// Run the check
checkTextbookTable();
