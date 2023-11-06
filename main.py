from flask import Flask, render_template, request
import simple_request_01 as malm
import pprint

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')


@app.route("/index.html")
def results():
    return render_template('index.html')

@app.route('/index.html', methods=['POST'])
def run_post():
    query_s = request.form['query_string']
    print(f'query={query_s}')

    lm_data = malm.marketing_text(query_s)
    pprint.pprint(lm_data)
    lm_blog = lm_data
    return render_template('index.html', lm_blog = lm_data)

if __name__ == "__main__":
    app.run(debug=True)