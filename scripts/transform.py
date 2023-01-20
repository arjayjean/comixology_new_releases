import extract as e


new_releases = []

def find_data(tag, attr):
    return e.soup.find_all(tag, class_=attr)

def find_text(text):
    return str(text.get_text()).strip()

def find_author(name):
    return name.replace('by', '').replace(',', ' ,').split(',')[0].replace('\n', '').lstrip().rstrip()

titles = [find_text(title) for title in find_data('span', 'csw-title-text')]

images = [image['src'] for image in find_data('img', 'csw-item-art')]

authors = [find_author(find_text(author)) for author in find_data('div', 'a-row csw-sub-title-row')]


prices = []
currency = [find_text(cu) for cu in find_data('span', 'csw-item-price-currency')]
dollars = [find_text(d) for d in find_data('span', 'csw-item-price-dollars')]
cents = [find_text(ct) for ct in find_data('span', 'csw-item-price-cents')]

def get_prices(cur, dol, cnt):
    for i in range(len(cur)):
        prices.append(f'{cur[i]}{dol[i]}.{cnt[i]}')


get_prices(currency, dollars, cents)


def get_new_releases(titl, aut, img, pri):
    for i in range(len(titl)):
        new_releases.append([titl[i], aut[i], img[i], pri[i]])



get_new_releases(titles, authors, images, prices)

# print(new_releases[0])