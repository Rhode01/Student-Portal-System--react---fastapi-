import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser, LoginForm } from "../api/authApi";

const Login: React.FC = () => {
  const [form, setForm] = useState<LoginForm>({ username: "", password: "" });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const data = await loginUser(form);
      sessionStorage.setItem("token", data.access_token);
      sessionStorage.setItem("role", data.role);

      if (data.role === "admin") navigate("/admin/dashboard");
      else navigate("/student/dashboard");
    } catch (err: any) {
      setError("Invalid username or password");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen items-center justify-center bg-[url('/school-bg.jpg')] bg-cover">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-10 rounded-xl shadow-xl w-96"
      >
        <h2 className="text-2xl font-semibold mb-4 text-center">
          Student Portal Login
        </h2>
        {error && <p className="text-red-600 mb-3 text-center">{error}</p>}
        <input
          className="w-full mb-3 p-2 border rounded"
          type="text"
          name="username"
          placeholder="Enter Username"
          onChange={handleChange}
          value={form.username}
        />
        <input
          className="w-full mb-3 p-2 border rounded"
          type="password"
          name="password"
          placeholder="Enter Password"
          onChange={handleChange}
          value={form.password}
        />
        <button
          className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700 disabled:opacity-50"
          disabled={loading}
          type="submit"
        >
          {loading ? "Logging in..." : "Login"}
        </button>
      </form>
    </div>
  );
};

export default Login;
