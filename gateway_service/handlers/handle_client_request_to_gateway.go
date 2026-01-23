package handlers

import (
	"context"
	"time"

	pb "github.com/ai-thinking-pipeline/generated/v3/go"
	zlog "github.com/ai-thinking-pipeline/utils/zlog"
)

type GatewayService struct {
	pb.UnimplementedGatewayServer
}

func (s *GatewayService) HandleClientRequestToGateway(
	ctx context.Context,
	req *pb.ClientRequestToGateway,
) (*pb.GatewayResponseToClient, error) {

	zlog.Info("[Gateway Service] - Handling client request")

	meta := &pb.RequestMeta{
		RequestId: req.Meta.RequestId,
		Time: &pb.Timestamp{
			UnixMs: time.Now().UnixMilli(),
		},
	}

	// Send request to Planner
	_, err := GatewayRequestToPlannerFn(req)
	if err != nil {
		zlog.Error("[Gateway] Planner request failed")
	} else {
		zlog.Info("[Gateway] Planner processed request successfully")
	}

	return &pb.GatewayResponseToClient{
		Response: &pb.Response{
			Meta:    meta,
			Message: "Request received successfully by Gateway.",
		},
	}, nil
}
