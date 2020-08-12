from bs4 import BeautifulSoup

def find_the_link(filepath):
    links = []
    with open(filepath) as f:
        text = f.read()
        bs =BeautifulSoup(text)
        for i in bs.find_all:
            links.append(i['body'])
    return links

if __name__ == '__main__':
    print find_the_link('helloworld.html')