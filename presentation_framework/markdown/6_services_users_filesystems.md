{{slide extra_class=first_slide}}

# Wnętrzności Linuxa
<br>
## Usługi
## Użytkownicy
## System plików


{{slide_end}}
{{slide extra_class=first_slide}}
## Plan wykładu

{{slide_end}}
{{slide}}
### #C3E88D Usługi
* Trochę teorii o procesach w systemie

* `systemd` - program, który zarządza usługami

* Uruchamianie i zatrzymywanie usług

* Prosta własna usługa

{{slide_end}}
{{slide}}
### #FFCB6B Użytkownicy ( i grupy)
* Po co nam są

* Uprawnienia

* `sudo`
{{slide_end}}
{{slide}}

### #82AAFF System plików

* Filozofia systemu plików na Linuxie

* Opis struktury systemu plików - co i gdzie jest

* Montowanie dysków, VFS


{{slide_end}}
{{slide}}
## Po co Wam to - cel wykładu

<br>

* Korzystanie z usług jest konieczne przy

    większości zadań administratorskich,
    
    więc #FF5370 warto to umieć

* Tak samo jest z uprawnieniami użytkowników

* #BB80B3 Wprowadzenie do Dockera - który będzie za tydzień

{{slide_end}}
{{slide extra_class=first_slide}}

# #C3E88D Usługi


{{slide_end}}
{{slide}}

### #C3E88D Teoria

* Usługa a proces

* Jakie programy działają jako zwykłe procesy?

* #BB80B3 Jakie powinny być usługami?


{{slide_end}}
{{slide extra_class=long}}



## Usługi, z których (nieświadomie) korzystacie

<br>

* #C3E88D SDDM/GDM - Uruchamia interfejs logowania i GUI

* #FFCB6B NetworkManager - Zarządza interfejsami sieciowymi

* #F78C6C SSHD - Pozwala połączyć się z serwerem przez SSH


{{slide_end}}
{{slide extra_class=long}}


### `systemd` - obecnie najpopularniejszy menedżer usług

<br>
`systemd, init - systemd  system and service manager`
<br>
<br>

* #FF5370   Wykorzystywany we wszystkich nowych dystrybucjach </span>

* #F78C6C   Kontrolowany za pomocą polecenia `systemctl` </span>

{{slide_end}}
{{slide extra_class=long}}




## Systemctl status

`systemctl status <service name>`


