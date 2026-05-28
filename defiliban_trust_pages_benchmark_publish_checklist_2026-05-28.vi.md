# DeFiliban Trust Pages Benchmark + Publish Checklist

Ngày: 2026-05-28

## Mục tiêu

Tài liệu này gộp 3 việc:

- benchmark bộ trust/publisher pages của DeFiliban với các pattern mạnh từ `crypto.news` và `CoinDesk`
- rà internal link stack giữa các trust pages
- chốt publish checklist: page nào publish được ngay, page nào nên polish thêm

## Nguồn benchmark

- Google News source transparency:
  - https://developers.google.com/search/blog/2021/06/google-news-sources
- Google News policies:
  - https://support.google.com/news/publisher-center/answer/6204050?hl=en
- crypto.news:
  - https://crypto.news/authors/
  - https://crypto.news/team-verification
- CoinDesk:
  - https://www.coindesk.com/masthead/
  - https://www.coindesk.com/ethics/

## Kết luận tổng quan

Bộ trust pages hiện tại của DeFiliban đã đủ khung để trông giống một publisher thật, không còn ở mức placeholder page.

Nếu so với chuẩn newsroom crypto mạnh:

- so với `crypto.news`: đã tiến rất gần
- so với `CoinDesk`: vẫn còn mỏng hơn ở lớp institutional proof, social verification, anti-impersonation workflow, và editorial governance chi tiết

Mức đánh giá thực dụng hiện tại:

- đủ tốt để publish theo wave 1
- chưa phải bản “fully institutional”

## Chấm điểm từng page

### 1. About

Điểm: `8/10`

Điểm mạnh:

- publisher identity đã rõ
- phạm vi coverage rõ
- có editorial approach
- có accountability language

Thiếu:

- chưa có company/entity detail nếu có
- chưa có official editorial email
- chưa có disclosure rõ nếu có sponsored/promotional content

### 2. Authors

Điểm: `8.5/10`

Điểm mạnh:

- có 3 author thật, role rõ, focus rõ
- có background credibility ngắn
- có link thẳng sang author archive

Thiếu:

- chưa có headshot/avatar chuẩn newsroom
- chưa có verified social/profile links
- chưa có previous publications / stronger public proof

### 3. Editorial Policy

Điểm: `8.5/10`

Điểm mạnh:

- có sourcing standards
- có editorial independence
- có anonymous/unverified claims section
- có AI and research tools section
- có conflicts of interest section

Thiếu:

- chưa có conflict policy thật chi tiết như newsroom lớn
- chưa có ownership/governance detail
- chưa có rule cụ thể cho investment disclosure ở từng article

### 4. Corrections Policy

Điểm: `8.5/10`

Điểm mạnh:

- phân biệt correction / clarification / update
- có working standard cho vị trí correction note
- có reader reporting flow
- có logic cho developing stories

Thiếu:

- chưa có example correction note mẫu
- chưa có dedicated corrections/editorial email
- chưa có rule cụ thể cho top-note vs bottom-note beyond current summary

### 5. Team Verification

Điểm: `8.5/10`

Điểm mạnh:

- có verified publication pages
- có verified contributor roles
- có official verification channels
- có anti-impersonation wording

Thiếu:

- chưa có official social handles để verify
- chưa có email/identity verification route riêng
- chưa có staff headshots / richer identity proof

### 6. Masthead

Điểm: `8/10`

Điểm mạnh:

- gom role và contributor structure thành một newsroom page riêng
- giúp publisher profile nhìn chuyên nghiệp hơn
- nối tốt với Authors + Team Verification

Thiếu:

- hiện vẫn thiên về contributor directory hơn là newsroom masthead đầy đủ
- chưa có editor / managing roles / contact owner
- chưa có anti-impersonation or organizational chain rõ như CoinDesk

## Benchmark so với crypto.news và CoinDesk

### So với crypto.news

DeFiliban đã bắt kịp phần lớn khung trust-page:

- About
- Authors
- Team Verification
- Editorial / transparency pages

Điểm còn kém `crypto.news` chủ yếu nằm ở:

- độ hoàn thiện của author/profile proof
- social verification
- các page hỗ trợ thật sự đã public trong navigation chưa

