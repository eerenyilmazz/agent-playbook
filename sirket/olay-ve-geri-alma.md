---
kapsam: always
owner: Eren
durum: taslak
---
# Olay ve Geri Alma

Adım adım yordam incident-postmortem skill'indedir. Bu dosya kuralları tanımlar.

## Prod sorunu
1. Önce etkiyi durdur, sonra kök nedeni ara.
2. İlk tercih geri almadır (önceki sürüm veya feature flag kapatma). Prod'da canlı düzeltme denemesi yapılmaz.
3. Ne gözlendiği, ne yapıldığı ve saatleri not alınır.
4. Etkilenen kullanıcı/müşteriye durum bildirilir.

## Hotfix
- `main`'den `hotfix/` branch'i açılır. Kapsam yalnızca sorunun kendisi.
- Review atlanmaz; hızlandırılır.
- Merge sonrası sürüm etiketlenir, değişiklik notuna eklenir.

## Geri alma kuralları
- Her yayının geri alma yolu yayından önce bellidir.
- Veri migrasyonu geri alınamıyorsa bu, yayın öncesinde açıkça yazılır.

## Postmortem şablonu
- **Özet:** Ne oldu, ne kadar sürdü, kimi etkiledi.
- **Zaman çizelgesi:** Tespit, müdahale, çözüm saatleri.
- **Kök neden:** Teknik ve süreçsel.
- **Ne iyi gitti / ne kötü gitti.**
- **Aksiyonlar:** Sorumlu ve tarih ile.

Postmortem suçlu aramaz; sistemi düzeltir.
