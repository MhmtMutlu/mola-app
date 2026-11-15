# Mola Privacy Policy

**Effective date:** 15 November 2026 · **Version:** 1.0

This is a translation provided for convenience. The binding text is the Turkish version:
https://mola.mm-apps.com/gizlilik/ (Section 14). It serves as the notice required by Article 10 of the Turkish
Personal Data Protection Law (KVKK, Law No. 6698) and Article 13 of the EU General Data Protection Regulation (GDPR).

---

## In short

- **We do not ask for your name, e-mail, phone number, location or advertising identifier.** There is no account to
  create and no password.
- **Your screen-time data never leaves your phone.** We cannot see which app you used for how long, and neither can a
  parent. Mola uses Apple's Screen Time system, which keeps usage data on the device.
- **We do not read your messages, photos or contacts.** Mola has neither the permission nor any way to do so.
- **Everything between your family's devices is end-to-end encrypted.** Rules, time requests, the short reason you
  write and the name shown inside the family are encrypted so that only your family's devices can open them. Our server
  **cannot read them.**
- If you use Mola only for yourself (focus and the tile wall), **nothing is sent to our server.**
- If you set up a family, our server in Türkiye holds only: randomly generated identifiers, encrypted envelopes that
  live at most 25 hours and, if you allowed notifications, the notification token Apple generated for your device.
- **We do not track you,** we do not **sell** your data and we show no ads. The app contains no analytics or
  crash-reporting tool.
- Questions? Write to us in Turkish or English: **destek@mm-apps.com**

---

## 1. Who we are (data controller)

Data controller: **Mehmet Mutlu** (an individual developer living in Türkiye; "Mola", "we").

- Contact: **destek@mm-apps.com**

We are not required to appoint a data protection officer (DPO). We have no representative in the European Union, the
United Kingdom or Switzerland; everyone, including users and authorities in those countries, reaches us directly.

## 2. What this policy covers

This policy covers the Mola app for iOS, iPadOS and watchOS, the app's family server ("relay") and your correspondence
with us. The App Store itself, Apple's Screen Time and Family Sharing features and Apple's notification service are
subject to Apple's own privacy policy.

## 3. What is kept where

### 3.1 What stays on your device only

These are **never sent** to our server (the part that goes to family devices travels encrypted, as in Section 3.2):

| Information | Explanation |
| --- | --- |
| Screen-time usage | Kept on the device by Apple's Screen Time system. Mola only learns, inside the device, that "this much of the daily limit is used"; even Mola cannot learn how long you spent in which app. |
| App selection | Which apps are limited is chosen in Apple's own picker and stays on the device. The selection consists of Apple-specific tokens that cannot be transferred to another device or to a server. |
| Rules, modes, time requests and their reasons | Stored on the device; sent to family devices end-to-end encrypted only. |
| The name shown in the family | The name you type during setup. It is visible only on your family's devices and does not have to be your real name. |
| Focus sessions and your tile wall | On your device only. |
| Encryption keys | In the device's keychain, on this device only. The family key passes from the parent's screen to the child's camera by QR code and never reaches the server. |

Deleting the app deletes this information from your device. If iCloud Backup is on, app data may be included in your
backup under Apple's backup rules; you manage that in iOS Settings.

### 3.2 What passes through our family server (only if you set up a family)

A parent's and a child's phone are on different Apple accounts, so commands and requests need a meeting point. That
server carries sealed envelopes only.

| | |
| --- | --- |
| **Data** | A randomly generated account number and session keys; when the account was opened and last signed in; a random family identifier and a random member identifier; a hash of the family's access token (not the token itself); when the device last connected; **encrypted envelopes** (sender and recipient member identifiers, an expiry time and encrypted content the server cannot read); a receipt record for envelopes addressed to everyone |
| **Purpose** | Delivering a command, rule, request or answer from one family device to the family's other devices; making sure only devices that know the family key can join |
| **Legal basis** | Entering into and performing a contract: KVKK Art. 5/2(c) · GDPR Art. 6(1)(b). Legitimate interest for the limits that prevent abuse: KVKK Art. 5/2(f) · GDPR Art. 6(1)(f) |
| **Retention** | An envelope for a single device is deleted **immediately** when that device takes it. Other envelopes live at most **25 hours**. The device record stays until you leave the family; it is deleted automatically if the device does not connect for **180 days**. Accounts that never joined a family are deleted after 2 days. |

The server cannot read inside an envelope: the content is encrypted on your device with your family's key
(ChaCha20-Poly1305) and signed with the sending device's key (Ed25519). The server holds **no** name, e-mail, usage
data, app list or rule.

**IP address.** Your device's IP address reaches the server by the nature of the connection. We do not store it with
your account: our web server keeps no access log, and the IP address and device information fields of session records
are left empty. To limit abuse, the address is used only in memory, in per-minute counters.

### 3.3 Notifications (optional)

