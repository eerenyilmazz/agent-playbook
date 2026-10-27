---
kapsam: always
owner: Eren
durum: taslak
---
# Mühendislik İlkeleri

## Kod
- Mevcut yapıyı koru. Yeniden yazma yok, yalnızca küçük ve geri alınabilir değişiklikler.
- Katmanlar: Controller → Service → Domain → Infrastructure. Controller'da iş mantığı yok.
- Fonksiyonlar kısa ve tek amaçlı olur. Magic number/string yok, sabit kullan.
- Constructor injection. Gereksiz soyutlama yok.

## Adlandırma
- İsim ne yaptığını söyler: `calculateTotal`, `isExpired`. Kısaltma yok.
- Yorum "neden"i açıklar, "ne"yi değil.

## Küçük diff
- Bir PR tek bir iş yapar. Hedef: 400 satırın altında.
- Refactor ile davranış değişikliği aynı PR'da olmaz.
- API, şema veya UI'yı bozan değişiklik açıkça işaretlenir.

## "Bitti" tanımı
1. Kod derleniyor, mevcut testler geçiyor.
2. Yeni kod için en az birim test var.
3. Kabul ölçütleri karşılandı (bkz. kabul-olcutleri.md).
4. Code review onayı alındı.
5. Gerekiyorsa dokümantasyon ve değişiklik notu güncellendi.
6. Geri alma yolu belli.
