package handlers

/*
Package handlers contains shared logic used by both the server and client
layers of the Gateway service.

This file specifically handles:
- Creating a gRPC client connection to the Gateway server
- Constructing and sending ClientRequestToGateway messages
- Receiving and logging GatewayResponseToClient responses

NOTE:
Although placed in handlers, this function represents outbound
(client-side) communication logic and may later be moved to a
dedicated client or transport layer for cleaner architecture.
*/


import (
	"context"
	"log"
	"time"

	pb "github.com/ai-thinking-pipeline/generated/v1/go"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func ClientRequestToGatewayFn() {
	conn, err := grpc.NewClient(
		"localhost:50050",
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	)
	if err != nil {
		log.Println(err)
	}
	defer conn.Close()

	client := pb.NewGatewayServiceClient(conn)

	resp, err := client.HandleRequest(
		context.Background(),
		&pb.ClientRequestToGateway{
			Meta: &pb.RequestMeta{
				RequestId: "req-1",
				Time: &pb.Timestamp{
					UnixMs: time.Now().UnixMilli(),
				},
			},
			UserPrompt: "Hello from Go",
		},
	)
	if err != nil {
		log.Println(err)
	}

	log.Println("Response:", resp.Message)

}

