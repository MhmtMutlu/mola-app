# Mola Privacy Policy

**Effective date:** 15 November 2026 · **Version:** 1.0

This is a translation provided for convenience. The binding text is the Turkish version:
https://mola.mm-apps.com/gizlilik/ (Section 14). It has been prepared as the notice required by Article 10 of the
Turkish Personal Data Protection Law (KVKK, Law No. 6698) and as the information required by Article 13 of the EU
General Data Protection Regulation (GDPR). The short KVKK notice: https://mola.mm-apps.com/kvkk/.

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
- If you use Mola only for yourself (blocking plans, focus and the tile wall), **nothing is sent to our server.**
- If you set up a family, our server in Türkiye holds only: randomly generated identifiers, encrypted envelopes that
  live at most 25 hours and, if you turned on notifications on the parent's phone, the notification token Apple
  generated for that phone. **No notification token is taken from children's phones.**
- **We do not track you,** we do not **sell** your data and we show no ads. The app contains no analytics or
  crash-reporting tool.
- If there is a problem, write to us in Turkish or English: **destek@mm-apps.com**

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

The site on which this page is published uses no cookies and no analytics tool. The site is hosted on GitHub Pages;
when you open the page, your IP address reaches the host (GitHub, USA), as on every website, and GitHub processes it
under its own privacy policy.

## 3. What is kept where

### 3.1 What stays on your device only

These are **never sent** to our server (the part that goes to family devices travels encrypted, as in Section 3.2):

| Information | Explanation |
| --- | --- |
| Screen-time usage | Kept on the device by Apple's Screen Time system. Mola only learns, inside the device, that "this much of the daily limit is used"; even Mola cannot learn how long you spent in which app. |
| App selection | Which apps are limited is chosen in Apple's own picker and stays on the device. The selection consists of Apple-specific tokens that cannot be transferred to another device or to a server. |
| Rules, modes, time requests and their reasons | Stored on the device; sent to family devices end-to-end encrypted only. |
| The name shown in the family | The name you type during setup. It is visible only on your family's devices and does not have to be your real name. |
| Your blocking plans, your daily limits, your own focus programs, your focus sessions, your daily focus times and your tile wall | On your device only. |
| Encryption keys | In the device's keychain, on this device only. The family key passes from the parent's screen to the child's camera by QR code and never reaches the server. |

Deleting the app deletes this information from your device. If iCloud Backup is on, app data may be included in your
backup under Apple's backup rules; you manage that in iOS Settings.

### 3.2 What passes through our family server (only if you set up a family)

A parent's and a child's phone are on different Apple accounts, so commands and requests need a server where they can
meet. That server carries sealed envelopes only.

| | |
| --- | --- |
| **Data** | A randomly generated account number and session keys; when the account was opened and last signed in; a random family identifier and a random member identifier; a hash of the family's access token (not the token itself); when the records were created and when the device last connected to the server; **encrypted envelopes** (the envelope identifier, sender and recipient member identifiers, creation and expiry times and encrypted content the server cannot read); a receipt record for envelopes addressed to everyone; for a device removed from the family, that device's random member identifier and a short notice, signed by the parent, that the server cannot read |
| **Purpose** | Delivering a command, rule, request or answer sent by one family device to the family's other devices; making sure only devices that know the family key can join the family |
| **Legal basis** | Entering into and performing a contract: KVKK Art. 5/2(c) · GDPR Art. 6(1)(b). Legitimate interest for the limits that prevent abuse: KVKK Art. 5/2(f) · GDPR Art. 6(1)(f) |
| **Retention** | An envelope for a single device is deleted **immediately** when that device takes it. Other envelopes live at most **25 hours**. The device record stays until you leave the family; it is deleted automatically if the device does not connect to the server at all for **180 days**. Accounts that never joined a family are deleted after 2 days. The account, record and envelopes of a device removed from the family are deleted **immediately**; the encrypted notice left for that device is deleted after 180 days. |

The server cannot read inside an envelope: the content is encrypted on your device with your family's key
(ChaCha20-Poly1305) and signed with the sending device's key (Ed25519). The server holds **no** name, e-mail, usage
data, app list or rule.

**IP address.** When your device connects to the server, its IP address reaches the server by the nature of the
connection. We do not store it together with your account: we configured our server software so that it keeps no
access log; the IP address and device information in session records are written, but deleted within one
hour at the latest. The address is used in memory, in short-lived counters that limit abuse. Our hosting provider may
keep network traffic records under its own responsibility, as required by its own legal obligations.

### 3.3 Notifications (optional, on the parent's phone only)

Notifications are used only on the **parent's phone** and only if you turn them on. Mola first explains on its own
screen what will happen; if you tap "Turn on notifications", iOS's prompt appears. If you turn them on, your child's
time request reaches you even while the app is closed. If you do not, Mola keeps working; requests arrive when you
open the app.

**Notifications are not used on children's phones and no notification token is taken from a child's phone.** A break
given by the parent or a new rule is applied when Mola is opened on the child's phone or when iOS gives the app a turn
in the background. Scheduled rules such as school, sleep and the daily limit are stored on the phone and work without
internet too.

