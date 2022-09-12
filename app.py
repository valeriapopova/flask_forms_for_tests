from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from flask import Flask, render_template, request, Response, redirect, jsonify
from werkzeug.exceptions import BadRequestKeyError

from config import Configuration
from forms import RequestForm, MethodForm, RequestGetForm

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/method', methods=['POST', 'GET'])
def get_method():
    form = MethodForm()
    if request.method == 'POST':
        try:
            method = request.form['method']
            if method == 'GET':
                return redirect('/method/get')
            else:
                return redirect('/method/post')
        except BadRequestKeyError:
            return Response("Пустое значение", 400)

    return render_template('forms.html', form=form), 200


@app.route('/method/get', methods=['POST', 'GET'])
def get_request():
    form = RequestGetForm()
    if request.method == 'POST':
        try:
            apiendpoint = request.form['ApiEndpoint']
            loop_count = request.form['Loop count']
            number_of_threads = request.form['Number of threads']
            start_time = datetime.now()
            urls = [apiendpoint] * int(number_of_threads)

            def fetch(url):
                try:
                    response = requests.get(url, stream=True)
                    return [response.status_code, response.json()]
                except requests.exceptions.RequestException as e:
                    return e

            def some_func():
                threads = []
                with ThreadPoolExecutor(max_workers=20) as executor:
                    for url in urls:
                        for i in range(int(loop_count)):
                            threads.append(executor.submit(fetch, url))
                    for task in as_completed(threads):
                        print(task.result())
                time_ = datetime.now() - start_time
                return time_

            r = some_func()
            return r

        except BadRequestKeyError:
            return Response("Пустое значение", 400)
    return render_template('forms_get.html', form=form), 200


@app.route('/method/post', methods=['POST', 'GET'])
def post_request():
    form = RequestForm()
    if request.method == 'POST':
        try:
            apiendpoint = request.form['ApiEndpoint']
            loop_count = request.form['Loop count']
            number_of_threads = request.form['Number of threads']
            master_product_id = request.form['master_product_id']
            links = request.form['Links']
            start_time = datetime.now()
            urls = [apiendpoint] * int(number_of_threads)
            data = [
                {
                    "master_product_id": master_product_id,
                    "links": [
                        links
                    ]
                }]

            def fetch(url):
                try:
                    response = requests.post(url, json=data, stream=True)
                    return [response.status_code, response.json()]
                except requests.exceptions.RequestException as e:
                    return e

            def some_func():
                threads = []
                with ThreadPoolExecutor(max_workers=20) as executor:
                    for url in urls:
                        for i in range(int(loop_count)):
                            threads.append(executor.submit(fetch, url))
                    for task in as_completed(threads):
                        print(task.result())
                time_ = datetime.now() - start_time
                return time_
            r = some_func()
            return r

        except BadRequestKeyError:
            return Response("Пустое значение", 400)

    return render_template('forms_post.html', form=form), 200