When you set up a family, Mola asks for permission to send notifications. If you allow it, a break given by a parent
or a child's time request arrives even while the app is closed. If you do not, Mola keeps working; commands and
requests arrive when the app is opened.

| | |
| --- | --- |
| **Data** | The **notification token** Apple generated for this device and app; whether the token is a test or a production one |
| **Purpose** | Waking your device when a new envelope arrives from your family |
| **Legal basis** | Explicit consent: KVKK Art. 5/1 · GDPR Art. 6(1)(a). You can withdraw it at any time in iOS Settings → Notifications → Mola; the app deletes the token from the server the next time it opens |
| **Retention** | Until you turn notifications off, leave the family, or Apple reports the token as invalid |
| **Recipient** | Apple Push Notification service (Sections 4 and 5) |

The notification contains **no** name, family identifier or message content. Because the server cannot read the
content, the notification only says "There's an update from your family"; your device shows the text in its own
language.

### 3.4 If you write to us

| | |
| --- | --- |
| **Data** | Your e-mail address, what you write and our replies |
| **Purpose** | Answering your question, handling your request |
| **Legal basis** | Legitimate interest and, for formal requests, legal obligation: KVKK Art. 5/2(f), 5/2(ç) · GDPR Art. 6(1)(f), 6(1)(c) |
| **Retention** | At most 24 months after the correspondence is closed |

### 3.5 What we never collect

First and last name, e-mail (unless you write to us), phone number, date of birth and age, password, location,
contacts, photos, messages, browsing history, health data, advertising identifier (IDFA). We do not show iOS's tracking
prompt. The app contains no analytics, crash-reporting, advertising or marketing tool.

## 4. Who we share your data with

We do not **sell** your data and do not **share** it for advertising. Only these recipients are involved:

