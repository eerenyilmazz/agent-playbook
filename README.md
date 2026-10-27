# md-kurallar

Agent ekibinin kural dosyaları.

## Yapı
- `sirket/` — Her işte yüklenen (always) kurallar. Kısa tutulur.
- `sablonlar/` — İş türüne göre yüklenen (task) kurallar.
- `roller/` — Rol bazlı kurallar.
- `skills/` — Adım adım yordamlar (SKILL.md).

## Kurallar
- md "ne ve neden"i anlatır, skill "nasıl"ı. Skill kural kopyalamaz, md'ye referans verir.
- Bir konu tek dosyada durur.
- Always dosyalarının toplamı 5000 token limitine sığmalı.
- Her dosyada `owner` ve `durum` (taslak/onaylı) alanı bulunur.
- Hukuk, mevzuat ve ödeme dosyaları uzman onayı olmadan "onaylı" olamaz.
