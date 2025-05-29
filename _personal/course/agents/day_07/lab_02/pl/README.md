
# AGI Day 07 – OpenAI Agents Evaluation with Langfuse

## Opis

Notebook demonstruje zastosowanie środowiska **Langfuse** do monitorowania, śledzenia oraz ewaluacji działania agentów AI wykorzystujących modele językowe w bibliotece `openai-agents`. Celem jest pokazanie, jak zintegrować narzędzia telemetryczne (OpenTelemetry) oraz platformę Langfuse w celu lepszego wglądu w procesy decyzyjne agentów i jakość ich odpowiedzi.

## Zakres działania

Notebook obejmuje:

- Konfigurację środowiska do śledzenia działania agentów,
- Integrację z platformą **Langfuse** poprzez OpenTelemetry,
- Tworzenie prostego agenta z instrukcją roli (prompt),
- Uruchamianie zadań i rejestrowanie ich przebiegu w Langfuse,
- Automatyczne przesyłanie metryk i logów z wykorzystaniem `logfire`.

## Technologie i biblioteki

W notebooku używane są następujące narzędzia:

- **`openai-agents`** – biblioteka do definiowania i uruchamiania agentów AI,
- **`langfuse`** – platforma do monitorowania interakcji z LLM-ami,
- **`logfire`** – instrumentacja do przesyłania danych telemetrycznych,
- **`OpenTelemetry`** – system śledzenia zdarzeń i metryk w czasie rzeczywistym,
- **`pydantic-ai[logfire]`** – do definiowania danych i obsługi CLI,
- **`nest_asyncio`** – umożliwia obsługę asynchroniczną w środowisku notebooka,
- **`datasets` (Hugging Face)** – umożliwia ładowanie i testowanie danych wejściowych.

## Kluczowe komponenty

- `Agent`, `Runner` – elementy biblioteki `openai-agents` odpowiadające za definicję i wykonanie agenta,
- `logfire.instrument_openai_agents()` – automatyczna instrumentacja logowania agentów,
- `OTLPSpanExporter`, `TracerProvider` – komponenty OpenTelemetry do przesyłania i zarządzania danymi śledzenia,
- Integracja z Langfuse przez zmienne środowiskowe i endpoint telemetryczny.

## Modele

Notebook wykorzystuje modele OpenAI dostępne przez interfejs OpenAI API. Dane uwierzytelniające i inne konfiguracje są wczytywane dynamicznie (np. z `google.colab.userdata`), co umożliwia ich bezpieczne przechowywanie.
