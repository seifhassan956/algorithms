import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import numpy as np
import time

# Visual parameters
BAR_WIDTH = 0.5
BAR_SPACING = 0.5
VAL_Y_SPACING = -3
ALIGNMENT = 'center'
BAR_COLOR = '#08fc0c'
HIGHLIGHT_COLOR = 'white'
EDGE_COLOR = 'black'
DELAY = 60
BG = 'black'
TEXT_COLOR = 'white'
# GRID_COLOR = 'white'

class SortVisualizer:
    """
        A class to visualize sorting algorithms with matplotlib animations
    """
    
    def __init__(self, size: int = 100, min_val: int = 10, max_val: int = 100, array: list[int] = None) -> None:
        self.size = size
        self.min_val = min_val
        self.max_val = max_val
        self.array = self.gen_array() if array is None else array
        
        # Setup figure
        self.fig , self.ax = plt.subplots(figsize=(15, 6))  # Wider figure
        
        # Set axes background to black
        self.ax.set_facecolor(BG)

        # Create bars with spacing
        self.bars = self.ax.bar(
                                range(self.size),       # 1. x-coordinates of the bars (positions)
                                self.array,             # 2. Heights of the bars (values)
                                width= BAR_WIDTH,       # 4. Width of each bar
                                align= ALIGNMENT,       # 5. Alignment of bars relative to their x-position
                                color= BAR_COLOR,           # 6. Color of the bars
                                edgecolor= EDGE_COLOR   # 7. Edge color of the bars
        )
        
        # Position labels
        VAL_Y_SPACING = -0.02 * self.max_val

        # Text values under each bar
        self.value_texts = [
                            self.ax.text(i, VAL_Y_SPACING, str(val), ha= ALIGNMENT, va='top', fontsize=9 , color= TEXT_COLOR)
                            for i, val in enumerate(self.array)
        ]
        
        # Adjust axes
        self.ax.set_xlim(-1 - BAR_SPACING, self.size + BAR_SPACING)
        self.ax.set_ylim(VAL_Y_SPACING - 5, self.max_val + 10)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_title('Sorting Algorithm Visualizer')
        
        # Add grid with custom styling
        # self.ax.grid(True, color= GRID_COLOR, linestyle='--', linewidth=0.5, alpha=0.3)
        
        # Available algorithms
        self.algorithms = {
            'Bubble Sort': self.bubble_sort_gen,
            'Insertion Sort': self.insertion_sort_gen,
            'Merge Sort': self.merge_sort_gen,
            'Quick Sort': self.quick_sort_gen
        }
    
    def gen_array(self) -> list[int]:
        """
            Generate a random array of integers
        """
        import numpy as np

        return np.random.randint(self.min_val , self.max_val + 1 , self.size , dtype = int)
    
    def update_fig(self, frame):
        """
            Update the bar heights, colors, and value labels for animation.
        """
        arr, highlights = frame
 
        # Update bars
        for bar , height in zip(self.bars, arr):
            bar.set_height(height)
        
        # Update values
        for text, val in zip(self.value_texts, arr):
            text.set_text(str(val))
        
        # Highlight active elements
        for i, bar in enumerate(self.bars):
            if i in highlights:
                bar.set_color(HIGHLIGHT_COLOR)
            else:
                bar.set_color(BAR_COLOR)

        # Update the title with execution time (this will update on each frame)
        self.elapsed_time = time.time() - self.start_time
        self.ax.title.set_text(f'{self.algorithm_name} - Execution Time: {self.elapsed_time:.4f} seconds')
        
        # Convert both to lists before concatenation
        return list(self.bars) + self.value_texts
    
    def bubble_sort_gen(self):
        """
            Generator function for bubble sort visualization
        """

        arr = self.array.copy()
        
        for i in range(self.size):
            swapped = False
            for j in range(self.size - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

                         #array , highlighted elements indices
                    yield arr, [j, j + 1]  # Highlight the swapped elements
            
            if not swapped:
                break
        
        yield arr, list(range(self.size))  # All elements highlighted when sorted
        print("Sorted array: ",arr)
    
    def insertion_sort_gen(self):
        """Generator function for insertion sort visualization."""
        pass
    
    def quick_sort_gen(self):
        """Generator function for selection sort visualization."""
        start = 0

        self.array = self.array.tolist() if isinstance(self.array, np.ndarray) else self.array
        arr = self.array.copy()

        end = len(arr) - 1

        def _quick_sort(arr, start, end):
                if start >= end:
                    return

                pivot = arr[end]  # Choosing the last element as the pivot
                i = start - 1  # Initialize i before partitioning

                for j in range(start, end):
                    if arr[j] < pivot:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
                        yield arr, [i, j]  # Yield the full array with swapped indices

                # Place pivot in its correct position
                i += 1
                arr[i], arr[end] = arr[end], arr[i]
                yield arr, [i, end]  # Highlight pivot swap

                pivot_index = i

                # Recursively apply quicksort on left and right partitions
                yield from _quick_sort(arr, start, pivot_index - 1)
                yield from _quick_sort(arr, pivot_index + 1, end)

        yield from _quick_sort(arr, 0, len(arr) - 1)
        yield arr, list(range(len(self.array)))
        print("sorted array: " , arr)

    def merge_sort_gen(self):
        """
            Generator function for merge sort visualization.
            Yields the array state after each merge operation with highlighted elements.
        """

        self.array = self.array.tolist() if isinstance(self.array, np.ndarray) else self.array
        arr = self.array.copy()


        def _merge_sort(arr):
            if len(arr) <= 1:
                yield arr, []  # Base case
                return arr  # Return sorted list

            mid = len(arr) // 2
            
            left = yield from _merge_sort(arr[:mid])  # Recursively sort left
            right = yield from _merge_sort(arr[mid:])  # Recursively sort right

            merged = []
            highlight = []
            l = r = 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    highlight.append(self.array.index(left[l]))
                    l += 1
                else:
                    merged.append(right[r])
                    highlight.append(self.array.index(right[r]))
                    r += 1
            
            merged.extend(left[l:])
            highlight.extend([self.array.index(x) for x in merged[l:]])

            merged.extend(right[r:])
            highlight.extend([self.array.index(x) for x in merged[r:]])

            if len(merged) == len(self.array):
                highlight = list(range(len(self.array)))
                print("sorted array: " , merged)

            yield merged, highlight
            return merged

        yield from _merge_sort(arr)
    
    def animate(self, algorithm_name: str = 'Bubble Sort', interval: int = DELAY):
        """
        Animate the sorting algorithm.
        
        Parameters:
            algorithm_name (str): Name of the algorithm to visualize
            interval (int): Delay between frames in milliseconds
        """
        if algorithm_name not in self.algorithms:
            raise ValueError(f"Algorithm '{algorithm_name}' not available")
        
        # Store the algorithm name and start time for dynamic title update
        self.algorithm_name = algorithm_name
        self.start_time = time.time()
            
        # calls specified algorithm fn
        generator = self.algorithms[algorithm_name]()
        

        anim = FuncAnimation(
                            self.fig,
                            func=self.update_fig,
                            frames=generator,
                            interval=interval,          # Delay between frames
                            repeat=False,
                            blit=False,                  # Optimize rendering (only redraw changed elements)
                            #save_count=1000            # Buffer for animation frames
                            cache_frame_data=False      # Prevents memory-intensive caching that isn't needed.
        )
        
        plt.show()
        # return HTML(anim.to_jshtml())
    