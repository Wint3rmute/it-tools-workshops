{{slide extra_class=first_slide}}

# #82AAFF Docker

## Podstawy kontenerów



{{slide_end}}
{{slide}}
## Plan wykładu

<br>

* #C3E88D Deployment - wdrażanie oprogramowania

* #FFCB6B Najczęstsze problemy w trakcie wdrożeń

* #F78C6C Idea kontenerów

* #BB80B3 Uruchamianie gotowych kontenerów Dockerowych

* #82AAFF Budowanie własnego kontenera


{{slide_end}}
{{slide}}
### #C3E88D Deployment - czyli "*works on my machine*"

<br>

* Co jest potrzebne, żeby uruchomić dany program?
 
* Jaki zestaw programów składa się na projekt?

* Jakie są zależności pomiędzy programami?

{{slide_end}}
{{slide}}

# #FF5370 Dependency hell

<br>

*Program A wymaga biblioteki B, która do kompilacji*

*wymaga programu C, który zależy na bibliotece D,*

*której wersja 2.137A nie jest kompatynilna z...*

{{slide_end}}
{{slide extra_class=long}}


### #C3E88D Projekt końcowy = program (kod/binarka) + *runtime*
<br>

#C3E88D *Runtime* #fff - wszystkie programy/biblioteki/ustawienia,

których program potrzebuje, żeby działać

{{slide_end}}
{{slide}}

Wraz z instalowaniem kolejnych bibliotek, rośnie ryzyko:

<br>

* Błędu w konfiguracji

* Problemów z wersjami pakietów/bibliotek

* Konfliktu między paczkami

{{slide_end}}
{{slide}}

A gdyby dało się zapakować #F78C6C aplikację #fff i #C3E88D runtime #fff

w #FF5370 jeden kontener#fff, który następnie pójdzie na produkcję?


<br>

Gratulacje, taka jest idea #82AAFF konteneryzacji#fff.
 

{{slide_end}}
{{slide}}

### #FFCB6B To nic nowego - trochę historii
<br>

FreeBSD - 1999: mechanizm #FFCB6B `jail`


*several independent mini-systems called #FFCB6B jails#fff,* 

*all sharing the same kernel, with #C3E88D very little overhead#fff.*

{{slide_end}}
{{slide}}

### #82AAFF Kontener &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #fff vs &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #C3E88D Maszyna wirtualna

![docker_vs_vm.png](images/docker_vs_vm.png)



{{slide_end}}
{{slide extra_class=long}}


## #82AAFF Podsumowanie

<br>

* #FF5370 Deployment nie jest łatwy

* #FFCB6B Skomplikowany program = skomplikowany setup

* #C3E88D Konteneryzacja - spakowanie razem aplikacji i runtime'u

* #BB80B3 Kontener `!=` Maszyna wirtualna


{{slide_end}}
{{slide extra_class=long}}

## Docker installation in 20 seconds

{{asciinema src=20_secs_to_docker}}

{{slide_end}}
{{slide}}

## #FF5370 Jak zrobić kontener 
<br>

* Plik #82AAFF `Dockerfile`

* Wybór *'podstawki'* - systemu bazowego

* Skrypty instalujące co trzeba

#C3E88D Done !

{{slide_end}}
{{slide}}

## #C3E88D Prosty `Dockerfile` - skrypt w Pythonie

{{asciinema src=simplest_docker}}

{{slide_end}}
{{slide}}

## #C3E88D Prosty przykład - aplikacja webowa
<br>

* Python - trochę kodu

* Framework Flask - biblioteki


{{slide_end}}
{{slide}}

{{asciinema src=flask}}

{{slide_end}}
{{slide}}

### #FF5370 Bezstanowość kontenerów dockerowych

{{asciinema src=stateless}}

{{slide_end}}
{{slide}}

### #82AAFF Udostępnianie systemu plików do kontenera

{{asciinema src=docker_volumes}}

{{slide_end}}
{{slide}}

### #F78C6C Wysyłanie kontenerów do chmury

{{asciinema src=docker_push}}

{{slide_end}}
{{slide}}

### `docker run -it kontener` (do eksperymentów) 
{{asciinema src=docker_runit}}

{{slide_end}}
{{slide}}

<!-- P O D S U M O W A N I E  -->

## #C3E88D Podsumowanie

<br>

* #FF5370 Kontener jest *bezstanowy* - nie pamięta zmian

* #FFCB6B Domyślnie kontener jest zamknięty na świat

    * Ekspozycja portów

    * Zamontowanie systemu plików

* #F78C6C Opcja `-it` pozwala na interakcję przez terminal

* #82AAFF Wasze kontenery można hostować na Docker Hubie


{{slide_end}}
{{slide extra_class=first_slide}}

# Większe projekty

# #BB80B3 `docker-compose`


{{slide_end}}
{{slide}}

## Docker-compose
<br>

* #C3E88D Zdefiniowanie wielu kontenerów na raz

* #F78C6C Określenie powiązań między kontenerami

* #BB80B3 Łatwiejsze montowanie systemu plików

{{slide_end}}
{{slide}}

![](images/docker-compose-example.png)


{{slide_end}}
{{slide extra_class=rly_long}}

{{asciinema src=docker-compose-example}}

{{slide_end}}
{{slide extra_class=long}}
## #82AAFF Podsumowanie

<br>

* #FF5370 *Skomplikowany software = skomplikowana konfiguracja*

* #F78C6C Kontener != Maszyna wirtualna

* #FFCB6B W kontenerze zamykamy: *aplikację, runtime i konfigurację*

* #C3E88D Kontenery są:

    * Odizolowane od hosta (chyba że sam coś udostępnisz)

    * *Stateless* - nie zapamiętują zmian w systemie plików

* #82AAFF Cały kontener możemy zuploadować do chmury


{{slide_end}}
{{slide extra_class=first_slide}}

# To koniec?

{{slide_end}}
{{slide extra_class=first_slide}}

# #C3E88D Ankietka

{{slide_end}}
{{slide}}

# To tyle w tym semestrze!

<br>

### #C3E88D Dziękuję wszystkim, którzy przychodzili :)

#BB80B3 Mam nadzieję, że nauczyliście się czegoś przydatnego



{{slide_end}}
{{slide}}


{{asciinema src=christmas_sh}}


{{slide_end}}


