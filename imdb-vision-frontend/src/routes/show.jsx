import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"

import SeriesGrid from "../components/SeriesGrid"
import "./show.css"

export default function Show() {
  const [series, setSeries] = useState({})

  const { id } = useParams()

  useEffect(() => {
    fetch(`http://localhost:5555/tv_series/${id}`)
    .then(resp => resp.json())
    .then(data => {
      // turn episode array into matrix
      const episodes = []
      let row = []
      let seasonNum = data.episodes[0].season_number
      data.episodes.forEach(episode => {
        if (episode.season_number !== seasonNum) {
          episodes.push(row)
          row = []
          seasonNum = episode.season_number
        }
        row.push(episode)
      })
      episodes.push(row)
      data.episodes = episodes
      
      setSeries(data)
    })
  }, [])

  if (JSON.stringify(series) === '{}') {
    return <p>Loading Series Info...</p>
  }

  return (
    <>
      <h2>{series.primary_title}</h2>
      <SeriesGrid series={series} />
    </>
  )
}