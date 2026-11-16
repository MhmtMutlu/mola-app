# Mola Gizlilik Politikası

**Yürürlük tarihi:** 15 Kasım 2026 · **Sürüm:** 1.0

Bu metin, KVKK (6698 sayılı Kişisel Verilerin Korunması Kanunu) madde 10 uyarınca aydınlatma metni ve AB Genel Veri
Koruma Tüzüğü (GDPR) madde 13 uyarınca bilgilendirme olarak hazırlanmıştır. Kısa KVKK aydınlatma metni:
https://mola.mm-apps.com/kvkk/. Bağlayıcı metin Türkçedir (Bölüm 14).

---

## Kısaca

- **Adını, e-postanı, telefonunu, konumunu ya da reklam kimliğini istemeyiz.** Mola'da hesap açmazsın, parola yoktur.
- **Ekran süresi verin telefonundan çıkmaz.** Hangi uygulamayı ne kadar kullandığını biz göremeyiz; ebeveyn de
  göremez. Mola, Apple'ın Ekran Süresi sistemini kullanır ve bu sistem kullanım verisini cihazda tutar.
- **Mesajlarını, fotoğraflarını, rehberini okumayız.** Mola'nın buna ne izni ne de bir yolu vardır.
- **Ailenizin cihazları arasındaki her şey uçtan uca şifrelidir.** Kurallar, süre istekleri, yazdığın kısa neden ve
  aile içinde görünen adın, yalnız ailenizin cihazlarının açabileceği şekilde şifrelenir. Sunucumuz bunları **okuyamaz.**
- Mola'yı yalnız kendin için (engelleme planları, odak ve çini duvarı) kullanırsan **sunucumuza hiçbir şey gitmez.**
- Aile kurarsanız Türkiye'deki sunucumuzda yalnız şunlar durur: rastgele üretilmiş kimlikler, şifreli ve en çok 25 saat
  yaşayan zarflar ve, ebeveyn telefonunda bildirimleri açtıysan, Apple'ın o telefon için ürettiği bildirim jetonu.
  **Çocuk telefonlarından bildirim jetonu alınmaz.**
- **Seni izlemeyiz,** verilerini **satmayız,** reklam göstermeyiz. Uygulamada analitik ya da çökme raporlama aracı yoktur.
- Sorun olursa Türkçe ya da İngilizce yaz: **destek@mm-apps.com**

---

## 1. Biz kimiz? (Veri sorumlusu)

