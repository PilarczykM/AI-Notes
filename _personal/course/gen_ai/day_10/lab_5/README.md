# 🧪 GenAI Day 10 Lab 5 – Wykrywanie Danych Osobowych (PII) z LangKit

## 📋 Opis

Ten notebook przedstawia praktyczne zastosowanie biblioteki **LangKit** do automatycznego wykrywania **danych osobowych (PII)** w interakcjach tekstowych między użytkownikiem a modelem językowym. PII to informacje takie jak:
- imiona i nazwiska,
- numery kart kredytowych,
- numery PESEL lub SSN,
- adresy zamieszkania,
- adresy e-mail,
- numery telefonów.

Celem notebooka jest przetestowanie wykrywania takich informacji w parach *prompt–response*, co ma kluczowe znaczenie dla budowy **bezpiecznych systemów AI**, szczególnie w zastosowaniach biznesowych, medycznych czy prawniczych.

## 📦 Wymagane biblioteki

Notebook korzysta z biblioteki:

- **`langkit[all]`** – zainstalowanej w pełnej wersji, zawierającej wszystkie potrzebne narzędzia do analizy tekstu i wykrywania PII.

## 🧠 Działanie

Notebook testuje wiele przykładów wejść i odpowiedzi, które potencjalnie zawierają dane osobowe. Używa funkcji `extract.pii()` do ich identyfikacji. Analizowane są sytuacje takie jak:
- podanie numeru SSN lub karty kredytowej,
- zmiana adresu,
- podanie numeru telefonu.

Dzięki temu możliwe jest automatyczne filtrowanie treści wrażliwych oraz budowa systemów, które nie przechowują i nie przetwarzają niepotrzebnych danych osobowych.

## 🛡️ Przykładowe użycie

Każda para prompt–response jest analizowana, a funkcja `extract.pii` wykrywa i wskazuje, gdzie w tekście pojawiły się informacje klasyfikowane jako PII. Wykrycie takich danych może być podstawą do:
- zamaskowania ich,
- ostrzeżenia użytkownika,
- logowania incydentu bezpieczeństwa.
