if __name__ == "__main__":
    from visualizerClass import SortVisualizer
    import numpy as np
    
    arr = np.random.randint(10 , 100 , 50 , dtype = int)

    print(arr)

    visualizer = SortVisualizer(size=50, min_val=10, max_val=100 , array = arr)
    visualizer.animate('Merge Sort', interval=30)
    print(visualizer.algorithm_name , visualizer.elapsed_time)
    print("*" * 100)

    visualizer = SortVisualizer(size=50, min_val=10, max_val=100 , array = arr)
    visualizer.animate('Quick Sort', interval=30)
    print(visualizer.algorithm_name , visualizer.elapsed_time)
    print("*" * 100)

    visualizer = SortVisualizer(size=50, min_val=10, max_val=100 , array = arr)
    visualizer.animate('Bubble Sort', interval=30)
    print(visualizer.algorithm_name , visualizer.elapsed_time)
