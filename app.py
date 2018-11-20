from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


# QUERY STRINGS
@app.route('/new/')
def query_strings(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is : {0} </h1>'.format(query_val)


# REMOVE QUERY STRINGS
@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there ! {} </h1>'.format(name)

# STRINGS
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> here is a string: ' + name + '</h1>'


# NUMBERS
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: ' + str(num) + '</h1>'


# MORE NUMBERS
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1>the sum is : {}'.format(num1 + num2) + '</h1>'


# FLOATS
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is: {}'.format(num1 * num2) + '</h1>'


# USING TEMPLATES
@app.route('/temp')
def using_templates():
    return render_template('hello.html')


