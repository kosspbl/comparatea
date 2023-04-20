##--------------AMAZON--------------
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

def first_name(term):

    urlf = "https://www.amazon.in/s?k=" + str(term).replace(" ", "+")

    ########################## ----- Amazon Related ----- #########################

    try:
        rf = requests.get(urlf, headers = headers)
    except requests.exceptions.ConnectionError:
        return 0, "", 0, "", ""
    except:
        return 0, "", 0, "", ""

    #for amazon
    soupa = BeautifulSoup(rf.text, "html.parser")

    #amazon product data lists
    a_product_prices = []
    a_product_names = []
    a_product_links = []
    a_product_pics = []

    ####amazon PRODUCTS

    #for storing product names
    n1 = soupa.find_all("img", class_ = "s-image", alt = True)

    for i in n1:
        a = i['alt']
        a_product_names.append(a)

    #for storing prices

    p1 = soupa.find_all("span", class_ = "a-price-whole")

    for j in p1:
        a = str(j.text).replace(",","")
        a_product_prices.append(int(a.replace(".","")))

    #for storing product links
    l1 = soupa.find_all('a', class_ = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal", href = True)
    for k in l1:
        a = k['href']
        a_product_links.append(a)

    # for storing product pics
    pics1 = soupa.find_all("img", class_ = "s-image", src = True)

    for l in pics1:
        a = l['src']
        a_product_pics.append(a)



    ##Gettings rid of sponsored items
    sponsor_div = soupa.find_all("span", class_ = "a-price _bGlmZ_price_23Ix_")
    offset = len(sponsor_div)
    print(offset)
    a_product_links = a_product_links[5:14]
    a_product_prices = a_product_prices[(5 + offset):(14 + offset)]
    a_product_names = a_product_names[5:14]
    a_product_pics = a_product_pics[5:14]

    for i in range(len(a_product_prices)):
        print(a_product_prices[i], " ", a_product_names[i])

    #if lists are empty then exception case is raised
    if not a_product_pics or not a_product_links or not a_product_names or not a_product_prices:
        return 0, "", 0, "", ""

     ##-----Bubble sorting all 4 lists of amazon
    for m in range(len(a_product_prices)) :
        for n in range(len(a_product_prices) - 1 - m) :
            if (a_product_prices[n + 1] < a_product_prices[n]):
                a_product_prices[n], a_product_prices[n + 1] = a_product_prices[n + 1], a_product_prices[n]
                a_product_names[n], a_product_names[n + 1] = a_product_names[n + 1], a_product_names[n]
                a_product_links[n], a_product_links[n + 1] = a_product_links[n + 1], a_product_links[n]
                a_product_pics[n], a_product_pics[n + 1] = a_product_pics[n + 1], a_product_pics[n]


    return 1, str(a_product_names[0]), int(a_product_prices[0]), "https://amazon.in" + str(a_product_links[0]), str(a_product_pics[0])

