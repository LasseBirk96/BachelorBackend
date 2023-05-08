import os
from flask import Flask
from LogicLayer import ingestion_job_handler

app = Flask(__name__)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=False, host="0.0.0.0", port=port)
