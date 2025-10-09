import axios, { formToJSON } from "axios"; 
import { login_url } from "../routes/routes";
export interface LoginResponse {
  access_token: string;
  token_type: string;
  role: string;
}
interface LoginForm {
  username: string;
  password: string;
}
export const loginUser = async (data: LoginForm): Promise<LoginResponse> => {
  const response = await axios.post<LoginResponse>(
    login_url,
    {
      username: data.username,
      password: data.password
    },
    {
      headers: {
        "Content-Type": "application/json"
      }
    }
  );
  return response.data;
};
