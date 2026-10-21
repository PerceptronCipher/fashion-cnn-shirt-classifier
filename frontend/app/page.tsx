"use client";

import { useState } from "react";
import { CameraCapture } from "@/components/camera-capture";
import { PredictionCard } from "@/components/prediction-card";
import { predictImage, type PredictResult } from "@/lib/api";

export default function Home() {
  const [result, setResult] = useState<PredictResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleCapture = async (imageData: string) => {
    setLoading(true);
    setError(null);
    try {
      setResult(await predictImage(imageData));
    } catch {
      setError("Could not reach the model. If the server was idle, wait about 20 seconds and try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="max-w-sm mx-auto p-4 pt-10">
      <h1 className="text-lg font-medium mb-4">Shirt Classifier</h1>
      <CameraCapture onCapture={handleCapture} />
      {loading && <p className="mt-4 text-sm text-muted-foreground">Reading the fabric…</p>}
      {error && <p className="mt-4 text-sm text-red-400">{error}</p>}
      {result && !loading && (
        <>
          <PredictionCard
            label={result.label}
            confidence={Math.round(result.confidence * 100)}
          />
          <ul className="mt-3 text-sm text-muted-foreground space-y-1">
            {result.top3.slice(1).map((p) => (
              <li key={p.label} className="flex justify-between">
                <span>{p.label}</span>
                <span className="font-mono">{Math.round(p.confidence * 100)}%</span>
              </li>
            ))}
          </ul>
        </>
      )}
    </main>
  );
}