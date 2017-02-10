def segment_length(p, q): return p - q

def point_on_line(p, q, d): return p + d

d = 2
temp = 0

points = [1,5,9,27,28,30,42]
# points = range(0,20,1)


points.append(points[-1])
points.reverse()
current = points.pop()
next = points.pop()
output = [current]

while points:
    seg_len = segment_length(next, current)
    print points
    print current, next, temp
   
    if (seg_len == d - temp):
        output.append(next)
        temp = 0
        current = next
        next = points.pop()

    elif (seg_len > d - temp):
        p = point_on_line(current, next, d - temp)
        output.append(p)
        temp = 0
        current = p

    elif (seg_len < d - temp):
        temp += seg_len
        current = next
        next = points.pop()

output.append(current)
if output[-1] == output[-2]: output.pop()

print points
print ''
print output