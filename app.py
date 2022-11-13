from flask import Flask, url_for
from integral import Integral
appFlask = Flask(__name__)
@appFlask.route('/numericalintegralservice/')
@appFlask.route('/numericalintegralservice/<a>/<b>')
def finalIntegral(a = 0,b=3.14):
    m=Integral(1000,float(a),float(b))
    return str(m)

appFlask.run(debug=True, port=5000)