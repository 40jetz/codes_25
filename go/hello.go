package main
import "fmt"

func main() {
	fmt.Println("hello, world")
	const conferenceTicket = 50
	var remainingTickets = 50

	fmt.Printf("welcome to %v booking\n", conferenceTicket)
	fmt.Printf("There are %v tickets remaining\n", remainingTickets)
}
