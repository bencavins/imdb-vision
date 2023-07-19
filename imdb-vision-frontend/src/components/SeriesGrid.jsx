import SeriesGridRow from "./SeriesGridRow"

export default function SeriesGrid({ series }) {

  return (
    <div id="series-grid">
      <table>
        {series.episodes.map(row => <SeriesGridRow rowData={row} />)}
      </table>
    </div>
  )
}