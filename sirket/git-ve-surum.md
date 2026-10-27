---
kapsam: always
owner: Eren
durum: taslak
---
# Git ve Sürüm

## Branch
- `main` her zaman yayınlanabilir durumda. Doğrudan push yok.
- İsimlendirme: `feature/kisa-ad`, `fix/kisa-ad`, `hotfix/kisa-ad`.
- Branch kısa ömürlü olur, birkaç günden uzun yaşamaz.

## Commit
- Conventional Commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`.
- Bozan değişiklik: `feat!:` ve gövdede `BREAKING CHANGE:` açıklaması.
- Bir commit tek mantıksal değişiklik içerir.

## PR
- Açıklamada: ne, neden, risk seviyesi (düşük/orta/yüksek), nasıl test edildi, geri alma yolu.
- En az bir onay ve yeşil CI olmadan merge yok.
- Squash merge tercih edilir.

## Sürümleme
- SemVer: MAJOR (bozan), MINOR (yeni özellik), PATCH (düzeltme).
- Her sürüm etiketlenir (`v1.4.2`) ve değişiklik notu yazılır.

## main'e alma
- Yüksek riskli değişiklik feature flag arkasında gelir.
- Hotfix `main`'den açılır, merge sonrası hemen etiketlenir.
