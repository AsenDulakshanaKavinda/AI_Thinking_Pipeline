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
	"log"
	"net"

	pb "github.com/ai-thinking-pipeline/generated/v1/go"
	"github.com/ai-thinking-pipeline/handlers"	
	"google.golang.org/grpc"
)

func Server() {
	lis, err := net.Listen("tcp", ":50050")
	if err != nil {
		log.Println(err)
	}

	gatewayServer := grpc.NewServer()
	pb.RegisterGatewayServiceServer(gatewayServer, &handlers.GatewayService{})

	log.Println("[Gateway Server] - Running on :50050")
	gatewayServer.Serve(lis)

}



