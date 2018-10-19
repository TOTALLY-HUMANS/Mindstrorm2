import rpyc

conn = rpyc.connect('192.168.2.2', port=18812)
conn.root.line_follower()
