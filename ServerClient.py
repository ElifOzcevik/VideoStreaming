#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def startServer1(node):
    node.cmd('cd /home/elif/httpServer')
    node.cmd('xterm -e sudo python -m SimpleHTTPServer 80 &')

def startClient(node):
    node.cmd('xterm -e chromium-browser --no-sandbox --user-data-dir=http://10.0.0.1 &')
    #node.cmd('xterm -e firefox --user-data-dir=http://10.0.0.1 --enable-logging &')

def emptyNet():

    "Create an empty network and add nodes to it."

    #net = Mininet( controller=Controller )
    net = Mininet( controller=RemoteController) 	

    info( '*** Adding controller\n' )
    net.addController( '127.0.0.1' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1')
    h2 = net.addHost( 'h2', ip='10.0.0.2')

    info( '*** Adding switch\n' )
    s3 = net.addSwitch( 's3' )

    info( '*** Creating links\n' )
    net.addLink( h1, s3 )
    net.addLink( h2, s3 )

    info( '*** Starting network\n')
    net.start()

    startServer1(h1)
    startClient(h2)

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
