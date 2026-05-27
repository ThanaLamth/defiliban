# Mức Độ Sẵn Sàng Google News Của DeFiliban

Ngày: 2026-05-27

## Nền Tảng Chính Thống

Google News hiện đánh giá nội dung web đủ điều kiện theo cách tự động. Không còn yêu cầu gửi publication thủ công để có trang nguồn trong Google News như trước.

Các nguồn chính thức cần bám:

- Google News tự tạo publication pages
- Technical guidelines của Google News
- Content policies của Google News
- Hướng dẫn schema bài viết của Google Search

## Kết Luận Hiện Tại

- Điều kiện kỹ thuật: gần đạt
- Mức độ minh bạch: còn thiếu
- Độ tin cậy nội dung: yếu đến trung bình
- Mức độ sẵn sàng tổng thể cho Google News: không còn bị chặn bởi lỗi kỹ thuật lớn, nhưng chưa đủ mạnh để kỳ vọng xuất hiện ổn định trên News surfaces

## Những Gì DeFiliban Đã Có

- Các section URL ổn định như `/news/`, `/crypto/`, và các đường dẫn market/category
- Card bài viết và link section render bằng HTML thật trên các trang chính
- Trang bài viết có title, date, byline trên nội dung đang live
- Site đã có Article schema
- `rb-etemplate` sitemap đã bị loại khỏi luồng sitemap đang public
- URL `rb-etemplate` đã bị loại khỏi sitemap và đặt `noindex`
- Đã dọn phần lớn promo attachment-style junk

## Những Gì Vẫn Đang Cản Google News

### 1. Tín Hiệu Minh Bạch Chưa Đủ

Google News policy nhấn mạnh phải rõ:

- ai viết nội dung
- ai là publisher
- tổ chức/công ty đứng sau site
- người đọc liên hệ publication bằng cách nào

Các điểm còn thiếu trên DeFiliban:

- icon social ở footer vẫn còn link placeholder `#`
- trang About / thông tin publisher chưa đủ mạnh
- Contact / editorial transparency cần rõ hơn
- author profile chưa đồng đều về chất lượng

### 2. Lịch Sử Chất Lượng Nội Dung Bị Pha Tạp

Site từng có số lượng lớn:

- bài promo
- bài presale / prediction
- attachment-style junk URL
- advertorial-like content độ tin cậy thấp

Dù đã cleanup, lịch sử đó vẫn làm trust yếu đi cho tới khi site chạy một giai đoạn xuất bản sạch hơn.

### 3. Chưa Tách News Và Non-News Đủ Rõ

Muốn vào Google News ổn định, publication phải trông nhất quán như một site tin tức.

Những dạng nội dung không nên chiếm tỷ trọng lớn:

- price prediction
- presale
- bài kiểu "best crypto to buy"
- sponsored/promotional content không disclosure rõ

## Điều Kiện Tối Thiểu Cần Duy Trì

- news sections phải crawl được bằng HTML link
- article URL phải ổn định và duy nhất
- byline và publish date phải nhìn thấy trên bài
- template/query URL phải bị loại khỏi index và sitemap
- low-value promo content không được quay lại

## Baseline Schema Nên Giữ

Trang bài nên nhất quán với:

- `Article` hoặc `NewsArticle`
- `headline`
- `image`
- `author`
- `datePublished`
- `dateModified`

Schema không đảm bảo vào Google News, nhưng giúp Google hiểu đúng trang bài.

## Đánh Giá Thực Tế

### Đã Ổn

- hướng cleanup kỹ thuật
- cleanup sitemap cho template URL
- cleanup promo attachment

### Chưa Ổn

- tín hiệu minh bạch của publisher
- quãng thời gian xuất bản sạch đủ dài
- tách biệt đủ rõ giữa news và promotional content

## Kết Luận Cuối

DeFiliban không còn bị giữ chân bởi đám technical junk rõ ràng như trước. Rào cản tiếp theo không còn là crawlability mà là trust, transparency, và độ nhất quán của chất lượng nội dung.

Muốn tăng khả năng xuất hiện trên Google News, DeFiliban cần vận hành như một site tin tức sạch và minh bạch trong một chu kỳ xuất bản liên tục, thay vì như một site crypto bị pha nhiều promo content.
