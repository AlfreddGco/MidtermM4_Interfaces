#!/usr/bin/bash
python3 -m grpc_tools.protoc -I=./protos --python_out=./interfases --grpc_python_out=./interfases ./protos/interfases.proto
echo "Python proto files built"
protoc -I=./protos --csharp_out=./clients --grpc_csharp_out=./clients ./protos/interfases.proto
echo "C# proto files built"
protoc -I=./protos --go_out=./gateway --grpc_go_out=./gateway ./protos/interfases.proto
echo "Go proto files built"
protoc -I ./protos --go_out ./gateway/Interfases --go_opt paths=source_relative \
    --grpc-gateway_out ./gateway/Interfases --grpc-gateway_opt paths=source_relative \
    --go-grpc_out ./gateway/Interfases --go-grpc_opt paths=source_relative \
    ./protos/interfases.proto