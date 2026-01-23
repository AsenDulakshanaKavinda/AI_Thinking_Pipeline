package handlers

import (
	"context"
	"time"

	pb "github.com/ai-thinking-pipeline/generated/v3/go"
	zlog "github.com/ai-thinking-pipeline/utils/zlog"
	"github.com/google/uuid"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func ClientRequestToGatewayFn() {
	conn, err := grpc.Dial(
		"localhost:50050",
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	)
	zlog.Info("Creating client - gateway connection")


	if err != nil {
		zlog.Error("Error while creating client - gateway connection" + err.Error())
		return
	}
	defer conn.Close()

	client := pb.NewGatewayClient(conn)

	genRequestID, err := uuid.NewRandom()
	if err != nil{
		zlog.Error("Failed to Generate the ID")
		return
	}

	resp, err := client.HandleClientRequestToGateway(
		context.Background(),
		&pb.ClientRequestToGateway{
			Meta: &pb.RequestMeta{
				RequestId: genRequestID.String(),
				Time: &pb.Timestamp{
					UnixMs: time.Now().UnixMilli(),
				},
			},
			UserPrompt: "Hello from Go",
		},
	)
	zlog.Info("Creating client Request to Gateway")
	if err != nil {
		zlog.Error(" Error while creating client Request to Gateway" + err.Error())
		return
	}

	zlog.Info(resp.Response.Message)
}
