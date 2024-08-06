from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def get_metrics():
    cpu_stats = psutil.cpu_stats()
    metricas = {
        'cpu_usage_percent': psutil.cpu_percent(interval=1),
        'cpu_cores':psutil.cpu_count(logical=False),
        'cpu_stats': {
            'ctx_switches': cpu_stats.ctx_switches,
            'interrupts': cpu_stats.interrupts,
            'soft_interrupts': cpu_stats.soft_interrupts,
            'syscalls': cpu_stats.syscalls
        },
        'memory_percent_used': psutil.virtual_memory().percent,
        'memory_available': psutil.virtual_memory().available,
        'memory_total': psutil.virtual_memory().total
    }
    return jsonify(metricas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)