from consts import *

import rpyc
from rpyc.utils.server import ThreadedServer


class NameServer(rpyc.Service):
	names = dict()

	def exposed_register(self, name, ip, port):
		if name in dict.keys(self.names):
			print(f"ERROR: name {name} already exists in the directory")
			raise Exception(f"name {name} already exists in the directory")
		
		self.names[name] = {
			"ip":ip,
			"port": port,
		}

		print(f"{name} binded to {ip}:{port}")
	
	def exposed_lookup(self, name):
		if name not in dict.keys(self.names):
			raise Exception(f"there is no name {name} registered in the directory")
		
		return self.names[name]

if __name__ == "__main__":
	server = ThreadedServer(NameServer(), hostname=NAME_SERVER_HOST, port=NAME_SERVER_PORT)
	server.start()
