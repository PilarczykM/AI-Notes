# AGI_day_03_lab_06 – Browser Agent

## 🎯 Cel projektu

Ten notebook przedstawia implementację agenta automatyzującego interakcję z przeglądarką internetową z wykorzystaniem biblioteki **Playwright** oraz modelu językowego dostarczanego przez **Together AI**.

Agent jest w stanie:

- analizować zrzuty ekranu i strukturę DOM (drzewo dostępności),
- planować i wykonywać akcje (nawigacja, kliknięcia, wypełnianie pól),
- korzystać z LLM w celu podejmowania decyzji o dalszych krokach na stronie.

## 🛠️ Użyte biblioteki

Notebook wykorzystuje następujące biblioteki:

- `playwright` – kontrola przeglądarki w trybie programistycznym,
- `together` – integracja z Together AI i ich modelami językowymi,
- `asyncio`, `base64`, `json`, `re` – standardowe biblioteki Pythona do zarządzania danymi, asynchroniczności i przetwarzania tekstu.

## 🧠 Modele

Notebook wykorzystuje model językowy **`meta-llama/Llama-4-Scout-17B-16E-Instruct`**, udostępniany przez Together AI. Model ten służy do analizowania kontekstu strony (zarówno wizualnego, jak i strukturalnego) oraz generowania decyzji w formacie JSON, które są następnie wykonywane przez agenta w przeglądarce.

## 🧪 Zakres działania

Agent może m.in.:

- odwiedzać strony,
- analizować zrzuty ekranu (konwertowane do base64),
- rozpoznawać strukturę drzewa dostępności,
- generować kolejne akcje w formacie JSON,
- dynamicznie reagować na błędy lub niepowodzenia działań.
