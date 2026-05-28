# DeFiliban Publish Matrix

Ngày: 2026-05-28

## Mục tiêu

Tài liệu này chốt 4 việc:

- page nào publish được ngay
- page nào nên giữ draft thêm một nhịp
- việc gì cần chỉnh tay trong WP trước khi publish
- thứ tự publish hợp lý

## Snapshot hiện tại

Các page draft đã có:

- Privacy Policy
  - ID `3`
  - slug `privacy-policy`
- About
  - ID `10262`
  - slug `about`
- Authors
  - ID `10268`
  - slug `authors`
- Editorial Policy
  - ID `10270`
  - slug `editorial-policy`
- Corrections Policy
  - ID `10272`
  - slug `corrections-policy`
- Team Verification
  - ID `10274`
  - slug `team-verification`
- Masthead
  - ID `10278`
  - slug `masthead`
- Terms of Service
  - ID `10286`
  - slug `terms-of-service`
- Disclaimer
  - ID `10287`
  - slug `disclaimer`

## Publish Now

Các page dưới đây có thể publish ngay nếu mục tiêu là hoàn thiện trust/legal stack wave 1:

1. About
2. Authors
3. Editorial Policy
4. Corrections Policy
5. Team Verification
6. Masthead
7. Privacy Policy
8. Terms of Service
9. Disclaimer

Lý do:

- nội dung đã đủ coherent
- slug sạch
- intent rõ
- cross-link giữa các trust pages đã khá đầy đủ

## Có thể giữ draft thêm nếu muốn cầu toàn

Nếu muốn polish thêm trước khi public, ưu tiên giữ draft thêm cho:

1. Team Verification
2. Masthead
3. Authors

Lý do:

- 3 page này sẽ mạnh hơn nhiều nếu có thêm avatar/headshot
- nếu có social/account chính thức thì nên thêm vào Team Verification
- nếu có role editor thật thì Masthead sẽ nhìn đúng chất newsroom hơn

Nhưng:

- đây là “nice to have”
- không phải blocker cho publish wave 1

## Nên publish theo thứ tự nào

Thứ tự publish khuyên dùng:

1. About
2. Authors
3. Editorial Policy
4. Corrections Policy
5. Privacy Policy
6. Terms of Service
7. Disclaimer
8. Team Verification
9. Masthead

Lý do:

- đi từ publisher identity
- sang editorial accountability
- rồi legal pages
- cuối cùng mới public các page verification/masthead hỗ trợ

## Việc cần chỉnh tay trong WP trước khi publish

### 1. Footer / menu trust links

Nên thêm cụm link sau vào footer hoặc footer nav:

- About
- Authors
- Editorial Policy
- Corrections Policy
- Privacy Policy
- Terms of Service
- Disclaimer
- Team Verification
- Masthead
- Contact

Đây là việc quan trọng nhất còn lại ở lớp UX / discoverability.

### 2. Contact page

Hiện tại live check cho thấy:

- `https://defiliban.io/contact/`
- meta robots đang là `follow, noindex`
- source còn dấu vết metadata/schema cũ chưa sạch

Khuyến nghị:

- dọn page này trước hoặc ngay sau khi publish trust stack
- quyết định rõ giữ `noindex` hay chuyển sang `index`

Nếu muốn trust profile sạch hơn:

- nên chuyển Contact thành page sạch, public, usable

### 3. Privacy slug conflict check

Hiện tại:

- draft privacy policy đúng là `privacy-policy`
- nhưng `/privacy/` đang 301 sang bài viết `privacy-bitcoin-or-ai-bitcoin`

Điều này không chặn publish `privacy-policy`, nhưng có thể gây nhiễu nếu người dùng hoặc plugin kỳ vọng slug `/privacy/`.

Không bắt buộc xử lý ngay, nhưng nên ghi nhớ.

### 4. Author archive polish

Nếu có thời gian, nên chỉnh:

- avatar/headshot
- bio formatting
- profile links nếu có

## Việc nên làm ngay sau khi publish

1. Purge cache
2. Mở từng page live để check:
   - title
   - meta description
   - internal links
   - không có text lỗi / markdown lỗi
3. Crawl lại riêng nhóm trust pages
4. Check source của:
   - Contact
   - Privacy Policy
   - About
   - Authors
5. Đảm bảo footer/menu đã thấy trust links

## Việc không cần chặn publish

Các điểm này nên cải thiện dần, nhưng không phải blocker:

- chưa có headshot cho author
- chưa có official social links
- chưa có dedicated editorial email
- chưa có company/entity detail sâu hơn trong About
- chưa có governance detail kiểu CoinDesk

## Publish Decision

### Publish ngay được

- About
- Authors
- Editorial Policy
- Corrections Policy
- Privacy Policy
- Terms of Service
- Disclaimer
- Team Verification
- Masthead

### Nên chỉnh tay trước hoặc ngay sau publish

- Contact page
- footer/menu trust links

## Kết luận cuối

Wave trust/legal/publisher pages hiện tại đã đủ để publish.

Nếu phải chọn 2 việc còn đáng làm nhất trước khi bấm publish hàng loạt, thì là:

1. thêm trust links vào footer/menu
2. dọn Contact page

Ngoài 2 điểm đó, phần còn lại đã ở mức đủ tốt cho wave 1.
