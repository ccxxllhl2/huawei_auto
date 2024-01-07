from concurrent import futures
import time
import grpc
import test_pb2
import test_pb2_grpc
import paramiko


class Display_Config(test_pb2_grpc.get_configServicer):
    def Login_info(self, request, context):
        ssh = paramiko.client.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=request.host,
                    port=22,
                    username=request.username,
                    password=request.password)
        cli = ssh.invoke_shell()
        cli.send('screen-length 0 temp\n')
        time.sleep(0.5)
        _ = cli.recv(9999).decode()
        cli.send('display cu\n')
        time.sleep(3)
        data = cli.recv(9999).decode()
        ssh.close()
        return test_pb2.Reply(message=data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    test_pb2_grpc.add_get_configServicer_to_server(Display_Config(), server)
    server.add_insecure_port('localhost:8000')
    server.start()
    try:
        print('Server Start!')
        while True:
            time.sleep(60*60)
    except KeyboardInterrupt:
        server.stop()

if __name__ == "__main__":
    serve()