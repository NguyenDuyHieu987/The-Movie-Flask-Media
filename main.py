from flask import *
from flask_cors import CORS, cross_origin
from waitress import serve
from gevent.pywsgi import WSGIServer
import os
import configs


app = Flask(__name__)


# CORS(app)

# api_cors_config = {
#     "allow_headers": "*",
#     "origins": "*",
#     "methods": ["OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"],
# }

# CORS(
#     app,
#     resources={
#         r"/*": api_cors_config,
#     },
# )


@app.route("/videos/<type>/<name>", methods=["GET"])
@cross_origin(origins=configs.ALL_ORIGINS_CONFIG)
def img_route(type, name):
    if type == "feature":
        src_video = f"videos/feature/{name}"

        return send_file(
            src_video,
            mimetype="video/mp4",
        )

    elif type == "television":
        src_video = f"videos/television/{name}"

        return send_file(
            src_video,
            mimetype="video/mp4",
        )


if __name__ == "__main__":
    # app.run(debug=True, port=5000, use_reloader=True)
    http_server = WSGIServer(("", 5000), app)
    http_server.serve_forever()
