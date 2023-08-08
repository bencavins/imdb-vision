import SeriesGridRow from "./SeriesGridRow"
import "./SeriesGrid.css"

export default function SeriesGrid({ series }) {

  const tdHeader = []
  for (let i = 0; i <= maxRowLength(series.episodes); i++) {
    if (i === 0) {
      tdHeader.push(<th>Season</th>)
    } else {
      tdHeader.push(<th>E{i}</th>)
    }
  }

  return (
    <div id="series-grid">
      <table>
        <thead>
          <tr>
            {tdHeader}
          </tr>
        </thead>
        <tbody>
          {series.episodes.map(row => <SeriesGridRow rowData={row} />)}
        </tbody>
      </table>
    </div>
  )
}

function maxRowLength(matrix) {
  let max = 0
  for (let row of matrix) {
    const length = row.length
    if (length > max) {
        max = length
    }
  }
  return max
}