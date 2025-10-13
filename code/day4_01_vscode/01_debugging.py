#%%imports

#%%definitions
def increment(i):
    i += 1
    print(f"incremented: {i}")
    return

#%%main
for i in range(10):
    increment(i)
    print(i)
