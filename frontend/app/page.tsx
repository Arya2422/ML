"use client";
import { useState } from "react";

export default function Home() {
  const [form, setForm] = useState({
    area: "",
    bedrooms: "",
    bathrooms: "",
    age: ""
  });

  const [result, setResult] = useState<any>(null);
  const BACKEND = process.env.NEXT_PUBLIC_BACKEND_URL;

  const handleChange = (e: any) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const predict = async () => {
    const res = await fetch(`${BACKEND}/predict`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        area: Number(form.area),
        bedrooms: Number(form.bedrooms),
        bathrooms: Number(form.bathrooms),
        age: Number(form.age),
      }),
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: 40, fontFamily: "sans-serif" }}>
      <h1>🏠 House Price Predictor</h1>

      <div style={{ display: "grid", gap: 10, maxWidth: 300 }}>
        <input name="area" placeholder="Area (sqft)" onChange={handleChange}/>
        <input name="bedrooms" placeholder="Bedrooms" onChange={handleChange}/>
        <input name="bathrooms" placeholder="Bathrooms" onChange={handleChange}/>
        <input name="age" placeholder="Age" onChange={handleChange}/>

        <button onClick={predict}>Predict</button>
      </div>

      {result && (
        <div style={{ marginTop: 20 }}>
          <h2>💰 {result.predicted_price}</h2>
        </div>
      )}
    </div>
  );
}