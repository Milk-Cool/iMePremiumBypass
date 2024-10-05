import json
import logging
from mitmproxy.http import HTTPFlow, Response
from base64 import b64decode


HOST = "api.imem.app"
PATH = "/api/premium/getOwnStatus"


def request(flow: HTTPFlow):
    if flow.request.host == HOST and (flow.request.path == PATH or flow.request.path == PATH + "/"):
        uid = json.loads(b64decode(flow.request.headers["authorization"].replace("Bearer ", "").split(".")[1]))["uid"]
        flow.response = Response.make(
            200,
            json.dumps({
                "payload": {
                    "active": True,
                    "userId": uid
                },
                "status": "ok"
            }),
            { "Content-Type": "application/json; charset=utf-8" }
        )
        logging.info(f"Faked premium for ID {uid}!")
