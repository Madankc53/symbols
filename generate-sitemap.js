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

function generateSitemaps() {
    const files = getHtmlFiles(__dirname);
    const currentDate = new Date().toISOString().split('T')[0]; // Format: YYYY-MM-DD
    
    // --- 1. GENERATE HTML SITEMAP ---
    let htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sitemap</title>
    <style>
        body { font-family: sans-serif; margin: 40px; line-height: 1.6; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        a { color: #0366d6; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Sitemap</h1>
    <ul>\n`;

    // --- 2. GENERATE XML SITEMAP ---
    let xmlContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

    // Loop through files and populate both string buffers
    files.forEach(file => {
        const urlPath = file === 'index.html' ? '' : file;
        const fullUrl = `${BASE_URL}${urlPath}`;
        const label = file.replace('.html', '').replace(/[-_]/g, ' ') || 'Home';
        
        // Append to HTML
        htmlContent += `        <li><a href="${fullUrl}">${label}</a></li>\n`;
        
        // Append to XML
        xmlContent += `  <url>\n    <loc>${fullUrl}</loc>\n    <lastmod>${currentDate}</lastmod>\n    <priority>${file === 'index.html' ? '1.0' : '0.8'}</priority>\n  </url>\n`;
    });

    // Close formats
    htmlContent += `    </ul>\n</body>\n</html>`;
    xmlContent += `</urlset>`;

    // Write both files to disk
    fs.writeFileSync(path.join(__dirname, HTML_OUTPUT), htmlContent);
    fs.writeFileSync(path.join(__dirname, XML_OUTPUT), xmlContent);
    
    console.log(`✅ Success: ${HTML_OUTPUT} and ${XML_OUTPUT} updated with ${files.length} links.`);
}

generateSitemaps();
