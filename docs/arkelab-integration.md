# agent-playbook ↔ ArkeLab entegrasyon notu

Tarih: 2026-11-04
Kaynak repo: https://github.com/eerenyilmazz/agent-playbook (geliştirici: Eren)
Durum: taslak. Repo'dan yalnız GitHub üzerinden okundu; klonlanmadı, betikler çalıştırılmadı.

## 1. Amaç

agent-playbook, ArkeLab'ın "Ekip ve Şablonlar" modelinin içerik katmanı olarak kullanılacak: şirket kuralları, şablon ve rol bilgileri md olarak playbook'ta yazılır, ArkeLab bunları kendi kayıtlarına (company / template / role / skill) aktarır. Plugin değil, ana geliştirmenin parçasıdır.

## 2. Repo özeti

- 132 dosya. Python betikleri: `scripts/load.py`, `scripts/check.py`. CI: `.github/workflows/check.yml`.
- `company/` (5 dosya, her zaman yüklenir), `templates/<tür>/` (8 tür, 28 dosya), `roles/<rol>/` (14 rol, 28 dosya), `skills/<ad>/SKILL.md` (12 skill), `examples/` (5), `docs/` (yalnız insan için), `AGENTS.md`, `INDEX.md` (üretilen yönlendirme tablosu).
- Dosya başlığı: `scope: always|task`, `when`, `owner`, `status: draft`; hassas dosyalarda `review: expert-required`.
- Bütçe: istem sınırı 5000 token (karakter÷4). `always` dosya başına 400, toplam 2500; `task` dosya başına 600.
- Yükleme sırası: company → skill → rol dosyaları → `when` eşleşmesine göre en çok 5 şablon dosyası.
- Öncelik: kullanıcı > proje README > company > şablon > rol > skill.
- Boşluk raporu: `Playbook gap: <dosya/konu> — <eksik> — <öneri>`.

## 3. Kavram eşlemesi

| Playbook | ArkeLab |
|---|---|
| `company/*.md` | Şirket dokümanı, katman `always` |
| `templates/<tür>/*.md` | Şablon dokümanı |
| `roles/<rol>/*.md` | Rol dokümanı (`roles[]` süzgeci) |
| `scope: always` / `task` | `tier: always` / `task` |
| `examples/*.md` | `tier: reference` |
| `docs/*.md` | İçe aktarılmaz (yalnız insan) |
| `when:` | `when` (en çok 200 karakter) |
| `owner:` | `owner` (en çok 80 karakter) |
| `status: draft` | `reviewedAt` boş |
| `review: expert-required` | karşılığı yok (bkz. §5) |
| `skills/<ad>/SKILL.md` | AI Araçları skill kaydı (tüm sağlayıcılara yazılır) |
| `Playbook gap:` satırı | `company_report` / görev yorumu / PM `company_review` boşlukları |

## 4. Ad eşlemesi

Roller:
- Aynı: `qa-security`, `code-reviewer`, `decision-maker`, `security-reviewer`, `devops-cloud`
- Farklı: `backend` → `backend-developer`, `frontend` → `frontend-developer`, `pm` → `project-manager`
- ArkeLab'da kaydı olmayan: `data-engineer`, `game-developer`, `mobile-developer`, `release-manager`, `technical-writer`, `ux-designer`

Şablonlar:
- Aynı: `software`, `web`, `web-panel`, `web-commerce`, `mobile`, `game`
- Farklı: `desktop` → `desktop-product`, `idle-game` → `game-idle`

Not: Eşleme tabloları ArkeLab kataloğundaki kimliklerin hatırlanmasına dayanıyor; uygulamadan önce koddan doğrulanmalı.

## 5. Uyumsuzluklar ve çözümleri

