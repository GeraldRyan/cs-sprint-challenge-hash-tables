#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    hashtable = {}
    last_port = ""
    for t in tickets:
        hashtable[t.source] = t.destination
        if t.destination == 'NONE':
            last_port = t.source

    print(hashtable)
    route = ["NONE"] * (length)
    route[0] = hashtable['NONE']
    route[length-2] = last_port
    for d in range(1, len(tickets)-1, 1):
        route[d] = hashtable[route[d-1]]
    print(route)
    return route


if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]

    reconstruct_trip(tickets, 3)
