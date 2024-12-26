#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
  # initialize window
  stdkeys.create_window()
  pluckedStrings = set()
  keyboard = "q2we4r5ty7u8i9op-[=]"
  n_iters = 0
  while True:
    # it turns out that the bottleneck is in polling for key events
    # for every iteration, so we'll do it less often, say every
    # 1000 or so iterations
    if n_iters == 1000:
      stdkeys.poll()
      n_iters = 0
    n_iters += 1

    # check if the user has typed a key; if so, process it
    if stdkeys.has_next_key_typed():
      key = stdkeys.next_key_typed()
      if key in keyboard:
        string = GuitarString(440 * 1.059463**(keyboard.index(key) - 12)) 
        string.pluck()
        pluckedStrings.add(string)

    sample = 0
    for i in pluckedStrings:
      i.sample()
      sample += i.sample()
      i.tick()
      if i.time() > 44100*1.5:
        pluckedStrings.remove(i)
        break
    play_sample(sample)