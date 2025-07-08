import grpc
from concurrent import futures
import greet_pb2
import greet_pb2_grpc
from alik import alik


class AlikService(greet_pb2_grpc.AlikServiceServicer):
    def SayAlik(self, request, context):
        result = alik(request.name)
        return greet_pb2.AlikResponse(message=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_AlikServiceServicer_to_server(AlikService(), server)
    server.add_insecure_port("[::]:50052")
    print("Alik serveri 50052 portda ishga tushdi")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
