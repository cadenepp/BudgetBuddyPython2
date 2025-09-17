from flask import Flask, render_template, request, flash, redirect, url_for

from Homework.BudgetBuddyPython2.BudgetManager import BudgetManager

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/income', methods=['POST'])
def calcs():
    budget = BudgetManager()

    new_expense = float(request.form['expense'])
    new_income = float(request.form['income'])

    if new_expense > 0:
        expense = ExpenseEntry(
    if new_income > 0:




    return redirect('summary.html', )



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e)



if __name__ == '__main__':
    app.run(debug=True)