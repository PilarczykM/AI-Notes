# 🛠️ AGI Day 08 – SmolAgents with Arize Phoenix

## 🎯 Cel notebooka

Notebook demonstruje integrację lekkich agentów **SmolAgents** z systemem **Arize Phoenix** w celu śledzenia, oceny i analizy ich działania. Głównym celem jest pokazanie, jak:
- tworzyć agentów z dostępem do narzędzi (np. wyszukiwarka, kod),
- uruchamiać ich na zadaniach tekstowych,
- automatycznie oceniać wyniki z użyciem modeli LLM,
- logować szczegóły interakcji do systemu obserwowalności Phoenix.

---

## 🧠 Użyty model językowy

Notebook korzysta z modelu klasy **GPT-4.1** (via `OpenAIModel`) do:
- automatycznego generowania odpowiedzi przez agenta,
- ewaluacji odpowiedzi w kontekście poprawności (`llm_classify`).

Model ten działa jako backend zarówno dla agenta (`LiteLLMModel`), jak i dla oceniającego (`OpenAIModel`).

---

## 🤖 Użyte biblioteki i narzędzia

| Biblioteka                         | Zastosowanie                                                                |
|------------------------------------|-----------------------------------------------------------------------------|
| `smolagents`                       | budowa lekkich agentów wykonujących kod, wyszukiwanie itp.                 |
| `phoenix` (`arize-phoenix`)        | monitorowanie działania agentów i logowanie oceny                          |
| `openinference.instrumentation`    | integracja śledzenia z Arize                                               |
| `langchain`                        | przetwarzanie tekstu i dokumentów, wyszukiwanie kontekstowe                |
| `datasets`                         | ładowanie danych testowych                                                 |
| `openai`                           | backend modelu LLM                                                         |

---

## 📁 Struktura działania

1. **Importy i konfiguracja**
   - Ładowanie bibliotek `SmolAgents`, `Phoenix`, `Langchain`
   - Ustawienie kluczy API i ścieżek środowiskowych

2. **Instrumentacja agenta**
   - Włączenie monitorowania SmolAgents przez `SmolagentsInstrumentor`

3. **Tworzenie agenta**
   - Agent typu `CodeAgent` z narzędziami: wyszukiwanie (DuckDuckGo), LLM, kod
   - Ładowanie dokumentów jako kontekstu
   - Wyszukiwanie i ekstrakcja kontekstu do zadań

4. **Rozwiązywanie zadań**
   - Agent odpowiada na pytania oparte na kontekście
   - Rejestrowanie działania z użyciem Phoenix trace spans

5. **Ewaluacja wyników**
   - Automatyczna ocena odpowiedzi przy użyciu modelu OpenAI
   - Wynik klasyfikowany jako `"correct"` lub `"incorrect"` przez `llm_classify`

6. **Logowanie i analiza**
   - Wyniki ocen rejestrowane przez `SpanEvaluations`
   - Możliwość filtrowania i analizy przez interfejs Phoenix (SpanQuery)

---

## 📂 Dane wejściowe

- Zbiór danych z `datasets` (np. QA tasks)
- Dokumenty tekstowe przetwarzane przez `Langchain` do ekstrakcji kontekstu

## 📤 Dane wyjściowe

- Ocenione odpowiedzi agentów wraz z metadanymi przesyłane do **Arize Phoenix**
- Informacje śledzące (`spans`) zawierające dane wejściowe, odpowiedzi i oceny

---

## 🧪 Przykładowe zastosowania

- Monitorowanie skuteczności agentów LLM w czasie rzeczywistym
- Budowa lekkich, obserwowalnych agentów działających w różnych środowiskach
- Automatyczna analiza błędów i poprawnych interakcji w dużych zbiorach danych
