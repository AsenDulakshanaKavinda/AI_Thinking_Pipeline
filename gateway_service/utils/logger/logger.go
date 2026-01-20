package logger

import (
	"os"

	"github.com/sirupsen/logrus"
	"gopkg.in/natefinch/lumberjack.v2"
)

var Log *logrus.Logger

func InitLogger(logDir, logFile string) {
    Log = logrus.New()

    // 1. Console
    Log.SetOutput(os.Stdout)
    Log.SetFormatter(&logrus.TextFormatter{
        FullTimestamp: true,
    })

    // 2. Rotating file
    lumberjackLogger := &lumberjack.Logger{
        Filename:   logDir + "/" + logFile,
        MaxSize:    5,  // MB
        MaxBackups: 3,
        MaxAge:     28, // days
        Compress:   true,
    }   

    // Multi-output (console + file)
    Log.SetOutput(lumberjackLogger)
    Log.SetLevel(logrus.InfoLevel)

}









