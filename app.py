from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('mail')
        response = make_response(redirect(url_for('hi', name=name)))
        response.set_cookie(name, mail)
        return response
    return render_template('upload.html')


@app.route('/hi/<name>', methods=['GET', 'POST'])
def hi(name):
    if request.method == 'POST':
        responce = make_response(redirect(url_for('form')))
        responce.set_cookie(name, '', 0)
        return responce
    return render_template('hi.html', name=name)



if __name__ == '__main__':
    app.run(debug=True)
