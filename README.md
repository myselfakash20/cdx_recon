# cdx_recon
CDX Recon - Wayback Machine Recon Tool

CDX Recon is a powerful Python tool designed for bug bounty hunters and security researchers. It automates the process of retrieving archived URLs, JavaScript files, API endpoints, and subdomains from the Wayback Machine (CDX API), helping to uncover hidden attack surfaces efficiently.

🎯 Features

✅ Fetch archived URLs from Wayback Machine 📂✅ Extract JavaScript, JSON, PHP, XML files for sensitive data discovery 🔑✅ Find old web pages that may have unpatched vulnerabilities ⚠️✅ Retrieve data within specific years to track website changes 📅✅ Save results to a file for further analysis 💾✅ Error handling & retry mechanism to avoid rate limiting 🚀✅ Fast and efficient execution with optimized requests ⚡

📌 Installation

# Clone the repository
git clone https://github.com/myselfakash20/cdx_recon.git
cd cdx_recon

# Install dependencies
pip install -r requirements.txt

🚀 Usage

🔍 Fetch All Archived URLs

python3 cdx_recon.py -d example.com

🗂 Extract Specific File Types (JS, JSON, PHP, XML, TXT, PDF, ASPX, JSP, etc.)

python3 cdx_recon.py -d example.com -f js

🕵️‍♂️ Find Old Web Pages by Year

python3 cdx_recon.py -d example.com --from-year 2015 --to-year 2020

💾 Save Results to a File

python3 cdx_recon.py -d example.com -f php -o results.txt

🔥 Example Output

[+] Fetching archived URLs...
[+] Found URLs:
http://example.com/login.php
http://example.com/admin.js
http://example.com/api/v1/user.json

⚠️ Disclaimer

This tool is intended for educational and legal security testing purposes only. Misuse of this tool is strictly prohibited.

🤝 Contributing

Feel free to fork, improve, and create pull requests to enhance this tool!

📧 Developer: Akash (myselfakash20)
