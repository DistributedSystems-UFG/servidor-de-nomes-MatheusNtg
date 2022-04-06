from random import choice, randint
import rpyc
from consts import * #-

conn_name_server = rpyc.connect(NAME_SERVER_HOST, NAME_SERVER_PORT)

conn_details_server1 = conn_name_server.root.exposed_lookup(SERVER1_NAME)
conn_details_server2 = conn_name_server.root.exposed_lookup(SERVER2_NAME)

conn_server1 = rpyc.connect(conn_details_server1["ip"], conn_details_server1["port"])
conn_server2 = rpyc.connect(conn_details_server2["ip"], conn_details_server2["port"])


for i in range(10):
	op1 = randint(0, 100)
	op2 = randint(0, 100)
	operand = choice(["+", "-", "*", "/"])

	server1_response = None
	server2_response = None
	if operand == "+":
		server1_response = conn_server1.root.exposed_sum(op1, op2)
		server2_response = conn_server2.root.exposed_sum(op1, op2)
	elif operand == "-":
		server1_response = conn_server1.root.exposed_sub(op1, op2)
		server2_response = conn_server2.root.exposed_sub(op1, op2)
	elif operand == "*":
		server1_response = conn_server1.root.exposed_mult(op1, op2)
		server2_response = conn_server2.root.exposed_mult(op1, op2)
	elif operand == "/":
		server1_response = conn_server1.root.exposed_div(op1, op2)
		server2_response = conn_server2.root.exposed_div(op1, op2)

	print(server1_response)
	print(server2_response)
		