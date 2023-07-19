import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"

export default function Show() {
  const [series, setSeries] = useState({})

  const { id } = useParams()

  useEffect(() => {
    fetch(`http://localhost:5555/tv_series/${id}`)
    .then(resp => resp.json())
    .then(data => setSeries(data))
  }, [])

  if (JSON.stringify(series) === '{}') {
    return <h1>Loading...</h1>
  }

  return (
    <>
      <h1>{series.primary_title}</h1>
      <h2>Grid goes here</h2>
    </>
  )
}