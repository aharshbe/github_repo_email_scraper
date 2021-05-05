
import requests
from os import system

# GitHub API key
username = ""
key = ""
# repo to search
    # follow org/repo or user/repo syntax
    # example of org search: paritytech/polkadot
    # example of user search: gavofyork/scripts
search = "" 
repo = f"https://api.github.com/repos/{search}/contributors?q=contributions&order=desc"

# Class which does cool scraping functions
class Scraper:
    # initialize
    def __init__(self, key):
        self.key = key
    # create an auth request
    def auth_request(self, repo_url):
        response = requests.get(repo_url, auth=(username, key))
        return response
    def test_rate_limit(self):
        # testing
        if (len(self.auth_request("https://api.github.com").json())>2):
            print("You're good to continue")
            return 1
        else:
            return 0
    # obtain handels from repo response
    def obtain_handels(self, response):
        handels = []
        for key in response:
            # obtain contributor GitHub handles
            handel = key["login"]
            print(handel)
            # add handel to array of handels
            handels.append(handel)
        if len(handels) < 1:
            return 1
        else:
            return handels
    # test to be sure handels were scraped
    def check_handels(self, handels):
        # check for handels
        if len(handels) > 0:
            print("handel(s) found, continuing...")
        else:
            print("no handels found, exiting...")
            exit()
    def obtain_email(self, handel):
        request_email = f"https://api.github.com/users/{handel}/events/public"
        obtain_email_response = self.auth_request(request_email).json()
        for response in obtain_email_response:
            try:
                email = response["payload"]["commits"][0]["author"]["email"]
                print("found email for "+handel)
                return email
            except:
                system('cls')
                print("searching...")
# example:
    # new_request = Scraper(key)
    # print(new_request.auth_request('https://api.github.com'))

test = Scraper(key)
good = test.test_rate_limit()
if good != 1:
    rate_limit = test.auth_request("https://api.github.com/rate_limit").json()["rate"]["reset"]
    print(f"problem with your auth token or your rate limit was exceeded. If the problem is your rate limit, covert your epoch stamp ({rate_limit}) to your time zone to see when it will reset, use (https://www.epochconverter.com/).")
    exit()

# intantiate new scraper object
s = Scraper(key)

# make first request for repo
request_handles = s.auth_request(repo).json()
print("finished making request.")

if not request_handles:
    print(f"Contributor is owner of repo, use their handel: {search.split('/')[0]}.")
    handels = [search.split('/')[0]]
else:
    # obtain handels from request
    handels = s.obtain_handels(request_handles)
    print("finished scraping handels.")

# create array of handels from request
s.check_handels(handels)
print("At least one handel obtained. checking for email(s)...")

# create a dictoionary of handels and emails
email_handel_dict = {}
# iterate through handels array of repo to obtain emails
for handel in handels:
    # store email and handel in dictionary
    email_handel_dict[handel] = s.obtain_email(handel)
system('cls')
print(f"Here is a dictionary of handels and their emails for {len(email_handel_dict.keys())} contributors of {search}:")
print(email_handel_dict)

# EOF