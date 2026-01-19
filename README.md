# TLE Checksum Validator

This repository provides a minimal Python module for validating the checksum
mechanism used in the NORAD Two-Line Element (TLE) format. The implementation
strictly follows the official TLE specification and does not rely on any
external libraries. The purpose of this project is to understand the internal
logic of the TLE format itself and to perform line-level data integrity
verification.

### Usage

You can run the script directly to see the test cases:

~~~bash
python tle_checksum.py
~~~

Or import the validation function into your own project:

~~~python
from tle_checksum import verify_checksum

# Example TLE Line 1
line = "1 25544U 98067A   23018.58912361  .00000576  00000+0  57894-3 0  9993"
is_valid = verify_checksum(line)

print(f"Checksum Valid: {is_valid}")
~~~

---

# TLE Checksum Doğrulayıcı (Türkçe)

Bu repository, NORAD Two-Line Element (TLE) formatında kullanılan checksum
mekanizmasının doğrulanmasını amaçlayan minimal bir Python modülüdür. Kod,
TLE standardına birebir uyumlu olup herhangi bir harici kütüphaneye bağımlı
değildir. Amaç, TLE formatının iç mantığını anlamak ve satır seviyesinde veri
bütünlüğü kontrolü sağlamaktır.

### Kullanım

Test durumlarını görmek için betiği doğrudan çalıştırabilirsiniz:

~~~bash
python tle_checksum.py
~~~

Veya doğrulama fonksiyonunu kendi projenize dahil edebilirsiniz:

~~~python
from tle_checksum import verify_checksum

# Örnek TLE 1. Satır 
line = "1 25544U 98067A   23018.58912361  .00000576  00000+0  57894-3 0  9993"
gecerli_mi = verify_checksum(line)

print(f"Checksum Geçerli mi: {gecerli_mi}")

~~~
