# AGI Day 06 Lab 03 – Generowanie i ulepszanie obrazów z agentami Autogen

## 🎯 Cel notebooka

Notebook prezentuje system automatycznego generowania i ulepszania obrazów za pomocą modelu DALL·E. Zawiera implementację klasy `DalleCreator`, która koordynuje współpracę pomiędzy:

- Agentem generującym obrazy,
- Agentem krytykiem, który ocenia wygenerowane obrazy i proponuje ulepszenia promptów.

Cały proces przebiega iteracyjnie — obrazy są generowane, oceniane i poprawiane aż do uzyskania zadowalającego efektu.

---

## 📚 Użyte biblioteki

- `autogen` – do tworzenia i obsługi agentów LLM,
- `openai` – do komunikacji z modelami OpenAI, w tym DALL·E,
- `matplotlib` – do prezentacji wygenerowanych obrazów,
- `PIL` (`Pillow`) – do przetwarzania obrazów,
- `diskcache` – do lokalnego buforowania danych,
- `google.colab.userdata` – do zarządzania API keyami w Colabie,
- `os`, `re`, `typing` – biblioteki pomocnicze.

---

## 🧠 Użyte modele LLM

Notebook wykorzystuje następujące modele:

- **gpt-4-turbo** – używany przez agentów do przetwarzania promptów, krytyki i iteracyjnego ulepszania,
- **gpt-4o-mini** – alternatywny model o wyższej multimodalności,
- **dalle** – model generujący obrazy na podstawie promptów tekstowych.