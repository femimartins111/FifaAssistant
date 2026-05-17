import PageHeader from '../components/PageHeader';
import StatPill from '../components/StatPill';
import { useData } from '../context/DataContext';

export default function HomePage() {
  const { metadata, loading } = useData();

  return (
    <section>
      <PageHeader
        title="Dashboard"
        description="A React rebuild of your FIFA Assistant with reusable components, page-level features, and hardcoded data filenames."
      />

      <div className="hero-grid">
        <div className="card hero-card">
          <h3>What this frontend covers</h3>
          <ul className="clean-list">
            <li>Team and player browsing</li>
            <li>Player comparison</li>
            <li>Random career generators</li>
            <li>Career idea generator</li>
            <li>Season stats entry and charts</li>
            <li>Image support for players and clubs</li>
          </ul>
        </div>

        <div className="card hero-card">
          <h3>Data snapshot</h3>
          {loading ? (
            <p>Loading dataset...</p>
          ) : (
            <div className="pill-grid">
              <StatPill label="Players" value={metadata.playersCount} />
              <StatPill label="Teams" value={metadata.teamsCount} />
              <StatPill label="Ideas" value={metadata.ideasCount} />
              <StatPill label="Formations" value={metadata.formationsCount} />
              <StatPill label="Continents" value={metadata.continentsCount} />
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
