import { useEffect, useState } from "react"
import { Link } from "react-router-dom"

export default function SearchResults({ search }) {
  const [results, setResults] = useState()

  useEffect(() => {
    fetch(`http://localhost:5555/tv_series/${search}`)
    .then(resp => resp.json())
    .then(data => setResults(data))
  }, [search])

  if (!search) {
    return <p>no search</p>
  }

  if (results === undefined) {
    return <p>Searching...</p>
  }

  return (
    <div id="search-results">
      {results.map(result => <Link to={`show/${result.id}`} key={result.id}>{result.primary_title} {result.start_year}-{result.end_year}</Link>)}
    </div>
  )
}