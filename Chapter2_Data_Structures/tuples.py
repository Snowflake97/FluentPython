t = (20, 8)
print("divmod(20, 8) = (%s, %s)" % divmod(*t))

a, b, *tail = range(5)
print("{}, {}, {}".format(a, b, tail))

a, *body, b = range(5)
print("{}, {}, {}".format(a, body, b))

*head, a, b = range(5)
print("{}, {}, {}".format(head, a, b))

colors = ['red', 'blue', 'black']
sizes = ['S', 'M', 'L']

shirts = tuple((color, size) for color in colors
               for size in sizes)
print(shirts)

print("{:15} | {:9.4f} |".format("testString", 5.4044))
