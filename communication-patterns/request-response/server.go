package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello, client!")
	})

	fmt.Println("Server listening on port 3000")
	http.ListenAndServe(":3000", nil)
}
