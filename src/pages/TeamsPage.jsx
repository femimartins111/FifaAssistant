import { useMemo, useState } from 'react';
import PageHeader from '../components/PageHeader';
import TeamCard from '../components/TeamCard';
import { useData } from '../context/DataContext';
import { uniqueValues } from '../utils/helpers';

const INITIAL_VISIBLE_COUNT = 25;
const LOAD_MORE_AMOUNT = 25;

export default function TeamsPage() {
  const { teams } = useData();

  // searchInput changes while typing.
  // search only changes when Enter is pressed, so the list does not reshuffle every key press.
  const [searchInput, setSearchInput] = useState('');
  const [search, setSearch] = useState('');

  const [selectedOvr, setSelectedOvr] = useState('All');
  const [visibleCount, setVisibleCount] = useState(INITIAL_VISIBLE_COUNT);

  const ovrOptions = useMemo(() => uniqueValues(teams, (team) => team.ovr), [teams]);

  const filteredTeams = useMemo(() => {
    const normalizedSearch = search.trim().toLowerCase();

    return teams.filter((team) => {
      const teamName = `${team.name ?? ''}`.toLowerCase();
      const searchMatch = normalizedSearch === '' || teamName.includes(normalizedSearch);
      const ovrMatch = selectedOvr === 'All' || Number(selectedOvr) === team.ovr;

      return searchMatch && ovrMatch;
    });
  }, [teams, search, selectedOvr]);

  const visibleTeams = useMemo(() => {
    return filteredTeams.slice(0, visibleCount);
  }, [filteredTeams, visibleCount]);

  function runSearch() {
    setSearch(searchInput);
    setVisibleCount(INITIAL_VISIBLE_COUNT);
  }

  function handleSearchKeyDown(event) {
    if (event.key === 'Enter') {
      runSearch();
    }
  }

  function handleOvrChange(event) {
    setSelectedOvr(event.target.value);
    setVisibleCount(INITIAL_VISIBLE_COUNT);
  }

  function loadMoreTeams() {
    setVisibleCount((currentCount) => currentCount + LOAD_MORE_AMOUNT);
  }

  return (
    <section>
      <PageHeader
        title="Teams"
        description="Browse clubs, ratings, average age, and badge images from allteams.xlsx."
      />

      <div className="toolbar card">
        <input
          type="text"
          value={searchInput}
          onChange={(event) => setSearchInput(event.target.value)}
          onKeyDown={handleSearchKeyDown}
          placeholder="Search team name, then press Enter..."
        />

        <select value={selectedOvr} onChange={handleOvrChange}>
          <option>All</option>
          {ovrOptions.map((ovr) => (
            <option key={ovr} value={ovr}>
              {ovr}
            </option>
          ))}
        </select>
      </div>

      <div className="entity-grid">
        {visibleTeams.map((team) => (
          <TeamCard key={team.name} team={team} />
        ))}
      </div>

      {visibleCount < filteredTeams.length && (
        <div style={{ marginTop: '20px', textAlign: 'center' }}>
          <button type="button" onClick={loadMoreTeams}>
            Load More
          </button>
        </div>
      )}
    </section>
  );
}
