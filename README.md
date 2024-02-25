# Jocul Piatra, Hartie, Foarfeca

Acest script Python implementează un joc simplu de Piatra, Hartie, Foarfeca în care jucătorul concurează împotriva AI-ului. Primul jucător care ajunge la 2 puncte câștigă jocul.

## Cum se joacă

1. Rulează scriptul.
2. Introdu alegerea ta între Piatra, Hartie sau Foarfeca când ești întrebat.
3. AI-ul va selecta aleator o alegere.
4. Câștigătorul rundei va fi anunțat, iar scorurile vor fi afișate.
5. Jocul continuă până când unul dintre jucători ajunge la 2 puncte.
6. Jucătorul cu 2 puncte câștigă jocul.

## Reguli

- Piatra învinge Foarfeca
- Foarfeca învinge Hartie
- Hartia învinge Piatra

## Explicație a codului

- Scriptul utilizează o buclă `while` pentru a continua jocul până când unul dintre jucători ajunge la 2 puncte.
- Funcția `random.randrange(0, 3)` generează un număr aleator care reprezintă alegerea AI-ului.
- Intrarea jucătorului este convertită în litere mici folosind metoda `.lower()` pentru a gestiona intrările care nu sunt sensibile la litere mari și mici.
- Logica jocului este implementată folosind expresiile `match` pentru a determina câștigătorul fiecărei runde.
- Scorurile sunt actualizate pe baza rezultatului fiecărei runde și afișate după fiecare rundă.
- Jocul se încheie când unul dintre jucători ajunge la 2 puncte, iar câștigătorul este anunțat.

### Notă
Scriptul este destinat unor scopuri educaționale și oferă un exemplu de bază al implementării unui joc Piatra, Hartie, Foarfeca în Python. Poate fi extins și îmbunătățit pentru caracteristici și funcționalități suplimentare.
