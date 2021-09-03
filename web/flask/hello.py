from flask import Flask,request

app =Flask(__name__)

@app.route("/")
def index():
    return '<div>Hello word</div>'

@app.route("/hello/<name>")
def hello(name):
    return "name is :{0}".format(name)
    
@app.route("/hello/<name>/<age>")
def hellogae(name,age):
    return "name is :{0}，age is {1}".format(name,age)

@app.route("/hello/<int:post_id>")
def hellopost(post_id):
    return "post_if is :{0}".format(post_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    print("--------login----------")
    return "---------login-----------"

def show_the_login_form():
    print("------------show----------")
    return "-------------"

if __name__=='__main__':
    app.run()