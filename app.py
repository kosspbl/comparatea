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

    #for amazon
    aProductName = ""
    aLink = ""
    aPics = ""
    aPrice = ""
    
    #for declaring winnner
    fwin = ""
    awin = ""


    if request.method == "POST" :
        search_key = str(request.form.get("name"))
        search_key.replace(" ", "+")
        fProductName, fPrice, fLink, fPics = flipkart.first_name(search_key)
        aProductName, aPrice, aLink, aPics = amazon.first_name(search_key)

        if fPrice <= aPrice:
            fwin = "Winner"
        else:
            awin = "Winner"
    return render_template('index.html',
                           result01 = fwin, result02 = awin,
                           result1 = "Cheapest on Flipkart : " + str(fProductName),
                           result2 = fLink, result3 = fPics,
                           result4 = "Cheapest on Amazon : " + str(aProductName),
                           result5 = aLink, result6 = aPics,
                           resultp1 = fPrice, resultp2 = aPrice)

if __name__ == '__main__':
    app.run()
