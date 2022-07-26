from http.client import LineTooLong
import os
import sys

# filename = input("filename: ")
# with open(filename, "w+") as f:
#   while True:
#       try:
#           f.write(input())
#           f.write("\n")
#       except EOFError:
#           break
# def multi_input():
#     try:
#         while True:
#             data=input()
#             if not data: break
#             yield data
#     except KeyboardInterrupt:
#         return

filename = input("filename: ")
with open(filename, "w+") as f:
  f.write(input())


