import math
import random
import pygame
import time
import tkinter as tk
from tkinter import messagebox, ttk
import sys
from collections import deque
import heapq
import psutil
import os
import tracemalloc
from tkinter import font as tkfont

# Định nghĩa trạng thái đích
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def find_zero(state):
    """Tìm vị trí ô trống (0) trong bảng"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    """Tạo danh sách trạng thái có thể di chuyển"""
    x, y = find_zero(state)
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

def bfs(initial_state):
    """Thuật toán BFS để tìm lời giải"""
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        state, path = queue.popleft()
        if state == GOAL_STATE:
            return path + [state]
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [state]))
    
    return None

def dfs(initial_state):
    """Thuật toán DFS để tìm lời giải"""
    stack = [(initial_state, [])]
    visited = set()
    
    while stack:
        state, path = stack.pop()
        
        if state == GOAL_STATE:
            return path + [state]
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                stack.append((neighbor, path + [state]))
    
    return None

def uniform_cost_search(initial_state):
    """Thuật toán Uniform Cost Search (UCS)"""
    pq = [(0, initial_state, [])]
    visited = set()
    
    while pq:
        cost, state, path = heapq.heappop(pq)
        
        if state == GOAL_STATE:
            return path + [state]
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                heapq.heappush(pq, (cost + 1, neighbor, path + [state]))
    
    return None

def iterative_deepening(initial_state, max_depth=20):
    """Thuật toán ID"""
    def dls(state, path, depth):
        if state == GOAL_STATE:
            return path + [state]
        if depth == 0:
            return None
        
        for neighbor in get_neighbors(state):
            result = dls(neighbor, path + [state], depth - 1)
            if result:
                return result
        
        return None
    
    for depth in range(max_depth):
        result = dls(initial_state, [], depth)
        if result:
            return result
    return None

def greedy(initial_state):
    """Thuật toán Greedy """
    def heuristic(state):
        return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))
    
    pq = [(heuristic(initial_state), initial_state, [])]
    visited = set()
    
    while pq:
        _, state, path = heapq.heappop(pq)
        
        if state == GOAL_STATE:
            return path + [state]
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                heapq.heappush(pq, (heuristic(neighbor), neighbor, path + [state]))
    
    return None

def heuristic(state):
    return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))

def simple_hill_climbing(initial_state):
    """Thuật toán Simple Hill Climbing"""
    current = initial_state
    path = [current]  # Lưu lại đường đi
    
    while True:
        neighbors = get_neighbors(current)
        next_state = min(neighbors, key=heuristic, default=None)
        
        if next_state and heuristic(next_state) < heuristic(current):
            current = next_state
            path.append(current)
        else:
            return path  # Trả về toàn bộ đường đi

def astar(initial_state):
    """Thuật toán A* để tìm lời giải"""
    def heuristic(state):
        return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))
    
    pq = [(heuristic(initial_state), initial_state, [])]
    visited = set()
    
    while pq:
        _, state, path = heapq.heappop(pq)
        
        if state == GOAL_STATE:
            return path + [state]
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                heapq.heappush(pq, (heuristic(neighbor), neighbor, path + [state]))
    
    return None

def ida_star(initial_state):
    """Thuật toán IDA* để tìm lời giải"""
    def heuristic(state):
        return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))
    
    def search(state, path, g, threshold):
        f = g + heuristic(state)
        if f > threshold:
            return f, None
        if state == GOAL_STATE:
            return f, path + [state]
        
        min_threshold = float("inf")
        for neighbor in get_neighbors(state):
            if neighbor not in path:
                new_threshold, result = search(neighbor, path + [state], g + 1, threshold)
                if result:
                    return new_threshold, result
                min_threshold = min(min_threshold, new_threshold)
        
        return min_threshold, None

    threshold = heuristic(initial_state)
    while True:
        new_threshold, result = search(initial_state, [], 0, threshold)
        if result:
            return result
        if new_threshold == float("inf"):
            return None
        threshold = new_threshold

def steepest_ascent_hill_climbing(initial_state):
    current = initial_state
    path = [current]
    while True:
        neighbors = get_neighbors(current)
        best_neighbor = min(neighbors, key=heuristic, default=None)
        if best_neighbor and heuristic(best_neighbor) < heuristic(current):
            current = best_neighbor
            path.append(current)
        else:
            return path

def stochastic_hill_climbing(initial_state):
    current = initial_state
    path = [current]
    while True:
        neighbors = get_neighbors(current)
        better_neighbors = [n for n in neighbors if heuristic(n) < heuristic(current)]
        if better_neighbors:
            current = random.choice(better_neighbors)
            path.append(current)
        else:
            return path

def simulated_annealing(initial_state, max_iterations=10000, initial_temp=100, cooling_rate=0.99):
    current = initial_state
    path = [current]
    temp = initial_temp
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current)
        if not neighbors:
            break
        
        next_state = random.choice(neighbors)
        delta_e = heuristic(current) - heuristic(next_state)
        
        if delta_e > 0 or math.exp(delta_e / temp) > random.random():
            current = next_state
            path.append(current)
        
        temp *= cooling_rate
        if heuristic(current) == 0:
            break
    
    return path

def beam_search(initial_state, beam_width=2):
    """Thuật toán Beam Search"""
    queue = [(heuristic(initial_state), initial_state, [])]
    
    while queue:
        queue.sort()
        queue = queue[:beam_width]  # Chỉ giữ lại số lượng trạng thái tốt nhất theo beam_width
        new_queue = []
        
        for _, state, path in queue:
            if state == GOAL_STATE:
                return path + [state]
            
            for neighbor in get_neighbors(state):
                new_queue.append((heuristic(neighbor), neighbor, path + [state]))
        
        queue = new_queue
    
    return None

def backtracking_search(initial_state, max_depth=30):
    """Thuật toán Backtracking Search để giải 8-Puzzle"""
    visited = set()

    def backtrack(state, path, depth):
        if state == GOAL_STATE:
            return path + [state]
        if depth == 0:
            return None
        
        visited.add(tuple(map(tuple, state)))

        for neighbor in get_neighbors(state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                result = backtrack(neighbor, path + [state], depth - 1)
                if result:
                    return result
        
        visited.remove(tuple(map(tuple, state)))  # Quay lui: bỏ khỏi visited
        return None

    return backtrack(initial_state, [], max_depth)

def local_search_csp(initial_state, max_steps=10000):
    """Thuật toán Local Search cho CSP - Min-Conflicts"""
    
    def conflicts(state):
        # Số lượng ô sai vị trí
        return sum(state[i][j] != GOAL_STATE[i][j] for i in range(3) for j in range(3))
    
    current = initial_state
    path = [current]
    
    for step in range(max_steps):
        if conflicts(current) == 0:
            return path  # Đã đạt mục tiêu
        
        neighbors = get_neighbors(current)
        if not neighbors:
            break
        
        # Chọn neighbor ít conflict nhất
        next_state = min(neighbors, key=conflicts)
        if conflicts(next_state) >= conflicts(current):
            # Không cải thiện -> chọn ngẫu nhiên neighbor
            next_state = random.choice(neighbors)
        
        current = next_state
        path.append(current)
    
    return path  # Nếu max_steps hết mà chưa đến goal thì trả về đường đi đã thực hiện

def draw_board(state, screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    TILE_SIZE = 100
    
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                pygame.draw.rect(screen, (100, 100, 250), (j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                text = font.render(str(value), True, (255, 255, 255))
                screen.blit(text, (j*TILE_SIZE + TILE_SIZE//3, i*TILE_SIZE + TILE_SIZE//3))
    
    pygame.display.flip()

def visualize_solution(solution, delay=500):
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("8-Puzzle Solver")
    
    for step in range(len(solution)):
        draw_board(solution[step], screen)
        pygame.time.wait(delay)  # Tự động chuyển sau 'delay' mili-giây
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    
    pygame.time.wait(2000)  # Đợi 2 giây trước khi đóng cửa sổ
    pygame.quit()

def evaluate_algorithm(algorithm_func, initial_state):
    """Đánh giá hiệu suất của thuật toán"""
    # Bắt đầu theo dõi bộ nhớ
    tracemalloc.start()
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    # Bắt đầu đo thời gian
    start_time = time.time()
    
    # Chạy thuật toán
    solution = algorithm_func(initial_state)
    
    # Kết thúc đo thời gian
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Kết thúc theo dõi bộ nhớ
    current_memory = process.memory_info().rss / 1024 / 1024  # MB
    max_memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # MB
    tracemalloc.stop()
    
    # Tính số bước
    steps = len(solution) - 1 if solution else 0
    
    return {
        "execution_time": execution_time,
        "initial_memory": initial_memory,
        "current_memory": current_memory,
        "max_memory": max_memory,
        "steps": steps,
        "solution": solution
    }

def start_solver():
    """Xử lý khi nhấn nút 'Giải' trong Tkinter"""
    try:
        initial_state = [[int(entry.get()) for entry in row] for row in entries]
        algorithm = algorithm_var.get()
        
        algorithms = {
            "BFS": bfs,
            "DFS": dfs,
            "UCS": uniform_cost_search,
            "ID": iterative_deepening,
            "Greedy": greedy,
            "A*": astar,
            "IDA*": ida_star,
            "Simple Hill Climbing": simple_hill_climbing,
            "Steepest Ascent Hill Climbing": steepest_ascent_hill_climbing,
            "Stochastic Hill Climbing": stochastic_hill_climbing,
            "Simulated Annealing": simulated_annealing,
            "Beam Search": beam_search,
            "Backtracking": backtracking_search,
            "Local Search CSP": local_search_csp
        }
        
        # Đánh giá thuật toán
        results = evaluate_algorithm(algorithms[algorithm], initial_state)
        
        if results["solution"]:
            # Hiển thị kết quả đánh giá
            evaluation_message = f"""Kết quả đánh giá thuật toán {algorithm}:
