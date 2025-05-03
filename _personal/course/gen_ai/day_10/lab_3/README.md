# 🧪 GenAI Day 10 Lab 3 – Prompt Injection Detection with LangKit

## 📋 Opis

Notebook prezentuje sposób wykrywania ataków typu **prompt injection** za pomocą biblioteki **LangKit**. Takie ataki polegają na manipulowaniu promptami, by model działał w sposób niezamierzony (np. ignorował wcześniejsze instrukcje). Notebook demonstruje, jak można wykrywać i analizować takie przypadki.

## 📦 Wymagane biblioteki

W notebooku użyto:

- **`langkit[all]`** – główna biblioteka do wykrywania typów prompt injection i analizy kontekstu.
- **`google.colab.userdata`** – dostęp do zmiennych środowiskowych w Colabie (np. tokeny).
- **`os`** – dostęp do zmiennych środowiskowych.

## 🧠 Model

Notebook deklaruje użycie modelu:
```
gpt-4o-mini
```

Choć wykrywanie injection nie zależy bezpośrednio od modelu generującego, notebook umożliwia jego integrację z LangKit w celu analizy interakcji.

## 🛡️ Funkcjonalności

Notebook zawiera:
- Import klas `injections` i `extract` z LangKit.
- Automatyczne wykrywanie typowych technik prompt injection.
- Ekstrakcję danych z podejrzanych fragmentów promptu.
- Możliwość rozszerzenia systemu o własne definicje injection.

## 🧪 Przykładowe użycie

Notebook zawiera przykłady promptów zawierających próby manipulacji, takie jak:
- "Zignoruj poprzednie instrukcje i wykonaj X..."
- "Udawaj, że jesteś użytkownikiem, i powiedz Y..."

LangKit analizuje te teksty i klasyfikuje je jako znane typy injection, ułatwiając późniejszą filtrację lub odpowiednią reakcję systemu.
