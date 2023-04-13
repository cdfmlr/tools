package main

import (
	"flag"
	"fmt"
	"net/http"
	"os"
	"strings"
	"time"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

var (
	addr  = flag.String("l", ":8080", "http listen address.")
	dir   = flag.String("d", ".", "static directory path.")
	https = flag.String("s", "", "enable TLS: `CERT_FILE:KEY_FILE`")
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

	var err error

	switch *https != "" {
	case true: // enable tls
		var cert, key string
		if cert, key, err = parseTlsConfig(*https); err == nil {
			fmt.Printf("Serving dir %s on HTTPS (%s).\n\tcert: %s\n\t key: %s\n", *dir, *addr, cert, key)
			err = router.RunTLS(*addr, cert, key)
		}
	case false: // http
		fmt.Printf("Serving dir %s on HTTP (%s).\n", *dir, *addr)
		err = router.Run(*addr)
	}

	if err != nil {
		fmt.Printf("Error: %s\n", err)
		os.Exit(1)
	}
}

// parseTlsConfig "certFile:keyFile" into certFile & keyFile
func parseTlsConfig(certAndKey string) (certFile, keyFile string, err error) {
	ss := strings.Split(certAndKey, ":")
	if len(ss) != 2 {
		return "", "", fmt.Errorf("bad -s value: \"CERT_FILE:KEY_FILE\" expected")
	}
	certFile, keyFile = ss[0], ss[1]
	return

}
