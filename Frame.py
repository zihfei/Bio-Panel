import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(5)
    
    print("Server is listening on port 8080...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        handle_request(client_socket)

def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode('utf-8')
    request_lines = request_data.split('\r\n')
    method, path, protocol = request_lines[0].split()
    
    if method == 'GET':
        if path == '/':
            response = "HTTP/1.1 200 OK\r\n\r\nHello, World!"
        else:
            response = "HTTP/1.1 404 Not Found\r\n\r\nPage Not Found"
    else:
        response = "HTTP/1.1 405 Method Not Allowed\r\n\r\nMethod Not Allowed"
    
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    start_server()
