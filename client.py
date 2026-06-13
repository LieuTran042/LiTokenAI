import socket

# Khởi tạo socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 9999

# Kết nối tới server
client.connect((HOST, PORT))

message = input("Nhập tin nhắn: ")

# Gửi dữ liệu
client.send(message.encode())

# Nhận phản hồi
response = client.recv(1024).decode()

print("Server trả về:", response)

# Đóng kết nối
client.close()