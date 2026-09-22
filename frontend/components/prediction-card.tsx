import { Progress } from "@/components/ui/progress";

interface PredictionCardProps {
  label: string;
  confidence: number; // 0-100
}

export function PredictionCard({ label, confidence }: PredictionCardProps) {
  return (
    <div className="border border-[#3A3D42] p-4 mt-4 relative">
  <div className="absolute -top-2 left-4 bg-[#14161A] px-2 text-[10px] tracking-wide text-[#EDE7DA]/60">
    RESULT
  </div>
  <div className="flex justify-between items-baseline">
    <span className="text-[#EDE7DA] text-base">{label}</span>
    <span className="font-mono text-[#D9A441] text-lg">{confidence}%</span>
  </div>
  <div className="h-px bg-[#3A3D42] mt-3 relative overflow-hidden">
    <div className="h-full bg-[#2F6F62]" style={{ width: `${confidence}%` }} />
  </div>
</div>
  );
}