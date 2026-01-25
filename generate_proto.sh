#!/usr/bin/env bash

set -e  # exit immediately if any command fails

echo "🚀 Generating gRPC code..."

# Paths
PROTO_DIR="proto/v4"
GO_OUT_GATEWAY="gateway_service/generated/v4/go"
PY_OUT_GATEWAY="gateway_service/generated/v4/python"
GO_OUT_PLANNER="planner_service/generated/v4/go"
PY_OUT_PLANNER="planner_service/generated/v4/python"
GO_OUT_REASONING="reasoning_service/generated/v4/go"
PY_OUT_REASONING="reasoning_service/generated/v4/python"

# Ensure output directories exist
mkdir -p "$GO_OUT_GATEWAY"
mkdir -p "$PY_OUT_GATEWAY"
mkdir -p "$GO_OUT_PLANNER"
mkdir -p "$PY_OUT_PLANNER"
mkdir -p "$GO_OUT_REASONING"
mkdir -p "$PY_OUT_REASONING"


# Generate Go code
echo "🔧 Generating Go code gateway..."
protoc \
  -I "$PROTO_DIR" \
  --go_out="$GO_OUT_GATEWAY" \
  --go-grpc_out="$GO_OUT_GATEWAY" \
  "$PROTO_DIR"/common.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto \
  "$PROTO_DIR"/reasoning.proto 

echo "🔧 Generating Go code planner..."
protoc \
  -I "$PROTO_DIR" \
  --go_out="$GO_OUT_PLANNER" \
  --go-grpc_out="$GO_OUT_PLANNER" \
  "$PROTO_DIR"/common.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto \
  "$PROTO_DIR"/reasoning.proto 

echo "🔧 Generating Go code reasoning..."
protoc \
  -I "$PROTO_DIR" \
  --go_out="$GO_OUT_REASONING" \
  --go-grpc_out="$GO_OUT_REASONING" \
  "$PROTO_DIR"/common.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto \
  "$PROTO_DIR"/reasoning.proto 

# Generate Python code
echo "🐍 Generating Python code for gateway..."
python3 -m grpc_tools.protoc \
  -I "$PROTO_DIR" \
  --python_out="$PY_OUT_GATEWAY" \
  --grpc_python_out="$PY_OUT_GATEWAY" \
  "$PROTO_DIR"/common.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto \
  "$PROTO_DIR"/reasoning.proto 

echo "🐍 Generating Python code planner..."
python3 -m grpc_tools.protoc \
  -I "$PROTO_DIR" \
  --python_out="$PY_OUT_PLANNER" \
  --grpc_python_out="$PY_OUT_PLANNER" \
  "$PROTO_DIR"/common.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto \
  "$PROTO_DIR"/reasoning.proto 

echo "🐍 Generating Python code reasoning..."
python3 -m grpc_tools.protoc \
  -I "$PROTO_DIR" \
  --python_out="$PY_OUT_REASONING" \
  --grpc_python_out="$PY_OUT_REASONING" \
  "$PROTO_DIR"/common.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto \
  "$PROTO_DIR"/reasoning.proto 

echo "✅ gRPC code generation completed successfully!"
