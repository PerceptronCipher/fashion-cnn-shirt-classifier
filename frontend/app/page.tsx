"use client";

import { useState } from "react";
import { CameraCapture } from "@/components/camera-capture";
import { PredictionCard } from "@/components/prediction-card";

export default function Home() {
  const [prediction, setPrediction] = useState<{ label: string; confidence: number } | null>(null);

  const handleCapture = (imageData: string) => {
    // TODO tomorrow: send imageData to FastAPI /predict, replace this mock
    console.log("Captured image, length:", imageData.length);
    setPrediction({ label: "Shirt", confidence: 78 });
  };

  return (
    <main className="max-w-sm mx-auto p-4 pt-10">
      <h1 className="text-lg font-medium mb-4">Shirt Classifier</h1>
      <CameraCapture onCapture={handleCapture} />
      {prediction && <PredictionCard label={prediction.label} confidence={prediction.confidence} />}
    </main>
  );
}