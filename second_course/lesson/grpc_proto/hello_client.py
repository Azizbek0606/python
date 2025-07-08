import grpc
import greet_pb2
import greet_pb2_grpc
from say_hello import hello


def run():
    # Mahalliy hello funksiyasini ishlatish
    print("Mahalliy hello funksiyasi:", hello("Ali"))

    # AlikService ga ulanish
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = greet_pb2_grpc.AlikServiceStub(channel)
        response = stub.SayAlik(greet_pb2.AlikRequest(name="Hasan"))
        print("Alik serveridan javob:", response.message)


if __name__ == "__main__":
    run()
