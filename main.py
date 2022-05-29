from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def Return():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def Answer():
    #Get Number1
    Number1 = request.form.get("Number1", type=int)
    # Get Number2
    Number2 = request.form.get("Number2", type=int)
    # Get Operation +,-,/,*
    operation = request.form.get("operation")
    # compare and do calculations
    # Addition
    if operation == '+': Answer = Number1 + Number2
    # Subtraction
    elif operation == '-': Answer = Number1 - Number2
    # Multiplication
    elif operation == '*': Answer = Number1 * Number2
    # Division
    elif operation == '/': Answer = Number1 / Number2
    # Error
    else: Answer = 'Error!'
    # Saving to a variable
    Value = Answer
    # Returning a page with values
    return render_template('form.html', Value=Value, num1=Number1, num2=Number2, op=operation)

if __name__ == '__main__':
    app.run(debug=True)