1. **`always` dosya boyutu.** Playbook 400 token (~1600 karakter) izin veriyor; ArkeLab `always` dokümanlarını 1200 karaktere kırpıyor. İçerik sessizce kesilir. Önce çözülmeli: limiti artır veya dosyaları kısalt.
2. **Birim belirsizliği.** Playbook 5000 *token*. ArkeLab `PROMPT_LIMIT=5000` değeri hatırımda karakter. Doğrulanmalı; karaksa bütçe yaklaşık 4 kat dar.
3. **Durum alanı.** `expert-required` için ArkeLab'da alan yok. Seçenekler: yeni `review` alanı, ya da `expert-required` dosyaları içe aktarmayıp yalnız listelemek. Öneri: yeni alan, uzman onayı olmadan `approved` sayılmasın.
4. **Python.** `load.py`/`check.py` uygulama içinde kullanılmaz. Yükleme ArkeLab'ın kendi yükleyicisinde kalır; `check.py` yalnız playbook CI'ında çalışır.
5. **Sıralama.** Playbook'un `when`'e göre şablon dosyası sıralaması ArkeLab'da yok (rol süzgeci var). İlk sürümde şart değil.
6. **Öncelik kuralı.** ArkeLab'da yalnız `hides` ve çakışma raporu var. Playbook'taki öncelik sırası şirket md'sine yazılır.
7. **ArkeLab'a özel kurallar.** Görev kapısı, `branch.publish`, owner-only main, Jira durumları playbook'ta yok ve olmamalı. Ayrı bir "ArkeLab çalışma kuralları" dokümanı olarak ArkeLab tarafında tutulur.
8. **Eksik rol kayıtları.** Playbook rol için yalnız md veriyor; `does / doesNot / handoff / evals` alanları ArkeLab'da ayrıca yazılmalı.
9. **Dil.** Playbook İngilizce, ArkeLab arayüzü ve mevcut md'ler Türkçe. Karar verilmeli (§8).
10. **Çifte içerik.** `electron/company-starter-docs.cjs` içindeki başlangıç md'leri playbook ile çakışır. Tek kaynak playbook olur, eskiler kaldırılır.

## 6. Tasarım

İçe aktarıcı, ArkeLab'ın mevcut plan → önizleme → onay (`apply`, hash, 15 dk) akışını kullanır; doğrudan veri yazmaz.

1. Playbook sürümünü (commit/etiket) oku, ağacı çek.
2. `INDEX.md` yerine dosya başlıklarından kendi tablosunu üret (ayrıştırma: `anahtar: değer`, `---` blokları).
3. Eşleme tablolarıyla her dosyayı company / şablon / rol dokümanına çevir; `docs/` ve betikleri atla.
4. Skill'leri `name`+`description` doğrulamasıyla (ad klasör adına eşit) AI Araçları akışına ver.
5. Ürettiği planı önizlet: eklenecek, değişecek, silinecek dosyalar; boyut ve bütçe uyarıları; ad çakışmaları.
6. Onaydan sonra `apply`; kayıtlar `draft` gelir; geçmişe kaynak commit yazılır.
7. Sonraki sürümde yalnız fark planı üret (kullanıcının yerel düzenlemesini ezme: çakışmada sor).

## 7. Aşamalar

1. **Hazırlık:** §5-1 ve §5-2'yi çöz (limit ve birim).
2. **İçe aktarıcı** + eşleme tabloları + testler (örnek playbook ağacıyla).
3. **Skill'ler** (12) ve **şirket/şablon md'leri**.
4. **Eksik 6 rol kaydı** (`does/doesNot/handoff/evals`).
5. **Güncelleme akışı** (fark planı) ve `Playbook gap` → rapor bağlantısı.
6. **Playbook CI'ına** `check.py` ile ArkeLab sınırlarının (boyut, ad) kontrolü.

## 8. Kararlar (Eren, 2026-11-04)

- **Dil:** İngilizce kalır. ArkeLab arayüzü Türkçe kalabilir; md gövdeleri çevrilmez.
- **`expert-required`:** ArkeLab'a yeni `review` alanı eklenir. Bu alanı taşıyan doküman uzman onayı (isim + tarih) olmadan `approved` sayılmaz. Dosyalar içe aktarılır.
- **Güncelleme:** PR akışı. Herkes PR açar, Eren (`@eerenyilmazz`, CODEOWNERS) onaylar; `check.py` CI'da geçmeden merge yok. Ayrıntı: `CONTRIBUTING.md`.
- **Starter md'ler:** `electron/company-starter-docs.cjs` içindeki başlangıç md'leri tamamen silinir; tek kaynak playbook.

## 8a. Playbook tarafında yapılanlar (2026-11-04)

- `company/` dosyaları ArkeLab'ın 1200 karakterlik `always` sınırının altında (en büyüğü 1188).
- `check.py` ArkeLab sınırlarını da denetliyor: `always` ≤ 1200 karakter, `when` ≤ 200, `owner` ≤ 80.
- Commit'lenmiş `__pycache__` silindi, `.gitignore` eklendi.

