import socket

# Khởi tạo socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ IP và Port
HOST = "127.0.0.1"
PORT = 9999

# Bind địa chỉ
server.bind((HOST, PORT))

# Lắng nghe kết nối
server.listen()

print(f"Server đang chạy tại {HOST}:{PORT}")

while True:
    # Chấp nhận client kết nối
    client_socket, address = server.accept()

    print(f"Kết nối từ: {address}")

    # Nhận dữ liệu
    data = client_socket.recv(1024).decode()

    print("Client gửi:", data)

    # Phản hồi
    response = f"Server đã nhận: {data}"

    client_socket.send(response.encode())

    # Đóng kết nối
    client_socket.close()