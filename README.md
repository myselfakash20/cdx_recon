# CDX Recon - Wayback Machine Recon Tool

**A fast and efficient tool for bug bounty hunters and security researchers**

🛠 About CDX Recon
CDX Recon is a powerful Python tool designed for bug bounty hunters and security researchers. It automates the retrieval of archived URLs, JavaScript files, API endpoints, and subdomains from the Wayback Machine (CDX API), helping you uncover hidden attack surfaces efficiently.

**🎯 Features** <br>

✅ Retrieve Archived URLs from Wayback Machine 📂<br>
✅ Extract JavaScript, JSON, PHP, XML files for sensitive data discovery 🔑<br>
✅ Find old web pages that may have unpatched vulnerabilities ⚠️<br>
✅ Fetch data from specific years to track website changes 📅<br>
✅ Save results to a file for further analysis 💾<br>
✅ Built-in Error Handling to avoid rate limiting 🚀<br>
✅ Optimized Requests for fast and efficient execution ⚡<br>

**📌 Installation**<br>

*Clone the repository and install dependencies:*

# Clone the repository
```
git clone https://github.com/myselfakash20/cdx_recon.git 
cd cdx_recon
```
# Install dependencies
`pip install -r requirements.txt` <br>

_**🚀 Usage**_

*💡Need help!:*

`python3 cdx_recon -h`<br>

![alt Text](https://raw.githubusercontent.com/myselfakash20/cdx_recon/refs/heads/main/image2.jpg)

*🔍 Fetch All Archived URLs:*

`python3 cdx_recon.py -d example.com`<br>

🗂 Extract Specific File Types (JS, JSON, PHP, XML, TXT, PDF, ASPX, JSP, etc.) <br>
`python3 cdx_recon.py -d example.com -f js`<br>

🕵️‍♂️ Find Old Web Pages by Year<br>
`python3 cdx_recon.py -d example.com --from-year 2015 --to-year 2020`<br>

💾 Save Results to a File<br>
`python3 cdx_recon.py -d example.com -f php -o results.txt`<br>

*🔥 Example Output*

![alt Text](https://raw.githubusercontent.com/myselfakash20/cdx_recon/refs/heads/main/image.jpg)

⚠️ Disclaimer<br>
**🚨 This tool is intended for educational and legal security testing purposes only.** <br>
**🚨 Unauthorized use of this tool on systems without permission is strictly prohibited.** <br>

**🤝 Contributing**<br>
*💡 Feel free to fork, improve, and create pull requests to enhance this tool!* <br>

📧 Developer: Akash (@myselfakash20)

**🎯 Happy Hunting & Stay Ethical! 🔥🚀**
