
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
    # obtain handles from repo response
    def obtain_handles(self, response):
        handles = []
        for key in response:
            # obtain contributor GitHub handles
            handle = key["login"]
            print(handle)
            # add handle to array of handles
            handles.append(handle)
        if len(handles) < 1:
            return 1
        else:
            return handles
    # test to be sure handles were scraped
    def check_handles(self, handles):
        # check for handles
        if len(handles) > 0:
            print("handle(s) found, continuing...")
        else:
            print("no handles found, exiting...")
            exit()
    def obtain_email(self, handle):
        request_email = f"https://api.github.com/users/{handle}/events/public"
        obtain_email_response = self.auth_request(request_email).json()
        for response in obtain_email_response:
            try:
                email = response["payload"]["commits"][0]["author"]["email"]
                print("found email for "+handle)
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
    print(f"Contributor is owner of repo, use their handle: {search.split('/')[0]}.")
    handles = [search.split('/')[0]]
else:
    # obtain handles from request
    handles = s.obtain_handles(request_handles)
    print("finished scraping handles.")

# create array of handles from request
s.check_handles(handles)
print("At least one handle obtained. checking for email(s)...")

# create a dictoionary of handles and emails
email_handle_dict = {}
# iterate through handles array of repo to obtain emails
for handle in handles:
    # store email and handle in dictionary
    email_handle_dict[handle] = s.obtain_email(handle)
system('cls')
print(f"Here is a dictionary of handles and their emails for {len(email_handle_dict.keys())} contributors of {search}:")
print(email_handle_dict)

# EOF