from my_app import app
from my_app.main import main
from my_app.settings import app_cfg
from flask import render_template, url_for, request, jsonify


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        main()
        some_json = request.get_json()
        return jsonify({'about': 'POSTED Version 2.0'}), 202
    else:
        return jsonify({'about': 'GET Version 1.0'})
    r# eturn render_template('index.html')
