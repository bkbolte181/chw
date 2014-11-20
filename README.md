chw
===

Homework calendar project that I've had kicking around for a while. Basically the idea is that users can see all their homework assignments in one place. It will also have a simple API that you can integrate with other services (e.g. Blackboard, WebAssign, etc). An open-source version of this idea seems pretty badly needed, although my weak coding skills may not be up to the task...

Completely unrelated: This is a bit of code to find how many unique partitions a particular number has. For example, the number 4 has 5 partitions, [4], [1, 3], [1, 1, 2], [1, 1, 1, 1] and [2, 2]. Is there a more efficient way to do this? The algorithm seems pretty heavy.

```python
def main():
    for i in range(1, 20):
        p = partitions(i, [], 1)
        print 'There are', p, 'partitions for the number', i

def partitions(num, current, min):
  total = 0
  if num == 0:
    return 1
  for i in range(min, num+1):
    tmp = current[:] + [i]
    total = total + partitions(num-i, tmp, i)
  return total

main()
```
