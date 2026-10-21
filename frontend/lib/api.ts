export interface Prediction {
  label: string;
  confidence: number; // 0-1
}

export interface PredictResult {
  label: string;
  confidence: number;
  top3: Prediction[];
}

export async function predictImage(dataUrl: string): Promise<PredictResult> {
  const blob = await (await fetch(dataUrl)).blob();
  const form = new FormData();
  form.append("file", blob, "capture.jpg");

  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/predict`, {
    method: "POST",
    body: form,
  });
  if (!res.ok) {
    throw new Error(`Prediction failed (${res.status})`);
  }
  return res.json();
}