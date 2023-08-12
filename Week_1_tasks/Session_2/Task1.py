import webbrowser

def Open_Site(Site):
    for site_url in Site:
        chrome_browser.open(site_url)
    return 1

url_list = [
    "https://www.facebook.com/",
    "https://www.python.org/",
    "https://www.softprayog.in/tutorials/top-command-in-linux",
    "https://docs.python.org/3/library/webbrowser.html"
]


# r : raw string literal
#A raw string literal treats backslashes (\) as literal characters and doesn't interpret them as escape characters.

chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

chrome_browser = webbrowser.get('chrome')

status = Open_Site(url_list)

if status == 1:
    print("Sites opened successfully")
else:
    print("Sites not opened")
