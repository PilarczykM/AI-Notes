# 🧮 AGI Day 08 – OpenAI Agent Evaluation Lab

## 🎯 Cel notebooka

Notebook demonstruje **proces ewaluacji agenta rozwiązującego zadania matematyczne**, zbudowanego w oparciu o model językowy (LLM). Ocena przeprowadzana jest automatycznie, a wyniki są logowane i analizowane za pomocą narzędzia **Phoenix (Arize)**.

---

## 🧠 Użyty model językowy

W eksperymencie wykorzystywany jest model klasy **GPT-4.1**. Jest on używany zarówno do:
- rozwiązywania zadań matematycznych przez agenta,
- automatycznej oceny poprawności wygenerowanych odpowiedzi (funkcja klasyfikująca `llm_classify`).

---

## 📦 Wymagane biblioteki

Notebook korzysta z następujących bibliotek:

| Biblioteka                       | Zastosowanie                                                                 |
|----------------------------------|------------------------------------------------------------------------------|
| `openai`                         | dostęp do modelu GPT-4.1                                                    |
| `openai-agents`                  | tworzenie agentów                                                          |
| `phoenix` (`arize-phoenix`)     | logowanie i analiza ewaluacji                                              |
| `openinference-instrumentation` | śledzenie działania modeli i agentów                                       |
| `pandas`, `asyncio`, `uuid`     | manipulacja danymi, operacje asynchroniczne                                |
| `nest_asyncio`                  | umożliwia uruchamianie pętli zdarzeń w środowisku notebooka                |
| `opentelemetry`                 | śledzenie i analiza działania aplikacji (trace/span)                       |

---

## 📁 Struktura działania

1. **Konfiguracja środowiska**
   - Instalacja niezbędnych bibliotek
   - Ustawienie zmiennych środowiskowych (klucz OpenAI, endpoint Phoenix)

2. **Tworzenie agenta**
   - Agent rozwiązujący zadania matematyczne przez `eval()`
   - Zdefiniowany jako narzędzie (`@function_tool`)

3. **Generowanie danych testowych**
   - Model generuje 25 różnorodnych zadań matematycznych na podstawie promptu

4. **Rozwiązywanie zadań przez agenta**
   - Każde zadanie rozwiązywane jest asynchronicznie
   - Odpowiedzi są rejestrowane i oceniane

5. **Ewaluacja odpowiedzi**
   - Ocena poprawności odpowiedzi za pomocą `llm_classify` i `openaimodel`
   - Wynik: `correct` lub `incorrect` + wyjaśnienie

6. **Logowanie wyników**
   - Wyniki ewaluacji przesyłane do systemu Phoenix (Arize) jako `span evaluations`
   - Przechowywanie metadanych, statusów i śledzenie działania (span tracing)

---

## 📂 Dane wejściowe

- Brak potrzeby ręcznego dostarczania danych – problemy matematyczne są generowane automatycznie przez model.

## 📤 Dane wyjściowe

- Wyniki ewaluacji przesyłane są do systemu Phoenix (Arize) jako `span evaluations`.

---

## 🧪 Przykładowe zastosowania

- Automatyczna ocena jakości rozwiązań generowanych przez agentów
- Testowanie nowych architektur agentów bez konieczności ręcznej oceny
- Śledzenie i analiza działania agenta w czasie rzeczywistym dzięki integracji z Arize Phoenix
