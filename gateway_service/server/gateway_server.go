package server

/*
Package server is responsible for initializing and running the
Gateway gRPC server.

This file handles:
- TCP listener setup
- gRPC server creation
- Service registration
- Blocking server execution using grpc.Server.Serve

NOTE:
Server() is a blocking call and should be run in a goroutine
if the application needs to perform additional tasks (e.g., client calls).
*/


import (
	"net"

	zlog "github.com/ai-thinking-pipeline/utils/zlog"
	pb "github.com/ai-thinking-pipeline/generated/v3/go"
	"github.com/ai-thinking-pipeline/handlers"	
	"google.golang.org/grpc"
)

func Server() {
	zlog.Info("[Gateway Server] - Starting on :50050")
	lis, err := net.Listen("tcp", ":50050")
	if err != nil {
		zlog.Error(err.Error())
	}

	gatewayServer := grpc.NewServer()
	pb.RegisterGatewayServer(gatewayServer, &handlers.GatewayService{})

	zlog.Info("[Gateway Server] - Running on :50050")
	gatewayServer.Serve(lis)

}



