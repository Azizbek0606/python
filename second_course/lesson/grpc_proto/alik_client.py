import grpc
import greet_pb2
import greet_pb2_grpc
from alik import alik


def run():
    # Mahalliy alik funksiyasini ishlatish
    print("Mahalliy alik funksiyasi:", alik("Hasan"))

    # HelloService ga ulanish
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.HelloServiceStub(channel)
        response = stub.SayHello(greet_pb2.HelloRequest(name="Ali"))
        print("Hello serveridan javob:", response.message)


if __name__ == "__main__":
    run()
