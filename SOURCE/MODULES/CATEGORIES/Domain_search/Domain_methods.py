# Imports
import json
import os
import re
import socket
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, quote, urljoin, urlparse
from urllib.request import Request, urlopen

# Clear the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()

DOMAINSEARCHER = r"""
 ██████████                                       ███                         █████████                                        █████     
░░███░░░░███                                     ░░░                         ███░░░░░███                                      ░░███      
 ░███   ░░███  ██████  █████████████    ██████   ████  ████████             ░███    ░░░   ██████   ██████   ████████   ██████  ░███████  
 ░███    ░███ ███░░███░░███░░███░░███  ░░░░░███ ░░███ ░░███░░███  ██████████░░█████████  ███░░███ ░░░░░███ ░░███░░███ ███░░███ ░███░░███ 
 ░███    ░███░███ ░███ ░███ ░███ ░███   ███████  ░███  ░███ ░███ ░░░░░░░░░░  ░░░░░░░░███░███████   ███████  ░███ ░░░ ░███ ░░░  ░███ ░███ 
 ░███    ███ ░███ ░███ ░███ ░███ ░███  ███░░███  ░███  ░███ ░███             ███    ░███░███░░░   ███░░███  ░███     ░███  ███ ░███ ░███ 
 ██████████  ░░██████  █████░███ █████░░████████ █████ ████ █████           ░░█████████ ░░██████ ░░████████ █████    ░░██████  ████ █████
░░░░░░░░░░    ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░░ ░░░░░             ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░      ░░░░░░  ░░░░ ░░░░

    [01] - Host Discovery
    [02] - URL checker
    [03] - Subdomain enumeration
"""


# Starts the main menu again when the user enters q.
def return_to_main_menu():
    main_menu = Path(__file__).resolve().parents[3] / "main_men.py"
    subprocess.run([sys.executable, str(main_menu)], check=False)


# Finds the available addresses for a hostname or IP address.
def host_discovery():
    """Resolve a hostname or IP address and display its discovered hosts."""
    while True:
        # Ask for a target or exit the function with q.
        target = input("\nTarget hostname or IP (q to return): ").strip()
        if target.lower() == "q":
            return_to_main_menu()
            return
        if not target:
            print("Please enter a hostname or IP address.")
            continue

        try:
            # Resolve IPv4 and IPv6 addresses through DNS.
            address_info = socket.getaddrinfo(target, None)
        except socket.gaierror:
            print(f"Could not resolve: {target}")
            continue

        addresses = sorted({entry[4][0] for entry in address_info})
        print(f"\nHost: {target}")
        print("Addresses:")
        for address in addresses:
            print(f"  - {address}")

        try:
            # Try to resolve the discovered host in reverse.
            reverse_name = socket.gethostbyaddr(addresses[0])[0]
        except (socket.herror, socket.gaierror, IndexError):
            reverse_name = None

        if reverse_name:
            print(f"Reverse DNS: {reverse_name}")
        return


# Queries certificate transparency data for names related to a domain.
def query_certificate_names(domain):
    # Encode the domain before placing it into the API request.
    endpoint = f"https://crt.name/v1/search?apex={quote(domain)}"
    request = Request(
        endpoint,
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (ShadXAlf subdomain checker)",
        },
    )

    # Download and decode the JSON response with a short timeout.
    with urlopen(request, timeout=10) as response:
        response_body = response.read().decode("utf-8-sig").strip()
        if not response_body:
            return []
        data = json.loads(response_body)

    # Accept common response shapes used by certificate APIs.
    records = data if isinstance(data, list) else data.get("results", data.get("data", []))
    names = set()
    for record in records:
        if isinstance(record, str):
            values = [record]
        elif isinstance(record, dict):
            values = [
                record.get("name", ""),
                record.get("domain", ""),
                record.get("common_name", ""),
                record.get("name_value", ""),
                record.get("sub", ""),
            ]
        else:
            values = []

        # Certificate names can contain several newline-separated entries.
        for value in values:
            for name in str(value).splitlines():
                clean_name = name.strip().lower().lstrip("*.").rstrip(".")
                if clean_name == domain or clean_name.endswith(f".{domain}"):
                    names.add(clean_name)

    return sorted(names)


# Interactively lists passive subdomain findings from certificate records.
def subdomain_enumeration():
    while True:
        # Ask for an apex domain or return to the main menu.
        raw_domain = input("\nApex domain (q to return): ").strip()
        if raw_domain.lower() == "q":
            return_to_main_menu()
            return

        # Remove an optional protocol and path from the user input.
        domain = urlparse(raw_domain if "://" in raw_domain else f"//{raw_domain}").hostname
        if not domain or "." not in domain:
            print("Please enter a valid domain, for example example.com.")
            continue

        domain = domain.lower().rstrip(".")
        try:
            subdomains = query_certificate_names(domain)
        except (HTTPError, URLError, TimeoutError, ValueError, json.JSONDecodeError) as error:
            print(f"Could not query certificate data: {error}")
            continue

        print(f"\nFound {len(subdomains)} certificate names for {domain}:")
        if subdomains:
            for subdomain in subdomains:
                print(f"  - {subdomain}")
        else:
            print("No matching names were found.")
        return


