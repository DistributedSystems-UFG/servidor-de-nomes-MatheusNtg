import socket
from consts import *

import rpyc
from rpyc.utils.server import ThreadedServer

SERVER1_PORT = 5020

def get_ip():
	host_name = socket.gethostname()
	ip = socket.gethostbyname(host_name)
	return ip

class Calculator(rpyc.Service):
	def exposed_sum(self, op1, op2):
		print(f"received sum operation with operands {op1} and {op2}")
		return {
			"server_name": SERVER1_NAME,
			"result": op1 + op2
		}

	def exposed_mult(self, op1, op2):
		print(f"received mult operation with operands {op1} and {op2}")
		return {
			"server_name": SERVER1_NAME,
			"result":op1 * op2
		}

	def exposed_div(self, op1, op2):
		print(f"received div operation with operands {op1} and {op2}")
		return {
			"server_name": SERVER1_NAME,
			"result":op1 / op2
		}

	def exposed_sub(self, op1, op2):
		print(f"received sub operation with operands {op1} and {op2}")
		return {
			"server_name": SERVER1_NAME,
			"result":op1 - op2
		}

if __name__ == "__main__":
	server_name_conn = rpyc.connect(NAME_SERVER_HOST, NAME_SERVER_PORT)
	my_ip = get_ip()
	try:
		print(f"Trying to registry: {SERVER1_NAME} -> {my_ip}:{SERVER1_PORT}")
		server_name_conn.root.exposed_register(SERVER1_NAME, my_ip, SERVER1_PORT)
	except:
		print("Failed to register server in the name server")
		exit()
	print("Successfully registry in the name server")
	server = ThreadedServer(Calculator(), hostname= my_ip, port = SERVER1_PORT)
	server.start()