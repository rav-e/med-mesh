import { useState } from 'react'
import { Register, Login } from '.'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <h1>MED MESH</h1>     
      <Register />
      <Login />

    </div>
  )
}

export default App
