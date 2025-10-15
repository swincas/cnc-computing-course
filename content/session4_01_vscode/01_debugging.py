#Lukas Steinwender
#%%imports

#%%definitions
def increment(i):
    i += 1
    print(f"incremented: {i}")
    return

#%%main
def main():
    for i in range(10):
        increment(i)
        print(i)

if __name__ == "__main__":
    main()