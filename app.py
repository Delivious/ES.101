from flask import Flask, request, jsonify, render_template, redirect, url_for
import datetime
app = Flask(__name__)
data = {
    'logs': []
}
app.secret_key = 'your_secret_key'
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('logs.html', data=data)

@app.route('/api/logs', methods=['GET', 'POST'])
def get_logs():
    if request.method == 'POST':
        print('Motion detected')
        data['logs'].append({
            'time': datetime.datetime.now().strftime("%m/%d/%Y - %H:%M:%S")
        })
        return 200

@app.route('/api/returnLogs', methods=['GET'])
def return_logs():
    return jsonify(data['logs'])

app.run(debug=True, host='0.0.0.0', port=5000)
