"use client";

import { useRef, useState, useCallback } from "react";
import { Camera } from "lucide-react";
import { Button } from "@/components/ui/button";

interface CameraCaptureProps {
  onCapture: (imageData: string) => void;
}

export function CameraCapture({ onCapture }: CameraCaptureProps) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [streaming, setStreaming] = useState(false);

  const startCamera = useCallback(async () => {
    const stream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: "environment" },
    });
    if (videoRef.current) {
      videoRef.current.srcObject = stream;
      setStreaming(true);
    }
  }, []);

  const capture = useCallback(() => {
    if (!videoRef.current || !canvasRef.current) return;
    const video = videoRef.current;
    const canvas = canvasRef.current;
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext("2d");
    ctx?.drawImage(video, 0, 0);
    const imageData = canvas.toDataURL("image/jpeg");
    onCapture(imageData);
  }, [onCapture]);

  return (
    <div className="rounded-none border border-[#3A3D42] overflow-hidden">
  <div className="aspect-[4/5] bg-[#1C1E23] relative flex items-center justify-center">
    {!streaming ? (
      <Button onClick={startCamera} variant="secondary">
        Start Camera
      </Button>
    ) : (
      <>
        <video ref={videoRef} autoPlay playsInline className="w-full h-full object-cover" />
        <div className="absolute inset-3 border border-[#EDE7DA]/40 pointer-events-none" />
        <div className="absolute left-3 right-3 h-px bg-[#D9A441] animate-scan pointer-events-none" />
      </>
    )}
    <canvas ref={canvasRef} className="hidden" />
  </div>
  {streaming && (
    <div className="p-4 flex justify-center border-t border-[#3A3D42]">
      <button
        onClick={capture}
        className="w-14 h-14 rounded-full bg-[#2F6F62] flex items-center justify-center"
      >
        <Camera className="text-[#EDE7DA]" size={22} />
      </button>
    </div>
  )}
</div>
  );
}