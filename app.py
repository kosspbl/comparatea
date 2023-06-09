from flask import Flask, request, render_template #importing flask libraries
from flipkart import flipkart_search
from amazon import amazon_search


print("This is app.py")

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
@app.route('/home', methods = ["GET", "POST"])
def index_page():
    search_key = ""

    #for flipkart
    fProductName = ""
    fLink = ""
    fPics = ""
    fPrice = ""
    fflag = None

    #for amazon
    aProductName = ""
    aLink = ""
    aPics = ""
    aPrice = ""
    aflag = None

    #for declaring winnner
    fwin = ""
    awin = ""

    if request.method == "GET" :
        aLink = "/error"
        fLink = "/error"
        return render_template("index.html",
                               result2 = fLink, result5 = aLink)


    if request.method == "POST" :
        search_key = str(request.form.get("name"))
        search_key.replace(" ", "+")
        fflag, fProductName, fPrice, fLink, fPics = flipkart_search(search_key)
        aflag, aProductName, aPrice, aLink, aPics = amazon_search(search_key)

        if fflag == 0 or aflag == 0:
            return render_template("error.html")
           # fwin = "Error : Flipkart/Amazon refused to connect"
           # awin = "Error : Flipkart/Amazon refused to connect"
           # fProductName, aProductName = "", ""
           # fPrice, aPrice = "", ""
           # aLink, fLink = "/error", "/error"
           # fPics, aPics = "", ""
        else:
            if fPrice <= aPrice:
                fwin = "Winner: "
            else:
                awin = "Winner: "
    return render_template('index.html',
                           result01 = fwin, result02 = awin,
                           result1 = str(fProductName),
                           result2 = fLink, result3 = fPics,
                           result4 = str(aProductName),
                           result5 = aLink, result6 = aPics,
                           resultp1 = "₹" + str(fPrice), resultp2 = "₹" + str(aPrice))

#error page
@app.route('/error', methods = ["GET", "POST"])
def error():
    return render_template("error.html")

#about page
@app.route('/about', methods = ["GET"])
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
