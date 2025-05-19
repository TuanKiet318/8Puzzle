# 8-Puzzle Solver

## Mô tả
Chương trình giải bài toán 8-Puzzle sử dụng nhiều thuật toán tìm kiếm khác nhau. Mỗi thuật toán được đánh giá dựa trên thời gian thực thi, bộ nhớ sử dụng và số bước thực hiện.

## Test Cases

### 1. Đầu vào đơn giản
```
1 2 3
0 4 5
7 8 6
```

### 2. Đầu vào phức tạp
```
2 6 5
0 8 7
4 3 1
```
## Phân Tích Chi Tiết Từng Thuật Toán

### 1. BFS (Breadth-First Search)

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00127 giây
  - Bộ nhớ sử dụng: 0.00088 MB
  - Bộ nhớ tối đa: 0.00384 MB
  - Số bước thực hiện: 3

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.01562 giây
  - Bộ nhớ sử dụng: 0.00123 MB
  - Bộ nhớ tối đa: 0.00456 MB
  - Số bước thực hiện: 23

#### Nhận xét
- **Độ phức tạp thời gian:** O(b^d)
  - b: số nhánh trung bình
  - d: độ sâu của lời giải
- **Độ phức tạp không gian:** O(b^d)
- **Ưu điểm:** 
  - Luôn tìm được lời giải tối ưu
  - Đảm bảo tìm được đường đi ngắn nhất
  - Hiệu quả với không gian tìm kiếm nhỏ
- **Nhược điểm:** 
  - Tiêu tốn nhiều bộ nhớ cho các trường hợp phức tạp
  - Thời gian thực thi tăng nhanh với độ sâu của cây tìm kiếm
  - Không hiệu quả với không gian tìm kiếm lớn
 > ![BFS Animation](images/BFS.gif)
### 2. DFS (Depth-First Search)

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00098 giây
  - Bộ nhớ sử dụng: 0.00076 MB
  - Bộ nhớ tối đa: 0.00312 MB
  - Số bước thực hiện: 3
 > ![DFS Animation](images/DFS.gif)
#### Đầu vào phức tạp
- **Evaluation:**
  - Số bước thực hiện: Không giải được

#### Nhận xét
- **Độ phức tạp thời gian:** O(b^m)
  - b: số nhánh trung bình
  - m: độ sâu tối đa của cây tìm kiếm
- **Độ phức tạp không gian:** O(b*m)
- **Ưu điểm:**
  - Sử dụng ít bộ nhớ hơn BFS
  - Hiệu quả với các bài toán có nhiều nhánh giải
  - Dễ cài đặt và triển khai
- **Nhược điểm:**
  - Không đảm bảo tìm được lời giải tối ưu
  - Có thể đi vào nhánh không hiệu quả
  - Thời gian thực thi không ổn định

### 3. UCS (Uniform Cost Search)

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00135 giây
  - Bộ nhớ sử dụng: 0.00095 MB
  - Bộ nhớ tối đa: 0.00392 MB
  - Số bước thực hiện: 3

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.01678 giây
  - Bộ nhớ sử dụng: 0.00128 MB
  - Bộ nhớ tối đa: 0.00467 MB
  - Số bước thực hiện: 23
 > ![UCS Animation](images/UCS.gif)
#### Nhận xét
- **Độ phức tạp thời gian:** O(b^C*/ε)
  - b: số nhánh trung bình
  - C*: chi phí của lời giải tối ưu
  - ε: chi phí tối thiểu của mỗi bước
- **Độ phức tạp không gian:** O(b^C*/ε)
- **Ưu điểm:**
  - Đảm bảo tìm được lời giải tối ưu
  - Xem xét chi phí của từng bước
  - Hiệu quả với các bài toán có chi phí khác nhau
- **Nhược điểm:**
  - Tiêu tốn nhiều bộ nhớ
  - Thời gian thực thi có thể lớn
  - Không sử dụng thông tin heuristic

### 4. ID (Iterative Deepening)

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00145 giây
  - Bộ nhớ sử dụng: 0.00082 MB
  - Bộ nhớ tối đa: 0.00345 MB
  - Số bước thực hiện: 3
 > ![ID Animation](images/ID.gif)
#### Đầu vào phức tạp
- **Evaluation:**
  - Số bước thực hiện: không giải được

#### Nhận xét
- **Độ phức tạp thời gian:** O(b^d)
  - b: số nhánh trung bình
  - d: độ sâu của lời giải
- **Độ phức tạp không gian:** O(b*d)
- **Ưu điểm:**
  - Kết hợp ưu điểm của BFS và DFS
  - Sử dụng ít bộ nhớ hơn BFS
  - Đảm bảo tìm được lời giải tối ưu
- **Nhược điểm:**
  - Thời gian thực thi có thể lớn hơn BFS
  - Lặp lại việc tìm kiếm ở các độ sâu khác nhau

### 5. Greedy Best-First Search

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00123 giây
  - Bộ nhớ sử dụng: 0.00088 MB
  - Bộ nhớ tối đa: 0.00356 MB
  - Số bước thực hiện: 3

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.01456 giây
  - Bộ nhớ sử dụng: 0.00118 MB
  - Bộ nhớ tối đa: 0.00434 MB
  - Số bước thực hiện: 71
 > ![Greedy Animation](images/Greedy.gif)
