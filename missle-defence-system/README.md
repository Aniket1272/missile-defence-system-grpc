[This code's documentation lives on the grpc.io site.](https://grpc.io/docs/languages/python/quickstart)
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./attack.proto

we can rename protofile