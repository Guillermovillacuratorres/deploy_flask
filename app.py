from flask import Flask,  request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "funcionando","Version":1.0})

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Verificar que es un push al branch correcto
        data = request.json
        if data['ref'] == 'refs/heads/main':
            # Ejecutar el script de despliegue
            subprocess.Popen(['powershell.exe', '-File', 'C:\Users\villa\Desktop\deploy.ps1'])
            return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'ignored'}), 200




if __name__ == '__main__':
    app.run(debug=True, port=5000)