package logger

/* 
Package logger implements the logger utils service for the GatewayService.

This file defines:
- The InitLogger function

Responsibilities:
- Create InitLogger function with both console and file loggers.
- Apply messageCfg(log message format) to improve readability.

*/

import (
	"os"

	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
	"gopkg.in/natefinch/lumberjack.v2"
)

var Log = zap.NewNop()

func InitLogger(logDir, logFile string) error {
    if err := os.MkdirAll(logDir, 0755); err != nil {
        return err
    }

    fileWriter := zapcore.AddSync(&lumberjack.Logger{
		Filename:   logDir + "/" + logFile,
		MaxSize:   5, // MB
		MaxBackups: 3,
		MaxAge:    28,
		Compress:  true, 
    })

	messageCfg := zapcore.EncoderConfig{
		TimeKey:      "time",
		LevelKey:     "level",
		NameKey:      "logger",
		MessageKey:   "msg",
		CallerKey:    "", // remove caller
		LineEnding:   zapcore.DefaultLineEnding,
		EncodeTime:   zapcore.TimeEncoderOfLayout("2006-01-02 15:04:05"),
		EncodeLevel:  zapcore.CapitalLevelEncoder,
		EncodeName:   zapcore.FullNameEncoder,
	}

    consoleEncoder := zapcore.NewConsoleEncoder(messageCfg)
    fileEncoder := zapcore.NewJSONEncoder(messageCfg)

    core := zapcore.NewTee(
        zapcore.NewCore(consoleEncoder, zapcore.AddSync(os.Stdout), zap.InfoLevel),
        zapcore.NewCore(fileEncoder, fileWriter, zap.InfoLevel),
    )

    Log = zap.New(core).Named("gateway")
	return nil
}











