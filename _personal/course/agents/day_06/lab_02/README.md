# AGI Day 06 Lab 02 – System wizualizacji z agentami Autogen

## 🎯 Cel notebooka

Notebook demonstruje działanie systemu opartego na wielu agentach, który automatycznie generuje i ulepsza wizualizacje danych. Głównym celem jest stworzenie iteracyjnego procesu, w którym agenci komunikują się między sobą, by:

- Wygenerować wykres z danych (komender),
- Ocenić jakość wykresu (krytyk),
- Poprawić kod na podstawie krytyki (programista).

Przykład użyty w notebooku to tworzenie wykresu temperatury z danych zapisanych w pliku CSV.

---

## 📚 Użyte biblioteki

- `autogen` – biblioteka do zarządzania agentami LLM i automatycznego generowania kodu,
- `matplotlib` – do tworzenia wykresów i wizualizacji danych,
- `PIL` (`Pillow`) – do przetwarzania obrazów,
- `os` – do operacji systemowych,
- `google.colab.userdata` – do pobierania danych użytkownika w środowisku Google Colab.

---

## 🧠 Użyte modele LLM

Notebook wykorzystuje model **gpt-4o-mini**, skonfigurowany bezpośrednio w kodzie w ramach listy `config_list_4v`. Model ten wykorzystywany jest przez agentów `autogen` do komunikacji, generowania kodu i przetwarzania multimodalnego.