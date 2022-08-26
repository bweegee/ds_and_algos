# https://www.hackerrank.com/challenges/new-year-chaos/problem
def scan (q):
    total = 0
    stack = [q[0]]
    for i in range(1, len(q)):
        last = i - 1
        if q[i] < q[last]:
            while stack and q[i] < stack[len(stack) - 1]:
                person = stack.pop()
                skip = person - (last + 1)
                last -= 1
                if skip >= 3:
                    return 'Too chaotic'
                elif skip <= 0:
                    total += 1
                else:
                    total += skip
        stack.append(q[i]) 
    return total
    
def minimumBribes(q):
    print(scan(q))
