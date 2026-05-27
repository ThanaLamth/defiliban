# Checklist WP Admin Cho DeFiliban Hướng Tới Google News

Ngày: 2026-05-27

Mục tiêu của checklist này là biến các yêu cầu về transparency, trust và technical hygiene thành các bước thao tác cụ thể trong WordPress admin.

## 1. Tạo Lớp Trang Publisher Transparency

### 1.1. Tạo Trang About

Đi vào:

- `Pages > Add New`

Tạo trang:

- `About`

Nội dung tối thiểu cần có:

- DeFiliban là publication gì
- publisher đứng sau site là ai
- site tập trung vào chủ đề gì
- quy trình xuất bản / định hướng editorial ngắn gọn
- liên kết sang Contact và Author pages

Yêu cầu:

- trang phải `Publish`
- phải `Indexable`
- không để `noindex`

### 1.2. Tạo Trang Authors

Đi vào:

- `Pages > Add New`

Tạo trang:

- `Authors`

Nội dung tối thiểu:

- danh sách tác giả đang hoạt động
- tên tác giả
- vai trò
- bio ngắn
- link về author archive tương ứng

Nếu team muốn tốt hơn:

- thêm ảnh thật
- thêm lĩnh vực chuyên môn

### 1.3. Tạo Trang Editorial Team / Team Verification

Đi vào:

- `Pages > Add New`

Tạo một trong hai:

- `Editorial Team`
- hoặc `Team Verification`

Nội dung tối thiểu:

- ai là đội biên tập
- ai review nội dung
- cách team kiểm tra bài viết

Trang này giúp site trông giống publication thật hơn.

### 1.4. Nâng Cấp Trang Contact

Đi vào:

- `Pages > All Pages > Contact`

Việc cần làm:

- thêm thông tin liên hệ thật
- nếu có email newsroom/editorial thì càng tốt
- nếu có form thì giữ
- nếu có địa chỉ công ty/nhóm vận hành thì thêm

SEO:

- bỏ `noindex` nếu mục tiêu là tăng transparency cho publisher

## 2. Chuẩn Hóa Author Layer

### 2.1. Review Tài Khoản Author

Đi vào:

- `Users > All Users`

Kiểm tra từng author đang viết bài:

- tên hiển thị có ổn định không
- profile có mô tả không
- có website/social/profile liên quan không

### 2.2. Chuẩn Hóa Bio Cho Author

Đi vào:

- `Users > Edit User`

Điền:

- `Biographical Info`
- tên hiển thị chuẩn
- nếu theme hỗ trợ: avatar/profile links

Mục tiêu:

- author page không được trống trơn
- người đọc và Google nhìn vào hiểu tác giả là ai

## 3. Dọn Footer Trust Layer

### 3.1. Sửa Social Links Dạng #

Đi vào:

- template footer đang dùng
- hoặc `Appearance > Menus`
- hoặc khu vực Foxiz / Elementor footer template

Việc cần làm:

- thay toàn bộ social link `#` bằng URL thật
- nếu không có URL thật thì xóa icon đó

Không để:

- Twitter `#`
- YouTube `#`
- Telegram `#`
- LinkedIn trống

### 3.2. Thêm Link Publisher Pages Ở Footer

Footer nên có link tới:

- About
- Contact
- Authors
- Editorial Team / Team Verification

Đây là bước rất nên làm cho publisher transparency.

## 4. Kiểm Tra Rank Math Cho News Hygiene

### 4.1. Ruby Templates

Đi vào:

- `Rank Math > Titles & Meta > Post Types > Ruby Templates`

Kiểm tra:

- `Ruby Template Robots Meta` = `noindex`

Đi vào tiếp:

- `Rank Math > Sitemap Settings > Post Types > Ruby Templates`

Kiểm tra:

- tắt `Include in Sitemap`
- tắt `Include in HTML Sitemap`

### 4.2. Contact / About / Authors / Editorial Pages

Với các trang transparency:

- không để `noindex`
- cho index bình thường

### 4.3. Search / Paginated / Misc Pages

Giữ:

- search pages `noindex`
- paginated single pages `noindex`
- các trang kỹ thuật không cần index phải tiếp tục bị chặn

## 5. Giữ News Sitemap Sạch

Đi vào kiểm tra:

- `https://defiliban.io/news-sitemap.xml`
- `https://defiliban.io/sitemap_index.xml`

Mục tiêu:

- không có template URLs
- không có attachment junk URLs
- chỉ còn bài news/article hợp lệ

## 6. Kiểm Soát Nội Dung Không Phù Hợp Với Google News

### 6.1. Dừng Xuất Bản

Không nên tiếp tục publish:

- price prediction
- presale
- "best crypto to buy"
- low-trust promo content

### 6.2. Nếu Có Sponsored Content

Phải:

- disclosure rõ
- không để lẫn với luồng news bình thường

## 7. Checklist Sau Khi Sửa

Sau khi hoàn tất các bước trên:

1. Purge cache
2. Kiểm tra live:
   - `About`
   - `Authors`
   - `Contact`
   - `Editorial Team` hoặc `Team Verification`
3. Kiểm tra source các trang đó không còn `noindex`
4. Kiểm tra footer social không còn `#`
5. Kiểm tra `rb-etemplate-sitemap.xml` vẫn `404`
6. Crawl lại site
7. Theo dõi GSC trong 2-4 tuần

## 8. Kết Quả Kỳ Vọng

Nếu làm xong checklist này, `DeFiliban` sẽ:

- giống một publication thật hơn
- tăng transparency signals
- giảm khoảng cách với kiểu setup của `crypto.news`
- có nền tốt hơn để Google tự đánh giá cho Google News surfaces