Thời gian thực thi: {results['execution_time']:.5f} giây
Bộ nhớ ban đầu: {results['initial_memory']:.5f} MB
Bộ nhớ hiện tại: {results['current_memory']:.5f} MB
Bộ nhớ tối đa: {results['max_memory']:.5f} MB
Số bước thực hiện: {results['steps']}"""
            
            messagebox.showinfo("Kết quả đánh giá", evaluation_message)
            visualize_solution(results["solution"])
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy lời giải.")
            
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số cho trạng thái ban đầu.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("8-Puzzle Solver")
    root.configure(bg='#f0f0f0')
    
    # Set window size and position
    window_width = 500
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Create main frame with padding
    main_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)
    main_frame.pack(expand=True, fill='both')
    
    # Title
    title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
    title_label = tk.Label(main_frame, text="8-Puzzle Solver", font=title_font, bg='#f0f0f0', fg='#2c3e50')
    title_label.pack(pady=(0, 20))
    
    # Create frame for puzzle input
    input_frame = tk.LabelFrame(main_frame, text="Nhập trạng thái ban đầu", font=("Helvetica", 12), 
                              bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
    input_frame.pack(pady=10, fill='x')
    
    # Create grid for entries with custom styling
    entries = []
    for i in range(3):
        row_entries = []
        for j in range(3):
            entry = tk.Entry(input_frame, width=5, font=("Helvetica", 20), justify="center",
                           bg='#ffffff', fg='#2c3e50', relief='solid', bd=1)
            entry.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
            row_entries.append(entry)
        entries.append(row_entries)
    
    # Configure grid weights
    for i in range(3):
        input_frame.grid_columnconfigure(i, weight=1)
        input_frame.grid_rowconfigure(i, weight=1)
    
    # Algorithm selection frame
    algo_frame = tk.LabelFrame(main_frame, text="Chọn thuật toán", font=("Helvetica", 12),
                             bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
    algo_frame.pack(pady=10, fill='x')
    
    # Style for combobox
    style = ttk.Style()
    style.configure('Custom.TCombobox', 
                   fieldbackground='#ffffff',
                   background='#ffffff',
                   foreground='#2c3e50',
                   arrowcolor='#2c3e50')
    
    algorithm_var = tk.StringVar(root)
    algorithm_var.set("BFS")
    algorithms = ["BFS", "DFS", "UCS", "ID", "Greedy", "A*", "IDA*", 
                 "Simple Hill Climbing", "Steepest Ascent Hill Climbing", 
                 "Stochastic Hill Climbing", "Simulated Annealing", 
                 "Beam Search", "Backtracking", "Local Search CSP"]
    
    algo_combo = ttk.Combobox(algo_frame, textvariable=algorithm_var, 
                             values=algorithms, state="readonly",
                             font=("Helvetica", 12), style='Custom.TCombobox')
    algo_combo.pack(fill='x', padx=5, pady=5)
    
    # Solve button with custom styling
    solve_button = tk.Button(main_frame, text="Giải", command=start_solver,
                           font=("Helvetica", 14, "bold"),
                           bg='#3498db', fg='white',
                           activebackground='#2980b9',
                           activeforeground='white',
                           relief='flat',
                           padx=20, pady=10,
                           cursor='hand2')
    solve_button.pack(pady=20)
    
    # Add hover effect for button
    def on_enter(e):
        solve_button['background'] = '#2980b9'
    
    def on_leave(e):
        solve_button['background'] = '#3498db'
    
    solve_button.bind("<Enter>", on_enter)
    solve_button.bind("<Leave>", on_leave)
    
    # Add some instructions
    instructions = """Hướng dẫn:
1. Nhập trạng thái ban đầu của puzzle (0-8)
2. Chọn thuật toán giải
3. Nhấn 'Giải' để xem kết quả"""
    
    instruction_label = tk.Label(main_frame, text=instructions,
                               font=("Helvetica", 10),
                               bg='#f0f0f0', fg='#7f8c8d',
                               justify='left')
    instruction_label.pack(pady=10)
    
    root.mainloop()
