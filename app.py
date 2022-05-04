from flask import Flask, request, render_template
import requests
from config import employee_service_host, employee_url, employee_time_sheet_service_host, employee_time_sheet_url
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/create_employee', methods=['POST'])
def add_employee():
    name = request.form.get('name')
    email = request.form.get('email')
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    payload = {'name': name, 'email': email}

    url = employee_service_host + employee_url
    headers = {'content-type':'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    _json = response.json()
    #print("response==", response.json())
    return render_template('index.html')


@app.route('/get_employee', methods=['GET'])
def get_employee():
    employee_id = request.args.get('employee_id')
    # the code below is executed if the request method
    # was GET or the credentials were invalid

    url = employee_service_host + employee_url + str(employee_id)
    headers = {'content-type':'application/json'}
    response = requests.get(url, headers=headers)
    _json = response.json()
    #print("response==", response.json())
    return render_template('index.html', employee_record=_json)

@app.route('/list_employee', methods=['GET'])
def list_employee():
    offset = request.args.get('offset')
    limit = request.args.get('limit')
    # the code below is executed if the request method
    # was GET or the credentials were invalid

    url = employee_service_host + employee_url + '?offset='+str(offset) + '&limit='+str(limit)
    headers = {'content-type':'application/json'}
    response = requests.get(url, headers=headers)
    _json = response.json()
    #print("response==", response.json())
    return render_template('index.html', employee_list=_json)

@app.route('/create_employee_time_sheet', methods=['POST'])
def add_employee_time_sheet():
    employee_id = request.form.get('employee_id')
    log_date = request.form.get('log_date')
    hrs = request.form.get('hrs')
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    payload = {'employee_id': employee_id, 'log_date': log_date, 'hrs': hrs}

    url = employee_time_sheet_service_host + employee_time_sheet_url
    headers = {'content-type':'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    _json = response.json()
    #print("response==", response.json())
    return render_template('index.html')


@app.route('/get_employee_time_sheet', methods=['GET'])
def get_employee_time_sheet():
    employee_time_sheet_id  = request.args.get('employee_time_sheet_id')
    # the code below is executed if the request method
    # was GET or the credentials were invalid

    url = employee_time_sheet_service_host + employee_time_sheet_url + str(employee_time_sheet_id)
    headers = {'content-type':'application/json'}
    response = requests.get(url, headers=headers)
    _json = response.json()
    #print("response==", response.json())
    return render_template('index.html', employee_time_sheet_record=_json)

@app.route('/list_employee_time_sheet', methods=['GET'])
def list_employee_time_sheet():
    employee_id = request.args.get('employee_id')
    log_date = request.args.get('log_date')
    offset = request.args.get('offset')
    limit = request.args.get('limit')
    # the code below is executed if the request method
    # was GET or the credentials were invalid

    url = employee_time_sheet_service_host + employee_time_sheet_url +'?employee_id='+str(employee_id) + '&log_date='+str(log_date) +'&offset='+str(offset) + '&limit='+str(limit)
    headers = {'content-type':'application/json'}
    print("url===", url)
    response = requests.get(url, headers=headers)
    _json = response.json()
    print("response==", response.json())
    return render_template('index.html', employee_time_sheet_list=_json)


if __name__=="__main__":
    app.run(host="127.0.0.1", port=8003)