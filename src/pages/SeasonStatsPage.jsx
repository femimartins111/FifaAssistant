import { useMemo, useState } from 'react';
import ChartCard from '../components/ChartCard';
import PageHeader from '../components/PageHeader';

const emptyForm = {
  name: '',
  goals: '',
  assists: '',
  appearances: '',
  averageRating: '',
  cleanSheets: '',
};

export default function SeasonStatsPage() {
  const [teamName, setTeamName] = useState('');
  const [seasonYear, setSeasonYear] = useState('');
  const [playerForm, setPlayerForm] = useState(emptyForm);
  const [entries, setEntries] = useState([]);

  const addEntry = () => {
    if (!playerForm.name.trim()) return;
    setEntries((current) => [
      ...current,
      {
        name: playerForm.name.trim(),
        goals: Number(playerForm.goals || 0),
        assists: Number(playerForm.assists || 0),
        appearances: Number(playerForm.appearances || 0),
        averageRating: Number(playerForm.averageRating || 0),
        cleanSheets: Number(playerForm.cleanSheets || 0),
      },
    ]);
    setPlayerForm(emptyForm);
  };

  const exportCsv = () => {
    if (!entries.length) return;
    const header = 'Player,Goals,Assists,Clean Sheets,Appearances,Average Rating\n';
    const body = entries
      .map(
        (entry) =>
          `${entry.name},${entry.goals},${entry.assists},${entry.cleanSheets},${entry.appearances},${entry.averageRating}`
      )
      .join('\n');
    const blob = new Blob([header + body], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const safeSeason = seasonYear.replaceAll('/', '_') || 'season';
    link.href = URL.createObjectURL(blob);
    link.download = `${teamName || 'team'}_${safeSeason}_stats.csv`;
    link.click();
  };

  const totalGoals = useMemo(() => entries.reduce((sum, entry) => sum + entry.goals, 0), [entries]);

  return (
    <section>
      <PageHeader title="Season Stats" description="The CLI season stats feature turned into a visual data-entry page." />

      <div className="card form-stack">
        <div className="toolbar toolbar-grid-2">
          <input value={teamName} onChange={(event) => setTeamName(event.target.value)} placeholder="Team name" />
          <input value={seasonYear} onChange={(event) => setSeasonYear(event.target.value)} placeholder="Season year e.g. 2025/2026" />
        </div>

        <div className="toolbar toolbar-grid-3">
          <input value={playerForm.name} onChange={(event) => setPlayerForm({ ...playerForm, name: event.target.value })} placeholder="Player name" />
          <input type="number" value={playerForm.goals} onChange={(event) => setPlayerForm({ ...playerForm, goals: event.target.value })} placeholder="Goals" />
          <input type="number" value={playerForm.assists} onChange={(event) => setPlayerForm({ ...playerForm, assists: event.target.value })} placeholder="Assists" />
          <input type="number" value={playerForm.appearances} onChange={(event) => setPlayerForm({ ...playerForm, appearances: event.target.value })} placeholder="Appearances" />
          <input type="number" step="0.1" min="0" max="10" value={playerForm.averageRating} onChange={(event) => setPlayerForm({ ...playerForm, averageRating: event.target.value })} placeholder="Average rating" />
          <input type="number" value={playerForm.cleanSheets} onChange={(event) => setPlayerForm({ ...playerForm, cleanSheets: event.target.value })} placeholder="Clean sheets" />
        </div>

        <div className="button-row">
          <button className="primary-btn" onClick={addEntry}>Add Player Stats</button>
          <button className="secondary-btn" onClick={exportCsv}>Export CSV</button>
        </div>
        <p className="muted">Total goals tracked: {totalGoals}</p>
      </div>

      {entries.length ? (
        <>
          <div className="card">
            <table className="compare-table">
              <thead>
                <tr>
                  <th>Player</th>
                  <th>Goals</th>
                  <th>Assists</th>
                  <th>Appearances</th>
                  <th>Average Rating</th>
                  <th>Clean Sheets</th>
                </tr>
              </thead>
              <tbody>
                {entries.map((entry) => (
                  <tr key={entry.name}>
                    <td>{entry.name}</td>
                    <td>{entry.goals}</td>
                    <td>{entry.assists}</td>
                    <td>{entry.appearances}</td>
                    <td>{entry.averageRating}</td>
                    <td>{entry.cleanSheets}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="chart-grid">
            <ChartCard title="Goals by Player" dataKey="goals" data={entries} />
            <ChartCard title="Assists by Player" dataKey="assists" data={entries} />
            <ChartCard title="Appearances by Player" dataKey="appearances" data={entries} />
            <ChartCard title="Average Rating by Player" dataKey="averageRating" data={entries} yDomain={[0, 10]} />
            <ChartCard title="Clean Sheets by Player" dataKey="cleanSheets" data={entries} />
          </div>
        </>
      ) : null}
    </section>
  );
}
