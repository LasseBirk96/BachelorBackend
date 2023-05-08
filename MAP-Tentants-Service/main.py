
import sys
import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
sys.path.append("..")
app = Flask(__name__)
CORS(app)
api = Api(app)
from LogicLayer.ServiceAPIs.CostCenterAPI import costcenter_endpoints
from LogicLayer.ServiceAPIs.BusinessGroupAPI import businessgroup_endpoints
from LogicLayer.ServiceAPIs.MuleApplicationAPI import muleapplication_endpoints
from LogicLayer.ServiceAPIs.BusinessGroupResourceAPI import businessgroupresource_endpoints
from LogicLayer.ServiceAPIs.MuleApplicationInstanceAPI import muleapplicationinstance_endpoints




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)


