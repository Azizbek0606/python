import grpc
from concurrent import futures
import greet_pb2
import greet_pb2_grpc
from say_hello import hello


class HelloService(greet_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        result = hello(request.name)
        return greet_pb2.HelloResponse(message=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port("[::]:50051")
    print("Hello serveri 50051 portda ishga tushdi")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
