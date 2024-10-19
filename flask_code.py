from flask import Flask, render_template, request
import subprocess
import os
import datetime
import time

app = Flask(__name__)

@app.route('/htop')
def htop_output():
    username = os.getlogin()  
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] 
    full_name = "Your Full Name"
    try:
        htop_process = subprocess.run(['htop'], capture_output=True, text=True)
        htop_output = htop_process.stdout
    except FileNotFoundError:
        htop_output = "htop command not found. Ensure it's installed."

    return render_template(
        'htop.html',
        username=username,
        server_time=server_time,
        full_name=full_name,
        htop_output=htop_output
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 