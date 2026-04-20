"use client";
import { useState } from "react";

export default function Home() {
  const [value, setValue] = useState("");
  const [result, setResult] = useState(null);

  const predict = async () => {
    const res = await fetch("https://ml-2-9upv.onrender.com/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ value: Number(value) }),
    });

    const data = await res.json();
    setResult(data.prediction);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>ML App</h1>
      <input value={value} onChange={(e)=>setValue(e.target.value)} />
      <button onClick={predict}>Predict</button>
      {result && <p>Result: {result}</p>}
    </div>
  );
}