### So với CoinDesk

CoinDesk vẫn hơn rõ ở:

- masthead có tính tổ chức mạnh hơn
- ethics/editorial governance sâu hơn
- anti-impersonation rõ hơn
- team roles và operational accountability rõ hơn

DeFiliban chưa cần copy level đó ngay. Với stage hiện tại, mục tiêu hợp lý là đạt “clean, coherent, trustworthy” trước.

## Rà internal link stack

Sau khi cập nhật batch ngày 2026-05-28, 6 trust pages đang nối với nhau rất tốt ở cấp content.

Kết quả thực dụng:

- `About` link sang 5 trust pages còn lại
- `Authors` link sang 5 trust pages còn lại
- `Editorial Policy` link sang 5 trust pages còn lại
- `Corrections Policy` link sang 5 trust pages còn lại
- `Team Verification` link sang 5 trust pages còn lại
- `Masthead` link sang 5 trust pages còn lại

Kết luận:

- internal trust stack ở cấp nội dung: `đạt`
- footer/menu/sitewide navigation: `chưa xử lý trong batch này`

## Navigation gap còn lại

Hiện mới chắc ở lớp content của từng page.

Các việc điều hướng còn nên làm thủ công trong WP:

1. thêm một cụm trust links ở footer
2. cân nhắc thêm `About` hoặc `Masthead` vào menu phụ / footer nav
3. nếu site có trang contact ở footer rồi, nên đặt cùng cụm với:
   - About
   - Authors
   - Editorial Policy
   - Corrections Policy
   - Team Verification
   - Masthead

Lý do:

- Google và user đều nhìn thấy trust stack dễ hơn
- giảm việc các page này “có tồn tại nhưng bị chôn”

## Vấn đề thực tế còn tồn tại

### 1. Contact page vẫn `noindex`

Check live hiện tại cho thấy:

- `https://defiliban.io/contact/`
- meta robots: `follow, noindex`

Điều này không phá trust stack hoàn toàn, vì page vẫn public và crawl được.

Nhưng nếu muốn profile publisher sạch hơn, nên cân nhắc:

- hoặc giữ public + noindex nếu muốn page chỉ làm utility
- hoặc chuyển sang index nếu muốn contact page đóng vai trust page đầy đủ

### 2. Contact page còn metadata/schema tàn dư

Live source hiện vẫn cho thấy dấu vết cũ như:

- meta description không sạch
- hình/schema tham chiếu asset Foxiz cũ

Đây là điểm nên dọn trước hoặc ngay sau lúc publish trust stack.

### 3. Author archives vẫn có thể nâng thêm

Nếu có thể, nên bổ sung:

- avatar/headshot
- profile links nếu có
- bio formatting sạch hơn

## Publish checklist

### Publish ngay được

- About
- Authors
- Editorial Policy
- Corrections Policy
- Team Verification
- Masthead

Lý do:

- nội dung đã đủ coherent
- cross-link nội bộ đã kín
- mỗi page đều có mục đích rõ

### Nên polish thêm nhưng không cần chặn publish

- thêm footer trust navigation
- thêm headshot/avatar cho author pages
- thêm official social verification nếu có
- thêm editorial/corrections email nếu có

### Nên fix sớm

- dọn metadata/schema của Contact page
- quyết định rõ Contact sẽ `index` hay `noindex`

## Khuyến nghị publish order

Nếu publish theo thứ tự an toàn:

1. About
2. Authors
3. Editorial Policy
4. Corrections Policy
5. Team Verification
6. Masthead

Nếu publish một lần cũng được, nhưng sau đó nên:

- add footer trust links
- recrawl internal pages
- kiểm tra lại source để chắc không còn lỗi meta/schema lạ

## Kết luận cuối

Bộ trust pages hiện tại của DeFiliban đã vượt qua mức “placeholder SEO pages” và đã ở mức publisher stack dùng được.

Nếu publish wave 1 ngay bây giờ:

- hợp lý
- không quá sớm
- nhưng nên kèm một mini round cleanup cho Contact page và footer navigation để profile tổng thể nhìn sạch hơn
