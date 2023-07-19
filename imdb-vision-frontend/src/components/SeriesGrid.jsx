import SeriesGridRow from "./SeriesGridRow"

export default function SeriesGrid({ series }) {

  const tdHeader = []
  for (let i = 0; i <= maxRowLength(series.episodes); i++) {
    if (i === 0) {
      tdHeader.push(<td>Season</td>)
    } else {
      tdHeader.push(<td>E{i}</td>)
    }
  }

  return (
    <div id="series-grid">
      <table>
        <thead>
          {tdHeader}
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