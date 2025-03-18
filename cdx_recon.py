import requests
import argparse
import re
import sys
import time
import threading
from urllib.parse import urlparse
from pyfiglet import figlet_format

def print_banner():
    banner = figlet_format("cdx_recon")
    print(banner)
    print("By Akash - Advanced CDX Recon Tool\n")

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def validate_domain(domain):
    domain = domain.strip().lower()
    domain = domain.replace("http://", "").replace("https://", "").split("/")[0]
    return domain

def fetch_cdx_data(target, file_type=None, from_year=None, to_year=None, retries=3):
    base_url = "https://web.archive.org/cdx/search/cdx"
    params = {
        "url": f"*.{target}/*",
        "output": "json",
        "fl": "original",
        "collapse": "urlkey"
    }
    headers = {"User-Agent": "Mozilla/5.0 (compatible; cdx_recon/1.0; +https://github.com/akash/cdx_recon)"}
    
    if from_year and to_year:
        params["from"] = f"{from_year}0101"
        params["to"] = f"{to_year}1231"
    
    for attempt in range(retries):
        try:
            response = requests.get(base_url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            
            if response.text.strip():
                try:
                    data = response.json()
                    urls = [entry[0] for entry in data[1:]] if len(data) > 1 else []
                    
                    # If filtering by file type, ensure proper filtering
                    if file_type:
                        urls = [url for url in urls if re.search(f"\\.{file_type}($|\\?)", url)]
                    
                    return urls
                except requests.exceptions.JSONDecodeError:
                    print("[-] Error: Received an invalid JSON response from the API.")
            else:
                print("[-] No data found in Wayback Machine for this domain.")
        except requests.exceptions.RequestException as e:
            wait_time = 2 ** attempt  # Exponential backoff
            print(f"[-] Attempt {attempt + 1}/{retries} - Error fetching data: {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
    
    print("[-] Max retries exceeded. Skipping...")
    return []

def extract_subdomains(urls, target):
    subdomains = set()
    for url in urls:
        parsed_url = urlparse(url)
        domain_parts = parsed_url.netloc.split(".")
        if len(domain_parts) > 2 and parsed_url.netloc.endswith(target):
            subdomains.add(parsed_url.netloc)
    return subdomains

def save_results(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(item + "\n")
    print(f"[+] Results saved to {filename}")

def main():
    print_banner()
    if not check_internet():
        print("[-] No internet connection. Please check your network and try again.")
        sys.exit(1)
    
    parser = argparse.ArgumentParser(description="CDX API Recon Automation Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("-f", "--filetype", help="Filter by file type (e.g., js, json, php, xml, txt, pdf, aspx, jsp)")
    parser.add_argument("-s", "--subdomains", action="store_true", help="Extract subdomains")
    parser.add_argument("-o", "--output", help="Save results to a file")
    parser.add_argument("--from-year", help="Start year for fetching archived data (YYYY)")
    parser.add_argument("--to-year", help="End year for fetching archived data (YYYY)")
    args = parser.parse_args()
    
    target = validate_domain(args.domain)
    
    print("[+] Fetching archived URLs...")
    urls = fetch_cdx_data(target, args.filetype, args.from_year, args.to_year)
    
    if urls:
        print("[+] Found URLs:")
        for url in urls:
            print(url)
    else:
        print("[-] No URLs found.")
    
    if args.subdomains:
        print("\n[+] Extracting subdomains...")
        subdomains = extract_subdomains(urls, target)
        
        if subdomains:
            for sub in subdomains:
                print(sub)
        else:
            print("[-] No subdomains found.")
    
    if args.output:
        save_results(args.output, urls + list(subdomains) if args.subdomains else urls)
    
if __name__ == "__main__":
    main()
