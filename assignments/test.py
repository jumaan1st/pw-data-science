from memory_profiler import profile

@profile
def create_list():
    # Create a large list to see memory usage
    data = [i for i in range(1000000)]
    print("List created with", len(data), "elements.")

@profile
def main():
    create_list()

if __name__ == "__main__":
    main()
