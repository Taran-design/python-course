total_calls = 0
def countdown(n):
    global total_calls
    total_calls += 1
    print("Function call:", total_calls, "countdown(",n,")", sep=" ")
    if n <= 0:
        print("Blast off")
        return
    print(n)
    countdown(n-1)
print("Starting countdown")
countdown(5)
print("Total function calls: ",total_calls)