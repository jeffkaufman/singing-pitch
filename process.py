ranges = []
with open("data.txt") as inf:
  for line in inf:
    high, low = [int(x) for x in line.strip().split()]
    ranges.append((low, high))

def compatible_ranges(interval_low, interval_high):
  r = []
  for singer_low, singer_high in ranges:
    while singer_low > interval_low:
      singer_low -= 12
      singer_high -= 12
    if interval_high <= singer_high:
      r.append((singer_low, singer_high))
  return r  

for interval in range(7, 24):
  half_interval_up = int(interval/2.0 + 0.5)
  half_interval_down = int(interval/2.0)

  midpoint = True
  print("\t".join([
        "%.2f" % ((len(ranges)-(len(compatible_ranges(
                  note - half_interval_down if midpoint else note,
                  note + half_interval_up if midpoint else note + interval)
                                    )))/len(ranges))
        for note in range(12)]))
