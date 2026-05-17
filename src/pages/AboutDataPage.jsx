import PageHeader from '../components/PageHeader';
import { useData } from '../context/DataContext';
import { DATA_PATHS } from '../data/loaders';

export default function AboutDataPage() {
  const { metadata, error } = useData();

  return (
    <section>
      <PageHeader title="Data Status" description="This page tells you exactly which files this frontend expects." />
      <div className="card">
        <h3>Hardcoded file requirements</h3>
        <ul className="clean-list">
          {Object.entries(DATA_PATHS).map(([key, value]) => (
            <li key={key}>
              <strong>{key}</strong>: {value}
            </li>
          ))}
        </ul>
      </div>

      <div className="card">
        <h3>How to wire your data</h3>
        <ol className="clean-list ordered-list">
          <li>Place the files in <code>public/data</code>.</li>
          <li>Keep the exact filenames used by your Python program.</li>
          <li>Start Vite and the frontend will load them on boot.</li>
          <li>External image URLs from the spreadsheets will render directly in cards.</li>
        </ol>
        {error ? <p className="error-text">Current load error: {error}</p> : null}
        <p className="muted">
          Loaded counts: {metadata.playersCount} players, {metadata.teamsCount} teams, {metadata.formationsCount} formations.
        </p>
      </div>
    </section>
  );
}
