#!/usr/bin/env python3
from ringbuffer import RingBuffer
import random

class GuitarString:

  def __init__(self, frequency: float):
    self.capacity = (int(44100 / frequency)+1)
    self.buffer = RingBuffer(self.capacity)
    self.numticks = 0

  @classmethod
  def make_from_array(cls, init: list[int]):
    stg = cls(1000)
    stg.capacity = len(init)
    stg.buffer = RingBuffer(stg.capacity)
    for x in init:
      stg.buffer.enqueue(x)
    return stg

  def pluck(self):
    self.numticks = 0
    if not self.buffer.is_empty():
      for i in range(self.capacity):
        self.buffer.dequeue()
    while not self.buffer.is_full():
      self.buffer.enqueue(random.uniform(-0.5, 0.5))

  def tick(self):
    self.buffer.enqueue(0.996 * 0.5 * (self.buffer.dequeue() + self.buffer.peek()))
    self.numticks += 1

  def sample(self) -> float:
    return self.buffer.peek()

  def time(self) -> int:
    return self.numticks
