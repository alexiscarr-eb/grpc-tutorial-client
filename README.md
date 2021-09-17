## How to build

1. Copy in updated proto
2. `python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/exampleservice.proto`
