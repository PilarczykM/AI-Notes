# 🗃️ AGI Day 08 – SQL Agent with Arize Phoenix

## 🎯 Cel notebooka

Ten notebook pokazuje, jak zbudować **agenta obsługującego zapytania SQL**, który korzysta z dużego modelu językowego (LLM), a jego działanie jest w pełni monitorowane i oceniane za pomocą platformy **Arize Phoenix**.

Celem jest umożliwienie użytkownikowi zadawania pytań w języku naturalnym, które następnie są automatycznie przekształcane na zapytania SQL, wykonywane na bazie danych i oceniane pod kątem trafności odpowiedzi.

---

## 🧠 Użyty model językowy

Notebook wykorzystuje model klasy **GPT-4.1** jako silnik dla agenta oraz dla ewaluacji. Model realizuje:
- transformację pytań użytkownika w zapytania SQL,
- automatyczną ocenę odpowiedzi (poprawność, zgodność z kontekstem).

---

## 🔌 Technologie i biblioteki

| Biblioteka / narzędzie            | Zastosowanie                                                             |
|-----------------------------------|--------------------------------------------------------------------------|
| `sqlite3`                         | lokalna baza danych do wykonywania zapytań SQL                          |
| `openai`                          | dostęp do modelu językowego GPT                                          |
| `phoenix` (`arize-phoenix`)       | śledzenie działania agenta, ewaluacja i logowanie danych                |
| `openinference.instrumentation`   | integracja i tracing operacji agenta                                     |
| `llm_classify` (`phoenix.evals`)  | automatyczna klasyfikacja jakości odpowiedzi                            |
| `pandas`, `json`, `os`            | obsługa danych, struktury i pliki konfiguracyjne                         |

---

## 🧱 Struktura działania

1. **Tworzenie bazy danych**
   - Lokalna baza SQLite z przykładowymi tabelami (np. `users`, `orders`)
   - Wypełnienie danymi testowymi

2. **Definicja agenta SQL**
   - Agent przekształca pytania w języku naturalnym na SQL
   - Wykonuje zapytanie i zwraca wynik użytkownikowi

3. **Śledzenie i instrumentacja**
   - Każda interakcja agenta jest logowana jako `span` w Phoenix
   - Automatyczna rejestracja zdarzeń i wyników zapytań

4. **Ewaluacja odpowiedzi**
   - Odpowiedzi oceniane przez model LLM (jako `correct` lub `incorrect`)
   - Logowanie oceny do `SpanEvaluations` w systemie Arize

5. **Wizualizacja i analiza**
   - Dane można przeglądać, filtrować i analizować w interfejsie Phoenix

---

## 📂 Dane wejściowe

- Tekstowe pytania w języku naturalnym, np.:  
  *„Ilu użytkowników złożyło zamówienia powyżej 100 USD?”*

- Baza danych SQLite utworzona w notebooku (`sqlite3.connect(...)`)

---

## 📤 Dane wyjściowe

- Wyniki zapytań SQL generowanych przez agenta
- Ocenione odpowiedzi (`correct` / `incorrect`) przez model GPT
- Metadane z trace spans logowane do **Arize Phoenix**

---

## 🧪 Przykładowe zastosowania

- Testowanie agentów SQL z interfejsem w języku naturalnym
- Śledzenie poprawności generowanych zapytań przez LLM
- Integracja LLM z bazami danych w środowisku produkcyjnym
