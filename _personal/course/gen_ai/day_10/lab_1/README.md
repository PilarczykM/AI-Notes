# 🧪 GenAI Day 10 Lab 1 – LLaMA Guard 3 Inference & Safety Analysis

## 📋 Opis

Ten notebook demonstruje wykorzystanie modelu **LLaMA Guard 3** firmy Meta do analizy bezpieczeństwa treści generowanych przez modele językowe. Umożliwia klasyfikację wypowiedzi pod kątem ryzykownych lub nieodpowiednich treści, takich jak przemoc, mowa nienawiści, manipulacja czy dezinformacja.

## 📦 Wymagane biblioteki

Notebook korzysta z następujących bibliotek:

- **`llama-recipes`** – narzędzia i przepisy do pracy z modelami LLaMA, w tym ich dostrajania i wdrażania.
- **`bitsandbytes`** – efektywna kwantyzacja modeli w celu zmniejszenia zużycia pamięci i przyspieszenia obliczeń.
- **`huggingface_hub`** – dostęp do modeli i zasobów udostępnianych przez społeczność.
- **`transformers`** – biblioteka do ładowania i używania nowoczesnych modeli NLP.
- **`google.colab.userdata`** – umożliwia bezpieczne przechowywanie i dostęp do danych w środowisku Google Colab.

## 🧠 Model

Model używany w notebooku:
```
meta-llama/Llama-Guard-3-8B
```

Jest to model zaprojektowany do **analizy bezpieczeństwa tekstów**. Jego celem jest identyfikowanie i klasyfikowanie treści, które mogą naruszać zasady etyczne lub wytyczne bezpieczeństwa.

## 🛡️ Funkcjonalności

Notebook oferuje:
- Tworzenie niestandardowych promptów do testowania.
- Symulację konwersacji (user–assistant) z oceną każdej wypowiedzi.
- Klasyfikację wypowiedzi według kategorii ryzyka (np. przemoc, dyskryminacja, nielegalna aktywność).
- Informację zwrotną, czy dana wypowiedź jest "bezpieczna" czy "potencjalnie ryzykowna".

## 🧪 Przykładowe użycie

W notebooku znajdują się przykłady promptów (zarówno neutralnych, jak i ryzykownych), które są analizowane przez model. Wyniki pokazują klasyfikację wypowiedzi oraz przypisanie ich do określonych kategorii ryzyka, co pozwala zrozumieć, jak model reaguje na różne rodzaje treści.
