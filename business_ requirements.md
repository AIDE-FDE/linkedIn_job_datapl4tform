### 📊 **Phân tích về công ty**

1. **Quy mô công ty theo ngành**: So sánh phân bố `company_size` giữa các `industry`.
2. **Tăng trưởng nhân sự theo thời gian**: Từ bảng `employee_counts`, bạn có thể phân tích tốc độ tăng trưởng nhân viên/follower theo `time_recorded`.
3. **Địa lý**: Thống kê số công ty theo `state`, `city`, `country`.
4. **Top công ty có nhiều việc làm**: Liên kết `companies` với `postings` để tìm công ty nào đăng nhiều job nhất.
5. **Công ty có followers lớn nhưng ít postings** → có thể phân tích sự mất cân đối giữa thương hiệu và tuyển dụng.

---

### 💼 **Phân tích về tuyển dụng (postings)**

1. **Phân phối mức lương**:

   * Theo `industry` hoặc `company_size`.
   * Theo `formatted_experience_level` (junior, mid, senior).
   * Theo `location`.
2. **Xu hướng remote**: Tỉ lệ `remote_allowed = 1` theo thời gian, ngành, vị trí địa lý.
3. **Hiệu quả tin tuyển dụng**:

   * `applies / views` → tỉ lệ apply.
   * So sánh sponsored vs non-sponsored.
4. **Thời gian sống của job**: từ `original_listed_time` → `closed_time`, tính thời gian mở trung bình.
5. **Xu hướng theo work type**: full-time, part-time, contract → xem ngành nào dùng nhiều.

---

### 🛠 **Phân tích kỹ năng (skills)**

1. **Top kỹ năng phổ biến**: từ `job_skills`.
2. **Kỹ năng theo ngành**: nối `job_industries` + `job_skills`.
3. **Kỹ năng và mức lương**: tìm các skill đi kèm với mức `normalized_salary` cao.
4. **Kỹ năng trending theo thời gian**: dựa vào `listed_time`.

---

### 💰 **Phân tích lương (salaries & postings)**

1. **So sánh nguồn lương**: bảng `salaries` vs thông tin trong `postings` → kiểm tra consistency.
2. **Mức lương trung vị theo ngành, vị trí, kỹ năng**.
3. **Pay period**: so sánh weekly, monthly, yearly.
4. **Lương & kinh nghiệm**: phân tích `formatted_experience_level` với `med_salary`.

---

### 🎁 **Phân tích phúc lợi (benefits)**

1. **Phúc lợi phổ biến nhất**: loại `benefit_type` được nhắc nhiều nhất.
2. **Phúc lợi theo ngành / vị trí địa lý**.
3. **Có benefit → có ảnh hưởng đến apply rate không?**

---

### 🔄 **Phân tích xu hướng theo thời gian**

* Dựa trên `listed_time`, `closed_time`, `expiry`, `time_recorded`:

  1. Xu hướng số lượng job postings theo tháng/quý.
  2. Sự thay đổi mức lương trung bình theo thời gian.
  3. Nhu cầu kỹ năng thay đổi thế nào qua các năm.

