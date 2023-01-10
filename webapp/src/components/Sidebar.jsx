import React from 'react'
import { useStateContext} from '../context/ContextProvider'
import {links} from '../data/dummy';
import { Link,NavLink} from 'react-router-dom';

const Sidebar = () => {
    const { username,userLoggedIn} = useStateContext();
  return (
    <div className = "ml-3 h-screen  md:overflow-hidden overflow-auto md:hover:over-flow-auto pb-10 border border-blue-500">
        {
            userLoggedIn && 

          <>
          {
                 <div className="mt-10">
                 {links.map((item) => (
                   <div key={item.title}>
                     <p className="text-gray-400 m-3 mt-4 uppercase"> {item.title}  </p>
                     {item.links.map((l) =>(
                       <NavLink to={`/${l.linkto}`} 
                       key={l.name} >
                       {l.icon}<span className="capitalize"> {l.name} </span>
                       </NavLink>
                     ))}
                   </div>
                 ))}
                 </div>
          }
          

          </>
    }
    </div>
  )
}

export default Sidebar