<code style="white-space: pre">
#C3E88D$#fff systemctl status sshd
* sshd.service - OpenSSH Daemon
  Loaded: loaded (/usr/lib/systemd/system/sshd.service;
  Active: #C3E88D active (running)#fff since Mon 2019-12-02 23:24:53
 Main PID: 14903 (sshd)
   Tasks: 1 (limit: 4915)
(...)
</code>

{{slide_end}}
{{slide}}

## Systemctl start/stop

`systemctl start/stop <service name>`

{{asciinema src=systemctl_start_stop}}


{{slide_end}}
{{slide}}


## Systemctl enable/disable

`systemctl enable/disable <service name>`

<br>

#C3E88D Uruchamianie usługi przy starcie systemu.


{{slide_end}}
{{slide}}

## #BB80B3 Przykład własnej usługi

<!-- warning: c u r s e d    m a r k d o w n   a h e a d -->
 
<code>
[Unit] <br>
#C3E88D Description#fff=#BB80B3Moja usługa uwu <br>
 <br> #fff
[Service] <br>
#C3E88D Type#fff=#BB80B3exec <br>
#C3E88D ExecStart#fff=#BB80B3/home/wint3rmute/moj_program <br>
#C3E88D RemainAfterExit#fff=#BB80B3true <br>
 <br>#fff
[Install] <br>
#C3E88D WantedBy#fff=#BB80B3multi-user.target <br>
</code>

{{slide_end}}
{{slide extra_class=long}}

{{asciinema src=custom_systemd_service}}


{{slide_end}}
{{slide}}

## #C3E88D Podsumowanie

<br>

* #FF5370 Usługi działają niezależnie od użytkowników

* #FFCB6B `systemctl` pozwala kontrolować usługi

* #F78C6C Usługi mogą startować razem z systemem

    * #F07178 I są wznawiane po restarcie

* #82AAFF Usługa = zwykły program + plik konfiguracyjny

{{slide_end}}
{{slide extra_class=first_slide}}

# #FFCB6B Użytkownicy (i grupy)

{{slide_end}}
{{slide}}

## Co może użytkownik?

<br>

* Posiadać pliki

* Uruchamiać programy

* Zmieniać uprawnienia *własnych* plików

* Należeć do grupy


{{slide_end}}
{{slide extra_class=long}}

{{asciinema src=ls_l}}

{{slide_end}}
{{slide extra_class=long}}
<code >
#82AAFFd#C3E88Drwx#FFCB6Br-x#FF5370r-x #fff 2 #F78C6C wint3rmute#BB80B3 wint3rmute #fff 4096 Nov  7 09:28 #82AAFF Music </code>
<code style="white-space:pre">
#C3E88DUpra#FFCB6Bwni#FF5370enia #F78C6C Użytkownik #BB80B3Grupa                      #82AAFF Nazwa
</code>

<br>


#82AAFF `d` - Directory - folder


`rwx - Read, Write, eXecute`

<br>

Ale po co nam aż trzy?

<code>
#C3E88Drwx#FFCB6Brwx#F78C6Crwx #fff - Dla #C3E88D właściciela#fff, dla #FFCB6B grupy#fff, dla #F78C6C pozostałych.
</code>

{{slide_end}}
{{slide extra_class=long}}

## Przykłady
<code>
#C3E88Drwx#FFCB6Brwx#F78C6Crwx #fff - Każdy może robić wszystko z tym plikiem.
</code>

<br>

<code>
#C3E88Drwx#FFCB6B---#F78C6C--- #fff - Tylko #C3E88D właściciel #fff ma dostęp do pliku.<br>
<br>
#FF5370 Inni użytkownicy nie mogą go nawet odczytać!
</code>

<br>

<code>
#C3E88Drwx#FFCB6Br-x#F78C6Cr-- #fff - #C3E88D właściciel#fff może wszystko#fff, #FFCB6B grupa <br>
<br>
#fff może odczytywać i wykonywać, #F78C6C reszta#fff może tylko czytać.
</code>

{{slide_end}}
{{slide extra_class=long}}

## Po co nam #FFCB6B grupy #fff ?

<br>
Grupy pozwalają nadać użytkownikom dostęp do części systemu:


* Grupa może posiadać folder, dostępny tylko dla członków grupy

* Grupa może mieć dostęp do wybranych poleceń/funkcji
    * `adm` - odczytywanie logów
    * `wireshark` - monitorowanie interfejsów sieciowych
    * `input` - monitorowanie urządzeń wejścia/wyjścia
{{slide_end}}
{{slide}}

{{asciinema src=file_permissions_and_ownership}}


{{slide_end}}
{{slide}}

## #FFCB6B Sudo
<br>
Plik `/etc/sudoers`:

<br>

Konfiguracja #FFCB6B `sudo` #fff - użytkownicy i grupy,

które mogą używać komendy #FFCB6B `sudo`#fff.



{{slide_end}}
{{slide}}



## #FFCB6B Podsumowanie

<br>

* #C3E88D Użytkownicy mogą posiadać pliki i uruchamiać procesy

* #FF5370 Każdy plik posiada prawa dostępu, określające:

    * #F78C6C Co może robić z nim właściciel

    * #F78C6C Co może robić z nim grupa

    * #F78C6C Co mogą robić z nim pozostali



{{slide_end}}
{{slide extra_class=first_slide}}

# #82AAFF System plików

{{slide_end}}
{{slide}}

## Filozofia 
<br>
#82AAFF *Everything is a file* #fff - wszystko jest plikiem

* Urządzenia peryferyjne

    * Klawiatury

    * Karty sieciowe

    * Karty dźwiękowe

* Dyski i pendrive'y

* #BB80B3 Strumienie do komunikacji międzyprocesowej

{{slide_end}}
{{slide extra_class=long}}

## Struktura systemu plików

`$ ls /`

* #C3E88D `bin` - Podstawowe programy wiersza poleceń (bash, ls, cat)

* #FFCB6B `etc` - Systemowe pliki konfiguracyjne

* #F78C6C `usr` - Aplikacje użytkownika (pliki wykonywalne programów)

* #F07178 `var` - Zmienne dane aplikacji (tabele baz danych)

* #FF5370 `dev` - Urządzenia (dyski, pendrive'y, karty SD, kamery)

* #82AAFF `home` - Katalogi użytkowników (tu zazwyczaj siedzisz)


{{slide_end}}
{{slide extra_class=long}}

## VFS
<br>

Wszystkie zamontowane urządzenia dyskowe połączone są w <br>
<br>
strukturę drzewiastą, którą nazywamy "pliki na komputerze".

#FFCB6B
<br>
Dane moga znajdować się na różnych dyskach (lub nawet <br><br>
gdzieś w internecie), i dalej być widoczne jak normalne pliki.

{{slide_end}}
{{slide}}

{{asciinema src=lsblk_example}}

{{slide_end}}
{{slide extra_class=long}}


{{asciinema src=usb_mount}}

{{slide_end}}
{{slide}}

## Ręczne montowanie
<br>

#FF5370 `mount`

*Zamontuj* urządzenie w wybranym miejscu systemu plików

<br>

#C3E88D `umount`

*Odmontuj* urządzenie z systemu plików
{{slide_end}}
{{slide}}

{{asciinema src=mount_umount}}


{{slide_end}}
{{slide}}


## #82AAFF Podsumowanie

<br>

* #C3E88D *Wszystko jest plikiem*

* #FFCB6B Wszystkie zamontowane urządzenia z danymi:

    * znajdują się na *drzewie plików*

    * mogą być *montowane* w różnych miejscach

* #BB80B3 Jako system plików można zamontować też:

    * Dysk sieciowy

    * Katalog na stronie internetowej


{{slide_end}}
{{slide extra_class=long}}

{{asciinema src=http_mount}}

{{slide_end}}
{{slide extra_class=first_slide}}

# #FF5370 Podsumowanie

{{slide_end}}
{{slide}}


<!-- P O D S U M O W A N I E  -->

## #C3E88D Usługi

<br>

* #FF5370 Usługi działają niezależnie od użytkowników

* #FFCB6B `systemctl` pozwala kontrolować usługi

* #F78C6C Usługi mogą startować razem z systemem

    * #F07178 I są wznawiane po restarcie

* #82AAFF Usługa = zwykły program + plik konfiguracyjny



{{slide_end}}
{{slide}}



## #FFCB6B Użytkownicy i grupy

<br>

* #C3E88D Użytkownicy mogą posiadać pliki i uruchamiać procesy

* #FF5370 Każdy plik posiada prawa dostępu, określające:

    * #F78C6C Co może robić z nim właściciel

    * #F78C6C Co może robić z nim grupa

    * #F78C6C Co mogą robić z nim pozostali




{{slide_end}}
{{slide}}


## #82AAFF System plików

<br>

* #C3E88D *Wszystko jest plikiem*

* #FFCB6B Wszystkie zamontowane urządzenia z danymi:

    * znajdują się na *drzewie plików*

    * mogą być *montowane* w różnych miejscach

* #BB80B3 Jako system plików można zamontować też:

    * Dysk sieciowy

    * Katalog na stronie internetowej


{{slide_end}}


