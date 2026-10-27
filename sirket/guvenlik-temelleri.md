---
kapsam: always
owner: Eren
durum: taslak
---
# Güvenlik Temelleri

Bu dosya tek kaynaktır. Ayrıntılı kontroller security-reviewer rolünde ve security-audit skill'inde, buraya referans vererek yazılır.

## Sır yönetimi
- Şifre, token, API anahtarı koda, commit'e, loga girmez.
- Sırlar ortam değişkeni veya secret manager'dan okunur. `.env` dosyası `.gitignore`'da.
- Sızan sır hemen iptal edilir ve yenilenir; geçmişten silmek yetmez.

## Girdi doğrulama
- Dışarıdan gelen her veri güvenilmezdir: istek, dosya, header, webhook.
- Doğrulama sunucu tarafında yapılır. İstemci doğrulaması yalnızca kullanıcı deneyimi içindir.
- SQL için parametreli sorgu. String birleştirme ile sorgu yok.
- Çıktı bağlama göre encode edilir (HTML, URL, JSON).

## Yetki
- Her endpoint yetkiyi kendisi kontrol eder. Varsayılan: erişim yok.
- Hata mesajları iç detay (stack trace, SQL) göstermez.

## Bağımlılık riski
- Yeni bağımlılık eklemeden önce: bakımı sürüyor mu, lisansı uygun mu, gerçekten gerekli mi?
- Sürümler sabitlenir (lock dosyası commit'lenir).
- Bilinen açıklar düzenli taranır; kritik açık bekletilmez.
