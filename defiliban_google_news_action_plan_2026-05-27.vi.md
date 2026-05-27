# Kế Hoạch Hành Động Google News Cho DeFiliban

Ngày: 2026-05-27

## Phải Sửa Ngay

- Thay toàn bộ social link placeholder `#` ở footer bằng URL social thật hoặc bỏ hẳn.
- Làm lại trang `About` để publisher identity rõ và đáng tin hơn.
- Làm lại trang `Contact` với thông tin liên hệ publication thật.
- Chuẩn hóa author bio cho các tác giả đang xuất bản bài news.
- Giữ `rb-etemplate` ở trạng thái bị loại khỏi sitemap và `noindex`.
- Không để attachment-style promo URL hoặc template junk quay lại.

## Nên Sửa Trong Tuần Này

- Thêm hoặc nâng cấp trang editorial/publisher information.
- Review các category/archive page đang đóng vai trò news hubs để đảm bảo chúng sạch, indexable và được cập nhật đúng.
- Xác nhận các article page luôn có:
  - title
  - author
  - publication date
  - modified date nếu có
- Audit nhóm launch/listing/news yếu còn live và quyết định:
  - giữ
  - rewrite
  - noindex
  - remove
- Recrawl lại site sau purge để xác nhận cụm promo attachment vừa dọn vẫn `404`.

## Loại Nội Dung Cần Dừng Xuất Bản

- price prediction
- presale pages
- bài kiểu "best crypto to buy"
- advertorial độ tin cậy thấp
- sponsored-looking content không disclosure rõ
- duplicate attachment/media permalink junk

## Hướng Xuất Bản Trong 2-4 Tuần Tới

- chỉ publish news sạch, factual
- giữ title bài thẳng, không hype
- tránh trộn commercial intent với news intent ở các section chính
- duy trì ổn định các section như `/news/` và `/crypto/`
- giữ nhịp publish đều thay vì bùng nổ rồi ngắt

## Tín Hiệu Thành Công Cần Theo Dõi

- ít URL rác hơn đi vào discovery
- crawl sau purge sạch hơn
- số `Discovered - currently not indexed` trong GSC bắt đầu giảm sau recrawl
- không còn template hoặc attachment junk URL mới
- author / about / contact transparency nhất quán hơn
