package handlers

import (
	"context"
	"time"

	pb "github.com/ai-thinking-pipeline/generated/v3/go"
	zlog "github.com/ai-thinking-pipeline/utils/zlog"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)


func GatewayRequestToPlannerFn(req *pb.ClientRequestToGateway) (*pb.PlannerResponseToGateway, error) {
	conn, err := grpc.Dial(
		"localhost:50051",
		grpc.WithTransportCredentials(insecure.NewCredentials()),
		grpc.WithBlock(),
	)

	if err != nil {
		zlog.Error("[Gateway] Failed to connect to Planner: " + err.Error())
		return nil, err
	}

	defer conn.Close()

	plannerClient := pb.NewPlannerClient(conn)

	plannerReq := &pb.GatewayRequestToPlanner{
		Meta: &pb.RequestMeta{
			RequestId: req.Meta.RequestId,
			Time: &pb.Timestamp{
				UnixMs: time.Now().UnixMilli(),
			},
		},
		UserPrompt: req.UserPrompt,
	}

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	resp, err := plannerClient.HandleGatewayRequestToPlanner(ctx, plannerReq)

	if err != nil {
		zlog.Error("[Gateway] Error calling Planner: " + err.Error())
		return nil, err
	}
	zlog.Info("[Gateway] Received response from Planner")
	return resp, nil
}







