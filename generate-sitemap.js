const fs = require('fs');
const path = require('path');

// CONFIGURATION
const BASE_URL = 'https://symbols.thenepal.io/'; 
const HTML_OUTPUT = 'sitemap.html';
const XML_OUTPUT = 'sitemap.xml';

function getHtmlFiles(dir, fileList = []) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const filePath = path.join(dir, file);
        if (file === 'node_modules' || file.startsWith('.')) return;
        
        if (fs.statSync(filePath).isDirectory()) {
            getHtmlFiles(filePath, fileList);
        } else if (file.endsWith('.html') && file !== HTML_OUTPUT) {
            let relativePath = path.relative(__dirname, filePath).replace(/\\/g, '/');
            fileList.push(relativePath);
        }
    });
    return fileList;
}

// Helper to make page names look professional
function cleanLabel(filePath) {
    if (filePath === 'index.html') return 'Home';
    
    // Remove '.html' and '/index' if it exists at the end
    let cleanPath = filePath.replace('.html', '').replace(/\/index$/, '');
    
    let prefix = '';
    // Check if it's a Nepali translation file
    if (cleanPath.startsWith('ne/')) {
        prefix = 'नेपाली: ';
        cleanPath = cleanPath.replace('ne/', '');
        if (!cleanPath) return 'नेपाली गृहपृष्ठ (Nepali Home)'; 
    }
    
    // Capitalize words nicely
    let words = cleanPath.replace(/[-_]/g, ' ').split(' ');
    let formattedWords = words.map(word => word.charAt(0).toUpperCase() + word.slice(1));
    
    return prefix + formattedWords.join(' ');
}

function generateSitemaps() {
    const files = getHtmlFiles(__dirname);
    const currentDate = new Date().toISOString().split('T')[0];
    
    // --- 1. GENERATE HTML SITEMAP ---
    let htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sitemap - National Symbols of Nepal</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 40px auto; max-width: 800px; line-height: 1.6; color: #333; }
        h1 { color: #111; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 12px 0; padding-left: 5px; }
        a { color: #0366d6; text-decoration: none; font-weight: 500; }
        a:hover { text-decoration: underline; color: #0056b3; }
    </style>
</head>
<body>
    <h1>Website Sitemap</h1>
    <ul>\n`;

    // --- 2. GENERATE XML SITEMAP ---
    let xmlContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

    // Loop through files and populate both
    files.forEach(file => {
        const urlPath = file === 'index.html' ? '' : file;
        const fullUrl = `${BASE_URL}${urlPath}`;
        const label = cleanLabel(file);
        
        // Append to HTML
        htmlContent += `        <li><a href="${fullUrl}">${label}</a></li>\n`;
        
        // Append to XML
        xmlContent += `  <url>\n    <loc>${fullUrl}</loc>\n    <lastmod>${currentDate}</lastmod>\n    <priority>${file === 'index.html' ? '1.0' : '0.8'}</priority>\n  </url>\n`;
    });

    htmlContent += `    </ul>\n</body>\n</html>`;
    xmlContent += `</urlset>`;

    fs.writeFileSync(path.join(__dirname, HTML_OUTPUT), htmlContent);
    fs.writeFileSync(path.join(__dirname, XML_OUTPUT), xmlContent);
    
    console.log(`✅ Success: ${HTML_OUTPUT} and ${XML_OUTPUT} updated.`);
}

generateSitemaps();
