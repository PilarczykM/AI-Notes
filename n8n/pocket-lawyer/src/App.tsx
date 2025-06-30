import {} from "@/components/ui/button";

import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
// import { toast } from "sonner"
import { Scale, FileText } from "lucide-react";

const App = () => {
  const [question, setQuestion] = useState("");
  const [category, setCategory] = useState("");
  const [advice, setAdvice] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const categories = [
    "Prawo pracy",
    "Umowa B2B/B2C/UoP",
    "Spółki i start-upy",
    "Nieruchomości",
    "Prawo rodzinne",
    "Spadki",
    "Prawo konsumenckie",
    "RODO / dane osobowe",
    "Mandaty i wykroczenia",
  ];

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!question.trim() || !category) {
      // toast({
      //   title: "Błąd",
      //   description: "Proszę wypełnić wszystkie pola",
      //   variant: "destructive",
      // });
      return;
    }

    setIsLoading(true);
    console.log("Wysyłanie danych do webhook...");

    const webhookData = {
      question: question.trim(),
      category: category,
      timestamp: new Date().toISOString(),
      source: "PocketLawyer",
    };

    try {
      const webhookUrl = "http://localhost:5678/webhook-test/pocket-lawyer";

      const response = await fetch(webhookUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(webhookData),
      });

      if (response.ok && response.body) {
        // toast({
        //   title: "Sukces",
        //   description:
        //     "Twoje pytanie zostało wysłane. Porada prawna zostanie wygenerowana.",
        // });

        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");
        let result = "";

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          result += decoder.decode(value, { stream: true });
        }

        // Finish decoding any remaining text
        result += decoder.decode();

        setAdvice(result);
      } else {
        throw new Error("Błąd wysyłania");
      }
    } catch (error) {
      console.error("Błąd webhook:", error);
      // toast({
      //   title: "Błąd",
      //   description: "Nie udało się wysłać pytania. Spróbuj ponownie.",
      //   variant: "destructive",
      // });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8 px-4">
      <div className="max-w-2xl mx-auto">
        <div className="text-center mb-8">
          <div className="flex items-center justify-center mb-4">
            <Scale className="h-12 w-12 text-navy mr-3" />
            <h1 className="text-4xl font-bold text-navy">PocketLawyer</h1>
          </div>
          <p className="text-lg text-text-dark">
            Profesjonalne porady prawne na wyciągnięcie ręki
          </p>
        </div>

        <Card className="shadow-lg border-0">
          <CardHeader className="bg-navy text-white rounded-t-lg">
            <CardTitle className="flex items-center">
              <FileText className="h-6 w-6 mr-2" />
              Formularz konsultacji prawnej
            </CardTitle>
          </CardHeader>
          <CardContent className="p-6">
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="space-y-2">
                <Label
                  htmlFor="question"
                  className="text-text-dark font-medium"
                >
                  Twoje pytanie prawne
                </Label>
                <Textarea
                  id="question"
                  placeholder="Opisz swoją sytuację prawną szczegółowo..."
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  className="min-h-[120px] border-gray-300 focus:border-navy focus:ring-navy"
                  required
                />
              </div>

              <div className="space-y-2">
                <Label
                  htmlFor="category"
                  className="text-text-dark font-medium"
                >
                  Kategoria sprawy
                </Label>
                <Select value={category} onValueChange={setCategory} required>
                  <SelectTrigger className="border-gray-300 focus:border-navy focus:ring-navy">
                    <SelectValue placeholder="Wybierz kategorię..." />
                  </SelectTrigger>
                  <SelectContent className="bg-white border-gray-200">
                    {categories.map((cat) => (
                      <SelectItem
                        key={cat}
                        value={cat}
                        className="hover:bg-gray-50"
                      >
                        {cat}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <Button
                type="submit"
                disabled={isLoading}
                className="w-full bg-navy hover:bg-accent-dark text-white font-medium py-3 transition-colors duration-200"
              >
                {isLoading ? "Wysyłanie..." : "Uzyskaj poradę"}
              </Button>
            </form>

            <div className="mt-8">
              <Label className="text-text-dark font-medium mb-3 block">
                Twoja porada prawna
              </Label>
              <Textarea
                placeholder="Twoja porada prawna pojawi się tutaj."
                value={advice}
                readOnly
                className="min-h-[150px] bg-gray-50 border-gray-200 cursor-default resize-none"
              />
            </div>
          </CardContent>
        </Card>
        <div className="bg-orange-200 text-orange-900 text-xs p-4 text-center mt-8">
          <strong>Zrzeczenie się odpowiedzialności prawnej: </strong>
          Informacje zamieszczone na tej stronie mają charakter wyłącznie
          informacyjny i nie stanowią porady prawnej. W celu uzyskania wiążącej
          opinii należy skonsultować się z prawnikiem.
        </div>

        <div className="text-center mt-8">
          <p className="text-sm text-gray-600">
            © {new Date().getFullYear()} PocketLawyer - Profesjonalne porady
            prawne
          </p>
        </div>
      </div>
    </div>
  );
};

export default App;
