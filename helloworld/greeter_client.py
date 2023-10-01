from __future__ import print_function

from greeter_server import Greeter  #importing Greeter class
import logging
import grpc
import attack_pb2
import attack_pb2_grpc

# Default method for testing purpose
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = attack_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(attack_pb2.HelloRequest(name="FINALLY..."))
    print("\nWAR RESULT: " + response.message)

# Actual method which is taking inputs from user
def run4():
    print("Here war is began and server will broadcast the information to the soldiers...\n Enter the details...\n")
    M = int(input("Enter the no. of soldiers (M):"))
    N = int(input("Enter the size of matrix (warzone) (N):"))
    T = int(input("Enter the duration of war (T):"))
    t = int(input("Enter the time interval for missile attack (t):"))
    Greeter.set_inputs_from_client(M,N,T,t) 
      
    #run()

if __name__ == "__main__":
    logging.basicConfig()
    run4() #CALL IT FOR ACTUAL CODE RUN
       

