package main

import (
	"flag"
	"fmt"
	"net/http"
	"os"
	"time"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

var (
	addr = flag.String("l", ":8080", "http listen address.")
	dir  = flag.String("d", ".", "static directory path.")
)

func init() {
	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(), "Usage: %s [options]\n", os.Args[0])
		fmt.Fprintf(flag.CommandLine.Output(), "  Serving static files from a directory over HTTP with CORS allowed.\n")
		fmt.Fprintf(flag.CommandLine.Output(), "Options:\n")
		flag.PrintDefaults()
	}
	flag.Parse()

	gin.SetMode(gin.ReleaseMode)
}

func main() {
	router := gin.Default()

	router.Use(cors.New(cors.Config{
		AllowAllOrigins:  true,
		AllowMethods:     []string{"*"},
		AllowHeaders:     []string{"*"},
		ExposeHeaders:    []string{"*"},
		AllowCredentials: true,
		MaxAge:           12 * time.Hour,
	}))

	router.StaticFS("/", http.Dir(*dir))
	fmt.Printf("Serving dir %s on HTTP (%s).\n", *dir, *addr)
	if err := router.Run(*addr); err != nil {
		fmt.Printf("Error: %s\n", err)
		os.Exit(1)
	}
}
