# grpc-example-python-client

To generate python packages:

```bash
python3 -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/**/*.proto
```