Veri sorumlusu: **Mehmet Mutlu** (Türkiye'de yaşayan bireysel geliştirici; "Mola", "biz").

- İletişim: **destek@mm-apps.com**

Bir veri koruma görevlisi (DPO) atamakla yükümlü değiliz. Avrupa Birliği'nde, Birleşik Krallık'ta ya da İsviçre'de bir
temsilcimiz yoktur; bu ülkelerdeki kullanıcılar ve makamlar dahil herkes bize doğrudan ulaşır.

## 2. Bu politika neyi kapsar?

Bu politika iOS, iPadOS ve watchOS için Mola uygulamasını, uygulamanın aile sunucusunu ("relay") ve bizimle yaptığın
yazışmaları kapsar. App Store'un kendisi, Apple'ın Ekran Süresi ve Aile Paylaşımı özellikleri ve Apple'ın bildirim
hizmeti, Apple'ın kendi gizlilik politikasına tabidir.

Bu sayfanın yayımlandığı site çerez ve analiz aracı kullanmaz. Site GitHub Pages üzerinde barındırılır; sayfayı
açtığında IP adresin, her web sitesinde olduğu gibi, barındırıcıya (GitHub, ABD) ulaşır ve GitHub bunu kendi gizlilik
politikasıyla işler.

## 3. Hangi bilgiler nerede durur?

### 3.1 Yalnız cihazında kalanlar

Bunlar sunucumuza **hiç gönderilmez** (aile cihazlarına giden kısım Bölüm 3.2'deki gibi şifreli gider):

| Bilgi | Açıklama |
| --- | --- |
| Ekran süresi kullanımı | Apple'ın Ekran Süresi sistemi cihazda tutar. Mola yalnız "günlük sınırın şu kadarı doldu" haberini cihazın içinde alır; hangi uygulamada ne kadar kaldığını Mola da öğrenemez. |
| Uygulama seçimi | Hangi uygulamaların sınırlanacağı Apple'ın seçim ekranında belirlenir ve cihazda kalır. Bu seçim başka bir cihaza ya da sunucuya aktarılamayan, Apple'a özgü belirteçlerdir. |
| Kurallar, modlar, süre istekleri ve nedenleri | Cihazda saklanır; aile cihazlarına yalnız uçtan uca şifreli gider. |
| Aile içinde görünen ad | Kurulumda yazdığın ad. Yalnız ailenizin cihazlarında görünür; gerçek adın olmak zorunda değildir. |
| Engelleme planların, günlük sınırların, kendi odak programların, odak oturumların, günlük odak sürelerin ve çini duvarın | Yalnız cihazında. |
| Şifreleme anahtarları | Cihazın anahtar zincirinde; yalnız bu cihazda. Aile anahtarı ebeveynin ekranındaki QR kodla çocuğun kamerasına geçer, sunucuya hiç gitmez. |

Uygulamayı silersen bu bilgiler cihazından silinir. iCloud yedeğin açıksa uygulama verileri Apple'ın yedekleme
kurallarına göre yedeğine girebilir; bunu iOS Ayarları'ndan yönetirsin.

### 3.2 Aile sunucumuzdan geçenler (yalnız aile kurarsanız)

Ebeveyn ve çocuk telefonları farklı Apple hesaplarında olduğu için, komutların ve isteklerin buluşacağı bir sunucu
gerekir. Bu sunucu yalnız kapalı zarf taşır.

| | |
| --- | --- |
| **Veriler** | Rastgele üretilen hesap numarası ve oturum anahtarları; hesabın açılış ve son giriş zamanı; rastgele aile kimliği ve rastgele üye kimliği; ailenin erişim jetonunun özeti (jetonun kendisi değil); kayıtların oluşturulma zamanları ve cihazın sunucuya en son bağlandığı zaman; **şifreli zarflar** (zarf kimliği, gönderen ve alıcı üye kimliği, oluşturulma ve son kullanma zamanı ve sunucunun okuyamadığı şifreli içerik); herkese giden zarflar için "alındı" kaydı; aileden çıkarılan bir cihaz için o cihazın rastgele üye kimliği ve sunucunun okuyamadığı, ebeveynin imzaladığı kısa bir bildirim |
| **Amaç** | Bir aile cihazının gönderdiği komutu, kuralı, isteği ya da yanıtı ailenin diğer cihazlarına iletmek; aileye yalnız aile anahtarını bilen cihazların katılabilmesini sağlamak |
| **Hukuki dayanak** | Sözleşmenin kurulması ve ifası: KVKK m.5/2(c) · GDPR m.6/1(b). Kötüye kullanımı önleyen sınırlar için meşru menfaat: KVKK m.5/2(f) · GDPR m.6/1(f) |
| **Saklama** | Tek cihaza giden zarf, o cihaz alınca **hemen** silinir. Diğer zarflar en çok **25 saat** yaşar. Cihaz kaydı, aileden ayrılana kadar; cihaz **180 gün** boyunca sunucuya hiç bağlanmazsa kendiliğinden silinir. Aileye hiç katılmamış hesaplar 2 gün sonra silinir. Aileden çıkarılan bir cihazın hesabı, kaydı ve zarfları **hemen** silinir; o cihaza bırakılan şifreli bildirim 180 gün sonra silinir. |

Sunucu zarfın içini okuyamaz: içerik cihazında ailenizin anahtarıyla şifrelenir (ChaCha20-Poly1305) ve gönderen
cihazın anahtarıyla imzalanır (Ed25519). Sunucuda ad, e-posta, kullanım verisi, uygulama listesi ya da kural **bulunmaz.**

**IP adresi.** Cihazın sunucuya bağlanırken IP adresi, bağlantının doğası gereği sunucuya ulaşır. Bunu hesabınla
birlikte saklamayız: sunucu yazılımımızı erişim günlüğü tutmayacak biçimde yapılandırdık; oturum kayıtlarındaki IP
adresi ve cihaz bilgisi yazılır, ancak en geç bir saat içinde silinir. Adres, kötüye kullanımı sınırlayan kısa süreli
sayaçlarda bellekte kullanılır. Barındırma sağlayıcımız, kendi yasal yükümlülükleri gereği ağ trafiği kayıtlarını kendi
sorumluluğunda tutabilir.

### 3.3 Bildirimler (isteğe bağlı, yalnız ebeveyn telefonunda)

Bildirimler yalnız **ebeveyn telefonunda** ve yalnız sen açarsan kullanılır. Mola önce ne olacağını kendi ekranında
anlatır; "Bildirimleri aç"a dokunursan iOS'un sorusu gelir. Açarsan çocuğunun süre isteği, uygulama kapalıyken de sana
ulaşır. Açmazsan Mola çalışmaya devam eder; istekler uygulamayı açtığında gelir.

**Çocuk telefonlarında bildirim kullanılmaz ve çocuk telefonundan bildirim jetonu alınmaz.** Ebeveynin verdiği mola ya
da yeni bir kural, çocuğun telefonunda Mola açıldığında ya da iOS uygulamaya arka planda sıra verdiğinde uygulanır. Okul,
uyku ve günlük sınır gibi planlı kurallar telefonda kayıtlıdır ve internet olmadan da çalışır.

| | |
| --- | --- |
| **Veriler** | Apple'ın bu telefon ve uygulama için ürettiği **bildirim jetonu**; jetonun test mi gerçek mi olduğu |
| **Amaç** | Ailenden yeni bir zarf geldiğinde ebeveynin telefonunu uyandırmak |
| **Hukuki dayanak** | Senin açtığın bildirim özelliğinin yerine getirilmesi: KVKK m.5/2(c) · GDPR m.6/1(b). Bildirimleri iOS Ayarları → Bildirimler → Mola'dan istediğin an kapatırsın |
| **Saklama** | Bildirimleri kapatana (kapattıktan sonra uygulamayı bir kez açtığında jeton sunucudan silinir), aileden ayrılana ya da Apple jetonun geçersiz olduğunu bildirene kadar |
| **Alıcı** | Apple'ın bildirim hizmeti (Bölüm 4 ve 5) |

Bildirimin içinde ad, aile kimliği ya da mesajın içeriği **yoktur.** Sunucu içeriği okuyamadığı için bildirim yalnız
"Ailenden yeni bir güncelleme var" der; metni telefonun kendi dilinde gösterir.

### 3.4 Bize yazarsan

| | |
| --- | --- |
| **Veriler** | E-posta adresin, yazdıkların ve yanıtlarımız |
| **Amaç** | Sorunu yanıtlamak, başvurunu sonuçlandırmak |
| **Hukuki dayanak** | Meşru menfaat ve, başvurularda, hukuki yükümlülük: KVKK m.5/2(f), m.5/2(ç) · GDPR m.6/1(f), m.6/1(c) |
| **Saklama** | Yazışma kapandıktan sonra en çok 24 ay |

### 3.5 Hiç toplamadıklarımız

Ad ve soyad, e-posta (bize yazmadıkça), telefon numarası, doğum tarihi ve yaş, parola, konum, rehber, fotoğraflar,
mesajlar, tarama geçmişi, sağlık verisi, reklam kimliği (IDFA). iOS'un "izleme izni" sorusunu sormayız. Uygulamada
analitik, çökme raporlama, reklam ya da pazarlama aracı yoktur.

## 4. Verilerini kimlerle paylaşıyoruz?

Verilerini **satmayız** ve reklam amacıyla **paylaşmayız.** Yalnız şu alıcılar söz konusudur:

| Alıcı | Ne alır? | Neden? | Rolü |
| --- | --- | --- | --- |
| **Ailenizin diğer cihazları** | Kurallar, komutlar, istekler ve aile içi ad; uçtan uca şifreli | Uygulamanın işlevi | — |
| **Güzel Hosting** (GNET İnternet Telekomünikasyon A.Ş., Türkiye) | Bölüm 3.2 ve 3.3'teki sunucu verileri | Sunucumuzun bulunduğu sanal sunucu hizmeti; veritabanı ve sunucu yazılımı (açık kaynaklı Supabase) bu sunucuda, bizim işletmemizle çalışır | Barındırma hizmeti sağlayıcı; herkese açık hizmet koşullarıyla çalışır, aramızda ayrıca bir veri işleme sözleşmesi yoktur |
| **Güzel Hosting**, kurumsal e-posta | Bize yazdığın e-postalar ve yanıtlarımız | Destek adresimiz bu hizmette barındırılır | Aynı |
| **MailChannels Corporation** (Kanada) | Sana gönderdiğimiz yanıtın içeriği ve e-posta adresin, yalnız iletim sırasında | Güzel Hosting'in posta iletim hizmeti | Güzel Hosting'in alt hizmeti; kendi koşullarıyla çalışır |
| **Apple** (Apple Distribution International Ltd. ve bağlı şirketleri) | Uygulamanın App Store'dan indirilmesi; Ekran Süresi ve Aile Paylaşımı (bunlar cihazında Apple'ın sistemidir); ebeveyn telefonunda bildirimleri açtıysan o telefonun bildirim jetonu, uygulamanın kimliği ve içeriksiz bir bildirim, sunucumuzdan; iOS ayarlarında izin verdiysen Apple'ın kendi çökme ve kullanım istatistikleri | App Store, Ekran Süresi, bildirim | Kendi koşulları ve gizlilik politikasıyla çalışır |
| **Yetkili kamu kurumları ve mahkemeler** | Yalnız hukuken zorunlu olan kadarı | Hukuki yükümlülük | — |

**Üçüncü tarafların kendi koşulları.** Apple, hizmetlerini kendi bağımsız koşulları ve gizlilik politikası altında
sunar ve bu hizmetler kapsamında topladığı verileri kendi sorumluluğunda işler: Apple Gizlilik Politikası
(https://www.apple.com/legal/privacy/). Bu şirketlerle ayrıca imzalanmış bir sözleşmemiz yoktur; hesap açarken herkese
sunulan çevrim içi koşullarını kabul ettik.

## 5. Verilerin yurt dışına aktarılıyor mu?

- **Aile sunucusundaki veriler Türkiye'de kalır.** Sunucumuz Türkiye'dedir. Bu veriler için ayrıca yedek almıyoruz:
  içerik en çok 25 saat yaşayan şifreli zarflardır.
- **Apple, bildirimler (yalnız ebeveyn telefonunda ve yalnız açarsan):** Bildirimleri açarsan telefonun Apple'a kendisi
  kaydolur ve jetonu Apple üretir. Ailenden bir zarf geldiğinde sunucumuz bu jetonu içeriksiz bir bildirimle Türkiye
  dışındaki Apple sunucularına gönderir; bu, bildirimler açık kaldıkça düzenli olur. Bu gönderim için standart sözleşme,
  taahhütname ya da yeterlilik kararı yoktur. Apple kendi koşulları ve gizlilik politikasıyla çalışır
  (https://www.apple.com/legal/privacy/). **Olası riskler:** bu bilgi, Türkiye'dekiyle aynı korumayı sağlamayabilecek
  bir ülkede işlenebilir; oradaki kamu makamlarının erişimi farklı kurallara bağlı olabilir. İstemiyorsan bildirimleri
  açma ya da kapat; Mola çalışmaya devam eder. Kapattıktan sonra uygulamayı bir kez açtığında jeton sunucudan silinir
  ve gönderim durur.
- **E-posta:** Bize yazdığın e-postalar Güzel Hosting'in Türkiye'deki sunucularında saklanır. Sana gönderdiğimiz
  yanıtlar MailChannels Corporation (Kanada; sunucuları Kuzey Amerika'da) üzerinden iletilir; yanıtın içeriği ve e-posta
  adresin iletim sırasında bu şirketin sunucularından geçer, orada saklanmaz. Bu yalnız bize yazdığında ve sana yanıt
  verdiğimizde olur.
- **AEA, Birleşik Krallık ve İsviçre'deki kullanıcılar için:** Verilerini telefonun doğrudan Türkiye'deki sunucumuza
  verir ve veriler orada işlenir; Türkiye için bir AB yeterlilik kararı yoktur. GDPR bize, sana bu hizmeti sunduğumuz
  için uygulanır (m.3/2). Bizim yaptığımız tek aktarım, bildirimleri açan ebeveyn telefonunun jetonunun Apple'a
  gönderilmesidir; bunun için standart sözleşme maddeleri yoktur ve bu gönderimi, senin açtığın özelliği sunmak için
  gerekli görüyoruz (GDPR m.49/1(b)).

## 6. Ne kadar süre saklıyoruz? (Özet)

| Veri | Süre |
| --- | --- |
| Tek cihaza giden şifreli zarf | Alınana kadar; en çok 25 saat |
| Herkese giden şifreli zarf ve alındı kayıtları | En çok 25 saat |
| Cihaz kaydı (rastgele kimlikler; ebeveynde bildirim jetonu) | Aileden ayrılana, çıkarılana ya da 180 gün sessizliğe kadar |
| Aileden çıkarılan cihaza bırakılan şifreli bildirim | 180 gün |
| Aileye katılmamış hesap | 2 gün |
| Aile kaydı | Son cihaz ayrılana kadar |
| E-posta yazışmaları | Kapandıktan sonra en çok 24 ay |

## 7. Aileden ayrılma ve silme

Silme uygulamanın içinden yapılır:

- **Ebeveyn, kendisi için:** Ayarlar → **Aileden ayrıl ve verilerimi sil.** Sunucudaki hesabın, gönderdiğin ve sana
  gelen zarflar, cihaz kaydın ve bildirim jetonun **hemen** silinir. Ailedeki tek ebeveynsen çocuk cihazlarının
  kayıtları da aynı anda silinir. Telefonundaki anahtarlar ve aile bilgileri de silinir.
- **Ebeveyn, çocuğu için:** Aile → çocuğun adı → **Aileden çıkar.** O cihazın sunucudaki hesabı, kaydı ve zarfları
  **hemen** silinir. Çocuğun telefonu bir sonraki bağlanışında bunu öğrenir ve aile bilgilerini ve kuralları kendisi
  siler.
- **Çocuk cihazı:** Çocuk, anlaşmadan tek başına çıkamaz; ama isteyebilir: Ayarlar → **Aileden ayrılmak istiyorum**
  ebeveyne bir istek gönderir, ebeveyn onaylayınca yukarıdaki silme yapılır.
- **Yalnız kendin için kullanıyorsan** sunucumuzda bir kaydın yoktur. Uygulamayı silmen yeterlidir.

Uygulamaya ulaşamıyorsan bize yazabilirsin (Bölüm 9). Ayrıntılı adımlar: https://mola.mm-apps.com/hesap-silme/

## 8. Otomatik kararlar ve profil çıkarma

Hakkında hukuki ya da benzer önemde sonuç doğuran, yalnız otomatik işlemeye dayanan bir karar vermeyiz; profil
çıkarmayız. Sunucudaki tek otomatik kural, kötüye kullanımı sınırlayan sayaçlardır (ör. bir cihaz saatte en çok 60 zarf
gönderebilir); sınır dolduğunda yalnız o gönderim reddedilir.

## 9. Hakların ve nasıl kullanacağın

**KVKK m.11 uyarınca** şu haklara sahipsin: kişisel verilerinin işlenip işlenmediğini öğrenme; işlenmişse bilgi talep
etme; işlenme amacını ve amaca uygun kullanılıp kullanılmadığını öğrenme; yurt içinde veya yurt dışında aktarıldığı
üçüncü kişileri bilme; eksik veya yanlış işlenmişse düzeltilmesini isteme; KVKK m.7 çerçevesinde silinmesini veya yok
edilmesini isteme; bu işlemlerin aktarıldığı üçüncü kişilere bildirilmesini isteme; münhasıran otomatik sistemlerle
analiz sonucu aleyhine çıkan sonuca itiraz etme; kanuna aykırı işleme nedeniyle zarara uğrarsan zararın giderilmesini
talep etme.

**GDPR m.15–22 uyarınca** (AEA'daysan; Birleşik Krallık ya da İsviçre'deysen oradaki eşdeğer kurallar uyarınca):
erişim, düzeltme, silme, işlemenin kısıtlanması, veri taşınabilirliği, meşru menfaate dayanan işlemeye itiraz etme ve
rızaya dayanan işlemede rızanı istediğin zaman geri alma hakların vardır.

**Uygulamanın içinden:** silme için Bölüm 7; bildirimleri kapatmak için iOS Ayarları → Bildirimler → Mola.

**Bize yazarak:** destek@mm-apps.com adresine "Kişisel veri başvurusu" konusuyla yaz ve **Ayarlar → Cihaz numarası**'nı
ekle. Sunucumuz adını bilmediği için hangi kaydın sana ait olduğunu ad ya da kimlik numarasıyla bulamayız; cihaz
numarası kaydı bulmamızı sağlar. Sunucuda senin hakkında okunabilir tek bilgi Bölüm 3.2 ve 3.3'teki rastgele
kimlikler, zamanlar ve bildirim jetonudur; şifreli zarfları biz de açamayız. Kaydı sana bağlayamazsak bunu açıklarız
(GDPR m.11). Kimliğini doğrulamak için gerekenden fazla bilgi istemeyiz. Başvurunu en geç **30 gün** içinde
ücretsiz yanıtlarız.

**Şikâyet hakkı:** Türkiye'de Kişisel Verileri Koruma Kurulu'na (https://www.kvkk.gov.tr), AEA'da bulunduğun ülkenin
veri koruma makamına başvurabilirsin.

## 10. Çocuklar

Mola bir aile uygulamasıdır ve çocukların cihazlarında çalışmak üzere tasarlanmıştır; bu yüzden özellikle az veriyle
çalışır. Kimseye yaşını sormayız.

- **Kurulumu ebeveyn yapar.** Çocuk cihazının aileye, ebeveynin kendi telefonunda gösterdiği QR kodla katılması
  öngörülmüştür; ebeveyn, QR kodu göstermeden önce çocuğun ebeveyni ya da vasisi olduğunu ve çocuğun bundan haberi
  olduğunu kendi telefonunda onaylar. Ekran Süresi izni, Aile Paylaşımı kuruluysa ebeveynin Apple hesabıyla onaylanır;
  kurulu değilse uygulama bunu açıkça gösterir.
- **Çocuk cihazından toplananlar:** yalnız Bölüm 3.2'deki rastgele kimlikler ve, bağlantı anında, IP adresi. Çocuktan
  ad, e-posta, doğum tarihi, konum ya da başka bir iletişim bilgisi istemeyiz; **çocuk cihazından bildirim jetonu
  alınmaz.** Kurulumda yazılan ad yalnız ailenin cihazlarında görünür, sunucumuz onu okuyamaz ve gerçek ad olmak
  zorunda değildir.
- **Bu kimlikler ne için kullanılır?** Yalnız uygulamanın iç işleyişi için: ailenin cihazları arasında zarf iletmek,
  cihazın aileye ait olduğunu doğrulamak ve sunucuyu kötüye kullanıma karşı korumak. Çocukla iletişim kurmak, profil
  çıkarmak, reklam göstermek ya da başka bir veriyle birleştirmek için **kullanılmaz;** sunucu içeriği okuyamadığı ve
  başka hiçbir bilgi tutmadığı için bunu yapacak bir yolu da yoktur.
- Çocuğun kullanım verisi, mesajları ve uygulama listesi cihazından çıkmaz; biz de ebeveyn de göremez. Çocuğun
  telefonunda, telefonun aileyle birlikte Mola ile yönetildiği ve hangi kuralın neden açık olduğu her zaman görünür.
- **Ebeveynlerin hakları:** çocuğunuzun cihaz kaydını uygulamadan hemen silebilir (Bölüm 7), onun hakkında sunucuda
  ne tutulduğunu bizden öğrenebilir ve daha fazla veri toplanmasını, cihazı aileden çıkararak durdurabilirsiniz.
- **ABD'deki ebeveynler için:** bu bölüm, çocukların çevrim içi gizliliğine ilişkin ABD kuralları (COPPA) kapsamındaki
  bildirimimizdir. Operatör: Mehmet Mutlu, Türkiye; e-posta: destek@mm-apps.com. Posta adresimizi ve telefon numaramızı
  bu adrese yazarak isteyebilirsiniz.

## 11. Verilerini nasıl koruyoruz?

- Aile içi iletişim uçtan uca şifrelidir ve her mesaj gönderenin anahtarıyla imzalanır; kilit, kural ve onay gibi
  komutları yalnız ebeveynin imzası geçerli kılar.
- Ailenin şifreleme anahtarı her eşlemeden sonra, bir cihaz aileden çıkarıldığında ve en geç 30 günde bir yenilenir;
  yeni anahtar her cihaza yalnız o cihazın açabileceği biçimde iletilir.
- Sunucuyla bağlantı TLS ile şifrelidir. Sunucudaki tablolara uygulamalar doğrudan erişemez; her işlem sunucudaki
  denetimli işlevlerden geçer.
- Anahtarlar cihazın anahtar zincirinde, yalnız o cihazda durur.
- Hiçbir sistem tam güvenli değildir. Bir veri ihlali olursa yasanın gerektirdiği makamlara ve, gerekiyorsa, sana
  bildiririz. Sunucudaki verinin doğası gereği (rastgele kimlikler ve okunamayan zarflar) bir ihlalde aile içeriğiniz
  açığa çıkmaz.

## 12. Politikadaki değişiklikler

Bu politikayı güncellersek yeni sürümü bu sayfada yayımlar, yürürlük tarihini ve sürüm numarasını değiştiririz. Önemli
bir değişiklikte (yeni bir veri türü, yeni bir alıcı) uygulamada da duyururuz.

## 13. İletişim

**destek@mm-apps.com** · Türkçe ya da İngilizce yazabilirsin. Genellikle birkaç iş günü içinde yanıtlarız.

## 14. Dil

Bu politikanın bağlayıcı metni Türkçedir. Diğer dillerdeki metinler kolaylık sağlamak için sunulan çevirilerdir; bir
çelişki olursa Türkçe metin geçerlidir. Yaşadığın ülkenin tüketici ve veri koruma hukukunun sana tanıdığı, sözleşmeyle
kaldırılamayan haklar saklıdır.
