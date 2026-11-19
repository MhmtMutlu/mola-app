# mola-app

Mola'nın web sitesi: tanıtım sayfası, gizlilik politikası, kullanım koşulları, KVKK aydınlatma metni, verileri silme
ve destek. Uygulama bu sayfaları buradan açar. GitHub Pages ile yayınlanır; alan adı `mola.mm-apps.com` olacak.

15 dil: Türkçe `/`, İngilizce `/en/`, diğerleri `/<kod>/` altında İngilizce yol adlarıyla (`build.py` → `LANGUAGES`). Bir dil,
`src/landing.<kod>.json` var olduğunda derlenir; hukuk metinleri yalnız Türkçe ve İngilizcedir, diğer diller İngilizcesine bağlanır.

| Sayfa | Türkçe | English |
|---|---|---|
| Tanıtım | `/` | `/en/` |
| Gizlilik politikası | `/gizlilik/` (bağlayıcı) | `/en/privacy/` |
| Kullanım koşulları | `/kosullar/` (bağlayıcı) | `/en/terms/` |
| KVKK aydınlatma metni | `/kvkk/` | – |
| Verileri silme | `/hesap-silme/` | `/en/delete-account/` |
| Destek | `/destek/` | `/en/support/` |

## Düzenleme
- Tanıtım sayfasının metinleri `build.py` içindeki `S` sözlüğünde; destek ve silme sayfaları `src/support.*.md`,
  `src/delete.*.md`.
- Gizlilik politikası, kullanım koşulları ve KVKK metni **burada düzenlenmez:** tek kaynak uygulama deposunun
  `docs/legal/` klasörü. Değişince: `python3 tools/import_legal.py ../mola` → `python3 build.py`.
- Derleme: `python3 build.py` (statik HTML'i depo köküne, `sitemap.xml` ve `robots.txt`'yi yazar, bütün iç bağlantıları
  kontrol eder). Derlenmiş HTML de commit'lenir; GitHub Pages ek bir derleme adımı çalıştırmaz.
- Stil: `assets/site.css` (renkler ve yarıçaplar uygulamanın MolaDesign token'larıyla aynı: kâğıt zemin, mürekkep yazı; başlıklar sistem serifi). İkon ve çini görselleri
  uygulama deposundan gelir (`scripts/app-icon.sh`, `docs/screens/`).
- Yayın günü: `build.py` → `APP_ID` ve `APP_STORE_LIVE = True`.

## Gizlilik
Site çerez, analiz veya üçüncü taraf istek kullanmaz; Nunito yazı tipi (SIL OFL) `assets/fonts/` altından sunulur.

## Yayına alma
1. Settings → Pages → Source: *Deploy from a branch* → Branch: `main` / `(root)`. Adres:
   <https://mhmtmutlu.github.io/mola-app/>.
2. Alan adı: depo köküne içeriği `mola.mm-apps.com` olan bir `CNAME` dosyası eklenir; DNS'te `mola` → CNAME
   `mhmtmutlu.github.io` (Cloudflare, gri bulut). Bütün bağlantılar göreli olduğu için başka değişiklik gerekmez
   (404 sayfası yalnız alan adı kökünde doğru çalışır).
