package client

/*
Package client contains client-side logic for communicating with the
Gateway gRPC server.

This package is responsible for:
- Initiating outbound gRPC calls to the GatewayService
- Acting as a test or internal client within the same process
- Sending structured requests and receiving responses

NOTE:
This package does NOT start any servers.
It is meant to be invoked by the main application entry point.
*/


import (

	"github.com/ai-thinking-pipeline/handlers"	
	zlog "github.com/ai-thinking-pipeline/utils/zlog"
)

func GatewayClient() {
	zlog.Info("[Gateway Client] - Sending the Client Request.")
	handlers.ClientRequestToGatewayFn()
}