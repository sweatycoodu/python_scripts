# A simple script to shorten URLs from the shell, using the TinyURL API.

# Import the required modules for the script to function.

import urllib.request
import urllib.parse

# Function to declare the URL to be shortened, prompted to the user.


def get_url():
    url = input("Source URL: ")
    # Display an error message if the URL is invalid.
    if not url.startswith('http://') and not url.startswith('https://'):
        print("Invalid URL...")
        return get_url()
    return url

# Function to shorten the URL, using the TinyURL API.


def shorten_url(url):
    request_url = ('https://tinyurl.com/api-create.php?' +
                   urllib.parse.urlencode({'url': url}))
    with urllib.request.urlopen(request_url) as response:
        return response.read().decode('utf-8')

# Function to print the shortened URL to the user.


def print_short_url(short_url):
    print("Shortened URL: {}".format(short_url))

# Function to repeat the process, if the user wishes to shorten another URL.


def repeat():
    while True:
        again = input("Shorten another URL? (y/n): ")
        if again.lower() == 'y':
            return True
        elif again.lower() == 'n':
            return False
        else:
            print("Invalid input. Please try again.")

# Main function to run the script.


def shorten_go():
    while True:
        url = get_url()
        short_url = shorten_url(url)
        print_short_url(short_url)
        if not repeat():
            break

# Run the script.


if __name__ == '__main__':
    shorten_go()
