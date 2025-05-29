# AGI Day 07 – Guardrails Lab

## Opis

Notebook prezentuje zastosowanie mechanizmów **guardrails** (szyn ochronnych) w kontekście pracy agentów AI opartych na dużych modelach językowych. Celem jest pokazanie, jak kontrolować dane wejściowe i chronić agentów przed potencjalnie szkodliwą lub niepożądaną treścią.

## Zakres działania

Notebook demonstruje kompletny pipeline przetwarzania tekstu, który obejmuje:

- Wykrywanie języka tekstu,
- Analizę sentymentu,
- Generowanie streszczenia,
- Tłumaczenie tekstu na inny język.

Każdy z tych etapów realizowany jest przez dedykowanego agenta AI.

## Technologie i biblioteki

Notebook wykorzystuje następujące komponenty:

- **Biblioteka `openai-agents`** – do budowy i zarządzania agentami,
- **Guardrails** – dekoratory i klasy służące do weryfikacji danych wejściowych,
- **Model językowy `llama3.2`** – lokalnie hostowany model LLM przez platformę **Ollama**,
- **Asynchroniczna obsługa zadań** – za pomocą `nest_asyncio` oraz `AsyncOpenAI`.

## Kluczowe komponenty

- `Agent` – reprezentuje pojedynczą jednostkę realizującą określone zadanie,
- `Runner` – służy do wywoływania agentów i zbierania wyników ich pracy,
- `input_guardrail` – mechanizm weryfikujący dane wejściowe przed przetworzeniem,
- `GuardrailFunctionOutput` oraz `InputGuardrailTripwireTriggered` – klasy zarządzające wynikami weryfikacji i reakcją na nieprawidłowe dane.

## Modele

Do obsługi zapytań wykorzystany jest model **`llama3.2`**, zainstalowany i uruchamiany lokalnie przy użyciu **Ollama**. Interakcja z modelem odbywa się poprzez interfejs `OpenAIChatCompletionsModel`.
