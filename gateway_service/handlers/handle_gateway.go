package handlers

/*
Package handlers implements the gRPC server-side handlers for the
GatewayService.

This file defines:
- The GatewayService struct
- The HandleRequest RPC method implementation

Responsibilities:
- Receive incoming gRPC requests from clients
- Apply business logic or orchestration
- Construct and return GatewayResponseToClient messages
- Send Planner request to Planner service

This layer should remain thin and delegate complex logic
to deeper service or domain layers in production systems.
*/


import (
	"context"
	"time"

	pb "github.com/ai-thinking-pipeline/generated/v3/go"
	zlog "github.com/ai-thinking-pipeline/utils/zlog"

)

type GatewayService struct {
	pb.UnimplementedGatewayServer
}


func (s *GatewayService) HandleClientRequestToGateway(ctx context.Context, req *pb.ClientRequestToGateway) (*pb.GatewayResponseToClient, error) {
	zlog.Info("[Gateway Service] - Handling client request to gateway")

	// create metadata
	responseMeta := &pb.RequestMeta{
		RequestId: req.Meta.RequestId,
		Time: &pb.Timestamp{
			UnixMs: time.Now().UnixMilli(),
		},
	}

	// construct response gateway -> client
	gateway_resp := &pb.GatewayResponseToClient {
		Response: &pb.Response{
			Meta: responseMeta,
			Message: "Request received successfully by Gateway.",
		},	
	}

	// send request gateway -> planner
	_, err := GatewayRequestToPlannerFn(req)
	if err != nil{
		zlog.Error("Error while sending request to planner.")
	} else {
		zlog.Info("[Gateway] Planner processed the request successfully")
	}


	return gateway_resp, nil
}












