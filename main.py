from __future__ import print_function

import logging

import grpc
from routes.user import user_pb2_grpc
from routes.user import user_pb2


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:5050") as channel:
        stub = user_pb2_grpc.UserStub(channel)
        response = stub.GetUser(user_pb2.UserRequest(ID=1))
    print("Greeter client received: " + response.Name + " " + response.Status)


if __name__ == "__main__":
    logging.basicConfig()
    run()
