import { useState } from "react"

import SearchResults from "./SearchResults"

export default function Search() {
  const [search, setSearch] = useState("")

  function handleSubmit(event) {
    event.preventDefault()
    setSearch(event.target.search.value)
  }

  return (
    <>
      <form id="series-search-form" onSubmit={handleSubmit}>
        <label>Search by Series Title: </label>
        <input type="text" name="search" />
        <input type="submit" />
      </form>
      {search ? <SearchResults search={search} /> : null}
    </>
  )
}