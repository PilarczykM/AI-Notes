# 🧪 GenAI Day 10 Lab 2 – Prompt Guard 86M Prompt Classification

## 📋 Opis

Notebook prezentuje użycie lekkiego modelu **Prompt Guard 86M** firmy Meta, zaprojektowanego do klasyfikacji promptów według określonych kategorii bezpieczeństwa. Służy do wczesnej identyfikacji potencjalnie ryzykownych zapytań kierowanych do modeli językowych, takich jak prośby o treści nielegalne, nieetyczne, czy dezinformujące.

## 📦 Wymagane biblioteki

W notebooku użyto:

- **`torch`** – do obliczeń tensorowych i inferencji modelu.
- **`transformers`** – do załadowania tokenizerów i modelu z Hugging Face.
- **`huggingface_hub`** – uwierzytelnianie i pobieranie modelu.
- **`google.colab.userdata`** – bezpieczne przechowywanie tokena użytkownika.

## 🧠 Model

Wykorzystany model:
```
meta-llama/Prompt-Guard-86M
```

To lekki model sekwencyjnej klasyfikacji tekstów, który umożliwia ocenę promptów pod kątem zgodności z zasadami bezpieczeństwa przed ich przesłaniem do większych modeli językowych.

## 🛡️ Funkcjonalności

Notebook umożliwia:
- Logowanie do Hugging Face i konfigurację modelu.
- Przekazanie promptu użytkownika i jego tokenizację.
- Klasyfikację promptu do jednej z wielu kategorii bezpieczeństwa.
- Obliczenie i wyświetlenie prawdopodobieństw przypisania do poszczególnych klas.

## 🧪 Przykładowe użycie

Zawiera przykłady promptów, które są klasyfikowane przez model, pokazując jak przypisywane są im kategorie takie jak: `Hate`, `Harassment`, `Violence`, `Self-harm`, itp. Pozwala to ocenić ryzyko związane z danym zapytaniem jeszcze przed wygenerowaniem odpowiedzi.
