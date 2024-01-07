import grpc
import test_pb2
import test_pb2_grpc


def run():
    connect = grpc.insecure_channel('localhost:8000')
    stub = test_pb2_grpc.get_configStub(channel=connect)
    response = stub.Login_info(test_pb2.Request(host='192.168.1.55',
                                                username='huaweiuser',
                                                password='Huawei@123'))
    print(response)

run()