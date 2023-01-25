## Web Scraper Project ##

This script is used to extract external references from a single provided URL 
using the BeautifulSoup library.

## Dependencies ##

This script requires the following dependencies to be installed beforehand:

* Python3
* Pip3
* Requests library
* Beautifulsoup4 library
* Urllib3 Library

You can install the required dependencies by manually entering the following commands into your terminal:

sudo apt update

sudo apt install python3

sudo apt install python3-pip

pip3 install requests beautifulsoup4 urllib3

Alternatively, you can use the supplied Bash script to install these dependencies by opening a terminal, navigating to the directory
where the script is located, and running the following commands:

sudo chmod +x webscraper_dependencies.sh

./webscraper_dependencies.sh

## Usage ##

To run the webscraper script, open a terminal, navigate to the directory where the script is located, and run the following command:

python3 webscraper.py [URL]

Replace '[URL]' with the URL of the webpage you want to extract external references from. 

For example, to extract external references from https://www.rit.edu, you would run the following command:

python3 webscraper.py https://www.rit.edu

The script will output a list of all unique external references found on the page, along with a count of the number of unique references.

## Note ##

This script only prints external references that are of the 'http' and 'https' protocol, do not include any other protocol.

This script will not run unless you specify either 'https://www.' or 'http://www.'

## Author ##

Mike Turkowski

Github: https://github.com/miketurkowski
