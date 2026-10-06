# XAUUSD AI Trading Bot (MetaTrader 5)

Dự án này là một hệ thống AI (Trí tuệ nhân tạo) được thiết kế chuyên biệt để phân tích giá Vàng (XAUUSD) trên nền tảng MetaTrader 5 (MT5). Hệ thống hoạt động như một "Bộ lọc" tín hiệu, áp dụng nhiều logic giao dịch tiên tiến để đưa ra khuyến nghị Mua/Bán/Đứng ngoài.

## Triết lý Giao dịch (Ensemble Logic)
Hệ thống ra quyết định dựa trên sự đồng thuận của 3 mô-đun (chuyên gia) độc lập:
1.  **SMC (Smart Money Concepts):** Quét các vùng thanh khoản bị phá vỡ (Liquidity Sweeps) và Fair Value Gaps (FVG) để tìm kiếm dòng tiền của "Cá mập".
2.  **Macro Correlation (Tương quan vĩ mô):** Phân tích sức mạnh của chỉ số Đô la Mỹ (DXY) để đánh giá động lực ngược chiều lên giá Vàng.
3.  **Mean Reversion (Hồi quy trung bình):** Sử dụng Bollinger Bands để ngăn chặn việc mua/bán đuổi khi giá đã đi quá xa giá trị thực tế.

Tín hiệu cuối cùng chỉ được phát ra khi có sự đồng thuận cao để bảo vệ vốn.

## Yêu cầu Hệ thống (Prerequisites)
Để chạy dự án này trên máy của bạn, bạn cần:
1.  Hệ điều hành Windows (Vì MetaTrader 5 chỉ hỗ trợ đầy đủ trên Windows).
2.  Cài đặt phần mềm **MetaTrader 5 (MT5)** và đăng nhập vào tài khoản (Demo hoặc Real).
3.  Cài đặt ngôn ngữ lập trình **Python 3.9+**.
4.  *(Quan trọng để đẩy code lên Github)* Cài đặt **Git**.

## Hướng dẫn Cài đặt
1. Mở Terminal (Command Prompt / PowerShell).
2. Cài đặt các thư viện cần thiết bằng lệnh:
   ```bash
   pip install -r requirements.txt
   ```
3. Mở phần mềm MT5. Đảm bảo bạn đã cho phép "Allow algorithmic trading" trong cài đặt (Tools -> Options -> Expert Advisors).
4. Chạy file chính:
   ```bash
   python main.py
   ```

## Tuyên bố Từ chối Trách nhiệm
Mã nguồn này được sinh ra với mục đích nghiên cứu và tư vấn tín hiệu. Giao dịch Vàng (XAUUSD) chứa đựng rủi ro tài chính cực kỳ lớn. Hãy luôn sử dụng chức năng tính toán Stop-Loss của hệ thống và kiểm thử trên tài khoản Demo trước khi giao dịch tiền thật.
