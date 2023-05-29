import socket

# Configurações do servidor
host = '127.0.0.1'  # Endereço IP do servidor
port = 8080  # Porta do servidor

# Criação do socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket à porta e endereço IP
server_socket.bind((host, port))

# Coloca o socket em modo de escuta
server_socket.listen(1)
print(f"Servidor TCP escutando em {host}:{port}")

# Aguarda por uma conexão
client_socket, client_address = server_socket.accept()
print(f"Conexão estabelecida com {client_address[0]}:{client_address[1]}")

# Recebe dados do cliente
data = client_socket.recv(1024).decode('utf-8')
print(f"Dados recebidos do cliente: {data}")

# Envia uma resposta ao cliente
response = "Olá, cliente! Recebi sua mensagem."
client_socket.send(response.encode('utf-8'))

# Fecha as conexões e o socket do servidor
client_socket.close()
server_socket.close()
