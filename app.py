import os
from flask import Flask, render_template, request
import stripe

# SECRET_KEY = "sk_test_AwJVJOGHQEbQujjfL5NRQqGg"
# PUBLISHABLE_KEY = "pk_test_2iglUrpb6YKX2uzV46WLoBnM"

# stripe_keys = {
#   'secret_key': os.environ['SECRET_KEY'],
#   'publishable_key': os.environ['PUBLISHABLE_KEY']
# }

stripe_keys = {
  'secret_key': 'sk_test_AwJVJOGHQEbQujjfL5NRQqGg',
  'publishable_key': 'pk_test_2iglUrpb6YKX2uzV46WLoBnM'
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__, template_folder='templates')
app.debug = True

@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = int(float(request.form['amount']) * 100)
    print(amount)
    token = request.form['stripeToken']

    # customer = stripe.Customer.create(
    #     email='customer@example.com',
    #     source=token
    # )

    print(amount)
    charge = stripe.Charge.create(
        # customer=customer.id,
        amount=amount,
        currency='usd',
        description='SAII Charge',
        source=token
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    app.run(debug=True)
