{{slide extra_class=first_slide}}

# Wiersz polecenia
## Podstawy


{{slide_end}}
{{slide}}

#BB80B3 *It's the high-level glue between you and the machine.*

<div style="padding-left:400px; padding-top: 10px">
~ Bash By Example, Part 1
</div>
{{slide_end}}
{{slide}}


## Co to tak naprawdę jest?

<br>

* Sposób #82AAFF interakcji z komputerem  </span> *(inaczej niż graficznie)*

* Przodek interfejsu graficznego

* #F07178 Genialne narzędzie </span> dla informatyków

{{slide_end}}
{{slide extra_class=first_slide}}

# Po co mi to? 

{{slide_end}}
{{slide}}

* #FF5370   Automatyzacja </span>

* #F78C6C   Większa wiedza i kontrola nad środowiskiem pracy </span>

* #FFCB6B   Szybkość *(ale nie przesadzajmy)* </span>

* #C3E88D   Terminal-only features 🤫 </span>

{{slide_end}}
{{slide extra_class=first_slide}}

# #F78C6C Trochę teorii

{{slide_end}}
{{slide}}

## Różne filozofie
#

Graficznie: #FF5370   uruchom raz, wyklikaj inne guziki</span>

Terminal: #C3E88D   uruchom wiele razy, z różnymi *opcjami*</span>

{{slide_end}}
{{slide extra_class=rly_long}}

## Opcje i flagi

### #C3E88D  Opcje </span>
Wszystko co przekazujemy do uruchamianego programu
{{asciinema src=cli_ping_basic.cast}}

{{slide_end}}
{{slide extra_class=rly_long}}


## Opcje i flagi
### #FF5370  Flagi </span>
Sposób na *poukładanie* opcji
{{asciinema src=cli_flag_basic.cast}}


{{slide_end}}
{{slide extra_class=rly_long}}
## Opcje i flagi
### #FF5370  Wiele flag - wiele opcji </span>
{{asciinema src=cli_flag_nonbasic.cast}}


{{slide_end}}
{{slide extra_class=rly_long}}


## Ok ale skąd wiedziałeś co to `-c` albo `-i`
#
### Czyli uniwersalne `--help`
#
{{asciinema src=cli_ping_help.cast}}

{{slide_end}}
{{slide}}

## `man` - #C3E88D Linux manual

{{asciinema src=man_ping}}


{{slide_end}}
{{slide extra_class=first_slide}}

# #BB80B3 Praktyka

{{slide_end}}
{{slide}}

### Pierwszy i najważniejszy tip

<br>

<h1 style="padding-left: 45px">
 #FF5370 Używaj taba
</h1>


{{slide_end}}
{{slide}}

{{asciinema src=use_the_damn_tab}}

{{slide_end}}
{{slide}}

### Pamiętaj o strzałkach

<br>

* #C3E88D ↑ -  poprzednia komenda w historii 

* #FF5370 ↓ - następna komenda w historii


{{slide_end}}
{{slide}}

{{asciinema src=arrows_history}}


{{slide_end}}
{{slide}}

### Jak #F78C6C *myśleć* #fff o terminalu

<br>

Na początek - jak o eksploratorze plików,

z dziwnym UI i wieloma funkcjami.


{{slide_end}}
{{slide extra_class=first_slide}}

## #C3E88D Strumienie, przekierowania, pipe'y


{{slide_end}}
{{slide}}

{{asciinema src=redirect}}

{{slide_end}}
{{slide}}

{{asciinema src=redirect_moar}}

{{slide_end}}
{{slide}}

## Output redirection

<br>

* #C3E88D `komenda > plik` #fff - zapisz do pliku wynik komendy

* #FF5370 `komenda >> plik` #fff - dopisz do pliku wynik komendy

{{slide_end}}
{{slide}}

{{asciinema src=pipe_grep}}


{{slide_end}}
{{slide}}

{{asciinema src=less}}

{{slide_end}}
{{slide}}

{{asciinema src=grep_dmesg}}


{{slide_end}}
{{slide}}


## Pipe  '`|`'
<br>

* Wysyła output jednej komendy do drugiej

* Może być łączone w #C3E88D łańcuchy


{{slide_end}}
{{slide}}

{{asciinema src=redirect_intro}}

{{slide_end}}
{{slide}}

{{asciinema src=redirect_showcase}}

{{slide_end}}
{{slide}}

## Przekierowanie inputu do programu
<br>

### `program <<< input`

<br>

#BB80B3 Dodatkowo:

### `program < plik_z_inputem`

{{slide_end}}
{{slide extra_class=first_slide}}

# Skrypty


{{slide_end}}
{{slide}}

{{asciinema src=script_live_coding}}


{{slide_end}}
{{slide extra_class=long}}

## Podsumowanie

<br>

* #FF5370 Czytajcie manual, komenda `man` powie wam wszystko

* #F78C6C Terminal jest naprawdę szybki - jeśli wiesz jak go używać

* #FFCB6B Shell potrafi zmusić programy do wspólnego działania

* #C3E88D Automatyzacja jest dziecinnie łatwa


{{slide_end}}
{{slide extra_class=long}}



### #BB80B3 *It's the high-level glue between you and the machine.*

{{slide_end}}
{{slide}}

### Co za tydzień?

{{slide_end}}
