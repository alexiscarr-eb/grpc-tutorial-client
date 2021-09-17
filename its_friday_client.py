from __future__ import print_function

import grpc

import exampleservice_pb2
import exampleservice_pb2_grpc


def run_its_friday():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = exampleservice_pb2_grpc.FridayServiceStub(channel)
        response = stub.ItsFriday(
            exampleservice_pb2.ItsFridayRequest(
                # can also pass in "Spanish"
                option="English"
            )
        )
    print(response)


if __name__ == '__main__':
    run_its_friday()