| Recipient | What they receive | Why | Role |
| --- | --- | --- | --- |
| **Your family's other devices** | Rules, commands, requests and the in-family name; end-to-end encrypted | The app's function | — |
| **Güzel Hosting** (GNET İnternet Telekomünikasyon A.Ş., Türkiye) | The server data of Sections 3.2 and 3.3 | The virtual server our server runs on; the database and server software (open-source Supabase) run there, operated by us | Processor |
| **Güzel Hosting**, business e-mail | E-mails you write to us and our replies | Our support address is hosted there | Processor |
| **MailChannels Corporation** (Canada) | The content of our reply and your e-mail address, in transit only | Güzel Hosting's mail relay service | Processor (a sub-service of Güzel Hosting) |
| **Apple** (Apple Distribution International Ltd. and its affiliates) | The download of the app from the App Store; Screen Time and Family Sharing (Apple's own system on your device); if you allowed notifications, your notification token and a fixed notification, from our server; Apple's own crash and usage statistics if you allowed them in iOS Settings | App Store, Screen Time, notifications | Independent controller |
| **Competent public authorities and courts** | Only what the law requires | Legal obligation | — |

**Third parties' own terms.** Apple provides its services under its own independent terms and privacy policy and
processes the data it collects through them under its own responsibility: Apple Privacy Policy
(https://www.apple.com/legal/privacy/). We have no separately signed agreement with these companies; we accepted the
online terms they offer to everyone when opening an account.

## 5. Is your data transferred abroad?

- **Data on the family server stays in Türkiye.** Our server is in Türkiye. We keep no backups of this data: the
  content is encrypted envelopes that live at most 25 hours.
- **Apple, notifications (only if you allow them):** When an envelope arrives from your family, our server sends your
  device's notification token and a fixed notification to Apple's servers outside Türkiye (Apple Push Notification
  service). This happens **regularly** for as long as you keep notifications on. There is no standard contract or
  undertaking notified to the Turkish Personal Data Protection Board for this transfer; to our knowledge the Board has
  issued no adequacy decision for the countries involved either. KVKK Art. 9/6(a) accepts explicit consent as a basis
  only for occasional transfers; because this transfer is regular, it is unclear whether that basis applies and we do
  not claim to rely on it. We reduced the transfer to the minimum: only the token Apple itself generated and a
  notification without content are sent. **Possible risks:** this information may be processed in a country that does
  not offer the same level of protection as Türkiye; access by public authorities there may follow different rules. If
  you do not want this, simply do not allow notifications, or turn them off; Mola keeps working.
- **E-mail:** E-mails you write to us are stored on Güzel Hosting's servers in Türkiye. Our replies are relayed through
  MailChannels Corporation (Canada; servers in North America) and are not stored there. We regard this as an occasional
  transfer necessary for our reply to reach you (KVKK Art. 9/6(b)).
- **Users in the EEA, the United Kingdom and Switzerland:** Data on the family server is processed in Türkiye. There is
  no EU adequacy decision for Türkiye. The transfer is necessary to provide the service you ask for (delivery between
  your family's devices): GDPR Art. 49(1)(b). What is transferred is random identifiers and encrypted envelopes the
  server cannot read.

## 6. How long we keep it (summary)

| Data | Period |
| --- | --- |
| Encrypted envelope for a single device | Until taken; at most 25 hours |
| Encrypted envelope for everyone, and receipts | At most 25 hours |
| Device record (random identifiers, notification token) | Until you leave the family or 180 days of silence |
| Account that never joined a family | 2 days |
| Family record | Until the last device leaves |
| E-mail correspondence | At most 24 months after it is closed |

## 7. Leaving the family and deletion

- **Parent:** Settings → **Leave the family and delete my data.** Your account on the server, the envelopes you sent
  and those addressed to you, your device record and your notification token are deleted **immediately**; if yours is
  the last device to leave, the family record is deleted too. The keys and family information on your device are
  deleted as well.
- **Child's device:** So that a child cannot step out of the agreement alone, this option is not offered on a child's
  device. To delete a child device's record on the server, write to us with its **Settings → Device number**
  (Section 9); the record of a device that does not connect for 180 days is deleted automatically anyway.
- **If you use Mola only for yourself,** there is no record of you on our server. Deleting the app is enough.

Step by step: https://mola.mm-apps.com/en/delete-account/

## 8. Automated decisions and profiling

We make no decision about you that is based solely on automated processing and has legal or similarly significant
effects, and we do no profiling. The only automated rules on the server are counters that limit abuse (for example, a
device can send at most 60 envelopes an hour); when a limit is reached, only that request is refused.

## 9. Your rights and how to use them

**Under KVKK Art. 11** you have the right to: learn whether your personal data is processed; request information if
it is; learn the purpose of processing and whether it is used accordingly; know the third parties to whom it is
transferred at home or abroad; request correction if it is incomplete or wrong; request deletion or destruction under
KVKK Art. 7; request that these operations be notified to third parties to whom the data was transferred; object to a
result against you arising from analysis solely by automated systems; and claim compensation if you suffer damage
from unlawful processing.

**Under GDPR Art. 15–22** (if you are in the EEA; under the equivalent rules if you are in the United Kingdom or
Switzerland) you have the rights of access, rectification, erasure, restriction of processing, data portability,
objection to processing based on legitimate interest, and withdrawal of consent at any time where processing is based
on consent.

**Inside the app:** for deletion see Section 7; to withdraw notification consent use iOS Settings → Notifications →
Mola.

**By writing to us:** write to destek@mm-apps.com with the subject "Personal data request" and include your
**Settings → Device number**. Our server does not know your name, so we cannot find your record by name or identity
number; the device number lets us find it. The only readable information about you on the server is the random
identifiers, times and notification token of Sections 3.2 and 3.3; we cannot open the encrypted envelopes either. If
we cannot link a record to you, we will explain that (GDPR Art. 11). We do not ask for more information than needed
to verify your identity. We answer free of charge within **30 days** at the latest.

**Right to complain:** In Türkiye you may apply to the Personal Data Protection Board (https://www.kvkk.gov.tr); in
the EEA, to the data protection authority of your country.

## 10. Children

Mola is a family app designed to run on children's devices; for that reason it works with especially little data.

- **A child's device joins the family only through a parent:** the parent shows a QR code on their own phone and the
  child's phone scans it. On the child's device, Screen Time access is approved with the Apple account of the parent
  in Family Sharing.
- We do not ask a child for a name, e-mail, date of birth or any other contact information. The name typed during
  setup is visible only on the family's devices and does not have to be a real name.
- A child's usage data, messages and app list never leave the device; neither we nor the parent can see them.
- The only things held on the server for a child's device are the random identifiers of Sections 3.2 and 3.3 and, if
  notifications were allowed, the notification token. Children are shown no ads, are not tracked and are not profiled.
- **For parents:** you can ask us to delete your child's device record or for any information concerning it
  (Section 9).

## 11. How we protect your data

- Communication inside the family is end-to-end encrypted and every message is signed with the sender's key; commands
  such as a lock, a rule or an approval are valid only with a parent's signature.
- The connection to the server is encrypted with TLS. Apps cannot access the server's tables directly; every operation
  goes through controlled functions on the server.
- Keys stay in the device's keychain, on that device only.
- No system is perfectly secure. If a data breach occurs, we will notify the authorities the law requires and, where
  necessary, you. By the nature of the data on the server (random identifiers and unreadable envelopes), a breach would
  not expose your family's content.

## 12. Changes to this policy

If we update this policy, we publish the new version on this page and change the effective date and version number.
For an important change (a new type of data, a new recipient) we also announce it in the app.

## 13. Contact

**destek@mm-apps.com** · You can write in Turkish or English. We usually answer within a few working days.

## 14. Language

The binding text of this policy is the Turkish one. Texts in other languages are translations provided for
convenience; in case of a conflict the Turkish text prevails. Rights that the consumer and data protection law of your
country gives you and that cannot be removed by contract are reserved.