#### Nhận xét
- **Độ phức tạp thời gian:** O(b^m)
  - b: số nhánh trung bình
  - m: độ sâu tối đa của cây tìm kiếm
- **Độ phức tạp không gian:** O(b^m)
- **Ưu điểm:**
  - Nhanh hơn A* trong một số trường hợp
  - Sử dụng thông tin heuristic
  - Hiệu quả với không gian tìm kiếm lớn
- **Nhược điểm:**
  - Không đảm bảo tìm được lời giải tối ưu
  - Phụ thuộc vào chất lượng hàm heuristic
  - Có thể bỏ qua các đường đi tốt

### 6. A* Search

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00112 giây
  - Bộ nhớ sử dụng: 0.00092 MB
  - Bộ nhớ tối đa: 0.00345 MB
  - Số bước thực hiện: 4

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 1.01868 giây
  - Bộ nhớ sử dụng: 0.00112 MB
  - Bộ nhớ tối đa: 14.23123 MB
  - Số bước thực hiện: 24
 > ![A* Animation](images/A-Star.gif)
#### Nhận xét
- **Độ phức tạp thời gian:** O(b^d)
  - b: số nhánh trung bình
  - d: độ sâu của lời giải
- **Độ phức tạp không gian:** O(b^d)
- **Ưu điểm:**
  - Cân bằng giữa thời gian và bộ nhớ
  - Hiệu quả nhất với bài toán phức tạp
  - Số bước thực hiện tối ưu
  - Kết hợp được ưu điểm của BFS và heuristic
- **Nhược điểm:**
  - Phụ thuộc vào chất lượng hàm heuristic
  - Yêu cầu nhiều bộ nhớ hơn một số thuật toán khác
  - Cần thiết kế hàm heuristic tốt

### 7. IDA* (Iterative Deepening A*)

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00134 giây
  - Bộ nhớ sử dụng: 0.00085 MB
  - Bộ nhớ tối đa: 0.00367 MB
  - Số bước thực hiện: 3

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 2.31234 giây
  - Bộ nhớ sử dụng: 0.00112 MB
  - Bộ nhớ tối đa: 0.04894 MB
  - Số bước thực hiện: 23
 > ![IDA* Animation](images/IDA-Star.gif)
#### Nhận xét
- **Độ phức tạp thời gian:** O(b^d)
  - b: số nhánh trung bình
  - d: độ sâu của lời giải
- **Độ phức tạp không gian:** O(b*d)
- **Ưu điểm:**
  - Kết hợp ưu điểm của ID và A*
  - Sử dụng ít bộ nhớ hơn A*
  - Đảm bảo tìm được lời giải tối ưu
- **Nhược điểm:**
  - Thời gian thực thi có thể lớn hơn A*
  - Lặp lại việc tìm kiếm ở các ngưỡng khác nhau

### 8. Simple Hill Climbing

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00089 giây
  - Bộ nhớ sử dụng: 0.00067 MB
  - Bộ nhớ tối đa: 0.00289 MB
  - Số bước thực hiện: 3
 > ![Simple Hill Climbing Animation](images/SHC.gif)
#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.01876 giây
  - Bộ nhớ sử dụng: 0.00134 MB
  - Bộ nhớ tối đa: 0.00478 MB
  - Số bước thực hiện: Không tìm thấy lời giải

#### Nhận xét
- **Độ phức tạp thời gian:** O(b*n)
  - b: số nhánh trung bình
  - n: số lần lặp
- **Độ phức tạp không gian:** O(1)
- **Ưu điểm:**
  - Nhanh nhất với bài toán đơn giản
  - Sử dụng ít bộ nhớ nhất
  - Đơn giản trong cài đặt
  - Không cần lưu trữ trạng thái
- **Nhược điểm:**
  - Dễ bị kẹt ở cực đại cục bộ
  - Không tìm thấy lời giải cho bài toán phức tạp
  - Không đảm bảo tìm được lời giải tối ưu
  - Phụ thuộc vào điểm khởi đầu

### 9. Steepest Ascent Hill Climbing

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00092 giây
  - Bộ nhớ sử dụng: 0.00072 MB
  - Bộ nhớ tối đa: 0.00312 MB
  - Số bước thực hiện: 4
#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.01923 giây
  - Bộ nhớ sử dụng: 0.00145 MB
  - Bộ nhớ tối đa: 0.00489 MB
  - Số bước thực hiện: Không tìm thấy lời giải

#### Nhận xét
- **Độ phức tạp thời gian:** O(b*n)
  - b: số nhánh trung bình
  - n: số lần lặp
- **Độ phức tạp không gian:** O(1)
- **Ưu điểm:**
  - Xem xét tất cả các lựa chọn có thể
  - Chọn bước đi tốt nhất tại mỗi bước
  - Đơn giản trong cài đặt
- **Nhược điểm:**
  - Vẫn dễ bị kẹt ở cực đại cục bộ
  - Thời gian thực thi có thể lớn
  - Không đảm bảo tìm được lời giải tối ưu

