import React from 'react'
import { useStateContext} from '../context/ContextProvider'

const Sidebar = () => {
    const { username,userLoggedIn} = useStateContext();
  return (
    <div className = "ml-3 h-screen  md:overflow-hidden overflow-auto md:hover:over-flow-auto pb-10 border border-blue-500">
        {
            userLoggedIn && 

            (<p>This is code for Sidebar</p>)
    }
    </div>
  )
}

export default Sidebar