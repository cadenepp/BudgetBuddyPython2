from flask import Flask, render_template, request, flash, redirect, url_for, session
from BudgetManager import BudgetManager
from classes.ExpenseEntry import ExpenseEntry
from classes.IncomeEntry import IncomeEntry
from custom_filter import format_price

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.jinja_env.filters['format_price'] = format_price

agent = BudgetManager()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summary', methods=['GET', 'POST'])
def summary():

    if request.method == 'POST':

        income_entry = float(request.form.get('income', 0))
        expense_entry = float(request.form.get('expense', 0))
        description_i = request.form.get('descriptionI', "No description added")
        description_e = request.form.get('descriptionE', "No description added")

        if income_entry > 0:
            income_obj = IncomeEntry(income_entry, description_i)
            agent.add_income(income_obj)
            session['income'] = income_obj.get_amount()

        if expense_entry > 0:
            expense_obj = ExpenseEntry(expense_entry, description_e)
            agent.add_expense(expense_obj)
            session['expense'] = expense_obj.get_amount()

        session['agent_tot_inc'] = agent.get_total_income()
        session['agent_tot_exp'] = agent.get_total_expense()
        session['agent_net_tot'] = agent.get_net_total()


    incomes_list = agent.incomes
    expenses_list = agent.expenses

    return render_template('summary.html', incomes_list=incomes_list, expenses_list=expenses_list)


@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e)


if __name__ == '__main__':
    app.run(debug=True, port=8000)