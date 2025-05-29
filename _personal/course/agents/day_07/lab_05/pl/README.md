
# AGI Day 07 – AutoGen Logging Demo

## Opis

Notebook prezentuje zastosowanie mechanizmu logowania w bibliotece **AutoGen** poprzez uruchomienie konwersacji między dwoma agentami (asystentem i użytkownikiem). Wszystkie działania są logowane do lokalnej bazy danych SQLite, a następnie analizowane za pomocą narzędzi takich jak `pandas` i `sqlite3`.

## Zakres działania

Notebook zawiera:

- Instalację biblioteki **AutoGen**,
- Konfigurację agenta asystenta (`AssistantAgent`) oraz użytkownika (`UserProxyAgent`),
- Rozpoczęcie i zatrzymanie sesji logowania,
- Uruchomienie konwersacji między agentami,
- Odczyt i analiza logów zapisanych w bazie SQLite (`logs.db`).

## Technologie i biblioteki

Wykorzystywane narzędzia i biblioteki:

- **`autogen`** – framework do tworzenia konwersacyjnych agentów AI,
- **`AssistantAgent`, `UserProxyAgent`** – klasy reprezentujące role asystenta i użytkownika,
- **`autogen.runtime_logging`** – mechanizm rejestracji interakcji i przebiegu działania agentów,
- **`sqlite3`** – do odczytu lokalnej bazy danych z zapisanymi logami,
- **`pandas`** – do przetwarzania i wyświetlania danych z bazy w formie tabel.

## Kluczowe komponenty

- `autogen.runtime_logging.start(...)` – inicjalizacja sesji logowania do pliku SQLite,
- `AssistantAgent` – agent LLM odpowiadający na pytania,
- `UserProxyAgent` – agent symulujący użytkownika wysyłającego zapytania,
- `user_proxy.initiate_chat(...)` – rozpoczęcie konwersacji,
- `autogen.runtime_logging.stop()` – zakończenie sesji i zamknięcie bazy,
- `logs.db` – plik z pełnymi zapisami sesji agentów.

## Model

Notebook wykorzystuje model językowy **`gpt-4o-mini`** skonfigurowany z użyciem klucza API OpenAI, przekazywanego dynamicznie w zmiennej `OPENAI_API_KEY`.
