import React,{ createContext,useContext,useState } from "react";
const StateContext = createContext();
export const ContextProvider = ({children}) =>{
    const [username, setUserName] = useState('');
    const [userLoggedIn, setUserLogggedIn] = useState(false);
    const handleUserName= (data)=> {
        setUserName({username:data});
    }
    const handleUserLoggedIn= (data)=>{
        setUserLogggedIn(data);
    }
    return(
        <StateContext.Provider value ={{username,handleUserName,userLoggedIn, handleUserLoggedIn,setUserName,setUserLogggedIn}}>
            {children}
        </StateContext.Provider>
    )
}
export const useStateContext = () =>useContext(StateContext);