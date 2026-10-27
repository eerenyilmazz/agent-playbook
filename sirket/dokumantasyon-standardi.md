---
kapsam: always
owner: Eren
durum: taslak
---
# Dokümantasyon Standardı

## README (her repoda)
- Proje ne yapar (2–3 cümle).
- Yerelde nasıl çalıştırılır.
- Testler nasıl çalıştırılır.
- Gerekli ortam değişkenleri (değerleri değil, isimleri).
- Sorumlu kişi.

## ADR (mimari karar kaydı)
Geri dönmesi pahalı her karar için yazılır. Ayrıntılı şablon: mimari-karar-kaydi.md (tek kaynak).
- Dosya: `docs/adr/0001-kisa-baslik.md`
- Bölümler: Bağlam, Karar, Alternatifler, Sonuçlar, Durum (önerildi/kabul/iptal).
- Kabul edilmiş ADR değiştirilmez; yeni ADR ile geçersiz kılınır.

## Değişiklik notu
- `CHANGELOG.md`, sürüm başına bir bölüm.
- Başlıklar: Eklenen, Değişen, Düzeltilen, Kaldırılan.
- Bozan değişiklikler en üstte ve açıkça işaretli.
- Kullanıcının anlayacağı dille yazılır, commit listesi kopyalanmaz.

## Genel
- Doküman kodla aynı PR'da güncellenir.
- Tekrar yok: bir bilgi tek yerde durur, diğer yerler link verir.
