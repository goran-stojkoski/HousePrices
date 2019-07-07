from flask import Flask, render_template, url_for, flash, redirect, request
from forms import QueryForm
from HousePriceGetter import HoursePriceGetter

application = app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


@app.route('/', methods=['GET', 'POST'])
def home():
    # blah = request.form['suburb']
    if request.method == "POST":
        suburb = request.form['suburb']
        state = request.form['state']
        proptype = request.form['proptype']
        minbed = request.form['minbed']
        maxbed = request.form['maxbed']
        if suburb == "Suburb":
            suburb = "Melbourne"
        if state == "State or Territory":
            state = "VIC"
        if proptype == "Property Type":
            proptype = ""
        if minbed == "Min Beds":
            suburb = ""
        if maxbed == "Max Beds":
            suburb = ""
        hp = HoursePriceGetter(suburb, state,proptype=proptype, minbed=minbed, maxbed=maxbed)
        return render_template('home.html',ppties=hp.ppty_list, suburb=suburb, state=state, minbed=minbed, maxbed=maxbed)
    return render_template('home.html')
# else:
#     return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
