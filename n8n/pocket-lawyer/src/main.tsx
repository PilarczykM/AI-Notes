import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";
// import { Toaster } from "@/components/ui/sonner"

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <div className="max-w-2xl mx-auto">
      <App />
    </div>
    {/* <Toaster /> */}
  </StrictMode>
);
