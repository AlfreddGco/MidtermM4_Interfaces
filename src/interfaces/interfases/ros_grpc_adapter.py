#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor

import rclpy, grpc
from rclpy.node import Node 
from std_msgs.msg import Int32MultiArray

from interfases import interfases_pb2_grpc
from interfases.interfases_pb2 import Coordinate

PORT = 50051

class CoordinateRosGrpcAdapter(Node, interfases_pb2_grpc.LocationTrackerServicer):
  def __init__(self):
    Node.__init__(self, 'ros_grpc_adapter')
    interfases_pb2_grpc.LocationTrackerServicer.__init__(self)
    self.x, self.y = -1, -1
    self.create_subscription(Int32MultiArray,
      '/coordinates', self.handleRosCoordinates, 10)

  def handleRosCoordinates(self, msg):
    self.x, self.y = msg.data

  def getCoordinate(self, req, ctx):
    return Coordinate(x = self.x, y = self.y)


def main():
  rclpy.init()
  node = CoordinateRosGrpcAdapter()

  server = grpc.server(ThreadPoolExecutor(max_workers = 10))
  server.add_insecure_port(f'[::]:{PORT}')

  interfases_pb2_grpc.add_LocationTrackerServicer_to_server(
    node, server)

  try:
    print(f"Starting grpc server listening on port {PORT}")
    server.start()
    rclpy.spin(node)
  except:
    pass
  finally:
    rclpy.shutdown()
    server.wait_for_termination()


if __name__ == '__main__':
  main()

