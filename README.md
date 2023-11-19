Ron, deoarece este uituc de fel, îşi notează toate parolele pe o bucată de hârtie. Cum el ştie ca fraţii lui îi caută mereu printre lucruri, a decis să codifice aceasta parolă într-un vector generic, păstrând fiecare caracter din parola iniţială în următorul format:
* primul octet reprezintă o poziţie din șirul de caractere care reprezintă parola initiala
* al doilea octet este caracterul propriu-zis care se găsește la poziţia respectivă

Voi o sa scrieți cod doar în funcția **decript_message** din fisierul **main.c**, care primeşte ca parametrii vectorul generic şi numărul de octeţi ai acestuia. 

Pentru a verifica dacă rezolvarea este corectă este suficient să rulați comanda 

```
sudo python3 checker/checker.py
```