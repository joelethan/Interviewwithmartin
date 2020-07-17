from flask import Flask, request, jsonify, render_template
# from flask_mail import Mail, Message

app = Flask(__name__)
# mail = Mail(app)

storage = ['maize', 'rice']
adminEmail = 'joelethan2@gmail.com'


@app.route('/',methods=['GET', 'POST'])
def Items():
    item = request.form.get('itemName')
    if item:
        storage.append(item)
    return render_template('front.html', items=storage)

if __name__ == "__main__":
    app.run(debug=True)
