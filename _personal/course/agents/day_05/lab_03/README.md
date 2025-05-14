# AGI Day 05 - Lab 03: Rezerwacja

## Cel notebooka

Notebook ten prezentuje wykorzystanie agentów AI do symulacji procesu rezerwacji — np. podróży lub wydarzenia — z użyciem narzędzi wyszukiwania, ekstrakcji informacji ze stron internetowych oraz interfejsu użytkownika. Celem jest pokazanie, jak duże modele językowe (LLM) mogą współpracować w zespole agentów do wykonania złożonego, praktycznego zadania.

## Użyte biblioteki

Notebook korzysta z następujących bibliotek:

- `os` – do obsługi zmiennych środowiskowych.
- `warnings` – do kontrolowania komunikatów ostrzegawczych.
- `crewai` – do definiowania agentów, zadań i ich współpracy.
- `crewai.process` – do zarządzania procesem pracy agentów.
- `crewai_tools` – zestaw gotowych narzędzi, m.in.:
  - `SerperDevTool` – wyszukiwanie informacji w internecie.
  - `ScrapeWebsiteTool` – ekstrakcja danych ze stron internetowych.
  - `WebsiteSearchTool` – przeszukiwanie zawartości stron.
- `langchain_openai.ChatOpenAI` – interfejs do modeli LLM od OpenAI.
- `google.colab.userdata` – do bezpiecznego zarządzania danymi w Google Colab.
- `IPython.display.Markdown` – do wyświetlania wyników w czytelnej formie.
- `gradio` – do budowy interfejsu użytkownika.

## Użyte modele LLM

W notebooku używany jest model:

- **GPT-4o-mini** – skonfigurowany w klasie `CFG` jako główny model językowy agentów.
