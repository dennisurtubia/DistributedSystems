# Dennis Felipe Urtubia
# Neste código se encontra o registro dos métodos que irão ser acessados de forma remota

import Pyro4
from Controller import Controller

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(Controller)
ns.register("ControllerService", uri)

print("Objeto registrado.")
daemon.requestLoop()