## 8b. ArkeLab kodundan doğrulananlar (2026-11-04, Arkhelab-main zip)

- **§5-2 birim: karakter.** `electron/company-system.cjs`: `PROMPT_LIMIT = 5000` karakter, tüm isteme (şirket + şablonlar + roller + doküman listeleri) uygulanır, 300 karakter pay ayrılır; sığmayan bölümler düşer ve uyarı eklenir. `always` dokümanlar içerik olarak gömülür ve 1200 karakterde kırpılır; `task` dokümanlar yalnız ad + `when` ile listelenir; `reference` yalnız ad.
- **Karar (Eren): 2 always + 4 task.** `engineering-principles` ve `security-basics` `always` ve kısaltılmış özet (toplam ~1300 karakter); ayrıntılar `security-details` (task) ve `git-and-versioning` (PR kuralları) dosyalarında. `git-and-versioning`, `incidents-and-rollback`, `documentation-standard`, `security-details` `task`. Öncelik sırası `engineering-principles`'ta. `check.py`: `always` gövdeleri toplamı ≤ 2400 karakter, `when` ≤ 60 karakter.
- **Ölçüm (içe aktarıcı ile, ArkeLab `brief`):** web-commerce + 3 rol → 3996; web-panel + web-commerce + 5 rol → 4601; mobile + web-panel + 5 rol → 4602 karakter (sınır 4700). 2 şablon + 7 rolde rol bölümü düşer (ArkeLab uyarı verir). Daha büyük ekipler için owner kararı: `PROMPT_LIMIT` veya rol bölümünün sırası.
- **§4 ad eşlemesi (düzeltilmiş):**
  - Roller aynı: `decision-maker`, `qa-security`, `code-reviewer`, `security-reviewer`, `devops-cloud`, `technical-writer`, `data-engineer`.
  - Roller farklı: `pm` → `project-manager`, `frontend` → `frontend-developer`, `backend` → `backend-developer`, `ux-designer` → `ui-ux-engineer`.
  - ArkeLab'da yok: `game-developer`, `mobile-developer`, `release-manager`. ArkeLab'da olup playbook'ta yok: `researcher`.
  - Şablonlar farklı: `idle-game` → `game-idle`, `desktop` → `desktop-product`. ArkeLab'da olup playbook'ta yok: `web-presentation`, `game-mobile`, `game-pc`, `game-hyper-casual`.
- **Kayıt sınırları:** kayıt başına en çok 30 doküman; ad `.md` ile biten ve benzersiz; içerik ≤ 20000; `when` ≤ 200; `owner` ≤ 80; `roles` ≤ 40 kimlik.
- **Main'e alma:** ArkeLab'da yalnız owner `burak` (Burakka1). Eren'in değişiklikleri kişisel branch'ten gelir.

## 8c. Hâlâ açık

- §10 kural çakışması: `git-and-versioning` (squash, protected main) ile ArkeLab yayınlama kuralları (`branch.publish`, owner-only main) — ArkeLab'a özel kurallar ArkeLab tarafında kalır; playbook genel kural olarak çelişmiyor ama agent önceliği için ArkeLab şirket kuralları playbook'un üstünde olmalı.
- Lisans: playbook'ta yok.

## 9. Kabul ölçütleri

- Örnek playbook içe aktarılınca 8 şablon, 14 rol, 12 skill, 5 şirket dosyası oluşur; hiçbiri `approved` gelmez.
- `always` toplamı istem sınırını aşarsa önizleme uyarır; sessiz kırpma yok.
- Aynı sürüm iki kez içe aktarılınca fark boştur.
- Yerel düzenlenmiş doküman sürüm güncellemesinde ezilmez.
- `npm run test` ve `npm run build` geçer.

## 10. Riskler

- İçerik hâlâ taslak; ödeme/vergi/mağaza politikası dosyaları uzman onayı olmadan güvenilmemeli.
- `git-and-versioning.md` ve `engineering-principles.md` ArkeLab kurallarıyla (main'e alma, Ponytail) çelişebilir; gövdeleri okunmadı.
- Repo'da `scripts/__pycache__/*.pyc` commit'lenmiş; `.gitignore` gerekli. Lisans görülmedi.

## 11. Doğrulanmayanlar

Dosya gövdelerinin çoğu okunmadı; `load.py` ve `check.py` çalıştırılmadı; CI sonucu bakılmadı; ArkeLab limit birimi ve katalog kimlikleri koddan teyit edilmedi.
