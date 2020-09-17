{{slide extra_class=first_slide}}


<br>
## Instalacja Linuxa
#### i najważniejsze sprawy po instalacji
<br>


{{slide_end}}
{{slide extra_class=long}}

# Cel prezentacji
<br>

* Wyjaśnienie kilku mitów dotyczących linuxa, jego instalacji, etc

* Dual-boot #82AAFF Windows</span> / #C3E88D Linux</span> - zrozumienie

* #F78C6C   Normalny czas pracy na baterii w przypadku laptopów </span>

* #FFCB6B  Rozwiązanie problemów z GPU w laptopach gamingowych </span>

{{slide_end}}
{{slide extra_class=first_slide}}

## Plan prezentacji

{{slide_end}}
{{slide}}


### #FFCB6B  FAQ </span>
* Czy nie zepsuję sobie komputera/laptopa
* Czy mogę mieć dalej Windowsa?
* Co to są te dystrybucje i którą wybrać?



### #FF5370  Instalacja </span>
* Jak przygotować komputer
* Pendrive z linuxem
* Proces instalacji


### #BB80B3  I co potem? </span>
* Praca na baterii
* Laptopy gamingowe i ich karty graficzne
* Podstawowe programy, edytory kodu, etc

{{slide_end}}
{{slide extra_class=first_slide}}

# #FFCB6B  FAQ </span>


{{slide_end}}
{{slide}}


## Czy nie zepsuję sobie komputera?
<br>

#FF5370 W najgorszym przypadku skasujesz sobie Windowsa,

#FF5370 ale tylko jeśli będziesz nieostrożny/na. Klikaj uważnie.

</span>

<br>

### #C3E88D Nie dasz rady zepsuć komputera na amen.


{{slide_end}}
{{slide}}

## Czy mogę mieć dalej windowsa?

![](images/grub.png)

##### #C3E88D Tak, możesz mieć Windowsa, komputer zapyta przy uruchomieniu</span>


{{slide_end}}
{{slide}}

## Czym są dystrybucje? Jaką wybrać?

<br>

* #FF5370  Mimo że wyglądają inaczej, są naprawdę podobne </span>

* #F78C6C   Nie wybieraj nic niszowego </span>

* #FFCB6B  Większa popularność - więcej supportu </span>
 
* #F78C6C   Ubuntu </span>/#C3E88D Manjaro </span>



{{slide_end}}
{{slide extra_class=first_slide}}

# #FF5370  Instalacja </span>

{{slide_end}}
{{slide}}

## Jak przygotować komputer?

* #F78C6C   Wolna partycja </span>

* #FFCB6B  BIOS/UEFI - czego używasz? </span>

* #C3E88D Wyłączenie windowsowego *fast startup* </span>


{{slide_end}}
{{slide}}

## Wolna partycja

![](images/partitions.png)


* #C3E88D Partitions manager </span>

* #FF5370  ~ 50GB - w miarę komfortowe minimum </span>

{{slide_end}}
{{slide}}


## BIOS/UEFI - czego używasz?

![](images/bios_uefi_mode.png)

{{slide_end}}
{{slide}}


## Wyłączenie windowsowego *fast startup*

![](images/fast_startup.webp)


{{slide_end}}
{{slide extra_class=first_slide}}

## Pendrive z linuxem


{{slide_end}}
{{slide}}

### No właśnie, którym linuxem?

![](images/download_iso.png)
{{slide_end}}

{{slide extra_class=big_slide}}



<div style="font-size:91%; float: left ; margin-right: 50px; margin-top: 65px">
<h4>Zupełnie nowy komputer</h4>
    <ul>
        <li>
            #C3E88D Manjaro </span>
        </li>
    </ul>
<h4>Komputer starszy niż rok</h4>
    <ul>
        <li>
            #F78C6C   Ubuntu </span>
        </li>
    </ul>
</div>

<div style="font-size:91%;float: right; margin-left: 50px">
<h4>Mocne podzespoły</h4>
    <ul>
        <li>
            #82AAFF GNOME Edition</span>
        </li>
    </ul>
<h4>Średnie podzespoły</h4>
    <ul>
        <li>
            #FF5370 KDE Edition</span>
        </li>
    </ul>
<h4>Słabe/Stare podzespoły</h4>
    <ul>
        <li>
            #FFCB6B XFCE/LXDE Edition</span>
        </li>
    </ul>
</div>

{{slide_end}}
{{slide}}

### Wypalanie pobranego ISO

* #C3E88D Rufus </span>

* #FF5370  Etcher </span>

{{slide_end}}
{{slide}}

### Uruchamianie z pendrive'a lub DVD

<br>

* Wyłącz komputer

* Podłącz pendrive

* Wejdź do BIOSa/UEFI

* Wyłącz #FF5370  secure boot</span>

* Przełącz #C3E88D boot device </span> na pendrive

* Reset


{{slide_end}}

{{slide extra_class=first_slide}}
# Proces instalacji


{{slide_end}}

{{slide}}

* #FF5370 Uważnie czytaj dialogi*</span>

* #C3E88D Jest tylko jeden trudny krok:</span>
    * *wybór partycji*

<br>

\* <span style="font-size: 70%"> #FFCB6B Możesz chcieć zainstalować *3rd party software*</span>


{{slide_end}}

{{slide extra_class=big_slide}}
## Wybór partycji
<br>

* #F78C6C  Komputer na BIOSIE</span>:
    
    * stworzona wcześniej partycja, punkt montowania `'/'`, ext4

<br>

* #82AAFF Komputer na UEFI</span>:
    
    * stworzona wcześniej partycja, punkt montowania `'/'`, ext4

    * pierwsza partycja na dysku, punkt montowania `'/boot/efi'`
        
        <span style="font-size: 70%"> #FF5370^ NIE FORMATUJ PARTYCJI EFI</span>
{{slide_end}}
{{slide extra_class=first_slide}}

# #BB80B3 Po instalacji</span>

{{slide_end}}
{{slide}}

## Praca na baterii

* Oszczędzanie baterii #FF5370 może być domyślnie wyłączone</span>

* #C3E88DProgramy do oszczędzania baterii</span>

    * `tlp`

    * `powertop` *(opcjonalnie)*


{{slide_end}}
{{slide extra_class=big_slide}}

# TLP




### #F78C6C   Ubuntu </span>

`sudo apt update`

`sudo apt install tlp`

`sudo systemctl enable tlp`


<br>
### #C3E88D  Manjaro </spam>

`sudo pacman -Syu tlp`

`sudo systemctl enable tlp`

{{slide_end}}
{{slide extra_class=long}}


### Laptopy gamingowe <spam style="color: #2d3c45">- gracze powstańcie</span>

#####  #C3E88D   Najlepiej po prostu wyłączyć GPU Nvidii </span>

<br>

`sudo echo "blacklist nouveau" > /etc/modprobe.d/pwr.conf`

{{slide_end}}
{{slide}}

## Podstawowe programy
<br>
#### #C3E88D  App store w Ubuntu i w Manjaro działa już naprawdę spoko </span>

Po więcej, zapraszam na kolejny wykład:

<br>

### #BB80B3  Instalowanie softu na Linuxie </span>
* Package managery

* Instalowanie apek spoza oficjalnych repozytoriów

{{slide_end}}