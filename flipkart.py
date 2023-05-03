##---------------FLIPKART----------------

def flipkart_search(term):

    urlf = "https://www.flipkart.com/search?q=" + str(term) #url of flipkart search

    ########################## ----- Flipkart Related ----- #########################

    import requests
    from bs4 import BeautifulSoup
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    try:
        rf = requests.get(urlf, headers = headers)
    except requests.exceptions.ConnectionError:
        return 0, "", 0, "", ""
    except:
    #if str(rf) != "<Response [200]>":
        return 0, "", 0, "", ""

    #for flipkart
    soupf = BeautifulSoup(rf.text, "lxml")

    #flipkart product data lists
    f_product_prices = [] 
    f_product_names = []
    f_product_links = []
    f_product_pics = []

    ####FLIPKART PRODUCTS

    #Stores all flipkart product names related divs/a tags classes
    n1 = [soupf.find_all("div", class_ = "_2WkVRV"),
     soupf.find_all("a", class_ = "s1Q9rs"),
     soupf.find_all("div", class_ = "_4rR01T")]

    namesf = []

    for i in n1 :
        if i :
            namesf = i

    ####FLIPKART PRICES
    p1 = [soupf.find_all("div", class_ = "_30jeq3"),
          soupf.find_all("div", class_ = "_30jeq3 _1_WHN1")]
    pricesf = []

    for i in p1 :
        if i :
            pricesf = i


    ####FLIPKART PRODUCT LINKS
    l1 = [soupf.find_all("a", class_ = "_2rpwqI", href = True),
          soupf.find_all("a", class_ = "s1Q9rs", href = True),
          soupf.find_all("a", class_ = "IRpwTa", href = True),
          soupf.find_all("a", class_ = "_1fQZEK", href = True),
          soupf.find_all("a", class_ = "_8VNy32", href = True)]

    linksf = []

    for i in l1 :
        if i :
            linksf = i

    ####FLIPKART IMAGE LINKS
    pic1 = [soupf.find_all("img", class_ = "_396cs4", src = True),
            soupf.find_all("img", class_ = "_2r_T1I", src = True)]
    picsf = []
    for i in pic1 :
        if i :
            picsf = i


    ##----For assignment in all lists, flipkart related
    for i in namesf:
        a = i.text
        f_product_names.append(a)

    for j in pricesf:
        b = j.text
        f_product_prices.append(int(b[1:].replace(",", "")))

    for k in linksf:
        c = k['href']
        f_product_links.append(c)

    for l in picsf:
        d = l['src']
        f_product_pics.append(d)

    ##--- to get rid of extra product suggestions
    f_product_prices = f_product_prices[0 : 9]
    f_product_links = f_product_links[0 : 9]
    f_product_pics = f_product_pics[0 : 9]
    f_product_names = f_product_names[0 : 9]


    #if lists are empty then exception case is raised
    if not f_product_pics or not f_product_links or not f_product_names or not f_product_prices:
        return 0, "", 0, "", ""


    ##-----Bubble sorting all 4 lists of flipkart
    for m in range(len(f_product_prices)) :
        for n in range(len(f_product_prices) - 1 - m) :
            if (f_product_prices[n + 1] < f_product_prices[n]):
                f_product_prices[n], f_product_prices[n + 1] = f_product_prices[n + 1], f_product_prices[n]
                f_product_names[n], f_product_names[n + 1] = f_product_names[n + 1], f_product_names[n]
                f_product_links[n], f_product_links[n + 1] = f_product_links[n + 1], f_product_links[n]
                f_product_pics[n], f_product_pics[n + 1] = f_product_pics[n + 1], f_product_pics[n]

    return 1, str(f_product_names[0]), int(f_product_prices[0]), str("https://www.flipkart.com" + str(f_product_links[0])), str(f_product_pics[0])
