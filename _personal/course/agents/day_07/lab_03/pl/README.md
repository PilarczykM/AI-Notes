
# AGI Day 07 – SmolAgents z Langfuse i OpenTelemetry

## Opis

Notebook demonstruje integrację frameworka **SmolAgents** z platformą **Langfuse** oraz systemem **OpenTelemetry** w celu monitorowania, instrumentacji i ewaluacji agentów AI. Przykładowym zastosowaniem jest uruchamianie agenta na zbiorze zadań matematycznych GSM8K, a następnie zbieranie i przesyłanie śladów działania do systemu Langfuse.

## Zakres działania

Notebook wykonuje następujące operacje:

- Instalacja i konfiguracja środowiska telemetrycznego (`OpenTelemetry`, `Langfuse`),
- Instrumentacja agenta `SmolAgents` z wykorzystaniem `SmolagentsInstrumentor`,
- Pobranie i przetwarzanie zbioru danych **GSM8K** (z Hugging Face),
- Uruchomienie agenta typu `CodeAgent` na danych testowych,
- Zbieranie wyników, identyfikatorów śladów (`trace_id`) oraz ocena odpowiedzi agenta,
- Rejestracja danych i ocen w systemie **Langfuse**.

## Technologie i biblioteki

W notebooku użyto:

- **`smolagents[telemetry]`** – biblioteka agentowa rozszerzona o możliwość zbierania metryk i logów,
- **`openinference-instrumentation-smolagents`** – moduł do instrumentacji agentów Smol w kontekście OpenInference,
- **`langfuse`** – platforma do śledzenia działania agentów LLM i gromadzenia ewaluacji,
- **`OpenTelemetry`** – framework do zbierania danych telemetrycznych (OTLP, eksport HTTP),
- **`datasets`** – biblioteka Hugging Face do pobierania danych (tu: zbiór `gsm8k`),
- **`HfApiModel`** – interfejs do modeli udostępnianych przez Hugging Face (tu: `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`).

## Kluczowe komponenty

- `CodeAgent` – agent Smol przeznaczony do rozwiązywania problemów wymagających kodowania rozwiązań (np. zadań matematycznych),
- `TracerProvider`, `OTLPSpanExporter`, `SimpleSpanProcessor` – komponenty OpenTelemetry używane do monitorowania,
- `Langfuse()` – obiekt odpowiedzialny za logowanie wyników i ocen agentów do platformy Langfuse,
- `format_trace_id` – umożliwia analizę śladów interakcji agenta z modelem.

## Model

Notebook wykorzystuje model `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B` dostępny przez Hugging Face, który jest wykorzystywany przez `CodeAgent` do przetwarzania danych wejściowych z zestawu `gsm8k`.
