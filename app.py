import os
import sys

import views
from flask import Flask, jsonify
from werkzeug.utils import cached_property

# from blueprints.basic_endpoints import blueprint as basic_endpoints

# from blueprints.basic_endpoints import blueprint as basic_endpoint
# from blueprints.documented_endpoints import blueprint as documented_endpoint


app = Flask(__name__)
# app.config['RESTPLUS_MASK_SWAGGER'] = False

# app.register_blueprint(basic_endpoints)
# app.register_blueprint(documented_endpoint)

app.add_url_rule("/", view_func=views.root, methods=['GET'])
app.add_url_rule("/read_ocr", view_func=views.read_ocr, methods=['POST'])
print("Server Ready", flush=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
