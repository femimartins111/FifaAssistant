import { NavLink, Route, Routes } from 'react-router-dom';
import TeamsPage from './pages/TeamsPage';
import PlayersPage from './pages/PlayersPage';
import ComparePage from './pages/ComparePage';
import GeneratorsPage from './pages/GeneratorsPage';
import SeasonStatsPage from './pages/SeasonStatsPage';

const navItems = [
  ['/players', 'Players'],
  ['/teams', 'Teams'],
  ['/compare', 'Compare'],
  ['/generators', 'Generators'],
  ['/season-stats', 'Season Stats'],
];

export default function App() {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div>
          <h1>FIFA Assistant</h1>
          <p className="muted">Modular React frontend built from your Python feature set.</p>
        </div>

        <nav className="nav-list">
          {navItems.map(([path, label]) => (
            <NavLink
              key={path}
              to={path}
              className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
            >
              {label}
            </NavLink>
          ))}
        </nav>
      </aside>

      <main className="main-content">
        <Routes>
          <Route path="/" element={<PlayersPage />} />
          <Route path="/players" element={<PlayersPage />} />
          <Route path="/teams" element={<TeamsPage />} />
          <Route path="/compare" element={<ComparePage />} />
          <Route path="/generators" element={<GeneratorsPage />} />
          <Route path="/season-stats" element={<SeasonStatsPage />} />
        </Routes>
      </main>
    </div>
  );
}