# 📊 AGI Day 08 – AgentEval Lab

## 🎯 Cel notebooka

Notebook służy do **automatycznej ewaluacji odpowiedzi generowanych przez agentów konwersacyjnych** w zadaniach matematycznych. Proces oceny oparty jest na kryteriach jakościowych generowanych przez model językowy, które następnie służą do oceny skuteczności agentów.

---

## 🧠 Użyty model językowy

W notebooku wykorzystano model językowy klasy **GPT-4.1** do:
- generowania kryteriów oceny jakości odpowiedzi,
- analizy treści przypadków testowych,
- automatycznej oceny odpowiedzi agentów.

Model jest wywoływany przez narzędzie oceny w ramach biblioteki `autogen`.

---

## 📦 Wymagane biblioteki

Notebook korzysta z poniższych bibliotek:

| Biblioteka              | Zastosowanie                                          |
| ----------------------- | ----------------------------------------------------- |
| `autogen`               | system agentowy i funkcje ewaluacyjne                 |
| `matplotlib`            | wizualizacja wyników                                  |
| `numpy`, `scipy`        | obliczenia statystyczne (średnie, przedziały ufności) |
| `os`, `json`, `pathlib` | zarządzanie plikami i danymi                          |
| `contextlib`            | bezpieczne ignorowanie błędów                         |
| `wget`, `unzip`         | pobieranie i rozpakowywanie danych testowych          |

---

## 📁 Struktura działania

1. **Przygotowanie środowiska**
   - Utworzenie katalogu roboczego
   - Pobranie i rozpakowanie zbioru danych testowych (rozmowy agentów)

2. **Wczytanie kryteriów oceny**
   - Parsowanie pliku JSON z definicją kryteriów do dalszej oceny

3. **Ocena przypadków testowych**
   - Przetworzenie danych wejściowych (usunięcie ground truth)
   - Użycie modelu do przypisania ocen wg wcześniej wygenerowanych kryteriów

4. **Zapis wyników**
   - Zapis ocenionych przypadków do pliku `evaluated_problems.json`

5. **Analiza wyników**
   - Obliczenie średnich wyników i przedziałów ufności
   - Oddzielna analiza przypadków poprawnych i niepoprawnych

6. **Wizualizacja**
   - Wykresy słupkowe porównujące skuteczność modelu względem różnych kryteriów

---

## 📂 Dane wejściowe

- `prealgebra.zip` – zbiór testowych rozmów w formacie `.json`
- `sample_math_criteria.json` – plik z kryteriami oceny

## 📤 Dane wyjściowe

- `evaluated_problems.json` – plik zawierający wyniki oceny jakości odpowiedzi
