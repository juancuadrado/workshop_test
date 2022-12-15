from flask import Flask, render_template
#import resquests
app = Flask(__name__)


#def index():
#    return "<h1> Hello World!</h1>"

@app.route('/')
def index():
    return render_template("index.html")

#def Images():
#    data = requests.list_images()
#    print(data)
#    return data
#@app.route('/user/<name>')
#def user(name):
#    return "<h1> Hello {}!!!</h1>".format(name)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
    