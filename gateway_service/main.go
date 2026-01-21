package main

/*
Main package is the application entry point for the Gateway Service.

This file is responsible for:
- Bootstrapping the gRPC server
- Starting the server in a background goroutine
- Triggering internal client requests for testing or demo purposes
- Keeping the application process alive

NOTE:
In production, server and client logic would typically run
in separate binaries. This combined setup is intended for
local development and learning.
*/


import (
	"time"

	"github.com/ai-thinking-pipeline/client"
	"github.com/ai-thinking-pipeline/server"
	zlog "github.com/ai-thinking-pipeline/utils/zlog"

)

func main() {
	// log.Println("Starting Gateway Service")
	zlog.Info("Gateway Server stating...")

	// start server in background
	go server.Server()

	// Give server time to start
	time.Sleep(5 * time.Millisecond)

	// send request
	client.GatewayClient()

	// keep server running
	select {}

}