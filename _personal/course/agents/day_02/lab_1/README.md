# AGI Day 02 – Lab 01: Agent z LLM i Interpreterem Kodu

## Opis

Ten notebook przedstawia praktyczne zastosowanie frameworku **LlamaIndex** w połączeniu z dużym modelem językowym od **Anthropic (Claude)**. Celem ćwiczenia jest utworzenie agenta, który potrafi dynamicznie korzystać z narzędzia do interpretacji kodu w Pythonie – umożliwiając wykonywanie obliczeń oraz odpowiadanie na pytania wymagające przetwarzania danych w czasie rzeczywistym.

Notebook demonstruje integrację różnych komponentów, budowę agenta opartego na funkcjach oraz jego wykorzystanie w scenariuszach związanych z analizą danych.

## Użyte biblioteki

- `llama-index` – główna biblioteka do budowy agentów opartych o LLM z dostępem do danych.
- `llama-index-llms-anthropic` – integracja modeli Anthropic (Claude) z LlamaIndex.
- `llama-index-tools-code-interpreter` – narzędzie umożliwiające agentowi wykonywanie kodu w Pythonie jako część jego odpowiedzi.

## Użyty LLM

- **Anthropic Claude** – duży model językowy, wykorzystany jako "mózg" agenta do przetwarzania języka naturalnego i koordynowania działania narzędzi.

## Przypadek użycia

Notebook tworzy **agenta z funkcją wywoływania kodu (FunctionCallingAgent)**, który potrafi:

- Przyjmować pytania użytkownika w języku naturalnym,
- Wnioskować, czy do odpowiedzi potrzebne jest uruchomienie kodu,
- Wygenerować odpowiedni kod w Pythonie,
- Uruchomić kod i zinterpretować wynik,
- Zwrócić końcową odpowiedź w sposób zrozumiały dla użytkownika.