### 10. Stochastic Hill Climbing

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00095 giây
  - Bộ nhớ sử dụng: 0.00075 MB
  - Bộ nhớ tối đa: 0.00323 MB
  - Số bước thực hiện: 4

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.02012 giây
  - Bộ nhớ sử dụng: 0.00152 MB
  - Bộ nhớ tối đa: 0.00512 MB
  - Số bước thực hiện: 30

#### Nhận xét
- **Độ phức tạp thời gian:** O(b*n)
  - b: số nhánh trung bình
  - n: số lần lặp
- **Độ phức tạp không gian:** O(1)
- **Ưu điểm:**
  - Có thể thoát khỏi cực đại cục bộ
  - Đa dạng hóa tìm kiếm
  - Hiệu quả với không gian tìm kiếm lớn
- **Nhược điểm:**
  - Không đảm bảo tìm được lời giải tối ưu
  - Thời gian thực thi không ổn định
  - Phụ thuộc vào xác suất chọn bước đi

### 11. Simulated Annealing

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00145 giây
  - Bộ nhớ sử dụng: 0.00098 MB
  - Bộ nhớ tối đa: 0.00367 MB
  - Số bước thực hiện: 4

#### Đầu vào phức tạp
- **Evaluation:**

  - Số bước thực hiện: Khồn giải được

#### Nhận xét
- **Độ phức tạp thời gian:** O(n)
  - n: số lần lặp
- **Độ phức tạp không gian:** O(1)
- **Ưu điểm:**
  - Có thể thoát khỏi cực đại cục bộ
  - Hiệu quả với bài toán phức tạp
  - Không bị kẹt ở lời giải cục bộ
  - Sử dụng ít bộ nhớ
- **Nhược điểm:**
  - Thời gian thực thi lâu nhất
  - Không đảm bảo tìm được lời giải tối ưu
  - Phụ thuộc vào tham số nhiệt độ
  - Cần điều chỉnh các tham số phù hợp 

### 12. Beam Search

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00112 giây
  - Bộ nhớ sử dụng: 0.00082 MB
  - Bộ nhớ tối đa: 0.00345 MB
  - Số bước thực hiện: 4

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.01567 giây
  - Bộ nhớ sử dụng: 0.00123 MB
  - Bộ nhớ tối đa: 0.00456 MB
  - Số bước thực hiện: 27

#### Nhận xét
- **Độ phức tạp thời gian:** O(b*w)
  - b: số nhánh trung bình
  - w: độ rộng của beam
- **Độ phức tạp không gian:** O(b*w)
- **Ưu điểm:**
  - Cân bằng giữa bộ nhớ và hiệu quả
  - Có thể tìm được lời giải tốt
  - Kiểm soát được bộ nhớ sử dụng
- **Nhược điểm:**
  - Không đảm bảo tìm được lời giải tối ưu
  - Phụ thuộc vào độ rộng beam
  - Có thể bỏ qua các đường đi tốt

### 13. Backtracking

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00123 giây
  - Bộ nhớ sử dụng: 0.00078 MB
  - Bộ nhớ tối đa: 0.00334 MB
  - Số bước thực hiện: 29

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.02456 giây
  - Bộ nhớ sử dụng: 0.00145 MB
  - Bộ nhớ tối đa: 0.00567 MB
  - Số bước thực hiện: 35

#### Nhận xét
- **Độ phức tạp thời gian:** O(n!)
  - n: số lượng biến cần gán giá trị
- **Độ phức tạp không gian:** O(n)
- **Ưu điểm:**
  - Đơn giản trong cài đặt
  - Sử dụng ít bộ nhớ
  - Có thể tìm tất cả các lời giải
- **Nhược điểm:**
  - Thời gian thực thi có thể rất lớn
  - Không hiệu quả với bài toán phức tạp
  - Không sử dụng thông tin heuristic

### 14. Local Search CSP

#### Đầu vào đơn giản
- **Evaluation:**
  - Thời gian thực thi: 0.00134 giây
  - Bộ nhớ sử dụng: 0.00085 MB
  - Bộ nhớ tối đa: 0.00356 MB
  - Số bước thực hiện: 4

#### Đầu vào phức tạp
- **Evaluation:**
  - Thời gian thực thi: 0.02678 giây
  - Bộ nhớ sử dụng: 0.00167 MB
  - Bộ nhớ tối đa: 0.00589 MB
  - Số bước thực hiện: 32

#### Nhận xét
- **Độ phức tạp thời gian:** O(n*d)
  - n: số biến
  - d: miền giá trị của biến
- **Độ phức tạp không gian:** O(n)
- **Ưu điểm:**
  - Hiệu quả với các ràng buộc đơn giản
  - Có thể tìm được lời giải tốt
  - Dễ mở rộng cho các ràng buộc mới
- **Nhược điểm:**
  - Không đảm bảo tìm được lời giải tối ưu
  - Phụ thuộc vào chiến lược tìm kiếm cục bộ
  - Có thể bị kẹt ở lời giải cục bộ
 
Link GitHub: https://github.com/TuanKiet318/8Puzzle