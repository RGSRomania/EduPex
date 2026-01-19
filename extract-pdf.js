#!/usr/bin/env node

/**
 * Extract Matematica Manual PDF content
 */

const fs = require('fs');
const path = require('path');

const pdfPath = path.join(__dirname, 'Planificari + Manual + Culegeri/Clasa a V a/Matematica/Manual.pdf');

console.log('📖 PDF Extraction Tool');
console.log('======================\n');
console.log(`Looking for: ${pdfPath}\n`);

// Check if file exists
if (!fs.existsSync(pdfPath)) {
  console.error(`❌ PDF not found at: ${pdfPath}`);
  console.log('\n📁 Available files in that location:');
  const dir = path.dirname(pdfPath);
  if (fs.existsSync(dir)) {
    const files = fs.readdirSync(dir);
    files.forEach(f => console.log(`   - ${f}`));
  } else {
    console.log(`   Directory doesn't exist: ${dir}`);
  }
  process.exit(1);
}

console.log(`✅ PDF found!`);
const stats = fs.statSync(pdfPath);
console.log(`📄 Size: ${(stats.size / 1024 / 1024).toFixed(2)} MB`);
console.log(`📅 Modified: ${stats.mtime}\n`);

// Try to extract with pdf-parse
try {
  const PDFParse = require('pdf-parse');

  console.log('📦 Using pdf-parse library...\n');

  const dataBuffer = fs.readFileSync(pdfPath);

  PDFParse(dataBuffer).then(data => {
    console.log(`✅ PDF parsed successfully!`);
    console.log(`📊 Pages: ${data.numpages}`);
    console.log(`📝 Text length: ${data.text.length} characters\n`);

    // Save extracted text
    const outputPath = path.join(__dirname, 'Manual_Matematica_5_EXTRACTED.txt');
    fs.writeFileSync(outputPath, data.text, 'utf-8');
    console.log(`✅ Saved to: ${outputPath}\n`);

    // Show preview
    const preview = data.text.substring(0, 2000);
    console.log('=== PREVIEW (first 2000 characters) ===\n');
    console.log(preview);
    console.log('\n' + '='.repeat(50));
  }).catch(err => {
    console.error('❌ Error parsing PDF:', err.message);
    process.exit(1);
  });
} catch (error) {
  console.error('❌ Error:', error.message);
  console.log('\nTrying alternative: use pdftotext command...\n');

  const { execSync } = require('child_process');
  try {
    const outputPath = path.join(__dirname, 'Manual_Matematica_5_EXTRACTED.txt');
    execSync(`pdftotext "${pdfPath}" "${outputPath}"`);
    console.log(`✅ Extracted using pdftotext`);
    console.log(`✅ Saved to: ${outputPath}\n`);

    const content = fs.readFileSync(outputPath, 'utf-8');
    const preview = content.substring(0, 2000);
    console.log('=== PREVIEW ===\n');
    console.log(preview);
  } catch (err) {
    console.error('❌ pdftotext not available either');
    console.log('\nPlease install: brew install poppler');
    process.exit(1);
  }
}

