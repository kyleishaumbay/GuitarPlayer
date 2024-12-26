#!/usr/bin/env python3
class RingBuffer:

  def __init__(self, capacity: int):
    self.MAX_CAP = capacity
    self._front = 0
    self._rear = 0
    self.buffer = []
    self._size = 0
    
    for i in range(self.MAX_CAP):
      self.buffer.append(0)
      
  def size(self) -> int:

    return self._size

  def is_empty(self) -> bool:

    return self.size() == 0

  def is_full(self) -> bool:

    return self.size() == self.MAX_CAP

  def enqueue(self, x: float):
    
    if self.is_full():
      raise RingBufferFull(Exception)
    else:
      self.buffer[self._rear] = x
      if self._rear + 1 == self.MAX_CAP:
        self._rear = 0
      else:
        self._rear +=1
      self._size += 1

  def dequeue(self) -> float:
    if self.is_empty():
      raise RingBufferEmpty(Exception)
    else:

      temp = self.buffer[self._front]
      self.buffer[self._front] = 0
      if self._front + 1 == self.MAX_CAP:
        self._front = 0
      else:
      #because the default value is 0
        self._front += 1
      self._size -= 1
      return temp

  def peek(self) -> float:
    if self.is_empty():
      raise RingBufferEmpty(Exception)
    else:
      return self.buffer[self._front]

class RingBufferFull(Exception):
  pass

class RingBufferEmpty(Exception):
  pass

