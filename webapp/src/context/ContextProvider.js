import React,{ createContext,useContext,useState } from "react";
const StateContext = createContext();
export const ContextProvider = ({children}) =>{
    const [username, setUserName] = useState('');
    const [userLoggedIn, setUserLogggedIn] = useState(false);
    const [usertoken,setUserToken] = useState();
    const [tokendata,setTokendata] = useState();
    const handleUserName= (data)=> {
        setUserName({username:data});
    }
    const handleUserLoggedIn= (data)=>{
        setUserLogggedIn(data);
    }
    const handleUserToken= (data)=>{
        setUserToken(data);
    }
    const handleTokenData= (data)=>{
        setTokendata(data);
    }
    return(
        <StateContext.Provider value ={{username,handleUserName,userLoggedIn, handleUserLoggedIn,usertoken,handleUserToken,tokendata,handleTokenData}}>
            {children}
        </StateContext.Provider>
    )
}
export const useStateContext = () =>useContext(StateContext);