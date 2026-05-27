# Phân Tích Khoảng Cách: DeFiliban So Với crypto.news Cho Google News

Ngày: 2026-05-27

## Mục Tiêu

Mục tiêu của file này là chỉ ra vì sao một site như `crypto.news` có thể xuất hiện trên Google News publication pages và News surfaces, trong khi `DeFiliban` hiện chưa đủ mạnh ở cùng mức đó.

Lưu ý quan trọng:

- Google News hiện tạo publication pages tự động.
- Không còn cơ chế "nộp site để được duyệt" theo kiểu cũ.
- Vì vậy, khoảng cách chính không nằm ở một form submit, mà nằm ở chất lượng publisher signals, transparency, và độ sạch của site.

## Điều Google Chính Thức Quan Tâm

Theo tài liệu chính thức của Google News / Publisher Center / Search:

- nội dung web phải crawl/index ổn định
- section pages phải có HTML links thật tới article pages
- article pages phải có title, byline, publish date rõ
- publication phải minh bạch về publisher, author, tổ chức, contact
- nội dung phải tuân thủ Google News policies

## Những Gì crypto.news Đang Có

Mình đã kiểm tra trực tiếp trên site và thấy các tín hiệu sau:

### 1. News Sitemap Chuẩn

- có `news-sitemap.xml`
- có `news:name`
- có `news:language`
- có `news:publication_date`
- có `news:title`
- có `news:keywords`

Đây là tín hiệu rất mạnh cho một publication news đang vận hành bài bản.

### 2. Cấu Trúc Publisher/Trust Rõ

Trong `page-sitemap.xml` của `crypto.news` có các trang:

- `/about/`
- `/authors/`
- `/contact-us/`
- `/team-verification/`

Tức là họ không chỉ có bài viết, mà còn có các lớp minh bạch để Google hiểu:

- ai là publisher
- ai là tác giả
- cách liên hệ publication
- đội ngũ editorial / verification là ai

### 3. Bài Viết Sạch Theo Chuẩn News

Một bài viết mẫu trên `crypto.news` có:

- indexable robots
- canonical sạch
- `og:type=article`
- `datePublished`
- `dateModified`
- `NewsArticle` trong source
- link tới author page

### 4. Homepage Có Tín Hiệu Publisher Rõ

Homepage và site-level content có dấu hiệu:

- about
- author
- contact
- team verification
- sponsored

Điều này giúp site trông như một publication thật, không phải một site content pha tạp.

## Những Gì DeFiliban Đang Có

### 1. Technical News Base Đã Có

`DeFiliban` hiện đã có:

- `news-sitemap.xml`
- article pages có `NewsArticle`
- có `datePublished`
- có `dateModified`
- có canonical
- có author page link
- đã dọn phần lớn technical junk như attachment-style promo URLs
- đã loại `rb-etemplate` khỏi sitemap và `noindex` template URLs

### 2. Section Pages Ổn Hơn Trước

Site có các hub/section như:

- `/news/`
- `/crypto/`
- các category path liên quan

Về mặt structure, phần này không còn là điểm yếu lớn nhất.

## Khoảng Cách Giữa DeFiliban Và crypto.news

### Gap 1. Thiếu Lớp Minh Bạch Publisher

Hiện tại:

- `/about/` của `DeFiliban` đang `404`
- `/authors/` đang `404`
- `/team-verification/` đang `404`
- `/contact/` đang `200` nhưng lại `noindex`

Trong khi `crypto.news` có các lớp này đầy đủ và indexable.

Đây là khoảng cách lớn nhất.

### Gap 2. Footer / Social / Trust Signals Còn Yếu

`DeFiliban` vẫn còn:

- social links dạng `#`
- contact/about chưa đủ mạnh
- chưa thể hiện rõ một lớp publication identity ở site-level

Điều này làm site trông yếu hơn trong mắt Google News so với một publisher thật.

### Gap 3. Lịch Sử Nội Dung Bị Pha Tạp

`DeFiliban` có lịch sử:

- price prediction
- presale
- "best crypto to buy"
- promo / attachment junk

Trong khi một site như `crypto.news` nhìn nhất quán hơn theo kiểu publication news.

Google không cần bạn "khai báo" đây là site news; Google nhìn vào hành vi xuất bản thực tế.

### Gap 4. Chưa Tách Rõ News Và Non-News

Muốn giống `crypto.news`, `DeFiliban` không chỉ cần bài news.

Nó còn cần:

- giảm mạnh content thương mại/hype
- giữ các section chính sạch theo hướng editorial
- tránh để publisher profile bị pha bằng quá nhiều commercial pages

## Cần Làm Trong WordPress

### A. Tạo Hoặc Khôi Phục Trang Transparency

Phải có và nên index:

- `About`
- `Authors`
- `Contact`
- `Editorial Team` hoặc `Team Verification`

### B. Chuẩn Hóa Author Layer

Mỗi author nên có:

- tên ổn định
- bio
- vai trò/chuyên môn
- author archive page
- nếu được, social/profile thật

### C. Dọn Footer Trust Layer

- thay social `#` bằng link thật
- nếu không có link thật thì bỏ
- tăng tín hiệu brand identity ở footer/sitewide

### D. Giữ News Sitemap Và Technical Hygiene

- giữ `news-sitemap.xml` sạch
- giữ template URLs ngoài sitemap
- không để attachment junk quay lại

## Cần Dừng Xuất Bản

Nếu muốn giống mô hình `crypto.news`, nên dừng:

- price prediction
- presale
- "best crypto to buy"
- advertorial độ trust thấp
- sponsored-like content không disclosure rõ

## Kết Luận Cuối

`DeFiliban` không thiếu một "setup bí mật" để vào Google News.

`DeFiliban` thiếu chủ yếu:

- publisher transparency
- author transparency
- editorial trust
- content profile đủ sạch và nhất quán

So với `crypto.news`, kỹ thuật cơ bản của `DeFiliban` hiện không quá tệ nữa. Khoảng cách lớn nhất nằm ở lớp publisher signals và chất lượng nội dung xuất bản liên tục.

## Tóm Tắt Hành Động

### Đã Có

- news sitemap
- article schema
- canonical/date/byline cơ bản
- cleanup technical junk lớn

### Thiếu

- About indexable
- Authors indexable
- Team Verification / Editorial Team
- Contact indexable và đủ mạnh
- social links thật
- publisher identity rõ

### Phải Làm Trong WP

- tạo/khôi phục các trang transparency
- chuẩn hóa author profiles
- sửa footer/social
- giữ sạch technical sitemap/index settings

### Phải Dừng Xuất Bản

- prediction
- presale
- "best crypto to buy"
- low-trust promo content
