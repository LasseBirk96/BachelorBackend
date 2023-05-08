import os
from flask import Flask
from LogicLayer import processor_job_handler

app = Flask(__name__)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(debug=False, host="0.0.0.0", port=port)


