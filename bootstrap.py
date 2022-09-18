from flask import Flask, render_template

app = Flask(__name__)

#cleanned files name
@app.route('/')
def bootstrap():
    return render_template('hp.html')

@app.route('/patient')
def template():
    return render_template('bt2.html') 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)