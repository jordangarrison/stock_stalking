// make_http_request.go
package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

func main() {
	// Make HTTP GET request
	apiURL := fmt.Sprintf("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo")
	response, err := http.Get(apiURL)
	if err != nil {
		log.Fatal(err)
	}
	defer response.Body.Close()

	// Copy data from the response to standard output
	n, err := io.Copy(os.Stdout, response.Body)
	if err != nil {
		log.Fatal(err)
	}

	log.Println("Number of bytes copied to STDOUT:", n)
}
