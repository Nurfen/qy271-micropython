from qy271 import QY271

Q = QY271(scl=13, sda=14)
for i in range(10):
    print(Q.get_bearing())