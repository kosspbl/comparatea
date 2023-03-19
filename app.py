from flask import Flask, request, render_template #importing flask libraries

print("This is app.py")

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index_page():
    search_key = ""
    filename = ""
    link = ""
    pics = ""
    if request.method == "POST" :
        import myfile
        search_key = str(request.form.get("name"))
        search_key.replace(" ", "+")
        filename, link, pics = myfile.first_name(search_key)
    return render_template('index.html', result1 = "First Product :  " + str(filename), result2 = link, result3 = pics)

if __name__ == '__main__':
    app.run()
