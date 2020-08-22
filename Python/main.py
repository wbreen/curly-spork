from urllib.request import urlopen

# PBJ_pets_url="http://www.petfinder.com/search/pets-for-adoption/?shelter_id%5B0%5D=VA647&"
test_url="http://olympus.realpython.org/profiles/aphrodite"

def scrape(url):
    page = urlopen(url)
    html_bytes = page.read()
    html_out = html_bytes.decode("utf-8")
    print(html_out)


def main(url):
    scrape(url)

if __name__ == '__main__':
    main(test_url)