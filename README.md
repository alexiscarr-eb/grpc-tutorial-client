## How to build a gRPC client

1. Run `pipenv shell`
2. Run `pipenv install`
3. Copy in updated proto
4. Run `python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/exampleservice.proto`
5. Add file with client name to repo (looks at `its_friday_client` for example)
6. Adding a line
## Run client

1. Run client by typing `python <client_file_name.py>` in terminal. For example, `python its_friday_client.py` will run the `its_friday_client`.
