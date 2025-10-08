import { useAuth0 } from '@auth0/auth0-react'
import { useEffect, useState } from 'react'
import { redirect } from 'react-router-dom'
export const Login = () => {
    const [loginDetails, setLoginDetails]  = useState({
      username:"",
      password:""
    }) 
    const {isAuthenticated,loginWithRedirect } = useAuth0()
    useEffect(()=>{
        if (isAuthenticated){
           redirect("/dashboard")
        }    
    })
    const handleFormSubmission = (event) =>{
      event.preventDefault();
    }
    const onChangeFormData = (e) => {
        const { name, value } = e.target;
        setLoginDetails((prev) => ({
          ...prev,
          [name]: value,
        }));
      };
  return (
    <div>
      <div>
          <form>
            <input type="text" name="username" 
             onChange={onChangeFormData}
            placeholder='Enter your registration Number'/>
            <input type="password" name="password" id="" placeholder='Enter password' />
            <input type="submit" value="Login" />
       </form>
      </div>
    </div>
  )
}
