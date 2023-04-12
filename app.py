from flask import Flask, request, render_template #importing flask libraries
import flipkart
import amazon


print("This is app.py")

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
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
        return render_template("index.html")


    if request.method == "POST" :
        search_key = str(request.form.get("name"))
        search_key.replace(" ", "+")
        fflag, fProductName, fPrice, fLink, fPics = flipkart.first_name(search_key)
        aflag, aProductName, aPrice, aLink, aPics = amazon.first_name(search_key)

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
                fwin = "Winner"
            else:
                awin = "Winner"
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

if __name__ == '__main__':
    app.run()
