import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Dashboard } from "./components/pages/Dashboard/Dashboard";
import { Login } from "./components/pages/Login/Login";
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}
