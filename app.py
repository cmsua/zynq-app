#!/usr/bin/env python3

from flask import Flask, Response, request
import os, json

app = Flask(__name__)

@app.route('/command', methods=["PUT"])
def command():
    name = request.get_json()["name"]
    if name == "loadFW":
        return { 'text': run('fw-loader load hexaboard-hd-tester-v2p0-trophy-v3') }
    elif name == "restart_services":
        return { 'i2c': run('service i2c-server restart'), 'daq': run('service daq-server restart') }
    elif name == "pwr_on":
        return { 'text': run('./pwr_on') }
    elif name == "pwr_off":
        return { 'text': run('./pwr_off') }
    else:
        return { 'error': 'Invalid Command' }

@app.route('/daq')
def daq():
    return { 'text': run('service daq-server status') }

@app.route('/i2c')
def i2c():
    return { 'text': run('service i2c-server status') }


def run(command):
    return os.popen(command).read()
