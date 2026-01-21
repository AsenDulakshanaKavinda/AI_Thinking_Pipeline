package zlog

/* 
Package zlog provides a simple, safe-to-use logging wrapper.

Responsibilities:
- It ensures the underlying logger is initialized only once
- and exposes convenient helper functions for common log levels.

*/

import (
	"sync"

	"github.com/ai-thinking-pipeline/utils/logger"
)

var (
	logDir = "logs"
	logFile = "logs.log"
	once    sync.Once
)

// init runs automatically when the package is imported
func init() {
	Init()
}

// Init initializes the logger exactly once
func Init() {
	once.Do(func() {
		_ = logger.InitLogger(logDir, logFile)
	})
}


func Info(msg string) {
	Init()
	logger.Log.Info(msg)
}

func Error(msg string) {
	Init()
	logger.Log.Error(msg)
}