# Collects safe HTML details without executing page scripts.
class PageScanner(HTMLParser):
    # Store the page information that we want to inspect.
    def __init__(self):
        super().__init__()
        self.title = ""
        self.forms = []
        self.password_fields = 0
        self._inside_title = False

    def handle_starttag(self, tag, attrs):
        # Read titles, forms, and password fields from opening HTML tags.
        attributes = dict(attrs)
        if tag.lower() == "title":
            self._inside_title = True
        elif tag.lower() == "form":
            self.forms.append(attributes.get("action", ""))
        elif tag.lower() == "input" and attributes.get("type", "").lower() == "password":
            self.password_fields += 1

    def handle_endtag(self, tag):
        # Stop collecting text when the title tag ends.
        if tag.lower() == "title":
            self._inside_title = False

    def handle_data(self, data):
        # Save visible text found inside the page title.
        if self._inside_title:
            self.title += data.strip()


# Downloads a limited amount of HTML for defensive analysis.
def fetch_page(url):
    # Download only a small part of the page with a short timeout.
    request = Request(
        url,
        headers={"User-Agent": "ShadXAlf-URL-Checker/1.0"},
    )
    with urlopen(request, timeout=8) as response:
        content_type = response.headers.get_content_type()
        body = response.read(512_000)
        return response.geturl(), response.status, content_type, body


# Checks a URL and its HTML for common phishing indicators.
def url_checker():
    # Ask for a URL and check it for common phishing warning signs.
    while True:
        # Let the user enter a URL or return to the main menu.
        raw_url = input("\nURL to check (q to return): ").strip()
        if raw_url.lower() == "q":
            return_to_main_menu()
            return
        if not raw_url:
            print("Please enter a URL.")
            continue

        # Add HTTPS when the user did not enter a protocol.
        url = raw_url if urlparse(raw_url).scheme else f"https://{raw_url}"
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            print("Invalid HTTP or HTTPS URL.")
            continue

        # Collect warnings instead of declaring a URL safe or unsafe too early.
        warnings = []
        hostname = parsed.hostname.lower()

        # Check the URL itself for suspicious patterns.
        if parsed.scheme != "https":
            warnings.append("The URL does not use HTTPS.")
        if parsed.username or parsed.password or "@" in parsed.netloc:
            warnings.append("The URL contains user-info before the host.")
        if hostname.startswith("xn--") or ".xn--" in hostname:
            warnings.append("The hostname uses punycode, which can hide look-alike characters.")
        if re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", hostname):
            warnings.append("The URL uses an IP address instead of a domain name.")
        if len(url) > 180:
            warnings.append("The URL is unusually long.")
        if len(parse_qs(parsed.query)) >= 6:
            warnings.append("The URL contains many query parameters.")

        # Download the page so its redirect and HTML content can be checked.
        try:
            final_url, status, content_type, body = fetch_page(url)
        except (HTTPError, URLError, TimeoutError, ValueError) as error:
            print(f"Could not fetch the URL: {error}")
            continue

        # Report when the page redirects to a different hostname.
        final_host = urlparse(final_url).hostname
        if final_host and final_host.lower() != hostname:
            warnings.append(f"The URL redirects to another host: {final_host}")

        # Inspect HTML forms, password fields, title text, and urgent wording.
        scanner = PageScanner()
        if "html" in content_type:
            scanner.feed(body.decode("utf-8", errors="replace"))
            page_text = body.decode("utf-8", errors="replace").lower()
            if scanner.password_fields:
                warnings.append("The page contains a password field.")
            if scanner.forms:
                external_forms = [
                    urljoin(final_url, action)
                    for action in scanner.forms
                    if action and urlparse(urljoin(final_url, action)).hostname != final_host
                ]
                if external_forms:
                    warnings.append("A form submits to another host.")
            if any(keyword in page_text for keyword in ("verify your account", "reset your password", "urgent action")):
                warnings.append("The page contains urgent account-related wording.")

        # Show the collected facts and the final assessment.
        print(f"\nFinal URL: {final_url}")
        print(f"HTTP status: {status}")
        print(f"Page title: {scanner.title or 'Not available'}")
        if warnings:
            print("\nWarnings:")
            for warning in sorted(set(warnings)):
                print(f"  - {warning}")
            print("\nAssessment: suspicious indicators found. Do not enter credentials.")
        else:
            print("\nAssessment: no basic phishing indicators found; this is not a safety guarantee.")
        return

# Color settings
CYAN = '\033[96m'

# Displays the domain menu and processes the user's selection.
def main():
    print(f"{CYAN}{DOMAINSEARCHER}{CYAN}")
    choice = input("Select an option: ").strip()

    if choice in {"1", "01"}:
        host_discovery()
    elif choice in {"2", "02"}:
        url_checker()
    elif choice in {"3", "03"}:
        subdomain_enumeration()
    elif choice.lower() == "q":
        return_to_main_menu()
        return
    else:
        print("This option is not implemented yet.")


if __name__ == "__main__":
    main()