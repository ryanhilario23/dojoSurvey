from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'ninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninjaninja'
    
@app.route('/')
def submit_form():
    return render_template('index.html')

@app.route('/results',methods = ['POST'])
def submitted_form():
    print(request.form)
    session['fullname'] = request.form['name']
    session['dojo'] = request.form['dojolocation']
    session['language'] = request.form['programlanguage']
    session['comments'] = request.form['comments']
    return render_template('results.html')



if __name__=="__main__":
    app.run(debug=True) 