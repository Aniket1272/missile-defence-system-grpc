[This code's documentation lives on the grpc.io site.](https://grpc.io/docs/languages/python/quickstart)
```bash
#Next we need to update the gRPC code used by our application to use the new service definition.
#From the examples/python/helloworld directory,
#run: 
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./attack.proto

