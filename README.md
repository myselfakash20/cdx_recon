# CDX Recon - Wayback Machine Recon Tool

**A fast and efficient tool for bug bounty hunters and security researchers**

🛠 About CDX Recon
CDX Recon is a powerful Python tool designed for bug bounty hunters and security researchers. It automates the retrieval of archived URLs, JavaScript files, API endpoints, and subdomains from the Wayback Machine (CDX API), helping you uncover hidden attack surfaces efficiently.

🎯 Features
✅ Retrieve Archived URLs from Wayback Machine 📂
✅ Extract JavaScript, JSON, PHP, XML files for sensitive data discovery 🔑
✅ Find old web pages that may have unpatched vulnerabilities ⚠️
✅ Fetch data from specific years to track website changes 📅
✅ Save results to a file for further analysis 💾
✅ Built-in Error Handling to avoid rate limiting 🚀
✅ Optimized Requests for fast and efficient execution ⚡

📌 Installation
Clone the repository and install dependencies:

bash
Copy code
# Clone the repository
`git clone https://github.com/myselfakash20/cdx_recon.git
cd cdx_recon `

# Install dependencies
pip install -r requirements.txt
🚀 Usage
🔍 Fetch All Archived URLs
bash
Copy code
python3 cdx_recon.py -d example.com
🗂 Extract Specific File Types (JS, JSON, PHP, XML, TXT, PDF, ASPX, JSP, etc.)
bash
Copy code
python3 cdx_recon.py -d example.com -f js
🕵️‍♂️ Find Old Web Pages by Year
bash
Copy code
python3 cdx_recon.py -d example.com --from-year 2015 --to-year 2020
💾 Save Results to a File
bash
Copy code
python3 cdx_recon.py -d example.com -f php -o results.txt
🔥 Example Output
less
Copy code
[+] Fetching archived URLs...
[+] Found URLs:
http://example.com/login.php
http://example.com/admin.js
http://example.com/api/v1/user.json
⚠️ Disclaimer
🚨 This tool is intended for educational and legal security testing purposes only.
🚨 Unauthorized use of this tool on systems without permission is strictly prohibited.

🤝 Contributing
💡 Feel free to fork, improve, and create pull requests to enhance this tool!

📧 Developer: Akash (@myselfakash20)

🎯 Happy Hunting & Stay Ethical! 🔥🚀
