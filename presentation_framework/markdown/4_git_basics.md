{{slide extra_class=first_slide}}

# <div style="padding-left: 90px">Git</div> 
### Praca w zespole
{{slide_end}}
{{slide}}

## Czym jest git

<br>

* #C3E88D VCS - system kontroli wersji

* #FFCB6B Zarządzanie kodem

* #F78C6C Dzielenie się kodem

* #BB80B3 Szybsze znajdywanie bugów

{{slide_end}}
{{slide}}


## Po co mi git

<br>

* #C3E88D Do dowolnego projektu grupowego

* #FFCB6B Do chwalenia się kodem na *gitlabie/githubie*

* #F78C6C Na każdej rekrutacji do pracy pytają o gita

* #BB80B3 Dobry nawyk na backup swojej osobistej pracy

{{slide_end}}
{{slide extra_class=first_slide}}
# Workflow


{{slide_end}}
{{slide}}

## Łatwy use case - na poczatek

<br>

* #C3E88D Repozytorium hostowane na GitHubie

* #FFCB6B Kilka osób pracujących jednocześnie

* #F78C6C Wysyłanie i pobieranie kodu z/do repozytorium

* #BB80B3 Rozwiązywanie merge conflictów

{{slide_end}}
{{slide}}

## `git clone <adres>`

<br>

#C3E88D Po prostu pobiera repozytorium


{{slide_end}}
{{slide}}


## `git status`

<br>

#C3E88D pokazuje *co się dzieje*

<br>

`$ git status`

`On branch master`



`No commits yet`



`nothing to commit (create/copy files and`

` use "git add" to track)`



{{slide_end}}
{{slide}}

## Po zapisaniu pliku w repozytorium

<br>

`Untracked files:`

`  (use "git add <file>..." to include`

` in what will be committed)`

<br>

#FF5370<code> file.cpp</code>



{{slide_end}}
{{slide}}

## #FFCB6B `git add -A`
Dodaje wszystkie zmiany do `snapshota`

<br>

#FFCB6B `git add ścieżka/do/pliku.cpp` 

doda pojedynczy plik


<br>

#FFCB6B `git add ścieżka/do/folderu` 

doda wszystkie zmiany w folderze

{{slide_end}}
{{slide}}

## `git status` po dodaniu plików

<br>

`Changes to be committed:`

`  (use "git rm --cached <file>..." to unstage)`

#C3E88D<code> new file:   file.cpp</code>



{{slide_end}}
{{slide}}

## #F78C6C `git commit -m "Opis zmian"`
<br>
Zapisuje aktualnie dodane zmiany do commmita

i nadaje mu wybraną przez Was nazwę.


{{slide_end}}
{{slide}}

## `git status` po zrobieniu commita

<br>

`On branch master`

`nothing to commit, working tree clean`

{{slide_end}}
{{slide}}


## #C3E88D `git push`
<br>
Wysłanie swoich commitów na serwer.

{{slide_end}}
{{slide}}


## #C3E88D `git pull`
<br>
Pobranie cudzych zmian z serwera.


{{slide_end}}
{{slide extra_class=first_slide}}
# #F78C6C Konflikty

{{slide_end}}
{{slide}}


`# Rozdział 1`

`Tu będzie rozdział 1`

<br>
<br>

`# Rozdział 2`

`Tu będzie rozdział 2`

<br>
<br>

`# Rozdział 3`


{{slide_end}}
{{slide}}
![](images/conflicting_files.png)

{{slide_end}}
{{slide}}

### #FF5370 Jeśli ktoś wykona `git pull`

<br>

![](images/auto_merge_fail.png)




{{slide_end}}
{{slide}}
![](images/conflict.png)



{{slide_end}}
{{slide}}

(...)

`# Rozdzial 2`

#C3E88D<code><<<<<<< HEAD </code>

`Tu będzie rozdział 2`

#FFCB6B<code>======= </code>

`Też zmieniam rozdzial 2`

#82AAFF<code>>>>>>>> b690756a26b0561e36382c61373505fa31575b08 </code>


`# Rozdział 3`

(...)
{{slide_end}}
{{slide}}

#C3E88D<code><<<<<<< HEAD </code>

'głowa' mojej wersji - moje zmiany

<br>

#82AAFF<code>>>>>>>> b690756a26b0561e36382c61373505fa31575b08 </code>

commit id zmiany z serwera - konfliktujące zmiany

{{slide_end}}
{{slide}}

## Jak to naprawić?
<br>
#C3E88D Wystarczy skasować* niechciane fragmenty kodu

<br>

<span style="font-size: 80%"> #BB80B3 *Nowoczesne edytory kodu mają do tego interfejs</span>

{{slide_end}}
{{slide}}


{{slide_end}}
{{slide}}

{{slide_end}}
