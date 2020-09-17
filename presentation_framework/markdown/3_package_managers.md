{{slide extra_class=first_slide}}


<br>
## Package management
#### instalowanie softu na Linuxie
<br>


{{slide_end}}
{{slide extra_class=long}}

# Cel prezentacji
<br>

* #C3E88D Czym i po co są **package managery**

* #FFCB6B Instalowanie softu oficjalnym package managerem

* #F78C6C Aktualizowanie i usuwanie pakietów

* #BB80B3 Instalowanie programów spoza repozytorium

{{slide_end}}
{{slide extra_class=image}}
<img class="meme" src="images/we_dont_do_that_here.jpg"/>
{{slide_end}}
{{slide}}

## Package manager

<br>

* #C3E88D Zarządza wszystkimi zainstalowanymi programami

* #FF5370 Pilnuje plików zainstalowanych aplikacji/bibliotek

* #FFCB6B Utrzymuje drzewo zależności - `dependency tree`

* #BB80B3 Aktualizuje cały system #s - za jednym zamachem

{{slide_end}}
{{slide extra_class=big_slide}}

#### #F78C6C Ubuntu - `apt`
{{asciinema src=upgrade_apt}}

#### #C3E88D Manjaro - `pacman`
{{asciinema src=upgrade_pacman}}


{{slide_end}}
{{slide extra_class=first_slide}}

# *"Workflow"*


{{slide_end}}
{{slide}}

### #FFCB6B 1. Aktualizacja listy pakietów
### #C3E88D 2. Pobieranie/aktualizowanie pakietów


{{slide_end}}
{{slide extra_class=big_slide}}

## Pobieranie informacji o nowych pakietach

<div style="width: 970px">

#F78C6C <code style="position: relative;left: -15px; top: 50px; font-size: 80% ">apt update</code>

{{asciinema src=update_apt}}



#C3E88D <code style="position: relative;left: -15px; top: 80px; font-size: 80% ">pacman -Sy </code>
{{asciinema src=update_pacman}}

{{slide_end}}

{{slide extra_class=big_slide}}

## Instalowanie nowych pakietów

<div style="width: 970px">

#F78C6C <code style="position: relative;left: -15px; top: 50px; font-size: 80% ">apt install </code>

{{asciinema src=install_apt}}



#C3E88D <code style="position: relative;left: -15px; top: 80px; font-size: 80% ">pacman -S </code>
{{asciinema src=install_pacman}}


{{slide_end}}

{{slide}}

#### Skąd mam wiedzieć jak nazywa się paczka, której szukam?

##### Google -> #F78C6C *ubuntu packages*

![](images/ubuntu_packages.png)


{{slide_end}}
{{slide}}


##### Google -> #C3E88D *arch packages*
![](images/arch_packages.png)

{{slide_end}}

{{slide extra_class=big_slide}}

## Instalowanie aktualizacji

<div style="width: 970px">

#F78C6C <code style="position: relative;left: -15px; top: 50px; font-size: 80% ">apt upgrade </code>

{{asciinema src=upgrade_apt}}



#C3E88D <code style="position: relative;left: -15px; top: 80px; font-size: 80% ">pacman -Su </code>
{{asciinema src=upgrade_pacman}}

{{slide_end}}
{{slide}}


## Update list pakietów + aktualizacja

<br>

#F78C6C `sudo apt update && sudo apt upgrade`

<br>

#C3E88D `sudo pacman -Syu`

{{slide_end}}
{{slide extra_class=first_slide}}
# #FF5370 Usuwanie pakietów
{{slide_end}}
{{slide}}

## #FF5370 Drzewo zależności - `dependency tree`

<br>

Program może opierać swoje działanie na innych

programach (automatycznie ściągnie je *package manager*).

<br><br>

Programy nawzajem zależne od siebie formują

#C3E88D strukturę drzewiastą.

{{slide_end}}
{{slide}}

### Wszystkie zależności #F78C6C Firefoxa

{{asciinema src=pactree}}
{{slide_end}}


{{slide}}

### #F78C6C Usuwanie pakietu na Ubuntu

<br>

* `apt remove`

* `apt autoremove`

<br>

{{asciinema src=remove_apt}}


{{slide_end}}

{{slide}}

### #C3E88D Usuwanie pakietu w Manjaro

<br>

`sudo pacman -Rscn`

<br>

{{asciinema src=remove_pacman}}

{{slide_end}}

{{slide}}
### Mojego programu nie ma w repozytoriach!


{{slide_end}}
{{slide}}

## #BB80B3 3rd party repositories

<br>

Osobne repozytoria dla produktów komercyjnych.

<br>

* #F78C6C Ubuntu - `snap`

* #C3E88D Manjaro - `AUR`
{{slide_end}}

{{slide}}

### #F78C6C `snap install`

{{asciinema src=snap_apt}}



{{slide_end}}
{{slide}}

## Google -> #BB80B3 snap store
<br>

* Discord

* Spotify

* VS Code

* IntelliJ IDEA

* PyCharm

{{slide_end}}
{{slide}}


## Dodawanie repozytoriów do `apta`
#### *Na przykładzie edytora Atom*
<br>

`sudo add-apt-repository ppa:webupd8team/atom`

`sudo apt update`

`sudo apt install atom`

<br>

*PPA - Personal Package Archive*

#FF5370 Uwaga, nieoficjalne (o s t r o ż n i e)


{{slide_end}}
{{slide}}


### #FF5370 Mojego pakietu nie ma absolutnie nigdzie
<br>

* Poszukaj alternatywy

* Jeżeli **naprawdę musisz** używać właśnie tego programu:
    * Używaj tylko oficjalnego tutoriala instalacyjnego

    * Staraj się rozumieć wklejane z internetu komendy


{{slide_end}}
{{slide extra_class=first_slide}}

# #C3E88D Podsumowanie

{{slide_end}}

{{slide extra_class=big_slide}}


#### #FF5370 Package manager
Narzędzie systemowe służące do instalowania pakietów.

<br>

#### #FFCB6B `update` vs `upgrade`
Pobranie nowej listy pakietów #FFCB6B vs #fff pobranie aktualizacji pakietów.

<br>

#### #F78C6C Dependency tree
Pakiety zależą na pakietach - i tak dalej.
{{slide_end}}
