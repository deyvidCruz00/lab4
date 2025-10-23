from flask import Flask, request, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

REQUESTS = Counter('app_requests_total', 'Total HTTP requests', ['path','method','code'])
LATENCY = Histogram('app_request_latency_seconds', 'Latency in seconds', ['path'])

@app.route('/')
def index():
    start = time.time()
    
    delay = random.choice([0.01, 0.02, 0.05, 0.2])
    time.sleep(delay)
    resp = jsonify({"msg": "hola desde app"})
    REQUESTS.labels(path='/', method='GET', code='200').inc()
    LATENCY.labels(path='/').observe(time.time() - start)
    return resp

@app.route('/health')
def health():
    REQUESTS.labels(path='/health', method='GET', code='200').inc()
    return "OK"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/error')
def simulate_error():
    REQUESTS.labels(path='/error', method='GET', code='500').inc()
    
    return jsonify({"error": "Esto es un error simulado"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
