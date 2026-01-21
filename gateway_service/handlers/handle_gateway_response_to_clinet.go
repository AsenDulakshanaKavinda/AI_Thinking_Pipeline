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

This layer should remain thin and delegate complex logic
to deeper service or domain layers in production systems.
*/


import (
	"context"
	"time"

	pb "github.com/ai-thinking-pipeline/generated/v1/go"
	zlog "github.com/ai-thinking-pipeline/utils/zlog"

)

type GatewayService struct {
	pb.UnimplementedGatewayServiceServer
}

func (s *GatewayService) HandleRequest(ctx context.Context, req *pb.ClientRequestToGateway) (*pb.GatewayResponseToClient, error) {
	zlog.Info("[Gateway Service] - Handling gateway request to client")
	return &pb.GatewayResponseToClient{
		Meta: &pb.RequestMeta{
			RequestId: req.Meta.RequestId,
			Time: &pb.Timestamp{
				UnixMs: time.Now().UnixMilli(),
			},
		},
		Message: "Processed: " + req.UserPrompt,
	}, nil
}

