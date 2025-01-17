from queue import Queue
q = Queue()
def generate_request(request_text):
    q.put(request_text)

def process_request():
    if q.empty():
        print("There is no any order in queue")
    else:
        while not q.empty():
            print("Doing ", q.get())

input_text = ""
while input_text != "exit":
    input_text = input("Enter text of the order: ")
    if input_text == "execute":        
        process_request()
    else:
        generate_request(input_text)