import React from 'react'
import { useStateContext } from '../context/ContextProvider';

const Dashboard = () => {
    const { username,tokendata} = useStateContext();
    const user1 = username['username'];
    
    return (
        <div className="relative flex flex-col justify-center pl-2"> Welcome {tokendata['firstname']} {tokendata['lastname']} !!</div>
    )
}

export default Dashboard