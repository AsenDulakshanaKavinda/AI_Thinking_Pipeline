#!/usr/bin/env bash

set -e  # exit immediately if any command fails

echo "🚀 Generating gRPC code..."

# Paths
PROTO_DIR="proto/v3"
GO_OUT_GATEWAY="gateway_service/generated/v3/go"
PY_OUT_GATEWAY="gateway_service/generated/v3/python"
GO_OUT_PLANNER="planner_service/generated/v3/go"
PY_OUT_PLANNER="planner_service/generated/v3/python"

# Ensure output directories exist
mkdir -p "$GO_OUT_GATEWAY"
mkdir -p "$PY_OUT_GATEWAY"
mkdir -p "$GO_OUT_PLANNER"
mkdir -p "$PY_OUT_PLANNER"


# Generate Go code
echo "🔧 Generating Go code gateway..."
protoc \
  -I "$PROTO_DIR" \
  --go_out="$GO_OUT_GATEWAY" \
  --go-grpc_out="$GO_OUT_GATEWAY" \
  "$PROTO_DIR"/main.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto

echo "🔧 Generating Go code planner..."
protoc \
  -I "$PROTO_DIR" \
  --go_out="$GO_OUT_PLANNER" \
  --go-grpc_out="$GO_OUT_PLANNER" \
  "$PROTO_DIR"/main.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto

# Generate Python code
echo "🐍 Generating Python code for gateway..."
python3 -m grpc_tools.protoc \
  -I "$PROTO_DIR" \
  --python_out="$PY_OUT_GATEWAY" \
  --grpc_python_out="$PY_OUT_GATEWAY" \
  "$PROTO_DIR"/main.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto

echo "🐍 Generating Python code planner..."
python3 -m grpc_tools.protoc \
  -I "$PROTO_DIR" \
  --python_out="$PY_OUT_PLANNER" \
  --grpc_python_out="$PY_OUT_PLANNER" \
  "$PROTO_DIR"/main.proto \
  "$PROTO_DIR"/gateway.proto \
  "$PROTO_DIR"/planner.proto

echo "✅ gRPC code generation completed successfully!"