| | |
| --- | --- |
| **Data** | The **notification token** Apple generated for this phone and app; whether the token is a test or a production one |
| **Purpose** | Waking the parent's phone when a new envelope arrives from your family |
| **Legal basis** | Performing the notification feature you turned on: KVKK Art. 5/2(c) · GDPR Art. 6(1)(b). You can turn notifications off at any moment in iOS Settings → Notifications → Mola |
| **Retention** | Until you turn notifications off (the token is deleted from the server when you open the app once after turning them off), leave the family, or Apple reports the token as invalid |
| **Recipient** | Apple's notification service (Sections 4 and 5) |

The notification contains **no** name, family identifier or message content. Because the server cannot read the
content, the notification only says "There's an update from your family"; your phone shows the text in its own
language.

### 3.4 If you write to us

| | |
| --- | --- |
| **Data** | Your e-mail address, what you write and our replies |
| **Purpose** | Answering your question, handling your request |
| **Legal basis** | Legitimate interest and, for formal requests, legal obligation: KVKK Art. 5/2(f), Art. 5/2(ç) · GDPR Art. 6(1)(f), Art. 6(1)(c) |
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
| **Güzel Hosting** (GNET İnternet Telekomünikasyon A.Ş., Türkiye) | The server data of Sections 3.2 and 3.3 | The virtual server service our server is located on; the database and server software (open-source Supabase) run on this server, operated by us | Hosting service provider; it operates under its publicly available terms of service, and there is no separate data processing agreement between us |
| **Güzel Hosting**, business e-mail | E-mails you write to us and our replies | Our support address is hosted on this service | Same |
| **MailChannels Corporation** (Canada) | The content of the reply we send you and your e-mail address, in transit only | Güzel Hosting's mail relay service | A sub-service of Güzel Hosting; it operates under its own terms |
| **Apple** (Apple Distribution International Ltd. and its affiliates) | The download of the app from the App Store; Screen Time and Family Sharing (these are Apple's system on your device); if you turned on notifications on the parent's phone, that phone's notification token, the app's identifier and a notification without content, from our server; Apple's own crash and usage statistics if you allowed them in iOS settings | App Store, Screen Time, notifications | It operates under its own terms and privacy policy |
| **Competent public authorities and courts** | Only as much as the law requires | Legal obligation | — |

**Third parties' own terms.** Apple provides its services under its own independent terms and privacy policy and
processes the data it collects through them under its own responsibility: Apple Privacy Policy
(https://www.apple.com/legal/privacy/). We have no separately signed agreement with these companies; we accepted the
online terms they offer to everyone when opening an account.

## 5. Is your data transferred abroad?

- **Data on the family server stays in Türkiye.** Our server is in Türkiye. We take no separate backups of this data:
  the content is encrypted envelopes that live at most 25 hours.
- **Apple, notifications (on the parent's phone only and only if you turn them on):** If you turn on notifications,
  your phone registers itself with Apple and Apple generates the token. When an envelope arrives from your family, our
  server sends this token, with a notification without content, to Apple's servers outside Türkiye; this happens
  regularly for as long as notifications stay on. There is no standard contract, undertaking or adequacy decision for
  this sending. Apple operates under its own terms and privacy policy (https://www.apple.com/legal/privacy/).
  **Possible risks:** this information may be processed in a country that may not provide the same protection as in
  Türkiye; access by public authorities there may be subject to different rules. If you do not want this, do not turn
  notifications on, or turn them off; Mola keeps working. When you open the app once after turning them off, the token
  is deleted from the server and the sending stops.
- **E-mail:** E-mails you write to us are stored on Güzel Hosting's servers in Türkiye. The replies we send you are
  relayed through MailChannels Corporation (Canada; its servers are in North America); the content of the reply and
  your e-mail address pass through this company's servers in transit and are not stored there. This happens only when
  you write to us and we reply to you.
- **For users in the EEA, the United Kingdom and Switzerland:** Your phone gives your data directly to our server in
  Türkiye and the data is processed there; there is no EU adequacy decision for Türkiye. The GDPR applies to us because
  we offer this service to you (Art. 3(2)). The only transfer we make is the sending to Apple of the token of a parent's
  phone that turned on notifications; there are no standard contractual clauses for it, and we regard this sending as
  necessary to provide the feature you turned on (GDPR Art. 49(1)(b)).

## 6. How long we keep it (summary)

| Data | Period |
| --- | --- |
| Encrypted envelope for a single device | Until taken; at most 25 hours |
| Encrypted envelope for everyone, and receipt records | At most 25 hours |
| Device record (random identifiers; on a parent's device, the notification token) | Until you leave the family, are removed from it, or 180 days of silence |
| Encrypted notice left for a device removed from the family | 180 days |
| Account that has not joined a family | 2 days |
| Family record | Until the last device leaves |
| E-mail correspondence | At most 24 months after it is closed |

## 7. Leaving the family and deletion

Deletion is done inside the app:

- **Parent, for themselves:** Settings → **Leave the family and delete my data.** Your account on the server, the
  envelopes you sent and those addressed to you, your device record and your notification token are deleted
  **immediately**. If you are the only parent in the family, the records of the children's devices are deleted at the
  same moment. The keys and family information on your phone are deleted as well.
- **Parent, for their child:** Family → the child's name → **Remove from family.** That device's account, record and
  envelopes on the server are deleted **immediately**. The child's phone learns this the next time it connects and
  deletes the family information and the rules itself.
- **Child's device:** A child cannot step out of the agreement alone, but can ask to: Settings → **I want to leave the
  family** sends a request to the parent, and when the parent approves, the deletion above is carried out.
- **If you use Mola only for yourself,** there is no record of you on our server. Deleting the app is enough.

If you cannot reach the app, you can write to us (Section 9). Detailed steps:
https://mola.mm-apps.com/en/delete-account/

## 8. Automated decisions and profiling

We make no decision about you that is based solely on automated processing and has legal or similarly significant
effects; we do no profiling. The only automated rule on the server is the counters that limit abuse (for example, a
device can send at most 60 envelopes an hour); when the limit is reached, only that sending is refused.

## 9. Your rights and how to use them

**Under KVKK Art. 11** you have the right to: learn whether your personal data is processed; request information if
it is; learn the purpose of processing and whether it is used accordingly; know the third parties to whom it is
transferred at home or abroad; request correction if it is incomplete or wrong; request deletion or destruction under
KVKK Art. 7; request that these operations be notified to third parties to whom the data was transferred; object to a
result against you arising from analysis solely by automated systems; and claim compensation if you suffer damage
from unlawful processing.

**Under GDPR Art. 15–22** (if you are in the EEA; under the equivalent rules there if you are in the United Kingdom or
Switzerland) you have the rights of access, rectification, erasure, restriction of processing, data portability,
objection to processing based on legitimate interest, and withdrawal of your consent at any time where processing is
based on consent.

**Inside the app:** for deletion see Section 7; to turn notifications off use iOS Settings → Notifications → Mola.

**By writing to us:** write to destek@mm-apps.com with the subject "Personal data request" and include your
**Settings → Device number**. Our server does not know your name, so we cannot find which record is yours by name or
identity number; the device number lets us find the record. The only readable information about you on the server is
the random identifiers, times and notification token of Sections 3.2 and 3.3; we cannot open the encrypted envelopes
either. If we cannot link the record to you, we will explain that (GDPR Art. 11). We do not ask for more information
than needed to verify your identity. We answer your request free of charge within **30 days** at the latest.

**Right to complain:** In Türkiye you may apply to the Personal Data Protection Board (https://www.kvkk.gov.tr); in
the EEA, to the data protection authority of the country you are in.

## 10. Children

Mola is a family app and is designed to run on children's devices; for that reason it works with especially little
data. We do not ask anyone their age.

- **The parent does the setup.** A child's device is intended to join the family with the QR code the parent shows on
  their own phone; before showing the QR code, the parent confirms on their own phone that they are the child's parent
  or guardian and that the child knows about this. Screen Time access is approved with the parent's Apple account if
  Family Sharing is set up; if it is not, the app shows this plainly.
- **What is collected from a child's device:** only the random identifiers of Section 3.2 and, at the moment of
  connection, the IP address. We do not ask a child for a name, e-mail, date of birth, location or any other contact
  information; **no notification token is taken from a child's device.** The name typed during setup is visible only on
  the family's devices, our server cannot read it and it does not have to be a real name.
- **What are these identifiers used for?** Only for the app's internal operation: delivering envelopes between the
  family's devices, verifying that the device belongs to the family and protecting the server against abuse. They are
  **not used** to contact the child, to profile, to show ads or to combine with any other data; because the server
  cannot read the content and holds no other information, it has no way of doing so either.
- A child's usage data, messages and app list never leave the device; neither we nor the parent can see them. On the
  child's phone it is always visible that the phone is managed with Mola together with the family, and which rule is
  on and why.
- **Parents' rights:** you can delete your child's device record from the app immediately (Section 7), learn from us
  what is held about them on the server, and stop any further collection of data by removing the device from the
  family.
- **For parents in the USA:** this section is our notice under the US rules on children's online privacy (COPPA).
  Operator: Mehmet Mutlu, Türkiye; e-mail: destek@mm-apps.com. You can ask for our postal address and telephone number
  by writing to this address.

## 11. How we protect your data

- Communication inside the family is end-to-end encrypted and every message is signed with the sender's key; commands
  such as a lock, a rule or an approval are made valid only by the parent's signature.
- The family's encryption key is renewed after every pairing, when a device is removed from the family, and every
  30 days at the latest; the new key is delivered to each device in a form only that device can open.
- The connection to the server is encrypted with TLS. Apps cannot access the server's tables directly; every operation
  goes through controlled functions on the server.
- Keys stay in the device's keychain, on that device only.
- No system is fully secure. If a data breach occurs, we will notify the authorities the law requires and, where
  necessary, you. By the nature of the data on the server (random identifiers and unreadable envelopes), a breach does
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
