from flask import Flask 

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
  return {
    "channel": "The Show",
    "tutorial": "React, Flask and Docker"
  }

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')