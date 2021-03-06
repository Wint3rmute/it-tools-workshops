## Słowem wstępu

Prawie wszystkie te programy można pobrać za pomocą swojego package managera (`apt install <pakiet>` lub `pacman -S <pakiet>`). Strony internetowe podaję po to, żeby poczytać na nich o danym programie i nauczyć się go używać. Nie próbujcie ściągać paczek .deb i je instalować, od tego są własnie package managery.

#

### Bateria w laptopie

[tlp](https://wiki.archlinux.org/index.php/Tlp) - apka do oszczędzania baterii, włącz i zapomnij

[Powertop](https://wiki.archlinux.org/index.php/powertop) - tak samo jak wyżej, najlepiej ogarnąć sobie obie

### Programy do spraw codziennych

[Flameshot](https://flameshot.js.org/#/) - Screenshoty po ludzku.

[KDE Connect](https://kdeconnect.kde.org/) - Jeśli używasz KDE i masz smartfona z Androidem.

[Simple Screen Recorder](https://www.maartenbaert.be/simplescreenrecorder/) - Jak w nazwie.

[Transmission](https://transmissionbt.com/) - Klient torrentów.

[VLC](https://www.videolan.org/index.html) - Mam nadzieję że nie trzeba przedstawiać xD

[ffmpeg](https://ffmpeg.org/) - Konwertuje między różnymi formatami video (i wiele więcej, jeśli chodzi o pracę z formatami/streamami video). 

#
### Usprawnienia shella

[zsh](https://wiki.archlinux.org/index.php/zsh) - Subiektywnie najlepszy shell (*yes fishermen, you heard me right*). Zainstalowana domyślnie na wszystkich normalnych dystrybucjach.

[Antigen](https://github.com/zsh-users/antigen) - Fajny menadżer rozszerzeń do zsh.

[Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh) - Jeśli jesteś zbyt leniwy/wa, żeby przeczytać instrukcję instalacji Antigena, Oh my Zsh jest minimalnie wolniejsze, ale instaluje się zupełnie automatycznie.


#
### Workflow w shellu

[TheFuck](https://github.com/nvbn/thefuck) - Poprawia literówki w komendach, intuicyjny sposób użycia.

[Aliasy pod komendy gitowe w Zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Cheatsheet#git) - Domyślnie aktywne w Oh My Zsh i w Antigenie.

[sshfs](https://github.com/libfuse/sshfs) - Montowanie zdalnego systemu plików przez SSH.

[Screen](https://linuxize.com/post/how-to-use-linux-screen/) - Wirtualne sesje terminalowe, mega przydatne przy pracy ze zdalnymi serwerami (można się odpiąć z SSH bez wyłączania procesów działających w shellu).

[Entr](http://entrproject.org/) - Narzędzie do automatyzacji, fajnie wytłumaczone [tutaj](https://youtu.be/9KAp_zWeI34).


#
### Git workflow

[Dodawanie klucza SSH](https://docs.github.com/en/enterprise/2.18/user/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) - korzystanie z gita bez hasła. Ten tutorial ma małą wadę: zamiast instalować `xclip` i wykonywać `$ xclip -sel clip < ~/.ssh/id_rsa.pub`, można równie dobrze zrobić `cat ~/.ssh/id_rsa.pub` i skopiować output z terminala.

#
### AUR helpers

**Tylko dla ludzi z Manjaro/Archem**

[Pikaur](https://github.com/actionless/pikaur) - Działa, tyle wystarczy.

#
### Narzędzia developerskie

[VS Code Live Share](https://docs.microsoft.com/pl-pl/visualstudio/liveshare/) - wspólne klepanie kodu w VS Code, niesamowicie wygodne.
